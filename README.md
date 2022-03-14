[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7137750&assignment_repo_type=AssignmentRepo)

# automaton

### First LFA Lab

Exercise 1. Implement a library/program in a programming language of your
choosing to load and validate the following input file:

```
Sigma :
    a
    b
End

States :
    1
    2
    3 ,F
    5 ,S
End

Transitions :
    1, a , 2
    1, b , 3
    2, a , 2
    2, b , 3
    3, a , 1
    5, b , 2
End
```

Sections can be in any order. By validation we ask to check that transition
section has valid states (first and third word) and valid words (word two). Note
that states can be succeeded by ”F”, ”S”, both or nothing. ”S” symbol can
succeed only one state.

Exercise 2. Familiarize yourself with Python Notebooks if python is your language of choice.

Exercise 3. Familiarize yourself with Latex (overleaf.com).
