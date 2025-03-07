# 使用官方的 Python 3.11 slim 映像
FROM python:3.11-slim

# 設定容器內的工作目錄
WORKDIR /app

# 如果有需求檔，先複製並安裝套件
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 複製所有程式碼到容器內
COPY . .

# 開放 5000 埠 (如果程式使用不同埠，請修改)
EXPOSE 5000

# 執行程式
CMD ["python", "main.py"]
