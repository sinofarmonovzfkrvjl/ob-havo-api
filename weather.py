import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

class UzbekistanWeatherNotFoundError(Exception):
    pass


class UzbekistanWeather:
    def __init__(self, place: str):
        self.place = place

    def today(self):
        if self.place.lower() == "toshkent":
            response = requests.get(f"https://www.ob-havo.com/asia/uzbekistan/tashkent?page=today")
        elif self.place.lower() == "andijon":
            response = requests.get(f"https://www.ob-havo.com/asia/uzbekistan/andijan?page=today")
        elif self.place.lower() == "buxoro":
            response = requests.get(f"https://www.ob-havo.com/asia/uzbekistan/bukhara?page=today")
        elif self.place.lower() == "guliston":
            response = requests.get(f"https://www.ob-havo.com/asia/uzbekistan/sirdaryo/guliston?page=today")
        elif self.place.lower() == "jizzax":
            response = requests.get(f"https://www.ob-havo.com/asia/uzbekistan/jizzakh?page=today")
        elif self.place.lower() == "zarafshon":
            response = requests.get(f"https://www.ob-havo.com/asia/uzbekistan/navoiy/zarafshon?page=today")
        elif self.place.lower() == "qarshi":
            response = requests.get(f"https://www.ob-havo.com/asia/uzbekistan/qashqadaryo/qarshi")
        elif self.place.lower() == "navoiy":
            response = requests.get(f"https://www.ob-havo.com/asia/uzbekistan/navoiy?page=today")
        elif self.place.lower() == "namangan":
            response = requests.get(f"https://www.ob-havo.com/asia/uzbekistan/namangan?page=today")
        elif self.place.lower() == "nukus":
            response = requests.get(f"https://www.ob-havo.com/asia/uzbekistan/karakalpakstan/nukus?page=today")
        elif self.place.lower() == "samarqand":
            response = requests.get(f"https://www.ob-havo.com/asia/uzbekistan/samarqand/samarkand?page=today")
        elif self.place.lower() == "termiz":
            response = requests.get(f"https://www.ob-havo.com/asia/uzbekistan/surxondaryo/termez?page=today")
        elif self.place.lower() == "urganch":
            response = requests.get(f"https://www.ob-havo.com/asia/uzbekistan/xorazm/urgench?page=today")
        elif self.place.lower() == "farg'ona":
            response = requests.get(f"https://www.ob-havo.com/asia/uzbekistan/fergana?page=today")
        elif self.place.lower() == "xiva":
            response = requests.get(f"https://www.ob-havo.com/asia/uzbekistan/xorazm/xiva?page=today")
        else:
            raise UzbekistanWeatherNotFoundError("Ob Havo malumoti topilmadi, shahar nomini to'g'ri yozganingiznga ishonch hosil qiling, yoki Weather().help() dan foydalaning")
        todaysoup = BeautifulSoup(response.content, 'html.parser')
        max_middle_temp = todaysoup.find("span", {"class": "fourteen-max"})
        min_middle_temp = todaysoup.find("span", {"class": "fourteen-min"})
        necessary_things = todaysoup.find_all("span", {"class": "day-value"})
        weather = todaysoup.find_all("div", class_="weather_des")
        yogingarchilik = todaysoup.find_all("span", class_="length_unit mm_unit")
        m_taqsin_s = todaysoup.find_all("span", class_="wind_unit")
        recommended_clothes = todaysoup.find_all("div", class_="wear_item_name")
        return [{"bugun": [
                    {"harorat": [{"min": min_middle_temp.text},
                        {"max": max_middle_temp.text}]},
                    {"3 soatlik harorat": {"00:00": {"harorat": necessary_things[0].text,
                                            "havo": weather[0].text,
                                            "shamol tezligi": f"{necessary_things[32].text}{m_taqsin_s[0].text}",
                                            "yog'ingarchilik": f"{necessary_things[16].text}{yogingarchilik[0].text}",
                                            "namlik": f"{necessary_things[24].text}%",
                                            "yomg'ir yog'ish ehtimoli": f"{necessary_things[8].text}%"},
                                "03:00": {"harorat": necessary_things[1].text,
                                            "havo": weather[1].text,
                                            "shamol tezligi": f"{necessary_things[32].text}{m_taqsin_s[1].text}",
                                            "yog'ingarchilik": f"{necessary_things[17].text}{yogingarchilik[1].text}",
                                            "namlik": f"{necessary_things[25].text}%",
                                            "yomg'ir yog'ish ehtimoli": f"{necessary_things[9].text}%"}, 
                                "06:00": {"harorat": necessary_things[2].text,
                                            "havo": weather[2].text,
                                            "shamol tezligi": f"{necessary_things[32].text}{m_taqsin_s[2].text}",
                                            "yog'ingarchilik": f"{necessary_things[18].text}{yogingarchilik[2].text}",
                                            "namlik": f"{necessary_things[26].text}%",
                                            "yomg'ir yog'ish ehtimoli": f"{necessary_things[10].text}%"}, 
                                "09:00": {"harorat": necessary_things[3].text,
                                            "havo": weather[3].text,
                                            "shamol tezligi": f"{necessary_things[32].text}{m_taqsin_s[3].text}",
                                            "yog'ingarchilik": f"{necessary_things[19].text}{yogingarchilik[3].text}",
                                            "namlik": f"{necessary_things[27].text}%",
                                            "yomg'ir yog'ish ehtimoli": f"{necessary_things[11].text}%"}, 
                                "12:00": {"harorat": necessary_things[4].text,
                                            "havo": weather[4].text,
                                            "shamol tezligi": f"{necessary_things[32].text}{m_taqsin_s[4].text}",
                                            "yog'ingarchilik": f"{necessary_things[20].text}{yogingarchilik[4].text}",
                                            "namlik": f"{necessary_things[28].text}%",
                                            "yomg'ir yog'ish ehtimoli": f"{necessary_things[12].text}%"},
                                "15:00": {"harorat": necessary_things[5].text,
                                            "havo": weather[5].text,
                                            "shamol tezligi": f"{necessary_things[32].text}{m_taqsin_s[5].text}",
                                            "yog'ingarchilik": f"{necessary_things[21].text}{yogingarchilik[5].text}",
                                            "namlik": f"{necessary_things[29].text}%",
                                            "yomg'ir yog'ish ehtimoli": f"{necessary_things[13].text}%"},
                                "18:00": {"harorat": necessary_things[6].text,
                                            "havo": weather[6].text,
                                            "shamol tezligi": f"{necessary_things[32].text}{m_taqsin_s[5].text}",
                                            "yog'ingarchilik": f"{necessary_things[22].text}{yogingarchilik[6].text}",
                                            "namlik": f"{necessary_things[30].text}%",
                                            "yomg'ir yog'ish ehtimoli": f"{necessary_things[14].text}%"},
                                "21:00": {"harorat": necessary_things[7].text,
                                            "havo": weather[7].text,
                                            "shamol tezligi": f"{necessary_things[32].text}{m_taqsin_s[6].text}",
                                            "yog'ingarchilik": f"{necessary_things[23].text}{yogingarchilik[7].text}",
                                            "namlik": f"{necessary_things[31].text}%",
                                            "yomg'ir yog'ish ehtimoli": f"{necessary_things[15].text}%"}}},
                    {"kiyimlarga oid tavfsiyalar": [clothe.text for clothe in recommended_clothes]}]}]
    
app = FastAPI()

@app.get("/", include_in_schema=False)
async def root():
    return "bu o'zbekiston obhavosni ko'rsatuvchi api"

@app.get("/mavjud-hududlar")
async def available_places():
    return "toshkent, andijon, farg'ona, navoiy, samarqand, surxondaryo, buxoro, xorazm, qashqadaryo, jizzax, xiva, guliston, zarafshon, qarshi, namangan, nukus, termiz, urganch"

@app.get("/contact-admin")
async def contact_admin():
    return {"telegram": "https://t.me/@sinofarmonov", "instagram": "https://www.instagram.com/python_dasturlash323"}

@app.get("/api/v1/obhavo/{place}")
async def weather(place: str):
    return UzbekistanWeather(place).today()