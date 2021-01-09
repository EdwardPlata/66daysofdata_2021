#!/bin/bash
set -e 
psql -c "CREATE database covid_db"
psql -c "COPY covid_19_surveillance FROM /data/data.csv DELIMITER ',' CSV HEAD;"
