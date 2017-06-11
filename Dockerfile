FROM python:3.6-alpine

MAINTAINER skyblue3350 <skyblue3350@gmail.com>

EXPOSE 80/tcp

ENV DEBUG="True" \
  HOST="0.0.0.0" \
  PORT=80 \
  SECRET_KEY="abcdefg" \
  SESSION_LIFETIME=1440 \
  LDAP_HOST="192.168.1.1" \
  LDAP_BASE_DN="dc=example,dc=co,dc=jp" \
  LDAP_USER_DN="ou=people" \
  LDAP_USER_RDN_ATTR="uid" \
  LDAP_GROUP_OBJECT_FILTER="(objectClass=posixGroup)"

WORKDIR /home/cypress

COPY . .

RUN apk --no-cache add musl-dev gcc openldap-dev
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
