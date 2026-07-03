# 🧳 携程智能行程规划助手

基于 LangGraph + DeepSeek 的 ReAct Agent 旅行规划系统

## 📌 项目简介

本项目是一个智能旅行规划助手，用户只需输入旅行需求（如“帮我规划一个深圳3日游”），Agent 会自动调用工具获取酒店、景点、天气等信息，并生成一份完整的行程计划。

该项目展示了 **ReAct Agent** 的完整工作流程：**推理（Reasoning）→ 调用工具（Acting）→ 整合结果 → 生成回答**。

## 🛠️ 技术栈

| 模块 | 技术 |
|------|------|
| Agent 框架 | LangGraph |
| 大模型 | DeepSeek Chat API |
| 工具定义 | LangChain @tool 装饰器 |
| 前端界面 | Streamlit |
| 开发语言 | Python 3.10+ |

## 🏗️ 项目结构
携程智能行程规划助手/
├── Agent.py # 命令行版本
├── streamlit_app.py # Web 界面版本
├── requirements.txt # 项目依赖
├── .env # API Key 配置（需自行创建）
└── README.md # 项目说明


## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/Ashyle16/xiecheng_ReAct_Agent.git
cd 携程智能行程规划助手

### 2. 安装依赖

```bash
pip install -r requirements.txt
```
### 3. 配置 API Key

DEEPSEEK_API_KEY=sk-xxxx

### 4. 运行项目
命令行版本：
```bash
python Agent.py
```

Web 界面版本：
```bash
streamlit run streamlit_app.py
```

### 5.使用示例

#### 输入：
帮我规划一个深圳3日游

#### Agent执行流程：
1. 调用 get_weather_tool 查询深圳天气
2. 调用 search_hotel_tool 查询深圳酒店
3. 调用 search_attractions_tool 查询深圳景点
4. 整合所有信息，生成 Markdown 格式的行程计划

#### 输出：
一份包含每日安排、酒店推荐、景点推荐、天气提醒的完整行程表。

### 📌 当前状态
✅ Agent 核心推理链路已跑通
✅ 酒店 / 景点 / 天气 三个工具已实现
✅ 命令行交互已跑通
✅ Streamlit Web 界面已跑通

⏳ 真实 API 对接（计划中，目前为 Mock 数据）

### 📬 联系方式
邮箱：18026604563@163.com

GitHub：2199745789@qq.com/Ashylle16

### 📄 说明
本项目为个人学习项目，用于展示 Agent 应用开发能力，数据均为 Mock 演示版本。