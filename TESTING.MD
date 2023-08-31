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

Automated Testing includes all the testing that is carried out by a program, like W3C HTML validation.

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
| I would like to be able to guess the AI ship's positions. | Game allows users to guess positions. |  ![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/df09b351-ce9d-48a7-b588-7337cc901d2c)|
| I would like to be able to win or lose. | Once either the player or AI has cleared all ships they are declared the winner  |  ![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/ff3134b7-9575-4d08-8272-a0d5bfe58b49)|
| I would like the AI to be intelligent enough to make winning a challenge. | The Ai remembers last ship it hit and will choose adjacent positions until the ship is clear | ![image](https://github.com/VitorBarbosaDev/VitorsMiniGames/assets/46977318/1bd6df30-21a7-4903-8fe3-502da7573bbd) |


### Full Testing


| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| `Buttons` |
|  |  |  |  |  |
| Play Button| Request username if null | Clicked button | asked user to input a string. | Pass |
| Play Button| Starts game if name input is not null.| Clicked button | Starts Game. | Pass |
| Mute Button | When clicked changes string and mutes and unmutes. | Clicked button | Unmuted or muted and changed string to reflect. | Pass |
| How to play Button | When clicked, pops up with a screen explaining how to play. | Clicked button | Shows how to play screen. | Pass |
| Leaderboard Button| When clicked, pops up a leaderboard screen with multiple scores gathered from the Firebase database. | Clicked button | pops up with leaderboard screen and allows scroll. | Pass |
| Fullscreen Button | When clicked, full screens the tab and also disappears on smaller screens. | Clicked button | full screens the tab and also disappears on smaller screens. | Pass |
| Restart Button | When clicked, restarts game | Clicked button | restarts game. | Pass |
| `Game Features` |
|  |  |  |  |  |
| Player Jump | When the screen is tapped, the space bar is pressed or clicked the screen player should jump. | Clicked screen, pressed spacebar and tapped screen | player jumps after all inputs. | Pass |
| Sounds | All sounds should play correctly when actions are performed. | I unmuted, died and jumped | background song is playing, jump plays when jump and die plays when crash into the obstacle. | Pass |
| Obstacles movement |  Obstacles should move to the other side of the screen and then reset to the right side | Played game | Obstacles move to one side and then appear on the other at the right time. | Pass |
| Obstacles height |  Obstacles have random heights | played game | Obstacles have random heights. | Pass |
| Score updates |  Score should update once player goes passed obstacles | played game | Score updates once a player goes past obstacles. | Pass |
| Score update leaderboard |  Once the game is over send the score to the database | played game | Once the game is over score is sent to the database and viewable on the leaderboard screen. | Pass |
| Pull leaderboard Scores |  Once the game is over scores are pulled from the database | played game |  Once the game is over scores are pulled from the database and viewable on the leaderboard screen. | Pass |
| `screens` |
|   |   |   |   |
| Leaderboard Screen| Once open player should be able to close by clicking outside the screen or using the x button. | Clicked outside and x button  | closes correctly | Pass |
| How to play Screen| Once open player should be able to close by clicking outside the screen or using the x button. | Clicked outside and x button  | closes correctly | Pass |
|   |   |   |   |  |

 - - -


## BUGS

### Known Bugs

Sometimes the resizing can be a bit funny and causes the game to restart.


### Solved Bugs

| No | Bug | How I resolved the issue |
| :--- | :--- | :--- |
| 1 | The player would double job if multiple inputs were inputted at the same time. | To fix this, I added a tiny time when a player can't jump again |
| 2 | When the height and width of the canvas were set to 100%% canvas text would stretch | In order to fix this, I removed that CSS and made it so the text was responsive in js. |
| 3 | The player could go above or below the canvas. | In order to fix this, I added a limit to stop the player from jumping too high and the player dies if he goes to the bottom. |
| 4 | Players on mobile couldn't tell where the column was. | In order to fix this, I added a marker to make it a bit easier for them to predict. |
| 5 | Game would run at different framerates depending on the device causing jumps and other variables to be different. | In order to fix this, I made the game time-dependent instead of frame rates so now the values I set feel the same everywhere. |
| 6 | Making codes for Firebase a bit more secure. | In order to fix this, I added them to a different file and encrypted them so that while easily breakable they are no longer in plain text I also added rules to the database that only allows scores and names to be added. |
