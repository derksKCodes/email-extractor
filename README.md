
# 📧 Email Crawler

A **Python script to extract email addresses from any website** by crawling Contact pages, About pages, and pages linked via social media icons.

---

## 🚀 Features

✅ Crawl **any website** and extract publicly listed email addresses  
✅ Automatically discovers **Contact** and **About** pages  
✅ Follows **social media links** (Facebook, Twitter, LinkedIn) for additional email collection  
✅ Outputs a **clean, deduplicated list of emails** for outreach or data analysis  
✅ Lightweight and easy to configure for different websites  

---

## 🛠️ Tech Stack

- **Python 3.8+**
- `requests` for HTTP requests
- `BeautifulSoup` for HTML parsing
- `re` for email pattern matching
- `tqdm` for optional progress bars

---

## 📦 Installation

### 1️⃣ Clone the repository:

```bash
git clone https://github.com/derksKCodes/email-extractor.git
cd email-extractor
```

### 2️⃣ (Optional but recommended) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚡ Usage

### Basic Usage

Run the crawler by specifying the target URL:

```bash
python email_crawler.py --url "https://example.com"
```

### Advanced Options

```bash
python email_crawler.py --url "https://example.com" --depth 2 --output extracted_emails.txt --verbose
```

### Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--url` | Target website URL to crawl | Required |
| `--depth` | Crawling depth (how many levels deep) | 2 |
| `--output` | Output file name for extracted emails | emails.txt |
| `--verbose` | Enable verbose logging | False |

### Example Output

```
Found emails:
- contact@example.com
- info@example.com
- support@example.com

Total emails found: 3
Results saved to: emails.txt
```

---

## 📂 Project Structure

```
email-crawler/
│
├── email_crawler.py          # Main crawler script
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── examples/
    ├── sample_output.txt     # Example output file
    └── test_urls.txt         # Test URLs for development
```

---

## 🔧 Configuration

Create a `config.py` file to customize crawler behavior:

```python
# Crawler settings
USER_AGENT = "Mozilla/5.0 (compatible; EmailCrawler/1.0)"
REQUEST_DELAY = 1  # Seconds between requests
MAX_RETRIES = 3
TIMEOUT = 10

# Email patterns
EMAIL_PATTERNS = [
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
]

# Pages to prioritize
PRIORITY_PAGES = ['contact', 'about', 'team', 'staff']

# Social media domains to follow
SOCIAL_DOMAINS = ['facebook.com', 'twitter.com', 'linkedin.com']
```

---

## 🛡️ Ethical Considerations

⚠️ **Important Guidelines:**

- ✅ Use this tool only on websites you own or have permission to crawl
- ✅ Avoid excessive requests that could disrupt servers
- ✅ Respect `robots.txt` where applicable
- ✅ Consider implementing rate limiting for large-scale crawling
- ✅ Use extracted emails responsibly and in compliance with GDPR/CAN-SPAM

---

## 📊 Performance & Limitations

### What it can do:
- Extract emails from static HTML content
- Follow internal links up to specified depth
- Handle basic redirects and common page structures
- Filter out common false positives

### Current limitations:
- Cannot extract emails from JavaScript-rendered content
- Limited by website's rate limiting and anti-bot measures
- May miss emails embedded in images or encoded formats

---

## 🔄 Upcoming Features

- [ ] **Proxy support** for scalable crawling
- [ ] **Rate limiting** and polite crawling mechanisms  
- [ ] **CSV/JSON export** for structured outputs
- [ ] **JavaScript rendering** support using Selenium/Playwright
- [ ] **Email validation** to filter out invalid addresses
- [ ] **Duplicate domain detection** to avoid redundant crawling

---

## 🧪 Testing

Run the test suite:

```bash
python -m pytest tests/
```

Test with sample URLs:

```bash
python email_crawler.py --url "https://httpbin.org/html" --verbose
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run linting
flake8 email_crawler.py

# Run tests
pytest tests/ -v
```

---

## 📈 Changelog

### v1.0.0 (Latest)
- Initial release with basic crawling functionality
- Email extraction from Contact and About pages
- Social media link following
- Command-line interface

---

```
MIT License

Copyright (c) 2024 Email Crawler

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 📬 Support & Contact

For questions, bug reports, or feature requests:

- **GitHub Issues**: [Create an issue](https://github.com/derksKCodes/email-crawler/issues)
- **Email**: 
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/derks01)

---

## ⭐ Acknowledgments

- Built with ❤️ using Python
- Inspired by the need for efficient email discovery tools
- Thanks to the open-source community for the amazing libraries

---

**⚠️ Disclaimer**: This tool is for educational and legitimate business purposes only. Users are responsible for ensuring compliance with applicable laws and website terms of service.