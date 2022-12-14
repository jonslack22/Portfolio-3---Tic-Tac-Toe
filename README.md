## Introduction

This project represents Portfolio Project 3 of Code Institute's Full Stack Software Development diploma. The primary programming language for project 3 is Python. I decided to create a Python version of Tic-Tac-Toe, or "Noughts and Crosses", as it is sometimes referred to.

Tic-Tac-Toe is a basic 2-player strategy game. It is played on a 3 by 3 grid, drawn up on paper or using a board. Players take turns in marking grid spaces using a 'X' or 'O' letter. The first player to attain three of their letter in a row, whether vertically, horizontally or diagonally, wins.

## Features for Future Implementation
*The project, as is, is feature-complete under my initial project scope. The following features would be of high priority for expanding the project:

- Introducing modal difficulty levels of the computer opponent. The current algorithm is very tough to beat. I would introduce two selectable easier opponents; speculatively, I would have the easiest opponent fail to check for both making winning moves and blocking winning moves, and another opponent having a percentage chance for the winning move check and blocking a winning move checks to be skipped, under the current algorithm.
- Creating an option for a 2 player version of the game, replacing the computer.


## Issues/Bugs

- Solved issues/bugs:
    - I experimented with editing the syntax of the choose_letter function after viewing a refactoring suggestion by Pylint to change it to use 'while in' instead of 'while not or'. However, the change caused the choose_letter function to be skipped from the perspective of testing in Gitpod's terminal. The syntax change was reversed and later refactored to use the set() constructor. These changes can be seen in the commit history.

    - After introducing the clear_console function as a means of clearing the terminal display of specific content, the game's announcement of who goes first was being skipped, and the player would come to see an empty grid for their first turn, or a grid with an instance of the computer having made its first move. I changed the print statement of the parent while loop to an input statement and redefined the introductory message and text within a new function (that also calls the clear_console function) to solve this. This can be seen in the commit history.

- Remaining bugs:
    - A bug regarding the ASCii art 'Tic Tac Toe' previously caused a small number of the ' | ', ' / ', ' ( ', ' ) ' and ' - ' characters to be displayed on the right-hand of the Gitpod terminal. The issue was traced to the presence of a '\' character in the 'e' letter of the ASCii art being the only character not recognised as a string character, . I replaced the rogue '\' with a '|' and this resolved the display issue, but did not address the underlying cause of the bug. I consider the current implementation a temporary fix.

    ![ASCii display bug](assets/readme_files/ascii_bug.PNG)

## Technologies Used
### Main Languages Used
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to Python Wiki")

### Frameworks, Libraries & Programs Used
- [GitPod](https://gitpod.io/ "Link to GitPod homepage")
    - GitPod was used for writing code, committing, and then pushing to GitHub.
- [GitHub](https://github.com/ "Link to GitHub")
    - GitHub was used to store the project after pushing.
- [Lucid](https://lucid.app/ "Link to Lucid homepage")
    - Lucid was used to create a flowchart of information in two instances; namely, for the nature of game progression, and the algorithm of the computer.


## Automated Testing

### Code Validation

The [PEP8 Online Checker](https://extendsclass.com/python-tester.html/) was used to validate the project's code.

**Outcome**

<details>
<summary>run.py Validation results</summary>

![run.py Validation results](assets/readme_files/pep8_validation.PNG.png)

</details>

## User Testing

The project was tested by my friend, a software tester and developer by trade, who provided useful suggestions on improving the UI and critiquing the project as a whole.

## Credits

The algorithm used by the computer, as defined by and slightly modified in the function 'computer_move' can be credited to [Chapter 10 of "Invent With Python" by Al Sweigart](http://inventwithpython.com/chapter10.html "Link to Chapter 10 of 'Invent With Python")

The function known as 'clear_console' can be credited to an answer of a question on [Stack Overflow](https://stackoverflow.com/questions/2084508/clear-terminal-in-python "Link to a Stack Overflow page concerning clearing a Python terminal")

Being able to centralise many of the text and grid elements of the game, as well as introducing line breaks via variables came about after viewing the code of a [Python Battleships game](https://github.com/Becky139/Battleship "Link to a fellow student's game").

The ASCII art of the game, later modified because of a bug, can be credited to an [ASCII art generator](http://www.network-science.de/ascii/ "Link to an ASCII art generator")

### Code

I consulted a wide array of sites for ideas and examples of how to structure a Python implementation of Tic Tac Toe. The following sites were used most frequently:

- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [W3Schools](https://www.w3schools.com/ "Link to W3Schools page")

## Acknowledgements

- I would like to thank my friend and software tester, Paolo Ferrier, for his help in testing the project
- I would like to thank my mentor Seun, for pointing me in the right direction in researching for building a Tic Tac Toe game.

[Back to top ⇧](#)