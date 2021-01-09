FROM postgres:latest 
RUN mkdir /data
RUN rm -f /docker-entrypoint-initdb.d/init-user-db.sh
#RUN mkdir /docker-entrypoint-initdb.d
COPY ./init-user-db.sh /docker-entrypoint-initdb.d/init-user-db.sh
COPY ./data.csv /data/data.csv 
