balance=5000
withdrawal_amount=int(input("enter the withdrawal amount: "))
if withdrawal_amount >balance:
    print("Trasanction Rejected:Insufficient Funds ")
else:

    print("Trasanction successful!")
    print(f"Reming balance:{balance}")