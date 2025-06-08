# 项目结构建议（适用于FastAPI + SQLAlchemy异步ORM）

# 项目目录结构：
#
# your_project/
# ├── main.py
# ├── api/
# │   ├── __init__.py
# │   └── comments.py
# ├── crud/       # 存放数据库操作逻辑
# │   ├── __init__.py
# │   └── comments.py
# ├── db/         # 存放数据库相关文件
# │   ├── __init__.py
# │   ├── database.py
# │   └── models.py
# ├── schemas/    # 存放数据模型
# │   ├── __init__.py
# │   └── comments.py
# └── utils/
#     └── dependencies.py