[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12803302&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Aquarium Tour >>
## CS110 Final Project  Fall, 2023

## Team Members

Megan Eng, Mingyang Liu

***

## Project Description

Creating a visual tour for Acquarium which user can interact with different exhibits to learn more about the animal.

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
3. Interact exhibits
4. Pop up screens with information
5. End Screen

### Classes

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
    Description: Verify that the player can move up, down, left, and right.
    Test Steps:
        1. Start the game.
        2. Click on the Start Button.
        3. Press the left arrow key 1-2 times.
        4. Verify that the player moves left.
        5.Press the right arrow key 1-2 times.
        6.Verify that the player moves right.
        7.Press the up arrow key 1-2times.
        8.Verify that the player moves up.
        9.Press the down arrow key 1-2 times.
        10.Verify that the player moves down.
    Expected Outcome: The player should move left, right, up, and down in response to the arrow key inputs.

Test Case 3: Collision Detection
    Test Description: Ensure that the player can collide with fishtanks without going off the screen.
    Test Steps:
        1. Start the game.
        2. Click on the Start Button.
        3. Freely move the character with the arrow keys so that it is makes contact with each fish tank.
    Expected Outcome: The Player should be able to touch each fish tank without going off the screen.

Test Case 4: Pop Up Window 
    Description: Ensure that when the player collides with a fishtank, a "pop up window" is displayed
    Test Steps:
        1. 1. Start the game.
        2. Click on the Start Button.
        3. Move the character with the arrow keys so that it is touching the fish tank and a "pop up window" will appear.
        4. Press on any arrow key to have the "pop up window" dissapear.
        5. Repeat steps 3-4 for all fish tanks.
    Expected Outcome: A Pop up Window should open and give information about the exhibit. The player colliding with the top left tank should not display the same information as when the player collides with the bottom right tank. Each tank corresponds to a different exhibit and there are 6 different exhibits.

Test Case 5: Game Over Condition
    Test Description: Confirm that the game ends when the player has viewed all fish tanks.
    Test Steps:
        1. Start the game.
        2. Click on the Start Button.
        3. Move the character with the arrow keys so that it is touching the fish tank.
        4. Press on any arrow key to have the pop up window disappear.
        5. Repeat steps 3-4 for all fish tanks.
        6. Verify that the game displays a "You Finished!" message.
    Expected Outcome: The game should display a "You Finished!" message when the player has viewed all aquarium exhibits.





