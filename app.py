from models import img2text, generate_history, text2speech
import streamlit as st


def main():
    st.set_page_config(layout="wide", page_title="Image 2 Audio Story Generator", page_icon="📚")

    st.header("Image 2 Audio Story Generator")
    st.subheader("Generate a story from an image")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        print(uploaded_file)
        bytes_data = uploaded_file.getvalue()
        with open (uploaded_file.name, "wb") as file:
            file.write(bytes_data)
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        scenario = img2text(uploaded_file.name)
        story = generate_history(scenario)
        text2speech(story)

        with st.expander("Scenario"):
            st.write(scenario)
        with st.expander("Story"):
            st.write(story)
         
        st.audio("audio.flac")

if __name__ == "__main__":
    main()