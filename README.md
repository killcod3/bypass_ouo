# bypass_ouo

`bypass_ouo` is a Python package that provides a method to bypass the ouo.io URL shortener. It is designed to handle reCAPTCHA challenges automatically and retrieve the original URL.

## Installation

To install `bypass_ouo`, simply use pip:

```bash
pip install bypass_ouo
```

## Usage

Here's a simple example of how to use `bypass_ouo`:

```python
from bypass_ouo import bypass_ouo

original_url = bypass_ouo("http://example.ouo.io")
print(original_url)
```

Replace `"http://example.ouo.io"` with the ouo.io URL you want to bypass.

## Features

- Automatic handling of reCAPTCHA challenges.
- Simple and intuitive interface.
- Returns the original URL hidden behind the ouo.io link.

## Requirements

`bypass_ouo` requires the following packages:

- beautifulsoup4
- curl_cffi
- requests

## Contributing

Contributions to `bypass_ouo` are welcome! Please read our Contributing Guidelines for details on how to submit pull requests.

## Testing

The package comes with a series of tests to ensure functionality. To run these tests, navigate to the project directory and run:

```bash
python -m unittest
```

## License

`bypass_ouo` is released under the MIT License.

## Author

`bypass_ouo` was created by @killcod3. You can find more about me and my work on [GitHub](https://github.com/killcod3).

## Disclaimer

This package is for educational purposes only. The author is not responsible for any misuse or for any damage that you may cause using this tool.
