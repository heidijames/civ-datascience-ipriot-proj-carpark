# IPRIoT Project: Simulated Workplace Scenario

A simulated workplace environment where students must demonstrate OO skills by interpreting and interacting with modern software requirements.

## Scenario

You are working as a junior software innovation engineer for the City of Moondalup in the Department of Transport. The department wants to upgrade a few public parking spaces by providing information about the number of available parking spots in near real time for each one. The parking lots in question do not have boom gates.

## Resources

For this project, you will be using foundational agile practices:

- An emphasis on collaboration and communication
- Small rapid iterations
- Minimal, user-focused documentation (how does this help the user?)

However, because in this simulation you may have limited access to developers and customers. They have provided you with some documentation to help get you started:

```text
│
├── docs/
│   ├── requirements.md
│   └── high_level_design.md
```

- **`requirements.md`**: provides a brief agile specification for the project. Please note that unlike a typical agile specifications some requirements are not-user driven but are constraints needed to achieve competency in the unit.
- **`high_level_design`**: because you are a junior developer, the senior developer was asked to write a more detailed specification to help you achieve some of the more difficult aspects of this project.

## Getting started

To get started with this project fork and then clone this repository:

1. From the top right, press **Fork**. This creates a copy of the repository in your GitHub account.

2. After the forking process is complete, press the green **Code** button *on your forked repository*.

3. Copy the URL displayed under "Clone with HTTPS" by pressing the clipboard icon next to it.

4. You did copy **your** forked repository URL, **not** this repository's URL, right?

5. Open a terminal (Command Prompt or Git Bash on Windows, Terminal on macOS and Linux) on your local machine.

6. Navigate to the directory where you want to clone the repository by using the `cd` command. For example:

```bash
cd /path/to/your/directory
```

7. Clone the repository to your local machine by running the `git clone` command followed by the copied URL:

```bash
git clone https://github.com/your-username/civ-ipriot-proj-carpark.git
```

### Making local changes

1. Change to the cloned repository's directory:

```bash
cd civ-ipriot-proj-carpark
```

2.  Create a new branch for your local modifications by running:

```bash
git checkout -b your-new-branch-name
```

Now you can make local modifications to the project files. After you have made the desired changes, follow these steps to commit and push them:

1. Stage the modified files by running:

```bash
git add .
```

2. Commit the changes with a descriptive message:

```bash
git commit -m "Your commit message here"
```

3. Push the changes to your forked repository on GitHub:

```bash
git push origin your-new-branch-name
```

## Optional: Install this project as a module (makes imports easier!)

The `setup.py` file contains information about the project, its dependencies, and how to run the main script.

To install the SmartPark project as a module in development mode, follow these steps:

1. Open a terminal and navigate to the SmartPark project directory (the one containing `setup.py`). 
2. Ensure you have a virtual environment activated for the project. If not, you can create one using:

```bash
python3 -m venv .venv
```

Then activate the virtual environment:

- On Linux/macOS:

```bash
source .venv/bin/activate
```

- On Windows:

```bash
.venv\Scripts\activate
```

3. Install the SmartPark project in development mode using:

```bash
pip install -e .
```

This command installs the project in editable mode, which means any changes you make to the source code will be immediately reflected in the installed module.



Project Context
This project was developed in response to a simulated brief from the City of Moondalup’s Department of Transport. As a junior software innovation engineer, the task was to create a modular, object-oriented system to manage public parking spaces without boom gates. The solution had to support real-time carpark monitoring, configuration management, logging, and testing. Agile-inspired practices—such as rapid iteration, clear user-oriented features, and minimal documentation—guided the development process.

The system needed to:

    Monitor and display available parking bays in real time
    Record car entry and exit with timestamps
    Support modular, maintainable code using object-oriented principles
    Read configurations from an external file
    Generate logs in a structured format
    Include unit tests for key functionality


Features

    Modular code using Object-Oriented Programming (OOP)
    Entry and Exit sensors with automatic bay assignment
    Driver Display: shows current available bays and weather
    Admin Monitor: displays all parked cars and bay allocations
    Temperature display using simulated or placeholder weather
    Real-time fee calculation based on parking duration
    Configuration via external config.json file
    Logging of car activity to log.txt with timestamp, fee, and bay
    Two simulations: normal and full carpark
    Unit tests for Carpark and Display classes


Development followed simplified agile practices with an emphasis on iteration, user-focused output, and minimal but purposeful documentation.

The system uses a config.json file to set up key parameters such as:

{
  "location": "Moondalup City Square Parking",
  "total_spaces": 75
}

This makes it easy to modify the simulation for different carpark sites or capacities without changing the source code. The config is parsed using a custom config_parser.py module.

How to Run
Ensure you have Python 3.10 or later installed.

1. Install Required Packages
   (If using the placeholder weather script, no extra packages are needed. If using real API integration, run:)

```bash
    pip install requests
```
    
2. Run the main simulation
   From your project folder:  

```bash    
    python main.py
```    

3. This will simulate real-time activity including car entries, exits, available bays, driver display, admin monitor, and temperature (placeholder or real).


Testing

Unit tests are located in the tests/ folder. To run all tests:

```bash
    python -m unittest discover tests
```


4. Run alternate simulations (optional)
To explore additional behavior like a full carpark scenario:

```bash
    python test_simulations.py
```

5. Folder Structure

📂 civ-datascience-ipriot-proj-carpark  # Main project directory
├── 📂 Project Docs        # Documentation and supporting files
│   ├── LICENSE            # License file
├── 📂 docs                # Additional documentation and guidelines
├── 📂 smartpark           # Core system modules for parking management
│   ├── __init__.py        # Initializes the smartpark module
│   ├── display.py         # Handles driver and admin display functions
│   ├── models.py          # Defines data structures for parking system components
│   ├── sensors.py         # Manages car entry and exit detection
│   ├── weather.py         # Processes simulated or real weather data
├── 📂 tests               # Unit tests for validating functionality
│   ├── __init__.py        # Initializes the tests module
│   ├── test_carpark.py    # Tests for the Carpark class
│   ├── test_config.py     # Validates configuration handling
│   ├── test_display.py    # Ensures proper functionality of the Display module
├── 📂 __pycache__         # Compiled Python bytecode for optimization
├── .gitignore             # Specifies files Git should ignore
├── .gitattributes         # Defines Git attributes and file handling rules
├── README.md              # Project overview and instructions 
├── config.json            # Defines carpark settings (location, capacity, etc.)
├── config_parser.py       # Parses configuration data
├── log.txt                # Stores car activity logs with timestamps and fees
├── main.py                # Runs the carpark simulation
├── test_simulations.py    # Simulates various carpark scenarios
├── weather.txt            # Stores weather data output


6. GitHub Repository:
https://github.com/heidijames/civ-datascience-ipriot-proj-carpark


