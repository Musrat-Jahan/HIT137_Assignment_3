# Report: Assignment 3 

## Overview

This report summarizes the tasks and objectives of the third assignment, focusing on the development of applications using programming concepts and teamwork through GitHub collaboration.

## Introduction
This assignment encompasses the creation of a Tkinter application and a 2D side-scrolling game, along with setting up a GitHub repository for group collaboration. The goals include:

1. Building a Tkinter application using object-oriented programming (OOP) concepts.
2. Developing a simple side-scrolling 2D game using Pygame.
3. Establishing a public GitHub repository for team contributions and documentation.

## Question 1: Tkinter Application Development
The first task involves creating a Tkinter application that utilizes various OOP concepts:

- **Multiple Inheritance**: Combining functionalities of multiple classes into a single class to promote code reusability.
- **Encapsulation**: Keeping data safe by restricting access to certain components of the application.
- **Polymorphism**: Allowing methods to do different things based on the object it is acting upon.
- **Method Overriding**: Redefining a method in a derived class to change its behavior.

### Example
A potential application is a simple image classification tool that uses pre-trained AI models. The application should:

1. Allow users to upload an image.
2. Send the image data to an AI model for classification.
3. Display the classification results on the interface.

### Question 2: Pygame Side-Scrolling Game
### Question 2 : 2D Side-Scrolling Game with Pygame

This is a 2D side-scrolling game built with Python and Pygame. In the game, the player controls a character that can move, jump, and shoot. The game includes enemies to fight, items to collect, three levels to complete, and a score system to track progress. There is also a health bar, lives system, and a boss at the end of the game.

#### **Game Design**
The game is made up of several parts, including player controls, projectiles, enemies, items to collect, and three different levels.

#### **Player Class**
The player character can do the following:
- **Move**: Move left and right across the screen.
- **Jump**: Perform jumps to avoid obstacles or reach higher platforms.
- **Health & Lives**: The player has a health bar. If the health goes to zero, they lose a life. The game is over when all lives are lost.
- **Shoot**: The player can shoot to fight enemies.

#### **Projectile Class**
Projectiles are the bullets or objects that the player shoots.
- **Move**: Projectiles fly in a straight line.
- **Damage**: They damage enemies when they hit them.
- **Disappear**: They vanish when they hit an enemy or go off the screen.

#### **Enemy Class**
Enemies are the characters or objects that the player has to defeat. 
- **Move**: Enemies might walk, fly, or patrol an area.
- **Attack**: Some enemies might attack or damage the player if touched.
- **Health**: Each enemy has health. When it reaches zero, they disappear.
- **Boss Enemy**: The final level has a stronger enemy that is harder to defeat.

#### **Collectible Class**
Collectibles are items that help the player.
- **Heal**: Restore the player’s health.
- **Extra Life**: Give the player an additional life.

#### **Level Design**
The game has three levels that get harder as the player progresses. The levels include:
- **Level 1**: A simple start with easy enemies.
- **Level 2**: More difficult with more enemies and obstacles.
- **Level 3**: The final challenge with a boss fight at the end.

#### **Scoring System**
The player earns points for:
- **Defeating enemies**.
- **Collecting items**.
The score increases as the player progresses through the levels and defeats more enemies or finds more collectibles.

#### **Health Bar and Lives**
- **Player Health Bar**: Shows the player’s health, which decreases if they take damage.
- **Enemy Health Bar**: Shows how much health enemies have left.
- **Lives**: The player starts with a few lives. If they lose all lives, it’s game over.

#### **Game Over Screen**
When the player loses all lives, a "Game Over" screen appears. The player can choose to restart the game and try again.

#### **Restart and Levels**
Players can restart the game from the beginning after losing. After beating a level, they move on to the next one.

#### **Output**
Output of this 2D side-scrolling game:
![pygame](Output/Q2pygame.png)

---
### Question 3: GitHub Repository Setup
The final task is to create a public GitHub repository for group collaboration:

1. **Repository Creation**: Establish a public repository for the assignment and ensure it is accessible to all group members.
2. **Adding Members**: Invite group members to the repository, ensuring they have permissions to contribute.
3. **Documentation of Contributions**: Use descriptive commit messages and document all changes in the repository to reflect team efforts.

#### Submission Guidelines
- **Zip File**: Compress all programming files and outputs for submission.
- **GitHub Link**: Include the GitHub repository link in the submission.

### Conclusion
This assignment emphasizes the importance of programming concepts, game design, and collaboration using GitHub. It showcases skills in application development and teamwork, preparing students for real-world software development practices.## Question 3: GitHub Repository

### Create a Public GitHub Repository

- **Repository Name**: `HIT137_Assignment_3`
- **Visibility**: Public

### Add Group Members

- **Collaborators**: Add all group members to the repository as collaborators.
- **Permissions**: Ensure all members have appropriate permissions to push code, manage issues, and review pull requests.

#### Document Contributions
- **Description**: This repository contains code and documentation for Assignment 2, including text extraction, NLP tasks, image manipulation, and string manipulation.
- **Commits**: Use descriptive commit messages to document changes and updates.
- **Issues**: Track tasks and bugs using GitHub Issues. Assign issues to team members and provide clear descriptions.
- **Pull Requests**: Create pull requests for code reviews and merging changes. Include explanations of what changes are made and why.

#### Submission

- **Final Submission**: Provide the GitHub repository link (https://github.com/Musrat-Jahan/HIT137_Assignment_3.git))  as part of final submission. 
- **Documentation**: Ensure that all group members’ contributions are visible in the commit history and pull requests.
- **Code Review**: Make sure that the repository is well-documented, with clear comments and explanations for code changes.

# Conclusion

The report outlines key tasks for demonstrating skills in data extraction, NLP techniques, image manipulation, and teamwork with GitHub, focusing on individual research and group work, with real-world applications like biomedical text analysis and coding challenges.

