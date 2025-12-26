## 🎥 Demo Video

A complete walkthrough of the project implementation, execution, and outputs is available here:

👉 https://drive.google.com/file/d/1DSf8vVuP9i8ihc7RjRGAEIYCeu8IIyny/view


```text


📘 Pulse - Module Extraction AI Agent
📌 Overview

This project implements an AI-powered documentation module extractor that crawls help-documentation websites and automatically identifies:
  Modules (major product areas)
  Submodules (specific features/actions)
  Descriptions for each module and submodule
  The system processes documentation content only (no external knowledge) and outputs a clean, structured JSON suitable for product and documentation analysis.

🎯 Objective

To build a scalable, explainable, and deterministic AI agent that can:
   Crawl help documentation URLs
   Infer hierarchical structure (Module → Submodule)
   Generate concise descriptions
    Work across multiple documentation websites in a single run

🧠 High-Level Architecture

URL List
  ↓
Crawler (requests + BeautifulSoup)
  ↓
HTML Cleaner & Section Parser
  ↓
Module & Submodule Inference
  ↓
Rule-Based Summarization
  ↓
Structured JSON Output


## 📁 Project Structure

pulse-module-extractor/
│
├── src/
│   ├── crawler.py        # Crawls documentation pages
│   ├── parser.py         # Cleans HTML and extracts structured sections
│   ├── extractor.py      # Infers modules and submodules
│   ├── summarizer.py     # Generates concise descriptions
│   └── utils.py          # Helper utility functions
│
├── output/               # Generated JSON outputs
│
├── app.py                # Entry point (multi-website execution)
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation


🌐 Supported Documentation Websites (Processed in One Run)

The current configuration processes four documentation websites automatically:

https://help.instagram.com/
https://wordpress.org/documentation/
https://support.neo.space/hc/en-us
https://help.zluri.com/

Each website generates a separate JSON output file.

▶️ How to Run

1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the application
python app.py

3️⃣ Output
After execution, the output/ folder will contain:
output/
├── wordpress_modules.json
├── zluri_modules.json
├── github_modules.json
├── instagram_modules.json
└── neo_modules.json



📄 Sample Output Format
[
  {
    "module": "Account Settings",
    "description": "Features related to managing account credentials, privacy, and preferences.",
    "submodules": {
      "Change Password": "Steps to update the account password securely.",
      "Delete Account": "Instructions for permanently deleting the user account."
    }
  }
]


🧩 Key Design Decisions

1) No topic modeling (LDA / BERTopic)
   Structural inference is used instead for higher accuracy.
2) Explainable logic
   Modules and submodules are derived from HTML heading hierarchy.
3) Deterministic output
   Same input always produces the same output.
4) Scalable pipeline
   Supports multiple websites in a single execution.


⚠️ Assumptions
1) Documentation websites use semantic HTML headings (h1, h2, h3)
2) Pages are publicly accessible
3) Content hierarchy reflects product structure


🚧 Limitations
1) Very deep or non-semantic HTML structures may reduce accuracy
2) No multilingual support
3) No JavaScript-rendered content handling
4) - Some documentation websites (e.g., Instagram Help Center, Neo Help Center) rely heavily on
     JavaScript-based rendering. Since this solution uses server-side HTML parsing (requests + BeautifulSoup), such pages may result in limited or empty extraction.



🛠️ Technologies Used
1) Python 3
2) requests
3) BeautifulSoup (bs4)

✅ Conclusion

This project demonstrates a clean, modular, and production-ready AI agent for extracting structured product intelligence from documentation websites, aligned with real-world product and engineering use cases.










