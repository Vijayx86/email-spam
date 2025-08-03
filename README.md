# AIMail – Python Gmail Cleanup Tool

A minimal Gmail utility designed to help automatically review and clean unwanted emails from your inbox, with optional AI-powered detection.

## Features

* Secure OAuth-based Gmail access
* AI analysis using state of the art models to flag suspicious messages
* Preview-before-delete mode
* Command-line usage with flexible arguments

## Basic Setup

1. Have Python 3 installed
2. Enable Gmail API in your Google Cloud project
3. Download your OAuth credentials JSON
4. Run:

```bash
pip install -r requirements.txt
python main.py
```

## Usage Examples

| Action                  | Command                                |
| ----------------------- | -------------------------------------- |
| Preview flagged emails  | `python main.py`                       |
| Process more emails     | `python main.py --max-emails 200`      |
| Delete flagged emails   | `python main.py --delete`              |
| Custom credentials file | `python main.py --credentials my.json` |

## File Overview

```
AIMail/
├── main.py              # Entry point
├── requirements.txt     # Dependencies
└── README.md            # (this file)
```

---

Made By Vijay ♥
