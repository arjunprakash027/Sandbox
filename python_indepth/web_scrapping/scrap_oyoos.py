import aiohttp
import asyncio

async def make_get_request(url, cookies,session):
    async with session.get(url,cookies=cookies) as response:
        if response.status == 200:
            print("Success!")
            content = await response.json()  # Adjust based on expected response format
            print("Response Content:", content)
            return content
        else:
            print("Failed to retrieve data. Status code:", response.status)
            content = await response.text()
            print("Response Content:", content)

async def main():
    #token_request_url = "https://www.oyoos.com/api/getUniqueToken?&qid=105372&locale=en"
    all_hotels_url = "https://www.oyoos.com/api/user/pmAssociatedHotel?hotelId=&allMessageFetched=false&locale=en-GB"
    booking_url = "https://www.oyoos.com/hms_ms/api/v1/get_booking_with_ids?qid=&checkin_till=2024-10-02&checkout_from=2024-10-02&batch_count=100&batch_offset=0&visibility_required=true&status=12%2C0&additionalParams=payment_hold_transaction%2Cguest&decimal_price=true&ascending=true&sort_on=checkin_date"

    cookies = {
        'uif': '',
        'uuid': '',
    }
    
    async with aiohttp.ClientSession() as session:
        #token = await make_get_request(token_request_url, cookies,session=session)
        await make_get_request(booking_url,cookies=cookies,session=session)

if __name__ == "__main__":
    asyncio.run(main())

    