def reverse(st):
    # სტრინგის გაყოფა სიტყვებად
    words = st.split()
    # სიტყვების შებრუნება და კვლავ გაერთიანება
    reversed_words = " ".join(words[::-1])
    return reversed_words
