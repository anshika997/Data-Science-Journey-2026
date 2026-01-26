## CodeBook Data Science Internship – Task 1

##  Project Overview
Welcome to **CodeBook – The Social Media for Coders**.  
This project is part of a **Data Science Internship assignment**, where user data is analyzed using **pure Python only** (no pandas, NumPy, or external libraries).

The dataset represents CodeBook users, their friends, and the pages they have liked.

---

##  Objective
The objective of this task is to:
- Load JSON data using Python built-in modules
- Understand the structure of the dataset
- Display users, their connections, and available pages in a readable format

---

##  Dataset Description

The data is stored in JSON format and contains:

### Users
Each user has:
- `id` : Unique user ID  
- `name` : User name  
- `friends` : List of friend user IDs  
- `liked_pages` : List of liked page IDs  

### Pages
Each page has:
- `id` : Unique page ID  
- `name` : Page name  

### Relationships
- A user can have multiple friends
- A user can like multiple pages

---


