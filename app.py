from PIL import Image

import streamlit as st

st.title(":blue[iBehave] - Buy My Behavioral Stats")
st.markdown("## Current BID: :green[$99]")
st.markdown("<b>Email for an invite to the platform and to bid for my data -> <a href='%s'>here</a></b>" % 'mailto:jawerty210@gmail.com?subject=iBehave Stats Bid', unsafe_allow_html=True)

st.markdown("### What is this? And Who am I")
st.markdown("My name is Jared Wright and I'm just a coder. I built a new way of tracking behavioral data. And I wanted to create a new system, a MARKETPLACE, for selling behavioral stats peer 2 peer. Today, we compete with FAANG and think different.")

my_image = Image.open('./profile_image.jpeg')

st.image(my_image)
st.markdown("### What are you getting with iBehave??")
st.markdown("- Daily habits")
st.markdown("- Interests")
st.markdown("- Things I like to search")
st.markdown("- Everything I input online")
st.markdown("- Perfect if you want to target my demo (African-American, Male, Software Engineer, in 20s, into exercising/sports)")
st.markdown("<b>Email for an invite to the platform and to bid for my data -> <a href='%s'>here</a></b>" % 'mailto:jawerty210@gmail.com?subject=iBehave Stats Bid', unsafe_allow_html=True)
