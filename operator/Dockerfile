FROM python:3.11
ARG ssh_prv_key
RUN mkdir /root/.ssh
# Add the keys and set permissions
RUN echo "$ssh_prv_key" > /root/.ssh/id_rsa && \
    chmod 600 /root/.ssh/id_rsa

RUN pip install kopf gitpython paramiko pandas
ADD /src /src
COPY /src /src

CMD kopf run /src/main.py --verbose