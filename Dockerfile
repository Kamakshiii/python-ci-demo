FROM python:3.10-slim
WORKDIR /app
COPY ..
RUN pip-install requirements.txt
CMD ["python", "app.py"]