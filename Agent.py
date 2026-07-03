import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent

load_dotenv()

# ========== 配置 DeepSeek ==========
llm = ChatOpenAI(
    base_url="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    model="deepseek-chat",
    temperature=0.3
)

# ========== Mock 数据 ==========
def search_hotel(city: str, check_in: str = "", check_out: str = "") -> str:
    mock_hotels = {
        "深圳": [
            {"name": "深圳威尼斯酒店", "price": 588, "rating": 4.8, "address": "南山区华侨城"},
            {"name": "深圳君悦酒店", "price": 799, "rating": 4.7, "address": "罗湖区宝安南路"},
            {"name": "深圳华侨城洲际大酒店", "price": 688, "rating": 4.6, "address": "南山区深南大道"},
        ],
        "杭州": [
            {"name": "杭州西湖国宾馆", "price": 899, "rating": 4.9, "address": "西湖区杨公堤"},
            {"name": "杭州君悦酒店", "price": 699, "rating": 4.7, "address": "上城区湖滨路"},
        ],
        "三亚": [
            {"name": "三亚海棠湾君悦酒店", "price": 999, "rating": 4.8, "address": "海棠区海棠北路"},
            {"name": "三亚亚龙湾万豪酒店", "price": 799, "rating": 4.6, "address": "亚龙湾国家度假区"},
        ]
    }
    hotels = mock_hotels.get(city, [{"name": f"{city}暂无酒店数据", "price": 0, "rating": 0, "address": ""}])
    return "\n".join([f"🏨 {h['name']} | ¥{h['price']}/晚 | {h['rating']}分 | {h['address']}" for h in hotels])


def search_attractions(city: str) -> str:
    mock_attractions = {
        "深圳": [
            {"name": "世界之窗", "desc": "5A景区，浓缩世界著名景点"},
            {"name": "欢乐谷", "desc": "大型主题乐园，适合亲子游玩"},
            {"name": "大梅沙海滨公园", "desc": "免费海滨浴场，夏季热门"},
        ],
        "杭州": [
            {"name": "西湖", "desc": "5A景区，世界文化遗产，免费开放"},
            {"name": "灵隐寺", "desc": "千年古刹，香火旺盛"},
            {"name": "宋城", "desc": "大型宋代文化主题公园"},
        ],
        "三亚": [
            {"name": "蜈支洲岛", "desc": "5A景区，海岛风光，潜水圣地"},
            {"name": "天涯海角", "desc": "4A景区，三亚地标"},
            {"name": "亚龙湾", "desc": "免费海滨，沙质细腻"},
        ]
    }
    attractions = mock_attractions.get(city, [{"name": f"{city}暂无景点数据", "desc": ""}])
    return "\n".join([f"📍 {a['name']} - {a['desc']}" for a in attractions])


def get_weather(city: str) -> str:
    mock_weather = {
        "深圳": "☀️ 晴，28-34°C，南风2级，湿度65%",
        "杭州": "🌤️ 多云，25-32°C，东风2级，湿度70%",
        "三亚": "☀️ 晴，27-33°C，东北风3级，湿度75%",
    }
    return mock_weather.get(city, f"🌥️ {city}天气数据暂不可用")


# ========== 定义工具 ==========
@tool
def search_hotel_tool(city: str, check_in: str = "", check_out: str = "") -> str:
    """查询指定城市的酒店信息。输入城市名，可选入住和离店日期。"""
    return search_hotel(city, check_in, check_out)


@tool
def search_attractions_tool(city: str) -> str:
    """查询指定城市的景点信息。输入城市名。"""
    return search_attractions(city)


@tool
def get_weather_tool(city: str) -> str:
    """查询指定城市的天气信息。输入城市名。"""
    return get_weather(city)


tools = [search_hotel_tool, search_attractions_tool, get_weather_tool]

# ========== 创建 Agent ==========
agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt="你是一个旅行规划助手。根据用户需求调用工具获取信息，输出完整的行程计划。"
)


# ========== 运行 ==========
if __name__ == "__main__":
    print("=" * 50)
    print("🧳 携程智能行程规划助手")
    print("=" * 50)
    print("\n💡 试试：帮我规划一个深圳3日游")
    print("输入 'exit' 退出\n")

    while True:
        user_input = input("\n✈️ 请输入：")
        if user_input.lower() == 'exit':
            print("👋 再见！")
            break

        try:
            response = agent.invoke({"messages": [("user", user_input)]})
            print("\n" + "=" * 50)
            print("🧳 规划结果：")
            print("=" * 50)
            print(response["messages"][-1].content)
            print("=" * 50)
        except Exception as e:
            print(f"❌ 出错：{e}")