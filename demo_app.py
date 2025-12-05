import streamlit as st

from app.assistant import handle_intent


def main():
    st.title("🤖 Virtual Assistant QA Demo")
    st.write(
        "Esta es una pequeña demo de un asistente virtual con lógica sencilla "
        "y una batería de tests automatizados en Pytest + Jenkins."
    )

    st.markdown("---")

    user_input = st.text_input("Escribe un mensaje para el asistente:")

    if st.button("Enviar") or user_input:
        if not user_input.strip():
            st.warning("Por favor, escribe algún texto.")
        else:
            response = handle_intent(user_input)

            st.subheader("Resultado")
            st.write(f"**Intent detectado:** `{response['intent']}`")
            st.write(f"**Respuesta del asistente:** {response['message']}")

            st.markdown("----")
            st.caption("Este comportamiento está cubierto por tests automatizados con Pytest.")


if __name__ == "__main__":
    main()
