# Pokédle: A Pokémon Wordle-like Game
#### Video Demo: https://www.youtube.com/watch?v=dXyVjyo1i3o
#### Description: 
Welcome to the Pokémon Wordle-Like Game! This project is a fun and engaging game where players try to guess the Pokémon. The game is inspired by the popular Wordle games and brings a unique twist by incorporating Pokémon.

### Table of Contents
- [Libraries Used](#libraries-used)
- [How It Works](#how-it-works)
- [Game Flow](#example-game-flow)
- [Project Structure](#project-structure)
- [Conclusion](#conclusion)

#### Libraries Used
- requests: This library is used to interact with the PokéAPI and fetch data about Pokémon.
- random: Used to randomly select a Pokémon for the player to guess.
- figlet: Adds aesthetic elements to the game by creating stylized text.
- inflect: Helps in ensuring that the game's messages and prompts use correct English grammar.

#### How It Works
- Random Pokémon Generation: The game starts by generating a random Pokémon. This is achieved using the random library, which selects a Pokémon from a specified range of generations. The random selection ensures that each game is unique and challenging.

- Fetching Pokémon Data: Once a Pokémon is selected, the game uses the requests library to fetch data from the PokéAPI. This data includes the Pokémon's name, type, height, weight, and generation. By using the PokéAPI, the game provides accurate and comprehensive details about each Pokémon.

#### Example Game Flow
- Start the Game: When the game starts, a random Pokémon is generated, and the player is prompted to start guessing.

- Making a Guess: The player makes a guess by typing the name of a Pokémon.

- Feedback and Hints: If the guess is incorrect, the game provides hints to help the player. These hints might include the type of the Pokémon, its height and other relevant information.

- Winning the Game: If the player guesses the Pokémon correctly, a congratulatory message is displayed, and the player is invited to start a new game.

- Restarting the Game: Players can play multiple rounds, with a new random Pokémon generated each time, ensuring that the game remains challenging and fun.

#### Project Structure
1. project.py
This is the main script of the project. It contains the core functionality of the Pokémon Wordle-like game. The script handles the following tasks:
    - Generating a random Pokémon using the random library.
    - Fetching Pokémon data from the PokéAPI using the requests library.
    - Displaying the game title and instructions using the figlet library.
    - Ensuring grammatically correct messages using the inflect library.
    - Managing the game flow, including starting the game, making guesses, providing feedback, and restarting the game.

2. README.md
This file provides an overview of the project, including its features, the libraries used, and instructions for getting started. It serves as a guide for users to understand how to set up and use the project. The README includes information on the following:
    - Project features and functionality.
    - List of libraries used in the project.
    - An explanation of the game flow.
    - A guide to the project structure, including descriptions of each file.

3. test_project.py
This file contains tests for the project using the pytest framework. The tests ensure that the core functionalities of the game are working correctly. The tests include:
    - Verifying the correct generation of random Pokémon.
    - Ensuring the proper fetching of Pokémon data from the PokéAPI.

4. requirements.txt
This file lists all the dependencies required for the project. It ensures that all necessary libraries are installed when setting up the project.

#### Conclusion
The Pokémon Wordle-Like Game is a delightful and engaging way to test your Pokémon knowledge. By incorporating random generation, accurate data fetching, aesthetic enhancements, and proper grammar, the game offers a comprehensive and enjoyable experience. Whether you're a casual player or a Pokémon enthusiast, this game is sure to provide hours of fun and challenge. Happy guessing!