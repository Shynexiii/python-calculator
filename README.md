# Python Calculator README

Welcome to the Python Calculator project, a straightforward script that performs basic arithmetic operations on integer inputs. This project is designed with a CI/CD pipeline using GitHub Actions to automate integration and deployment processes.

## Prerequisites

- Python 3.x installed on your machine.
- Docker installed if you want to run the application as a container.
- A GitHub account to set up and use GitHub Actions.

## Installation

To start using the Python Calculator:

```sh
git clone https://github.com/Shynexiii/python-calculator.git
cd python-calculator
```

The script does not require additional installations or dependencies.

## GitHub Actions CI/CD Pipeline

The `.github/workflows` directory contains the GitHub Actions workflow configurations that set up CI/CD for this project.

### Features

- **Continuous Integration:** Automates testing by running `test_calc.py` for each push or pull request to the main branch.
- **Continuous Deployment:** Deploys the application automatically once the main branch passes all tests.

To utilize the GitHub Actions CI/CD pipeline:

1. Fork the repository.
2. Go to the 'Actions' tab in your GitHub repository.
3. Enable GitHub Actions if it's not already set up.
4. Adjust the `.github/workflows` YAML files to fit your deployment targets.

GitHub Actions will trigger workflows based on the events defined in your repository (e.g., pushes to the main branch).

## Usage

To run the script:

```sh
python3 prog.py
```

Follow the prompts to perform an operation on two integers. The script will ask whether to continue or exit after displaying the result.

## Testing

Execute unit tests with:

```sh
python3 -m unittest test_calc
```

This will validate the arithmetic operations within the `calc.py` module.

## Docker Usage

Build a Docker image with:

```sh
docker build -t python-calculator .
```

Run your container:

```sh
docker run -it --rm python-calculator
```

## Conclusion

This README outlines the basic setup and use of the Python Calculator, including the implementation of a CI/CD pipeline with GitHub Actions to maintain a production-ready codebase.

Calculate with ease using the Python Calculator!
