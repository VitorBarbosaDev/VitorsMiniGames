# VitorsMiniGames - Testing

![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/c1ff6854-86d6-4a3d-a64a-e29ae86d78d6)



Use the following link to access the [ deployed project on Heroku](https://vitorsbattleships-728ecb558e1a.herokuapp.com/)

---

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [CI Python Linter](#CI-Python-Linter)


* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)

* [BUGS](#bugs)
  * [Known Bugs](#known-bugs)
  * [Solved Bugs](#solved-bugs)

---

## AUTOMATED TESTING

Automated Testing includes all the testing that is carried out by a program

###  CI Python Linter
CI Python Linter was used to validate the Python code

![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/blob/6cecc410f066b6f3d413e62dbfb71da65dcf7f19/TestingImages/Screenshot%202023-08-31%20005921.png)



## MANUAL TESTING

### Testing User Stories


| Goals | How are they achieved? | Image |
| :--- | :--- | :--- |
| `Visitors` |
|  |  |  |
| I want to play a game on the web | The website is available on the web  | ![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/c0a232ef-3e8f-438a-ab48-998526cbc009) |
| I want to be able to choose where I place my ships. | The game allows the player to choose where ships are placed. | ![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/217add24-f69b-4471-8c3d-67c1ef906897)|
| I would like to be able to guess the AI ship's positions. | The game allows users to guess positions. |  ![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/df09b351-ce9d-48a7-b588-7337cc901d2c)|
| I would like to be able to win or lose. | Once either the player or AI has cleared all ships they are declared the winner  |  ![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/ff3134b7-9575-4d08-8272-a0d5bfe58b49)|
| I would like the AI to be intelligent enough to make winning a challenge. | The Ai remembers the last ship it hit and will choose adjacent positions until the ship is clear | ![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/1bd6df30-21a7-4903-8fe3-502da7573bbd) |


### Full Testing


| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| `Game Features` |
|  |  |  |  |  |
| Enter grid size | Will accept int larget then 5 otherwise re-prompts |Entered 6| Accepts int larget then 5 otherwise re-prompts. | Pass |
| Placing Ship | Allows the user to place a ship and doesn't allow them to place outside the grid. | Entered 20 20  | Got promoted to enter another position. | Pass |
| Guessing AI ship position |  will show m if miss will show h if hit | inputted 4 5 | I hit the AI so a h showed up. | Pass |
| Win |  After all ships are gone player wins | played game | After I cleared all ships game displays you have won. | Pass |
| Show guesses |  After every guess show guesses grid | guess ai position | After guessing a grid appeared with all my previous guesses. | Pass |


 - - -


## BUGS

### Known Bugs

No known bugs


### Solved Bugs

| No | Bug | How I resolved the issue |
| :--- | :--- | :--- |
| 1 | The player could place ships outside the grid. | added check to ensure this wasn't possible |
| 2 | The player could crash the game by inputting the wrong type of variable | To fix this I added string validation to all inputs. |
| 3 | The player board wasn't showing. | I was overwriting the player's board by calling the AI grid in the same method. |
| 4 | If you inputted h instead of H the game wouldn't place ship | I added an upper to ensure the string enter was always upper case. |
| 5 | The AI would continue to place positions even if off the board. | Added a check that caused the AI to go back to picking random if only the other option is off the board. |
