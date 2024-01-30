# Retriever
![img](./app/frontend/props/retriever.jpeg)

This repo contains a llamav2 powered chatbot. I built it as part of a work application challenge.
It ``retrieves`` information from a csv file which is found in ``./app/backend/data/listings.csv``.

You may want to know which is the average price of the current listings, or which is the max price listed, to which 
property it belongs and where it is located.

In the notebooks folder, there are some EDA's from the challenge's data. I dropped the NAN's as there were few and then
decided to use langchain and an open-source llama2-7b model.


---
### Running the chatbot
The app folder has all the files to build a compose docker file. Once downloading this repo, run the following command 
in terminal
``docker compose up -d --build``. This will launch a composed docker app made of 2 different dockers.

The frontend docker will be running in the port ``8501`` so be sure to have it available, if not you may want to modify 
the fronend-dockerfile and the docker-compose file.


---

This is my first backend-frontend project and I'm happy to share it with the world.

Things that can be improved:
* There is not any user input check, so the user could prompt inject the model to generate a desired answer.
* If wanted to improve performance, embeddings and models could be converted to llama.ccp framework.
* It might be interesting to generate metrics of the API usage.



