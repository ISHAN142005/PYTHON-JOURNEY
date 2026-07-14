# keep taking password till password is not correct

password = "Ish12345"
EnteredPassword = input("Enter Password:")
while EnteredPassword != password:
    EnteredPassword = input(
        "Wrong Password!Try Again and Enter Again!\nEnter Password:"
    )

print("You logged in successfully:-)")
