FROM tiangolo/uvicorn-gunicorn-fastapi
RUN pip install pandas
EXPOSE 80
COPY ./Netflix /Netflix 