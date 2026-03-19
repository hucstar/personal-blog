# Personal Blog

一个基于 **Flask** 的个人博客项目（当前为基础版本），用于快速启动个人站点开发。

## ✨ Features

- 使用 Flask 快速搭建 Web 应用
- 提供根路由 `/` 示例页面
- 支持本地开发调试（debug 模式）
- 项目结构简洁，便于后续扩展（蓝图、数据库、模板等）

## 📁 Project Structure
```

text personal-blog/ ├── app/ # 应用目录（可用于后续模块化扩展） ├── config.py # 配置文件 ├── requirements.txt # Python 依赖列表 ├── run.py # 项目启动入口 ├── .gitignore ├── LICENSE └── README.md``` 

## 🚀 Quick Start

### 1) Clone 项目
```

bash git clone <your-repo-url> cd personal-blog``` 

### 2) 创建并激活虚拟环境（Windows）
```

powershell py -m venv .venv ..venv\Scripts\activate``` 

> 如果 `py` 命令不可用，可改为：
>
> ```powershell
> python -m venv .venv
> ```

### 3) 安装依赖
```

bash pip install -r requirements.txt``` 

### 4) 启动项目
```

bash python run.py``` 

启动后访问：

- http://127.0.0.1:5000/

## 🛠 Development Notes

- 当前项目以最小可运行 Flask 应用为基础。
- 调试模式已开启，适合本地开发。
- 后续可考虑增加：
  - 页面模板（Jinja2）
  - 数据库支持（SQLAlchemy）
  - 用户系统（登录/注册）
  - 文章管理（CRUD）
  - API 与前后端分离架构

## ✅ Requirements

- Python 3.9+
- pip

## 📄 License

本项目使用 `LICENSE` 文件中声明的开源协议。
