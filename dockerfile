FROM python:slim
ENV TOKEN='your token'
COPY . .
RUN pip install -r req.txt
CMD python bot.py