expenses = []
def add_expense():
# Travail de l'etudiant A
    description = input("Description : ")
    amount = float(input("Montant : "))
    expenses.append({"description": description, "amount": amount})
    print("Depense ajoutée.")

def show_expenses():
# Travail de l'etudiant B
    if not expenses:
        print("Aucune dépense enregistee.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} - " 
              f"{expense['amount']} €")

def show_total():
# Travail de l'etudiant B
    total = sum(item["amount"] for item in expenses)
    print(f"Total : {total:.2f}")

def show_average():
    if not expenses:
        print("No expenses recorded.")
        return
    total = sum(item["amount"] for item in expenses)
    average = total / len(expenses)
    print(f"Average expense: {average:.2f}")
    
def main():
   while True:
    print("\n===== SUIVI DES DEPENSES =====")
    print("1. Ajouter une depense")
    print("2. Afficher les depenses")
    print("3. Afficher le total")
    print("4. Quitter")
    print("5. Show average")
    choice = input("Votre choix : ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Au revoir !")
        break
    elif choice == "5":
        show_average()
   else:
     print("Choix invalide.")
if __name__ == "__main__":
    main()


