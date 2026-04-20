(
echo FROM python:3.10-slim
echo.
echo WORKDIR /app
echo.
echo COPY requirements.txt .
echo RUN pip install --no-cache-dir -r requirements.txt
echo.
echo COPY . .
echo.
echo CMD ["python", "app.py"]
) > Dockerfile
