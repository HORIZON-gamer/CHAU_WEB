import streamlit as st
from PIL import Image

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(
    page_title="Analytical Solutions - Expert Consultant",
    page_icon="🔬",
    layout="wide"
)
# --- CSS ĐỂ BO TRÒN ẢNH (Tùy chọn cho đẹp) ---
st.markdown("""
<style>
    .profile-pic {
        border-radius: 50%;
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 150px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR PROFILE ---
with st.sidebar:
    # 1. Ảnh đại diện (Profile Picture)
    # Lưu ý: Bạn cần có file ảnh 'profile.jpg' trong thư mục
    # Cách hiển thị ảnh tròn bằng HTML/CSS để giống LinkedIn
    # st.markdown('<img src="https://i.imgur.com/w2EwBqK.png" class="profile-pic">', unsafe_allow_html=True)
    # (Nếu bạn dùng ảnh thật trên máy, hãy thay đường link trên bằng cách dùng st.image thông thường)
    st.image("CHAU.jpg", width=150)
    
    st.write("") # Tạo khoảng trống
    
    # 2. Tên & Chức danh (Name & Headline)
    st.markdown("<h3 style='text-align: center;'>Chau Huynh</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'><i>Analytical Chemist</i><br>Skilled in Method Development, Instrumentation, Lab Training & Quality Management</p>", unsafe_allow_html=True)
    
    st.write("---")
    
    # 3. Nút kết nối LinkedIn (Call to Action)
    # st.link_button là tính năng mới của Streamlit, rất đẹp và tiện
    st.link_button("👔 Connect on LinkedIn", "https://www.linkedin.com/in/chauhuynh90", use_container_width=True)
    
    st.write("---")
    


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

# Thêm vào trang Tools & Resources
    st.subheader("📉 Cost of Downtime Calculator")
    st.write("See how much money you lose when your instrument is down.")

    col1, col2 = st.columns(2)
    with col1:
        samples_per_day = st.number_input("Samples per day:", value=50)
        price_per_sample = st.number_input("Price per sample ($):", value=100)
    with col2:
        days_down = st.number_input("Days instrument is down:", value=3)
        engineer_cost = st.number_input("Cost to hire me ($):", value=1000)
    
    lost_revenue = samples_per_day * price_per_sample * days_down
    roi = (lost_revenue - engineer_cost)
    
    st.warning(f"⚠️ You are losing **${lost_revenue:,.0f}** in revenue.")
    if roi > 0:
        st.success(f"✅ By hiring me, you save **${roi:,.0f}** instantly!")

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
    

    st.info("Or email me directly at: **huynhminhchau8990@gmail.com**")



    # Ở trang Contact hoặc trang Home
    st.write("---")
    st.header("📅 Need urgent help?")
    st.write("Book a free 30-minute consultation directly on my calendar.")

    # Cách đơn giản nhất: Nút bấm
    st.link_button("👉 Book a Free Call with Chau", "https://calendly.com/huynhminhchau8990/30min")

    # Cách chuyên nghiệp (Nhúng cả lịch vào):
    st.components.v1.iframe("hhttps://calendly.com/huynhminhchau8990/30min", height=600)





