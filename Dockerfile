FROM python:3.10-slim

WORKDIR /ArmLetters

EXPOSE 8000

ENV VIRTUAL_ENV=/ArmLetters/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

#RUN apt update
#RUN apt install -y procps curl

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-b 0.0.0.0", "main:app"]
# gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0 main:app
# sudo iptables -I INPUT 6 -m state --state NEW -p tcp --dport 80 -j ACCEPT
# sudo netfilter-persistent save