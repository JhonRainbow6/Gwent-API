# The Witcher 3 API Gwent Cards 
A personal API for Gwent cards in The Witcher 3 build with FastAPI and docker for future deploy.

## Development tools
* Cards are stored in `cards.json`
* Init Docker files for images
* This project is being developed using Python 3.11

### How to Set up (using a virtual venv)

1. Create and active a venv
   
    ```bash
    # Creation
    python3 -m venv venv

    # Activation (linux)
    source venv/bin/activate
    ```
2. Intall Dependencies
   
    ```bash
    pip install -r requirements.txt
    ```

3. Run it

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```
The API will be run in `http://localhost:8000`.


### EndPoints (for now)
    
*   `GET /cards`: Receive the list of all cards.
*   `GET /cards/{deck_name}`: Receive all the cards from a specific deck (ex. `Nilfgaard`).
*   `GET /cards/search/{card_name}`: Search a card for his name.
