import requests as req

def get_flight_details(PNR):
    res = req.get(f'https://api.travelport.com/9/air/receipt/reservations/{PNR}/receipts')
    print(res)

get_flight_details('5RYL3Q')