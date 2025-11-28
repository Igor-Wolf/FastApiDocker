Passo a passo meu pc

py -3.10 -m venv venv310

Ative a venv pelo Shell do vscode:

.\venv310\Scripts\activate

pip install fastapi[standard]

fastapi dev main.py --port 8085


pip freeze > requirements.txt
uvicorn main:app  --port 8000 --reload




doocker 

docker run -d -p 8000:8000 fastapi
