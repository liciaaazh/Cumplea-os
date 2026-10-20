import streamlit as st

st.set_page_config(
    page_title="生日快乐!!",
    page_icon="🩷",
    layout="centered"
)

def main():
    st.title("🩷生日快乐!!🩷")
    st.header("祝你生日快乐，天天开心，永远美丽动人！")
    st.write("From: 星娜")
    st.write("To: 欣怡")

def lateral():
    with st.sidebar:
        st.title("🩷 你和我的故事 ...")
        st.write("你和我的故事，我们的照片")

        st.subheader("🎵 A song for you")
        st.video("https://youtu.be/OqBuXQLR4Y8")

        # Aquí van todas las imágenes
        

        st.write("...🩷")

def boton():
    with st.container(border=True):
        st.write("🩷 这是我给你准备的一个小礼物! 🩷")
        st.write(
            "虽然简单，但我希望你能喜欢这个小小的惊喜！爱你呀"
        )

        if st.button("Show text"):
            st.session_state.mostrar_texto = True

        if st.session_state.get("mostrar_texto", False):
            st.write(
                "🎂 首先，生日快乐xxy！怎么快你又长大了一岁。"
                "你也成熟了，学了新的东西。我希望接下来我们可以继续当朋友然后走下去，"
                "希望如果你有困难的话找我，希望发生任何愉快或不愉快的事情都能分享给我，"
                "我也很愿意听。时间过得很快，我们又回到了10月24号，我的闺蜜16岁啦！🎂"
            )

            st.write(
                "🎁 我的中文作文水平也就那样，但是我还是有很多想跟你说的，"
                "所以我只能用西语表达了 🎁"
            )

            st.write(
                "🎉 Querida Anna, aunque no siempre podré estar a tu lado, "
                "en este sentido literal, quiero que sepas que en el fondo "
                "siempre estaré por y para ti. En esta nueva etapa de la vida, "
                "por ejemplo, ten en cuenta que cualquier cosa, cualquier duda, "
                "estoy aquí. "
                "También quiero que pases un feliz cumpleaños, obviamente, "
                "y que hayan más de estos en los que yo esté incluida. "
                "Espero que estés teniendo una buena noche. "
                "¡Felices 16! 🎉"
            )

            st.write(
                "💌 Te quiero mucho, y espero que te lo pases genial. "
                "¡Felices 16! 💌"
            )

main()
lateral()
boton()
