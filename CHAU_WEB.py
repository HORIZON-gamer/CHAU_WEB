import streamlit as st
from PIL import Image

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(
    page_title="Analytical Solutions - Expert Consultant",
    page_icon="🔬",
    layout="wide"
)

# --- MENU ĐIỀU HƯỚNG (SIDEBAR) ---
with st.sidebar:
    st.title("🔬 Navigation")
    page = st.radio("Go to:", ["Home", "My Services", "Tools & Resources", "Contact"])
    
    st.write("---")
    st.write("### 📞 +46 76 086 6539")
    st.write("📧 huynhminhchau8990@gmail.com")
    st.write("📍 Sweden")
    st.write("Developed by Chau Huynh")

# --- TRANG CHỦ (HOME) ---
if page == "Home":
    st.title("Optimize Your Lab's Performance 🚀")
    st.subheader("Professional Consulting for Analytical Chemistry & Instrumentation")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        Are your instruments causing downtime? Do you need robust method validation?
        
        I am a Analytical Chemist & Service Engineer specializing in:
        * **Chromatography (HPLC, GC, IC)**
        * **Spectroscopy (ICP-OES, ICP-MS, IR, UV, XRF, XRF)**
        * **Mass Spectrometry**
        * **and more**
        
        With decades of experience fixing complex hardware and optimizing workflows, I help laboratories improve throughput, ensure quality, and reduce costs.
        """)
        st.info("💡 **Why me?** I don't just fix machines; I provide engineering solutions to prevent future failures.")

    with col2:
        # Bạn có thể để ảnh đại diện của bạn ở đây
        st.success("## 10+ Years Experience")
        st.write("✅ Certified Engineer")
        st.write("✅ ISO 17025 Expert")
        st.write("✅ Method Dev Specialist")

# --- TRANG DỊCH VỤ (SERVICES) ---
elif page == "My Services":
    st.title("🛠️ Consulting Services")
    
    st.markdown("### 1. Instrument Maintenance & Repair")
    st.write("Troubleshooting complex issues for Agilent, Thermo, Shimadzu, and Waters systems. Preventive maintenance planning to minimize downtime.")
    
    st.markdown("---")
    
    st.markdown("### 2. Method Development & Validation")
    st.write("Developing robust analytical methods for HPLC/GC/ICP. Full validation support according to ICH, FDA, or ISO guidelines.")
    
    st.markdown("---")
    
    st.markdown("### 3. Quality Assurance (IQ/OQ/PQ)")
    st.write("Installation, Operation, and Performance Qualification protocols. Ensuring your data integrity and audit readiness.")

# --- TRANG CÔNG CỤ (TOOLS - SHOW OFF KỸ NĂNG) ---
elif page == "Tools & Resources":
    st.title("🧮 Lab Tools")
    st.write("Free tools I built to assist lab technicians.")

    # Tool 1: Đổi đơn vị Áp suất
    st.subheader("Pressure Converter")
    col1, col2, col3 = st.columns(3)
    with col1:
        psi = st.number_input("Enter PSI:", min_value=0.0)
    with col2:
        bar = psi * 0.0689476
        st.metric("Bar", f"{bar:.2f}")
    with col3:
        mpa = psi * 0.00689476
        st.metric("MPa", f"{mpa:.3f}")

    st.markdown("---")
    
    # Tool 2: Tính pha loãng (C1V1 = C2V2)
    st.subheader("Dilution Calculator (C1V1 = C2V2)")
    c1 = st.number_input("Stock Concentration (C1):", value=1000.0)
    c2 = st.number_input("Target Concentration (C2):", value=10.0)
    v2 = st.number_input("Final Volume (V2) in mL:", value=100.0)
    
    if c1 > 0:
        v1 = (c2 * v2) / c1
        st.success(f"🧪 You need to take **{v1:.2f} mL** of stock solution.")

# --- TRANG LIÊN HỆ (CONTACT) ---
elif page == "Contact":
    st.title("📬 Get in Touch")
    st.write("Ready to optimize your laboratory? Send me a message.")
    
    contact_form = """
    <form action="https://formsubmit.co/YOUR_EMAIL_HERE" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px;">
        <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px;">
        <textarea name="message" placeholder="How can I help you?" required style="width: 100%; padding: 10px; margin-bottom: 10px; height: 150px;"></textarea>
        <button type="submit" style="background-color: #4CAF50; color: white; padding: 12px 20px; border: none; cursor: pointer; width: 100%;">Send Message</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
    
    st.info("Or email me directly at: **your.email@example.com**")