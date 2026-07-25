# DevUtilityTool

A developer productivity CLI tool built with **Python** and **Typer** to automate common development tasks. The project follows a modular, service-based architecture and a professional Git/GitHub workflow using feature branches and pull requests.

---

## ✨ Features

* Create new projects instantly
* Initialize Git repositories
* Create Python virtual environments
* Generate projects from templates
* Organize files by type
* Generate cryptographically secure passwords
* Generate text and file hashes
* Validate project names
* Custom exception handling
* Modular and scalable architecture

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-github-username>/DevUtilityTool.git
```

### 2. Navigate to the project

```bash
cd DevUtilityTool
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 📖 Commands

## 👋 Greeting

Print a simple greeting message.

```bash
python main.py hello
```

---

## 📁 Initialize Project

Create a new project.

```bash
python main.py init MyProject
```

Create a project with Git initialized.

```bash
python main.py init MyProject --git
```

Create a project with a Python virtual environment.

```bash
python main.py init MyProject --venv
```

Create a project using the default template.

```bash
python main.py init MyProject --template default
```

Create a FastAPI project.

```bash
python main.py init MyProject --template fastapi
```

---

## 📂 File Organizer

Organize files into folders based on their extensions.

```bash
python main.py organize Downloads
```

Example output:

```text
Downloads/
│
├── Images/
├── Documents/
├── Videos/
├── Music/
├── Python/
└── Archives/
```

---

## 🔐 Password Generator

Generate a cryptographically secure password.

Default password (12 characters):

```bash
python main.py password
```

Generate a password with a custom length.

```bash
python main.py password --length 20
```

Generate a password without symbols.

```bash
python main.py password --no-symbols
```

Generate a password without digits.

```bash
python main.py password --no-digits
```

Generate a password with lowercase letters only.

```bash
python main.py password \
    --no-uppercase \
    --no-digits \
    --no-symbols
```

---

## 🔑 Hash Generator

Generate the hash of text.

Default (SHA-256):

```bash
python main.py hash "Hello World"
```

Generate an MD5 hash.

```bash
python main.py hash "Hello World" --algorithm md5
```

Generate a SHA-1 hash.

```bash
python main.py hash "Hello World" --algorithm sha1
```

Generate the hash of a file.

```bash
python main.py hash document.pdf
```

Generate the hash of a file using MD5.

```bash
python main.py hash document.pdf --algorithm md5
```

Supported algorithms:

* MD5
* SHA-1
* SHA-256

---

# 🏗️ Project Structure

```text
DevUtilityTool/
│
├── src/
│   ├── commands/
│   │   ├── greet.py
│   │   ├── hash.py
│   │   ├── init.py
│   │   ├── organize.py
│   │   └── password.py
│   │
│   ├── config/
│   │   ├── file_type.py
│   │   └── hash_algorithms.py
│   │
│   ├── services/
│   │   ├── git_service.py
│   │   ├── hash_service.py
│   │   ├── organizer_service.py
│   │   ├── password_service.py
│   │   ├── project_creator.py
│   │   ├── project_initializer.py
│   │   ├── template_service.py
│   │   └── venv_service.py
│   │
│   ├── app.py
│   └── __init__.py
│
├── templates/
│   ├── default/
│   └── fastapi/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🏛️ Architecture

The project follows a layered architecture.

### Commands Layer

Responsible for parsing CLI arguments and interacting with the user.

### Services Layer

Contains the business logic.

### Config Layer

Stores reusable configuration values such as supported file types and hashing algorithms.

This separation of concerns makes the project easy to maintain, test, and extend.

---

# 🛣️ Roadmap

## ✅ Completed

* [x] Greeting command
* [x] Project initialization
* [x] Git integration
* [x] Python virtual environment creation
* [x] Project templates
* [x] File organizer
* [x] Secure password generator
* [x] Text and file hash generator
* [x] Custom exception handling

## 🚧 Planned

* [ ] Duplicate file finder
* [ ] JSON formatter
* [ ] Bulk file renamer
* [ ] Logging support
* [ ] Unit tests
* [ ] Configuration file support
* [ ] Publish to PyPI

---

# 🛠️ Technologies Used

* Python 3
* Typer
* Pathlib
* Hashlib
* Secrets
* Shutil
* Subprocess
* Git
* GitHub

---

# 🎯 Learning Objectives

This project is being developed to practice and demonstrate:

* Python application architecture
* CLI development with Typer
* File and directory handling
* Secure password generation
* File hashing
* Git automation
* Exception handling
* Modular software design
* Professional Git and GitHub workflow

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 🚧 Project Status

This project is currently under active development and is being built as a learning project to explore Python CLI development and software engineering best practices.

While many features are functional and follow clean architectural principles, the project is not yet intended for production use. Planned improvements include comprehensive unit tests, CI/CD, enhanced logging, configuration management, packaging for PyPI, and additional CLI utilities.

---

# 📄 License

This project is licensed under the MIT License.
