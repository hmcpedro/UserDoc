import manage_user

new_user = manage_user.cadastro()
new_user = manage_user.set_user(new_user)

print("-----" * 5)

new_user.describe_user()
new_user.doc_user()