echo Hello there!
set /p choice=Do you have a localhost server running [y/n]?: 

echo Starting installation for SindiAI...
pip install -r requirements.txt
python create_db.py
python server.py
