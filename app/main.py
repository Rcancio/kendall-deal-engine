import streamlit as st

def monthly_payment(price, down_pct, rate, years=30):
    loan = price * (1 - down_pct / 100)
    r = rate / 100 / 12
    n = years * 12
    return loan * (r * (1 + r)**n) / ((1 + r)**n - 1)

def monthly_pmi(price, down_pct, pmi_rate_annual=0.3):
    loan = price * (1 - down_pct / 100)
    return loan * (pmi_rate_annual / 100) / 12

st.set_page_config(page_title="Kendall Deal Engine", layout="centered")
st.title("🏡 Kendall Deal Engine")

price = st.number_input("Purchase price", min_value=0, value=600000, step=5000)
down = st.number_input("Down payment %", min_value=0.0, value=5.0, step=0.5)
rate = st.number_input("Interest rate %", min_value=0.0, value=5.5, step=0.1)
taxes = st.number_input("Monthly taxes", min_value=0.0, value=750.0, step=25.0)
hoa = st.number_input("Monthly HOA", min_value=0.0, value=200.0, step=25.0)
insurance = st.number_input("Monthly insurance", min_value=0.0, value=400.0, step=25.0)

pmi_rate = 0.3

pi = monthly_payment(price, down, rate)
pmi = monthly_pmi(price, down, pmi_rate) if down < 20 else 0.0
piti = pi + taxes + hoa + insurance + pmi
income_needed = piti / 0.28

offer_low = price * 0.90
offer_high = price * 0.95

st.subheader("Results")
st.write(f"**Monthly P&I:** ${pi:,.0f}")
st.write(f"**Monthly PMI (0.30%):** ${pmi:,.0f}")
st.write(f"**Total PITI:** ${piti:,.0f}")
st.write(f"**Income needed (28%):** ${income_needed:,.0f}/mo (~${income_needed*12:,.0f}/yr)")
st.write(f"**Suggested offer range:** ${offer_low:,.0f} – ${offer_high:,.0f}")
