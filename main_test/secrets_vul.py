"""
SECRETS TEST FILE - FOR SECURITY SCANNING VALIDATION ONLY

This file contains an intentionally fake AWS access key + secret access key pair
to trigger "Critical/High" secret detections in scanners.

DO NOT use in production code.
"""

# High-confidence AWS patterns (classic)
AWS_ACCESS_KEY_ID_2 = "AKIAIOSFOdfsfsdfDNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY_2 = "wJalrXUtnsdfsdfsfFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Optional: include a session token too (some tools treat full triples as higher confidence)
AWS_SESSION_TOKEN_2 = (
    "IQoJb3JpZ2luX2VjsdfsfsfdsfsEJr//////////wEaCXVzLWVhc3QtMSJGMEQCIH"
    "EXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMPLE"
)