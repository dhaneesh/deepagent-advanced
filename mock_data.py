ATM_DATA = {
    "60601": [
        {"id": "ATM001", "name": "Chicago Loop ATM",      "address": "123 S Michigan Ave", "hours": "24/7",         "fee": "No fee"},
        {"id": "ATM002", "name": "Millennium Park ATM",   "address": "201 E Randolph St",  "hours": "24/7",         "fee": "No fee"},
        {"id": "ATM003", "name": "River North ATM",       "address": "445 N Wabash Ave",   "hours": "6am–midnight", "fee": "No fee"},
    ],
    "10001": [
        {"id": "ATM004", "name": "Midtown Manhattan ATM", "address": "350 5th Ave",        "hours": "24/7",         "fee": "No fee"},
        {"id": "ATM005", "name": "Penn Station ATM",      "address": "8 W 31st St",        "hours": "24/7",         "fee": "$2.50 non-member"},
    ],
    "90210": [
        {"id": "ATM006", "name": "Beverly Hills ATM",     "address": "9876 Wilshire Blvd", "hours": "24/7",         "fee": "No fee"},
    ],
}

OFFICERS_DATA = {
    "chicago": [
        {"name": "Margaret Chen",  "title": "Senior Investment Officer", "phone": "312-555-0101", "email": "m.chen@xyzbank.com",     "specialty": "Equities & ETFs"},
        {"name": "David Okafor",   "title": "Investment Officer",        "phone": "312-555-0182", "email": "d.okafor@xyzbank.com",   "specialty": "Fixed Income"},
        {"name": "Sarah Kowalski", "title": "Wealth Manager",            "phone": "312-555-0147", "email": "s.kowalski@xyzbank.com", "specialty": "Retirement Planning"},
    ],
    "new york": [
        {"name": "James Thornton", "title": "Chief Investment Officer",  "phone": "212-555-0201", "email": "j.thornton@xyzbank.com", "specialty": "Alternative Assets"},
        {"name": "Priya Nair",     "title": "Investment Officer",        "phone": "212-555-0233", "email": "p.nair@xyzbank.com",     "specialty": "ESG Portfolios"},
    ],
    "los angeles": [
        {"name": "Carlos Rivera",  "title": "Investment Officer",        "phone": "310-555-0301", "email": "c.rivera@xyzbank.com",   "specialty": "Real Estate Investment"},
    ],
}

PORTFOLIO_DATA = [
    {"name": "Apex Technologies Inc.",  "sector": "Technology",       "stake": "4.2%", "value": "$840M",  "rating": "A+"},
    {"name": "GreenBridge Energy",      "sector": "Renewable Energy", "stake": "6.8%", "value": "$1.2B",  "rating": "A"},
    {"name": "MedCore Diagnostics",     "sector": "Healthcare",       "stake": "3.1%", "value": "$620M",  "rating": "A"},
    {"name": "Urban Logistics Co.",     "sector": "Transportation",   "stake": "5.5%", "value": "$950M",  "rating": "A-"},
    {"name": "Pacific Foods Group",     "sector": "Consumer Goods",   "stake": "2.9%", "value": "$480M",  "rating": "B+"},
    {"name": "Sentinel Cybersecurity",  "sector": "Technology",       "stake": "7.3%", "value": "$1.5B",  "rating": "A+"},
    {"name": "Clearwater Pharma",       "sector": "Pharmaceuticals",  "stake": "4.0%", "value": "$760M",  "rating": "A"},
]

RETIREMENT_DATA = [
    {
        "name": "XYZ Gold 401(k)", "type": "401(k)",
        "min_contrib": "$50/mo",   "match": "Up to 6% employer match",
        "features": ["Roth option available", "Target date funds", "Low expense ratios"],
    },
    {
        "name": "XYZ Silver IRA",  "type": "Traditional IRA",
        "min_contrib": "$25/mo",   "match": "N/A",
        "features": ["Tax-deferred growth", "Flexible contribution", "600+ fund choices"],
    },
    {
        "name": "XYZ Roth IRA",    "type": "Roth IRA",
        "min_contrib": "$25/mo",   "match": "N/A",
        "features": ["Tax-free withdrawals", "No required minimum distributions", "Estate planning benefits"],
    },
    {
        "name": "XYZ Executive SEP", "type": "SEP-IRA",
        "min_contrib": "Up to 25% of income", "match": "N/A",
        "features": ["High contribution limits", "Self-employed friendly", "Simple administration"],
    },
]

LOCATIONS_DATA = [
    {"city": "Chicago",     "branches": 14, "flagship": "200 W Adams St, Chicago IL 60606",  "hours": "Mon–Fri 9am–5pm, Sat 9am–1pm"},
    {"city": "New York",    "branches": 22, "flagship": "1 World Trade Center, NY 10007",    "hours": "Mon–Fri 8am–6pm, Sat 9am–2pm"},
    {"city": "Los Angeles", "branches": 11, "flagship": "333 S Grand Ave, LA 90071",         "hours": "Mon–Fri 9am–5pm, Sat 9am–1pm"},
    {"city": "Houston",     "branches":  8, "flagship": "1000 Main St, Houston TX 77002",    "hours": "Mon–Fri 9am–5pm"},
    {"city": "Boston",      "branches":  6, "flagship": "100 Federal St, Boston MA 02110",   "hours": "Mon–Fri 9am–5pm, Sat 10am–1pm"},
]