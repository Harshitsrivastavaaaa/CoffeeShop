## CHAR BUCKS COFFEE ##
import math
print("Welcome to Charbucks")
print("1-> Cuppachino Hot")
print("2-> Lioni Cold")
print("3-> Latte")
print("4-> Americano")
c=int(input("Choose Your Coffee: "))
Base_cost = 20
cup_price = 8.63
if c==1:
    print("1-> Small")
    print("2-> Medium")
    print("3-> Large")
    print("4-> Bucket")
    s = int(input("Choose Your preferred Mug: "))
    Base_cost = 50
    cup_price = 8.63
    small_cost = 80
    medium_cost = 160
    large_cost = 199
    bucket_cost = 299


    if s==1:
        total_cs = cup_price + Base_cost + small_cost
        GST = ((total_cs / 100) * 12)
        final_cs = total_cs + GST
        print("You Order is Cuppachino Hot Small Mug")
        print("Total Amount: Rs.",final_cs)
        print("Round off Amount: Rs.",math.ceil(final_cs))
        print("Amount of Rs.", (math.ceil(final_cs) - final_cs), "will be donated for a good cause ")
        print("Thankyou, Have a Great Time !")

    elif s==2:
        total_cs = cup_price + Base_cost + medium_cost
        GST = ((total_cs / 100) * 12)
        final_cs = total_cs + GST
        print("You Order is Capichino Hot Medium Mug")
        print("Total Amount:Rs.",final_cs)
        print("Round off Amount: Rs.", math.ceil(final_cs))
        print("Amount of Rs.", (math.ceil(final_cs) - final_cs), "will be donated for a good cause ")
        print("Thankyou, Have a Great Time !")

    elif s==3:
        total_cs = cup_price + Base_cost + large_cost
        GST = ((total_cs / 100) * 12)
        final_cs = total_cs + GST
        print("You Order is Cuppachino Hot Large Mug")
        print("Total Amount:Rs.",final_cs)
        print("Round off Amount: Rs.", math.ceil(final_cs))
        print("Amount of Rs.", (math.ceil(final_cs) - final_cs), "will be donated for a good cause ")
        print("Thankyou, Have a Great Time !")

    elif s==4:
        total_cs = cup_price + Base_cost + bucket_cost
        GST = ((total_cs / 100) * 12)
        final_cs = total_cs + GST
        print("You Order is Cuppachino Hot Bucket Mug")
        print("Total Amount:Rs.",final_cs)
        print("Round off Amount: Rs.", math.ceil(final_cs))
        print("Amount of Rs.", (math.ceil(final_cs) - final_cs), "will be donated for a good cause ")
        print("Thankyou, Have a Great Time !")

elif c==2:
    print("1-> Small")
    print("2-> Medium")
    print("3-> Large")
    print("4-> Bucket")
    s = int(input("Choose Your preffered Mug: "))
    small_cost = 130
    medium_cost = 170
    large_cost = 249
    bucket_cost = 349

    if s==1:
        total_cs = cup_price + Base_cost + small_cost
        GST = ((total_cs / 100) * 12)
        final_cs = total_cs + GST
        print("You Order is Lioni Cold Small Mug")
        print("Total Amount:Rs.", final_cs)
        print("Round off Amount: Rs.", math.ceil(final_cs))
        print("Amount of Rs.", (math.ceil(final_cs) - final_cs), "will be donated for a good cause ")
        print("Thankyou, Have a Great Time !")

    elif s==2:
        total_cs = cup_price + Base_cost + medium_cost
        GST = ((total_cs / 100) * 12)
        final_cs = total_cs + GST
        print("You Order is Lioni Cold Medium Mug")
        print("Total Amount:Rs.",final_cs)
        print("Round off Amount: Rs.", math.ceil(final_cs))
        print("Amount of Rs.", (math.ceil(final_cs) - final_cs), "will be donated for a good cause ")
        print("Thankyou, Have a Great Time !")

    elif s==3:
        total_cs = cup_price + Base_cost + large_cost
        GST = ((total_cs / 100) * 12)
        final_cs = total_cs + GST
        print("You Order is Lioni Cold Large Mug")
        print("Total Amount:Rs.",final_cs)
        print("Round off Amount: Rs.", math.ceil(final_cs))
        print("Amount of Rs.", (math.ceil(final_cs) - final_cs), "will be donated for a good cause ")
        print("Thankyou, Have a Great Time !")

    elif s==4:
        total_cs = cup_price + Base_cost + bucket_cost
        GST = ((total_cs / 100) * 12)
        final_cs = total_cs + GST
        print("You Order is Lioni Cold Bucket Mug")
        print("Total Amount:Rs.",final_cs)
        print("Round off Amount: Rs.", math.ceil(final_cs))
        print("Amount of Rs.", (math.ceil(final_cs) - final_cs), "will be donated for a good cause ")
        print("Thankyou, Have a Great Time !")

elif c==3:
    print("1-> Small")
    print("2-> Medium")
    print("3-> Large")
    print("4-> Bucket")
    s = int(input("Choose Your preferred Mug: "))
    small_cost = 90
    medium_cost = 120
    large_cost = 149
    bucket_cost = 199

    if s==1:
        total_cs = cup_price + Base_cost + small_cost
        GST = ((total_cs / 100) * 12)
        final_cs = total_cs + GST
        print("You Order is Latte Small Mug")
        print("Total Amount:Rs.",final_cs)
        print("Round off Amount: Rs.", math.ceil(final_cs))
        print("Amount of Rs.", (math.ceil(final_cs) - final_cs), "will be donated for a good cause ")
        print("Thankyou, Have a Great Time !")

    elif s==2:
        total_cs = cup_price + Base_cost + medium_cost
        GST = ((total_cs / 100) * 12)
        final_cs = total_cs + GST
        print("You Order is Latte Medium Mug")
        print("Total Amount:Rs.",final_cs)
        print("Round off Amount: Rs.", math.ceil(final_cs))
        print("Amount of Rs.", (math.ceil(final_cs) - final_cs), "will be donated for a good cause ")
        print("Thankyou, Have a Great Time !")

    elif s==3:
        total_cs = cup_price + Base_cost + large_cost
        GST = ((total_cs / 100) * 12)
        final_cs = total_cs + GST
        print("You Order is Latte Large Mug")
        print("Total Amount:Rs.",final_cs)
        print("Round off Amount: Rs.", math.ceil(final_cs))
        print("Amount of Rs.", (math.ceil(final_cs) - final_cs), "will be donated for a good cause ")
        print("Thankyou, Have a Great Time !")

    elif s==4:
        total_cs = cup_price + Base_cost + bucket_cost
        GST = ((total_cs / 100) * 12)
        final_cs = total_cs + GST
        print("You Order is Latte Bucket Mug")
        print("Total Amount:Rs.", final_cs)
        print("Round off Amount: Rs.", math.ceil(final_cs))
        print("Amount of Rs.", (math.ceil(final_cs) - final_cs), "will be donated for a good cause ")
        print("Thankyou, Have a Great Time !")

elif c==4:
    print("1-> Small")
    print("2-> Medium")
    print("3-> Large")
    print("4-> Bucket")
    s = int(input("Choose Your preferred Mug: "))
    small_cost = 60
    medium_cost = 80
    large_cost = 119
    bucket_cost = 169

    if s==1:
        total_cs = cup_price + Base_cost + small_cost
        GST = ((total_cs / 100) * 12)
        final_cs = total_cs + GST
        print("You Order is Americano Small Mug")
        print("Total Amount:Rs.",final_cs)
        print("Round off Amount: Rs.", math.ceil(final_cs))
        print("Amount of Rs.", (math.ceil(final_cs) - final_cs), "will be donated for a good cause ")
        print("Thankyou, Have a Great Time !")

    elif s==2:
        total_cs = cup_price + Base_cost + medium_cost
        GST = ((total_cs / 100) * 12)
        final_cs = total_cs + GST
        print("You Order is Americano Medium Mug")
        print("Total Amount:Rs.",final_cs)
        print("Round off Amount: Rs.", math.ceil(final_cs))
        print("Amount of Rs.", (math.ceil(final_cs) - final_cs), "will be donated for a good cause ")
        print("Thankyou, Have a Great Time !")

    elif s==3:
        total_cs = cup_price + Base_cost + large_cost
        GST = ((total_cs / 100) * 12)
        final_cs = total_cs + GST
        print("You Order is Americano Large Mug")
        print("Total Amount:Rs.",final_cs)
        print("Round off Amount: Rs.", math.ceil(final_cs))
        print("Amount of Rs.", (math.ceil(final_cs) - final_cs), "will be donated for a good cause ")
        print("Thankyou, Have a Great Time !")

    elif s==4:
        total_cs = cup_price + Base_cost + bucket_cost
        GST = ((total_cs / 100) * 12)
        final_cs = total_cs + GST
        print("You Order is Americano Bucket Mug")
        print("Total Amount:Rs.",final_cs)
        print("Round off Amount: Rs.", math.ceil(final_cs))
        print("Amount of Rs.", (math.ceil(final_cs) - final_cs) ,"will be donated for a good cause ")
        print("Thankyou, Have a Great Time !")

## COMPLETE PROGRAM ENDS HERE ##