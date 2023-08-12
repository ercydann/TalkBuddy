# Realtime Chat App

The Realtime Chat App is a web application that enables users to engage in real-time text-based conversations with their friends. Built using the Django framework, the app allows users to send and receive messages, view message history, and receive chat notifications. It fosters seamless communication and interaction between users.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
  - [Chat Index](#chat-index)
  - [Chat Detail](#chat-detail)
  - [Send Messages](#send-messages)
  - [Receive Messages](#receive-messages)
  - [Chat Notifications](#chat-notifications)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Realtime Chat App offers a platform for users to communicate with their friends in real-time. Whether it's casual conversations or important discussions, this app ensures that you can keep the conversation flowing seamlessly.

## Features

### Chat Index

- Display a list of friends to initiate chat conversations.
- Click on a friend's profile to open the chat detail page.

### Chat Detail

- Engage in real-time conversations with friends.
- View the chat history with your friend.
- Send new messages and receive messages in real-time.

### Send Messages

- Compose and send messages to friends.
- Messages are instantly delivered to the recipient.
- Message input supports text and multimedia.

### Receive Messages

- Receive new messages in real-time.
- Messages are instantly displayed in the chat.

### Chat Notifications

- Receive notifications for new unread messages.
- Notification count appears next to each friend's profile.

## Project Structure

The project structure is organized as follows:

- `mychatapp/`: The main Django app directory.
  - `templates/mychatapp/`: Contains HTML templates for the app's pages.
    - `index.html`: Displays the list of friends for chat.
    - `detail.html`: Displays the chat conversation with a friend.
  - `models.py`: Defines the database models for user profiles, friends, and chat messages.
  - `forms.py`: Contains form definitions for chat message input.
  - `views.py`: Implements the views for rendering pages and handling chat operations.
  
## Technologies Used

- Django
- JavaScript (AJAX)
- HTML
- CSS

## Installation

1. Clone the repository: `git clone https://github.com/your-username/realtime-chat-app.git`
2. Navigate to the project directory: `cd realtime-chat-app`
3. Set up a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
5. Install dependencies: `pip install -r requirements.txt`
6. Apply migrations: `python manage.py migrate`

## Usage

1. Run the Django development server: `python manage.py runserver`
2. Open your web browser and visit: `http://localhost:8000`
3. You can now use the Realtime Chat App to communicate with friends in real-time.

## Contributing

Contributions are welcomed! To contribute to the Realtime Chat App:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature/your-feature-name`
3. Implement your changes and commit: `git commit -m "Add your feature"`
4. Push your changes to your branch: `git push origin feature/your-feature-name`
5. Open a pull request on the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

---

Connect with us on LinkedIn:

## www.linkedin.com/in/danny-ercy-ndikuriyo

