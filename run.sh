#! /bin/bash

./install_venv.sh

. loguruvenv/bin/activate
python src/bugged.py
