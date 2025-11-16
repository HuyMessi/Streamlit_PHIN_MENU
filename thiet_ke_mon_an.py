import streamlit as st
#page confis
st.set_page_config(
    page_title="Menu PHIN coffee",
    layout='wide'
)
Dict_menu_gia={
    "Ca_phe_sua":15_000,
    "Americano":20_000,
    "Matcha_latte":30_000,
    "Nuoc_cam": 25_000,
    "Sinh_to_xoai": 30_000
}

Dict_menu={
    "Ca_phe_sua":1,
    "Americano":1,
    "Matcha_latte":1,
    "Nuoc_cam": 1,
    "Sinh_to_xoai": 1
}
Dict_menu_name = {
    "Ca_phe_sua": "Cà phê sữa",
    "Americano": "Americano",
    "Matcha_latte": "Matcha Latte",
    "Nuoc_cam": "Nước cam",
    "Sinh_to_xoai": "Sinh tố xoài"
}
if "lst_mon_an" not in st.session_state:
    st.session_state.lst_mon_an = []
    
st.header("MENU PHIN COFFEE☕")
col1, col2 = st.columns(2)
with col1:
    frm_mon_an = st.form("frm_mon_an")
    with frm_mon_an:
        st.title("Chọn nước uống")
        Dict_menu["Ca_phe_sua"]=st.number_input("Cà phê sữa (15,000 VNĐ)", value=0, step=1)
        Dict_menu["Americano"]=st.number_input("Americano (20,000 VNĐ)", value=0,step=1)
        Dict_menu["Matcha_latte"]=st.number_input( "Matcha Latte (30,000 VNĐ)", value=0,step=1)
        Dict_menu["Nuoc_cam"]=st.number_input("Nước cam (25,000 VNĐ)", value=0,step=1)
        Dict_menu["Sinh_to_xoai"] = st.number_input("Sinh tố xoài (30,000 VNĐ)", value=0,step=1)
        btn = frm_mon_an.form_submit_button("Đặt món")
with col2:
    st.title("Hóa đơn của bạn")
    lst_mon_an = []
    for key in Dict_menu:
        item = {
        "Món ăn": Dict_menu_name[key],
        'Đơn giá': Dict_menu_gia[key],
        "Số lượng": Dict_menu[key],
        "Thành tiền": Dict_menu_gia[key] * Dict_menu[key]
    }
        lst_mon_an.append(item);
    st.table(lst_mon_an)

    tong_tien = 0
    for item in lst_mon_an:
        tong_tien += item["Thành tiền"]
    st.title(f"✅Tổng hóa đơn của bạn là: {tong_tien}")
    
    
