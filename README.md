# JobShield Odisha - SerpApi Hackathon

Fake job alert detector for students and job seekers in Odisha.

## Problem
Students in Odisha are getting fake job scams on WhatsApp/Telegram promising high salary for data entry work with upfront fees.

## Solution
JobShield verifies any job offer in real-time using SerpApi before you apply or pay.

## How we used SerpApi
- **Google Jobs API:** To check if the job posting actually exists online
- **Google Search API:** To verify company details and find scam/fraud reports

## Live Demo
Streamlit App: https://jobshield-odisha-o7whpr6zlnncyaaw9fbqgf.streamlit.app/
Video Demo: https://drive.google.com/file/d/10NiuX_ZuzraHXAytbHgGY9p4L3EtHO1O/view?usp=drivesdk

## Tech Stack
Python, Streamlit, SerpApi (google-search-results)

## How to Run
1. Clone this repo
2. pip install -r requirements.txt
3. Create .env file with: SERPAPI_API_KEY=your_key_here
4. streamlit run app.py

## Team
Built by Debashree-35 for SerpApi Hackathon
