[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12803302&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Aquarium Tour >>
## CS110 Final Project  Fall, 2023

## Team Members

Megan Eng, Mingyang Liu

***

## Project Description

Creating a visual tour for Acquarium which user can see pictures and introductions of each part. Then, the user can quit the screen as soon as they want.

***    

## GUI Design
### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design
### Features

1. Start menu 
2. Moving character
3. Interact with objects/exhibits
4. Pop up screens with information
5. Ending menu

### Classes

- << You should have a list of each of your classes with a description >>

Player 
 A circle that the user can move by clicking on the up, down, left, and right keyboard keys

Timer 
 A timer used in the backend to determine how far the player moves

FishTank 
 A rectangle that the user can collide with to recieve a pop-up window with more information about the exhibit

Button 
 Anytime the user clicks on a button, the controller prompts a new event  

## ATP

Test Case 1: Menu Navigation
    Description: Test the navigation through the game's main menu.
    Test Steps:
        1. Start the game.
        2. Click on the Start Button.
    Expected Outcome: The main menu should allow the player to navigate to the Game Screen.

Test Case 2: Player Movement
    Description: Verify that the player can move up, down, left, and right without leaving the game screen bounds.
    Test Steps:
        1. Start the game.
        2. Click on the Start Button.
        3. Press the left arrow key 3-4 times.
        4. Verify that the player moves left without going off of the screen.
        5.Press the right arrow key 3-4 times.
        6.Verify that the player moves right without going off of the screen.
        7.Press the up arrow key 3-4 times.
        8.Verify that the player moves up without going off of the screen.
        9.Press the down arrow key 3-4 times.
        10.Verify that the player moves down without going off of the screen.
    Expected Outcome: The player  should move left,right, up, and down in response to the arrow key inputs.

Test Case 3: Collision Detection

    Test Description: Ensure that collisions between the player's bullets and enemy ships are detected correctly.
    Test Steps:
    Start the game.
    Fire a player's bullet towards an enemy ship.
    Verify that the bullet hits the enemy ship.
    Fire a player's bullet that misses the enemy ship.
    Verify that no collision is detected.
    Expected Outcome: Bullets should correctly collide with enemy ships.

Test Case 4: 
    Description:
    Test Steps:
        1. 
    Expected Outcome: 

Test Case 5: Game Over Condition

    Test Description: Confirm that the game ends when the player loses all lives.
    Test Steps:
    Start the game.
    Play until the player loses all lives.
    Verify that the game displays a "Game Over" message.
    Expected Outcome: The game should display a "Game Over" message when the player loses all lives.





