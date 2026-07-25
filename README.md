# DevUtilityTool

A developer productivity CLI built with **Python** and **Typer** to automate common development tasks. The project follows a modular, service-based architecture and a professional Git/GitHub workflow using feature branches and pull requests.

> **🚧 Project Status**
>
> This project is under active development and is being built as a learning-focused portfolio project to explore Python CLI development and software engineering best practices. Existing features are functional and follow clean architectural principles, while additional features and improvements are planned before the first stable release.

---

# ✨ Features

* 📁 Create new projects instantly
* 🌿 Initialize Git repositories
* 🐍 Create Python virtual environments
* 📦 Generate projects from templates

  * Default
  * FastAPI
* 📂 Organize files automatically by file type
* 🔐 Generate cryptographically secure passwords
* 🔑 Generate hashes for text and files
* ✅ Validate project names
* ⚠️ Custom exception handling
* 🏗️ Modular service-based architecture
* 🌳 Professional Git feature-branch workflow

---

# 🚀 Installation

## Prerequisites

* Python 3.10 or later
* Git *(optional, only required for Git initialization)*

---

### 1. Clone the repository

```bash
git clone https://github.com/<your-github-username>/DevUtilityTool.git
```

### 2. Navigate into the project

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

### 6. Install the CLI in editable mode

```bash
pip install -e .
```

Verify the installation:

```bash
devtool --help
```

---

# 📖 Command Reference

| Command    | Description                       |
| ---------- | --------------------------------- |
| `hello`    | Print a greeting message          |
| `init`     | Create a new project              |
| `organize` | Organize files by extension       |
| `password` | Generate secure passwords         |
| `hash`     | Generate hashes for text or files |

---

# 👋 Greeting

Print a greeting message.

```bash
devtool hello
```

---

# 📁 Project Initialization

Create a new project.

```bash
devtool init MyProject
```

Create a project with Git initialized.

```bash
devtool init MyProject --git
```

Create a project with a virtual environment.

```bash
devtool init MyProject --venv
```

Create a project using the default template.

```bash
devtool init MyProject --template default
```

Create a FastAPI project.

```bash
devtool init MyProject --template fastapi
```

---

# 📂 File Organizer

Organize files into folders according to their file types.

```bash
devtool organize Downloads
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
├── C++/
├── CSV/
├── Packet_Tracer/
├── Archives/
└── MarkDowns/
```

Supported categories include:

* Images
* Documents
* Videos
* Music
* Python
* C++
* CSV
* Archives
* Packet_Tracer
* MarkDowns

---

# 🔐 Password Generator

Generate a secure password using Python's `secrets` module.

Generate the default password (12 characters).

```bash
devtool password
```

Generate a 20-character password.

```bash
devtool password --length 20
```

Exclude symbols.

```bash
devtool password --no-symbols
```

Exclude digits.

```bash
devtool password --no-digits
```

Generate a password containing lowercase letters only.

```bash
devtool password \
    --no-uppercase \
    --no-digits \
    --no-symbols
```

---

# 🔑 Hash Generator

Generate the SHA-256 hash of text.

```bash
devtool hash "Hello World"
```

Generate an MD5 hash.

```bash
devtool hash "Hello World" --algorithm md5
```

Generate a SHA-1 hash.

```bash
devtool hash "Hello World" --algorithm sha1
```

Generate the hash of a file.

```bash
devtool hash document.pdf
```

Generate the MD5 hash of a file.

```bash
devtool hash document.pdf --algorithm md5
```

### Supported Algorithms

| Algorithm | Supported |
| --------- | --------- |
| MD5       | ✅         |
| SHA-1     | ✅         |
| SHA-256   | ✅         |

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
├── pyproject.toml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🏛️ Architecture

The project follows a layered architecture.

### Commands Layer

Responsible for parsing CLI arguments and interacting with users.

### Services Layer

Contains the business logic of the application.

### Config Layer

Stores reusable configuration such as file-type mappings and supported hash algorithms.

This separation of concerns makes the project easier to maintain, test, and extend.

---

# 🛣️ Roadmap

## ✅ Completed

* [x] Greeting command
* [x] Project initialization
* [x] Git repository initialization
* [x] Python virtual environment creation
* [x] Project templates
* [x] File organizer
* [x] Secure password generator
* [x] Text hash generation
* [x] File hash generation
* [x] Project name validation
* [x] Custom exception handling

## 🚧 Planned

* [ ] Duplicate file finder
* [ ] JSON formatter
* [ ] Bulk file renamer
* [ ] Logging support
* [ ] Unit tests
* [ ] Configuration management
* [ ] GitHub Actions (CI)
* [ ] Publish to PyPI

---

# 🛠️ Technologies Used

* Python
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
* CLI application development with Typer
* Modular software design
* File and directory management
* Secure password generation
* File hashing
* Git automation
* Exception handling
* Professional Git & GitHub workflow

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.
