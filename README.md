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

## Issues and Bugs

- Solved bugs:

- Remaining bugs:
    - A curious bug regarding the ASCii art 'Tic Tac Toe' previously caused a small number of the '\, |, / and -' characters to be spliced and displayed on the right-hand of the Gitpod terminal. The issue was traced to the presence of a '\' character in the 'e' letter of the ASCii art being recognised not as a string character, despite other '\' characters in the art being interpreted as desired. I replaced the rogue '\' with a '|' and this resolved the issue, but did not address the original problem of the character's misinterpretation. I consider the current implementation a temporary fix.

    ![ASCii display bug](assets/readme_files/ascii_bug.PNG)

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