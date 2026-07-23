import re
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Layer 1 : Known Companies
# -----------------------------
KNOWN_COMPANIES = {
    "flipkart": "E-Commerce",
    "paytm": "FinTech",
    "ola": "Transportation",
    "uber": "Transportation",
    "swiggy": "FoodTech",
    "zomato": "FoodTech",
    "byju": "EdTech",
    "unacademy": "EdTech",
    "cred": "FinTech",
    "razorpay": "FinTech",
    "meesho": "E-Commerce",
    "nykaa": "E-Commerce"
}

# -----------------------------
# Layer 2 : Regex Patterns
# -----------------------------
SECTOR_PATTERNS = {
    r'bank|finance|payment|wallet|loan|credit|fintech': 'FinTech',
    r'health|hospital|medical|pharma|bio': 'Healthcare',
    r'education|learn|school|edtech': 'EdTech',
    r'food|restaurant|kitchen|delivery': 'FoodTech',
    r'ecommerce|shopping|retail|market': 'E-Commerce',
    r'taxi|cab|transport|mobility|logistics': 'Transportation',
    r'ai|artificial intelligence|machine learning': 'AI',
    r'saas|software|cloud': 'SaaS'
}

# -----------------------------
# Layer 3 : Investor Mapping
# -----------------------------
INVESTOR_SECTOR_MAP = {
    "sequoia": "Technology",
    "accel": "Technology",
    "y combinator": "Technology",
    "softbank": "Technology",
    "matrix": "Technology"
}


def reclassify_sector(row):
    """
    Reclassify a startup sector using
    1. Company Name
    2. Regex Patterns
    3. Investor Information
    """

    current = str(row.get("sector_clean", "")).strip()

    if current not in ["", "Unknown", "Other", "nan", "None"]:
        return current

    company = str(row.get("startup_name", "")).lower()

    for name, sector in KNOWN_COMPANIES.items():
        if name in company:
            return sector

    for pattern, sector in SECTOR_PATTERNS.items():
        if re.search(pattern, company):
            return sector

    investors = str(row.get("investors_name", "")).lower()

    for investor, sector in INVESTOR_SECTOR_MAP.items():
        if investor in investors:
            return sector

    return "Other"


def apply_reclassification(df):
    """
    Apply reclassification to the dataframe.
    """

    df = df.copy()

    df["sector_final"] = df.apply(reclassify_sector, axis=1)

    return df


def plot_reclassification_impact(df):
    """
    Compare original vs reclassified sectors.
    """

    if "sector_clean_old" not in df.columns:
        print("sector_clean_old column not found.")
        return

    before = df["sector_clean_old"].value_counts().head(10)
    after = df["sector_final"].value_counts().head(10)

    fig, ax = plt.subplots(1,2, figsize=(16,6))

    before.plot(kind="bar", ax=ax[0], title="Before Reclassification")
    after.plot(kind="bar", ax=ax[1], title="After Reclassification")

    plt.tight_layout()
    plt.show()