# Hangman
Hangman is a Python Terminal game. Users can try to guess the word by inputting letters until they guess the word and win or lose the game by running out of tries. 
You can read more about the game <a href = "https://en.wikipedia.org/wiki/Hangman_(game)" target="_blank" rel="noopener">here</a>.

<a href = "https://nelas-hangman.herokuapp.com/" target="_blank" rel="noopener">Click here</a> to try out the game. 
![Hangman MockUp image](images/mockup.png)

## How to play:
* Start by choose either reading the rules or start the game.
* When player start the game, the program randomly chooses one word from the list with 300 different words.
* The word is represented with underscores to show how many letters are in the word.
* If the letter is correct, the underscore will be replaced with the correct letter.
* If the letter is wrong, the player will lose a "live" until there is zero lives left. The player gets 6 tries.
* The player wins when the word is guessed and loses if the lives runs out. 
* If the player wins/loses, the menu will start over. 

## Wireframes/FlowChart

During the planning proccess I made a Flowchart to set the basic steps to help guide my coding process. 
As the game is played in the terminal, no wireframes is made for a visual look. 
![Hangman FlowChart image](images/Wireframes.png)

## Design

The game is very limited because of it is played trough the terminal. 
More information about future design is written under [Future Features](#future-features)

## Features

### Existing Features

#### Start -> Menu
* When you enters the terminal-game, you will be able to make a chose between start the game or read the rules.

![Hangman Start image](images/game-1.png)

#### Rules

* If you press 1, the rules will show up.

![Hangman Rules image](images/game-2.png)

#### Playing the game

* If you press 2, the game will start and it will tell you if you guessed correct or wrong.
If you already guessed a letter, it will tell you to try another letter.

![Hangman play game image](images/game-4.png)

#### End of the game-round

* If you guess wrong letter 6 time, the game will end and you will lose. 
* If you guess the correct word by inputting correct letters, it will tell you that you won.

* When the round is over, it tells you to chose in the menu again. Read more about this in [Future Features](#future-features)

![Hangman play game image](images/game-5.png)

### Future Features

* Add design to the game, like color and fix the background. 
* Add level choices so the player can chose if they want to play an easy level or difficult. 
* Add a function that ends game in terminal instead of going back to menu. 

## Testing 

I have manually tested this project by doing following:
* Passed the code through a PEP8 linter and confirmed there are no problems.
* Tested in my local terminal and the Code Institute Heroku terminal

### Validator testing
* PEP8 - No errors were returned


### Solved bugs
* I made a function for the variable 'word', but should have instead passed it in an another function. I solved this by passing it to the menu function.

### Deployment

This project was deployed using Cod Insititutes moch terminal for Herouku.


## Credits

* Inspiration for building the game: <a href = "https://www.youtube.com/watch?v=m4nEnsavl6w" target="_blank" rel="noopener">here</a>.
* Logo made by: <a href = "https://www.ascii-art-generator.org/" target="_blank" rel="noopener">here</a>.
* I want to thank Code Institute and Slack Community for all the help through this project. 

