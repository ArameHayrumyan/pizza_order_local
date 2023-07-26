[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/SG_4L6US)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11435034&assignment_repo_type=AssignmentRepo)
# pizza-ordering

## Task: Pizza Ordering
### Introduction: The pizza ordering platform which allows customer to choose necessary ingredients for their pizza and order a pizza with that ingredients.
#### Your API server should have:
- `/ingredients` endpoint, which returns list of types of available ingredients i.e. sausages, tomatoes, cheeses, etc.
- `/ingredients/<type>` endpoint, which returns all available ingredients of that type with their price, available quantity and image url
- `/order` endpoint, which
 1. accepts POST request
 2. receives JSON, which includes names of ingredients and their counts
 3. returns order ID, its final price and the time when it will be ready
- `/take/<order_id>` endpoint, which
 1. will set the status of order to done, if it was requested after the order was ready
 2. will return Will be ready in x minutes message, if it was requested too soon
