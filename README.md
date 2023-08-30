# VitorsMiniGames
The main purpose of this project was to re-create the classic board game of battleships but in Python and make it available online for anyone to play and have fun

![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/c1ff6854-86d6-4a3d-a64a-e29ae86d78d6)


Use the following link to access the [ deployed project on Heroku](https://vitorsbattleships-728ecb558e1a.herokuapp.com/)

---

## Main Objectives
My Main objective for this project was to learn from the mistakes that I have made in project two. Especially the fact I didn't test the app enough and submitted it with an audio loading error. So for this one every function has been tested and I have tried to break each one in many different ways.

- I wanted to re-create battleships
- I wanted the player to be able to expand or shrink the board
- I wanted it to have intelligent Ai that
- I wanted to make it easy to understand



## UX & Design
The website design was already provided by Code Institute.
But in the terminal, I did choose to use a dictionary of 

~ for empty (water)
S for a ship
H for a hit
M for a miss


### User Stories

- As a visiting user, I would like to be able to choose a board size
- As a visiting user, I would like to be able to place my ships
- As a visiting user, I would like to be able to guess the AI ship's positions
- As a visiting user, I would like to be able to win or lose.
- As a visiting user, I would like the AI to be intelligent enough to make winning a challenge.

---

## Features

The main goal of this problem was for me to be able to show off my Python skills so to aid with this Code Institute kindly provided a template that allowed us to have a Python project that works online. This did come with limitations though like for example the site is not responsive and only works without no problems on certain browsers

### Existing Features

- Entry Screen
    When the user loads up the site they are greeted with a welcome and then they are promoted to enter a grid size
    minimum size a grid can be is 5.
  
    ![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/c0a232ef-3e8f-438a-ab48-998526cbc009)
  
- Placement Mode
    Then they get to choose where they want to place each of their ships and if they enter an incorrect value they are         promoted to try again.
  
    ![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/217add24-f69b-4471-8c3d-67c1ef906897)
  
- Game Mode
  After placing their ships the user can then begin playing the game and trying to guess where the ai ships are placed
  
    ![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/05aa80a0-8bd7-46fa-883e-8cf4b29f295f)
  
    They are promoted to enter rows and columns again, and there is input validation to make sure the user can not crash       the game
  
    ![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/df09b351-ce9d-48a7-b588-7337cc901d2c)
  
    After the player puts in a successful guess the AI then guess
  
    ![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/1bd6df30-21a7-4903-8fe3-502da7573bbd)
  
    The AI will use its intelligent AI to guess positions close to a hit
  
- End Game
    After guessing all the AI positions or losing the game will say you lose or win
  
    ![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/ff3134b7-9575-4d08-8272-a0d5bfe58b49)
  
    You will then be promoted if you want to play again If you say y the game will start again if you say n it will print
    thank you for playing
  
    ![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/2e0e78f6-ad52-4c43-bfa3-1d1c8a111c7b)



     
### Future Features

- In the future, I would like to implement multiplayer mode to allow players to be able to be able to play against other     people locally the toughest part of that would be figuring out how to hide where the ships are because everything else     should convert pretty easily

---

## Tools & Technologies Used
I used the following technologies and resources to create this site:

- [Git](https://git-scm.com) - For version control
- [GitHub](https://github.com) - For code hosting
- [Python](https://www.python.org) - Main programming language
- [CI Python Linter](https://pep8ci.herokuapp.com) - For code verification
---


#### Functions

Here is a list of functions used in this Battleship project, along with brief explanations of their functionalities. More detailed descriptions can be found within the code itself, in the form of comments.

- `initialize_grid(size)`
    - Initializes a grid with a given size, filling it with '~' to represent empty water.

- `get_grid_size()`
    - Prompts the user to input the size of the grid and validates it.

- `display_grid(grid)`
    - Displays the current state of the grid to the console.

- `display_guess_grid(grid)`
    - Displays the grid for guesses, replacing ships with '~' to hide them.

- `is_valid_guess(row, col, grid_size)`
    - Checks if a given guess is valid within the grid dimensions.

- `place_ship(grid, row, col, orientation, length)`
    - Places a ship of a given length and orientation at a specified location on the grid.

- `place_multiple_ships(grid, ship_lengths, placer)`
    - Places multiple ships on the grid, either for the player or the computer.

- `is_within_grid(row, col, orientation, length, grid_size)`
    - Checks if a ship placement is within the bounds of the grid.

- `is_empty(grid, row, col, orientation, length)`
    - Checks if a ship placement overlaps with other ships.

- `is_valid_placement(grid, row, col, orientation, length)`
    - Checks if a ship placement is both within the grid and not overlapping with other ships.

- `place_player_ships(grid, ship_length)`
    - Allows the player to place a ship of a given length on their grid.

- `place_computer_ships(grid, ship_length)`
    - Automatically places a ship of a given length for the computer.

- `make_guess(grid, row, col)`
    - Makes a guess on the grid and returns whether it was a hit or miss.

- `get_player_guess(player_previous_guesses, grid_size)`
    - Gets and validates the player's guess, ensuring it hasn't been guessed before.

- `computer_turn(player_grid, previous_hits, previous_guesses)`
    - Determines the computer's guess based on previous hits and guesses.

- `main_game_loop(player_grid, computer_grid, ship_lengths)`
    - The main game loop, which continues until all ships for one player are sunk.

---





## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

---

## Development
The following chapters will give some insights into my thinking process and why I have decided to use things the way they are.

### Limitations
Due to the fact, that we have been provided with a template there are some limitations like the fact it doesn't fully work on some browsers and it's not responsive.

### Challenges 
Figuring out how to place multiple ships was a bit of a challenge luckily I did have a decent amount of Python experience from previous work I have done with it so I managed to pull everything together at the end. Getting the more complex AI right was also tough as it kept going to the next position even if it didn't exist but i managed to figure that out 

### Error Handling
There is a lot of input validation going on in the project especially when the user is placing ships and making guesses 

### Refactoring
I did have to do some refactoring near the end of the project as the main function started getting too complex so i split it into other functions and called them in the main function This made it easier to read 



# Deployment

This project leverages a [provided template](https://github.com/Code-Institute-Org/python-essentials-template) to offer a terminal interface within a contemporary web browser, thereby enhancing its accessibility.

You can find the application deployed live on [Heroku](https://vitorsbattleships-728ecb558e1a.herokuapp.com/).

## Deploying on Heroku

This project is deployed on [Heroku](https://www.heroku.com), a cloud-based Platform as a Service (PaaS) that allows for full application hosting.

To deploy your app on Heroku, follow these steps post-account setup:

- Navigate to the top-right corner of your Heroku Dashboard, click **New** and then choose **Create new app** from the dropdown.
- Provide a unique name for your app, select the nearest region (either EU or USA), and click **Create App**.
- In the **Settings** tab of your new app, select **Reveal Config Vars**. Add a KEY named `PORT` with the value `8000`.
- Below, click **Add Buildpack** to add support for dependencies. The sequence is crucial: add `Python` first and `Node.js` second. (You can drag to rearrange them if needed.)

Two additional files are essential for Heroku deployment:
- `requirements.txt`
- `Procfile`

Install the necessary packages for this project by running:
- `pip3 install -r requirements.txt`

Update the requirements file with:
- `pip3 freeze --local > requirements.txt`

To connect your GitHub repository to your Heroku app, You go to deploy tap then click on GitHub then you can search for your GitHub repo

Then you can either enable automatic deploys or you can manual deploy
Then your project should be deployed


## Local Deployment

To run this project locally, you can clone or fork it. Make sure to install all packages listed in the `requirements.txt` file using:
- `pip3 install -r requirements.txt`

---



#### Cloning

---

## How to Fork the Repository

To make your own copy of the `VitorsMiniGames` repository, follow these steps:

1. Sign in to your GitHub account, or create one if you haven't already.
2. Navigate to the repository at `VitorBarbosaDev/VitorsMiniGames`.
3. Find the "Fork" button located in the upper-right corner and click it.

## How to Clone the Repository

To get a local copy of the `VitorsMiniGames` repository, adhere to these guidelines:

1. Log in to your GitHub account, or sign up if you are not a member.
2. Visit the repository page at `VitorBarbosaDev/VitorsMiniGames`.
3. Click the "Code" button and choose your preferred cloning method (either HTTPS, SSH, or GitHub CLI). Then, copy the URL that appears.
4. Open the terminal in your code editor and go to the directory where you'd like to store the cloned repository.
5. Type `git clone` into the terminal, paste the URL you copied earlier, and hit "Enter." The repository will now be cloned to your local machine.

---




### Acknowledgements
Special thanks to my mentor Alex for his invaluable assistance.
