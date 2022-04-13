# 拉取镜像
FROM python:3.7.9

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 工作目录
WORKDIR /code

# 安装依赖
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# 复制项目到工作目录
COPY . /code/
