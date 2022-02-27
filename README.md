# Introduction

`scripts` is a collection of scripts that I use to automate my development workflow.

## Installation

* Clone this repository to your local machine

    ```bash
    git clone https://github.com/harmonify/scripts
    ```

* Install Python version 3.6 or higher [here](https://www.python.org/downloads/)
* Add Python to your PATH
* Add the cloned repository to your PATH, for convenience

### Add a new PATH variable

Some links to community answers on how to add a new PATH variable to your local machine:

* [For Windows](https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho)
* [For Linux](https://unix.stackexchange.com/questions/26047/how-to-correctly-add-a-path-to-path)

## Usage

An example of using `ginit`, a script that initializes a new Git repository and adds common metadata files to it:

```bash
# without adding the `scripts/` folder to your PATH
python ginit

# with adding the `scripts/` folder to your PATH
ginit
```

Refer to each script, `<script> --help`, for more information.

## Contributing

You can contribute to this project by making a pull request or opening an issue.

## Author

* [Harmonify](https://github.com/harmonify)

## License

This project is licensed under the MIT license. See the [LICENSE](LICENSE) file for more information.
