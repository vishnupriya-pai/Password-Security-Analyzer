import streamlit as st
import re
import math
import secrets
import string

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Password Security Analyzer",
    page_icon="🔐",
    layout="centered"
)

# -----------------------------
# Common weak passwords
# -----------------------------
COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "welcome",
    "letmein",
    "iloveyou",
    "abc123",
    "monkey",
    "football",
    "dragon",
    "master",
    "login",
    "passw0rd"
}

# -----------------------------
# Password analysis
# -----------------------------
def analyze_password(password):
    score = 0
    feedback = []
    warnings = []

    length = len(password)

    # Length
    if length >= 8:
        score += 15
    else:
        feedback.append("Use at least 8 characters.")

    if length >= 12:
        score += 10

    if length >= 16:
        score += 10

    # Character types
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[^A-Za-z0-9]", password))

    if has_lower:
        score += 10
    else:
        feedback.append("Add lowercase letters.")

    if has_upper:
        score += 10
    else:
        feedback.append("Add uppercase letters.")

    if has_digit:
        score += 10
    else:
        feedback.append("Add numbers.")

    if has_special:
        score += 15
    else:
        feedback.append("Add special characters such as !, @, #, or $.")

    # Common password
    if password.lower() in COMMON_PASSWORDS:
        score -= 30
        warnings.append("This is a commonly used password.")

    # Repeated characters
    if re.search(r"(.)\1\1", password):
        score -= 10
        warnings.append("Avoid repeating the same character multiple times.")

    # Sequential numbers
    sequences = [
        "0123456789",
        "1234567890",
        "9876543210"
    ]

    lower_password = password.lower()

    for sequence in sequences:
        for i in range(len(sequence) - 2):
            if sequence[i:i + 3] in password:
                score -= 5
                warnings.append("Avoid predictable number sequences.")
                break

    # Sequential letters
    alphabet = string.ascii_lowercase

    for i in range(len(alphabet) - 2):
        sequence = alphabet[i:i + 3]

        if sequence in lower_password or sequence[::-1] in lower_password:
            score -= 5
            warnings.append("Avoid predictable letter sequences.")
            break

    # Spaces are allowed and useful in passphrases
    if " " in password and length >= 12:
        score += 5

    # Keep score between 0 and 100
    score = max(0, min(score, 100))

    # Strength
    if score < 30:
        strength = "Very Weak"
    elif score < 50:
        strength = "Weak"
    elif score < 70:
        strength = "Moderate"
    elif score < 85:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback,
        "warnings": warnings,
        "length": length,
        "lower": has_lower,
        "upper": has_upper,
        "digit": has_digit,
        "special": has_special
    }


# -----------------------------
# Entropy calculation
# -----------------------------
def calculate_entropy(password):
    if not password:
        return 0

    charset_size = 0

    if re.search(r"[a-z]", password):
        charset_size += 26

    if re.search(r"[A-Z]", password):
        charset_size += 26

    if re.search(r"\d", password):
        charset_size += 10

    if re.search(r"[^A-Za-z0-9]", password):
        charset_size += 32

    if charset_size == 0:
        return 0

    entropy = len(password) * math.log2(charset_size)

    return round(entropy, 2)


# -----------------------------
# Resistance estimate
# -----------------------------
def estimate_resistance(entropy):
    if entropy < 28:
        return "Very low"
    elif entropy < 36:
        return "Low"
    elif entropy < 60:
        return "Moderate"
    elif entropy < 80:
        return "High"
    else:
        return "Very high"


# -----------------------------
# Strong password generator
# -----------------------------
def generate_password(length=16):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special = "!@#$%^&*"

    # Guarantee at least one of each category
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(numbers),
        secrets.choice(special)
    ]

    all_characters = lowercase + uppercase + numbers + special

    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Secure shuffle
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🔐 Password Security Analyzer")

st.write(
    "Analyze a password locally and get security recommendations. "
    "Your password is not stored by this application."
)

st.divider()

# Password input
password = st.text_input(
    "Enter a password to analyze",
    type="password"
)

# -----------------------------
# Analysis
# -----------------------------
if password:

    result = analyze_password(password)

    score = result["score"]
    strength = result["strength"]

    st.subheader("📊 Security Score")

    st.progress(score / 100)

    st.metric(
        label="Password Score",
        value=f"{score}/100"
    )

    # Strength message
    if strength == "Very Weak":
        st.error(f"🔴 {strength}")

    elif strength == "Weak":
        st.warning(f"🟠 {strength}")

    elif strength == "Moderate":
        st.warning(f"🟡 {strength}")

    elif strength == "Strong":
        st.success(f"🟢 {strength}")

    else:
        st.success(f"🔵 {strength}")

    st.divider()

    # -----------------------------
    # Character analysis
    # -----------------------------
    st.subheader("🔎 Character Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.write(
            f"📏 Length: **{result['length']} characters**"
        )

        st.write(
            f"{'✅' if result['lower'] else '❌'} Lowercase letters"
        )

        st.write(
            f"{'✅' if result['upper'] else '❌'} Uppercase letters"
        )

    with col2:
        st.write(
            f"{'✅' if result['digit'] else '❌'} Numbers"
        )

        st.write(
            f"{'✅' if result['special'] else '❌'} Special characters"
        )

        entropy = calculate_entropy(password)

        st.write(
            f"🎲 Estimated entropy: **{entropy} bits**"
        )

    # -----------------------------
    # Resistance
    # -----------------------------
    st.subheader("🛡️ Security Resistance")

    resistance = estimate_resistance(entropy)

    st.info(
        f"Estimated resistance level: **{resistance}**"
    )

    st.caption(
        "Entropy is an estimate based on character variety and password length; "
        "it is not a guarantee of real-world crack time."
    )

    # -----------------------------
    # Warnings
    # -----------------------------
    if result["warnings"]:
        st.subheader("⚠️ Security Warnings")

        for warning in set(result["warnings"]):
            st.warning(warning)

    # -----------------------------
    # Suggestions
    # -----------------------------
    if result["feedback"]:
        st.subheader("💡 Suggestions")

        for suggestion in result["feedback"]:
            st.write("•", suggestion)

    else:
        st.success(
            "✅ Your password satisfies the basic checks!"
        )

# -----------------------------
# Password generator
# -----------------------------
st.divider()

st.header("🎲 Strong Password Generator")

st.write(
    "Generate a new password using a cryptographically secure random generator."
)

length = st.slider(
    "Password length",
    min_value=12,
    max_value=32,
    value=16
)

if st.button("Generate Strong Password"):

    generated = generate_password(length)

    st.code(generated)

    generated_entropy = calculate_entropy(generated)

    st.success(
        f"Generated password length: {len(generated)} | "
        f"Estimated entropy: {generated_entropy} bits"
    )

# -----------------------------
# Security tips
# -----------------------------
st.divider()

st.header("🛡️ Password Security Tips")

tips = [
    "Use a unique password for every important account.",
    "Prefer long passwords or passphrases.",
    "Avoid names, birthdays, usernames, and common words.",
    "Avoid predictable patterns such as 123456 or abc123.",
    "Consider using a reputable password manager.",
    "Never share your password with other people.",
    "Enable multi-factor authentication when available."
]

for tip in tips:
    st.write("🔹", tip)

st.divider()

st.caption(
    "Password Security Analyzer • Educational Cybersecurity Project"
)