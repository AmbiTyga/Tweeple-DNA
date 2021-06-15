# Tweeple-DNA
Tweeple DNA is a FastAPI based project that classifies twitter-people's account into bot or human, as well as assigns probabilty for being a bot  ranging from 0-1.

The project is based on DNA compression method from [Detecting Bot Behaviour in Social Media using Digital DNA Compression](http://ceur-ws.org/Vol-2563/aics_35.pdf), where we assign activity of the user throughout its timeline forming an activity class string, which is then converted to bytes and compressed using `zlib` package. To compare we use features we got from this method, and we try LightGBM and XGBoost on the features.


## Dataset
Dataset was collected from [Bot Repository](https://botometer.osome.iu.edu/bot-repository/datasets.html) of [Botometer](https://botometer.osome.iu.edu/), an OSoMe project.

## Experiment

For experimenting the project, do as the following:

- Clone the repo

```
git clone https://github.com/AmbiTyga/Tweeple-DNA.git
```
- Move to the Directory
```
cd Tweeple-DNA
```
- Go to `main.py`, at line 18, replace the Twitter tokens. To get the tokens refer to [Developer Portal](https://developer.twitter.com/en/portal/dashboard)
- Create Virtual Environment. I recommend using [pipenv](https://pypi.org/project/pipenv/)
```
pipenv shell
```
- Install the required packages
```
pipenv install -r requirements.txt
```
- Move to `/app` directory
```
cd app
```
- Run the app into local system
```
uvicorn main:app
```
- Copy the host link, in my case its `http://127.0.0.1:8000`, you can also use `http://localhost:8000`. For more description you can refer to `http://localhost:8000/docs`.
- Try GET using Python, do the following:
```
>>> import requests
>>> url = "http://localhost:8000/predict"
>>> id = {'id':'ambi_tyga'}
>>> requests.post(url,json=id).json()
{'Bot Probabilty': 0.43629276266830935, 'Label': 'human'}
```