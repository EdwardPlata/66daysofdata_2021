#!/bin/bash

git clone https://github.com/EdwardPlata/66daysofdata_2021.git ~/project

PROJDIR="~/project/Simple_Stock_App"
python3 -m pip install -r "${PROJDIR}/requirements.txt"
streamlit run "${PROJDIR}/Simple_Stock_App.py
