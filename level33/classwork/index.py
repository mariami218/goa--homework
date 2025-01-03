def mask_sensitive_data(data):
    # თუ მონაცემი არის საკრედიტო ბარათი, ტელეფონი ან პასუხი საიდუმლო კითხვაზე,
    # ჩვენ მას ვმალავთ, deixando მხოლოდ რამდენიმე ბოლო სიმბოლო
    if isinstance(data, str):
        return '*' * (len(data) - 4) + data[-4:]
    return data

# მაგალითად, საკრედიტო ბარათის ნომერი
credit_card = "1234 5678 9876 5432"
masked_credit_card = mask_sensitive_data(credit_card)
print(f"მალებული საკრედიტო ბარათი: {masked_credit_card}")

# ტელეფონის ნომერი
phone_number = "555-123-4567"
masked_phone_number = mask_sensitive_data(phone_number)
print(f"მალებული ტელეფონი: {masked_phone_number}")

# საიდუმლო კითხვაზე პასუხი
secret_answer = "MyPetName"
masked_secret_answer = mask_sensitive_data(secret_answer)
print(f"მალებული პასუხი: {masked_secret_answer}")







