import requests
from bs4 import BeautifulSoup
import time

url_to_scrape = 'http://apps.who.int/immunization_monitoring/globalsummary/schedules?sc%5Bc%5D%5B%5D=AUS&sc%5Bd%5D=&sc%5Bv%5D%5B%5D=AP&sc%5Bv%5D%5B%5D=BCG&sc%5Bv%5D%5B%5D=CHOLERA&sc%5Bv%5D%5B%5D=DIP&sc%5Bv%5D%5B%5D=DIPHTERIA&sc%5Bv%5D%5B%5D=DT&sc%5Bv%5D%5B%5D=DTAP&sc%5Bv%5D%5B%5D=DTAPHEP&sc%5Bv%5D%5B%5D=DTAPHEPBIPV&sc%5Bv%5D%5B%5D=DTAPHEPIPV&sc%5Bv%5D%5B%5D=DTAPHIB&sc%5Bv%5D%5B%5D=DTAPHIBHEPB&sc%5Bv%5D%5B%5D=DTAPHIBHEPIPV&sc%5Bv%5D%5B%5D=DTAPHIBIPV&sc%5Bv%5D%5B%5D=DTAPIPV&sc%5Bv%5D%5B%5D=DTIPV&sc%5Bv%5D%5B%5D=DTPHIBHEP&sc%5Bv%5D%5B%5D=DTWP&sc%5Bv%5D%5B%5D=DTWPHEP&sc%5Bv%5D%5B%5D=DTWPHIB&sc%5Bv%5D%5B%5D=DTWPHIBHEPB&sc%5Bv%5D%5B%5D=DTWPHIBHEPBIPV&sc%5Bv%5D%5B%5D=DTWPHIBIPV&sc%5Bv%5D%5B%5D=DTWPIPV&sc%5Bv%5D%5B%5D=HEPA&sc%5Bv%5D%5B%5D=HEPA_ADULT&sc%5Bv%5D%5B%5D=HEPAHEPB&sc%5Bv%5D%5B%5D=HEPA_PEDIATRIC&sc%5Bv%5D%5B%5D=HEPB&sc%5Bv%5D%5B%5D=HEPB_ADULT&sc%5Bv%5D%5B%5D=HEPB_PEDIATRIC&sc%5Bv%5D%5B%5D=HEPB_PEDIATRIC&sc%5Bv%5D%5B%5D=HFRS&sc%5Bv%5D%5B%5D=HIB&sc%5Bv%5D%5B%5D=HIB&sc%5Bv%5D%5B%5D=HIBMENC&sc%5Bv%5D%5B%5D=HPV&sc%5Bv%5D%5B%5D=INFLUENZA&sc%5Bv%5D%5B%5D=INFLUENZA_ADULT&sc%5Bv%5D%5B%5D=INFLUENZA_PEDIATRIC&sc%5Bv%5D%5B%5D=IPV&sc%5Bv%5D%5B%5D=JAPENC&sc%5Bv%5D%5B%5D=JE_INACTD&sc%5Bv%5D%5B%5D=JE_LIVEATD&sc%5Bv%5D%5B%5D=MEASLES&sc%5Bv%5D%5B%5D=MENA&sc%5Bv%5D%5B%5D=MENAC&sc%5Bv%5D%5B%5D=MENACWY&sc%5Bv%5D%5B%5D=MENACWY-135+CONJ&sc%5Bv%5D%5B%5D=MENACWY-135+PS&sc%5Bv%5D%5B%5D=MENB&sc%5Bv%5D%5B%5D=MENBC&sc%5Bv%5D%5B%5D=MENC_CONJ&sc%5Bv%5D%5B%5D=MM&sc%5Bv%5D%5B%5D=MMR&sc%5Bv%5D%5B%5D=MMRV&sc%5Bv%5D%5B%5D=MR&sc%5Bv%5D%5B%5D=MUMPS&sc%5Bv%5D%5B%5D=OPV&sc%5Bv%5D%5B%5D=PNEUMO_CONJ&sc%5Bv%5D%5B%5D=PNEUMO_PS&sc%5Bv%5D%5B%5D=RABIES&sc%5Bv%5D%5B%5D=ROTAVIRUS&sc%5Bv%5D%5B%5D=RUBELLA&sc%5Bv%5D%5B%5D=TBE&sc%5Bv%5D%5B%5D=TD&sc%5Bv%5D%5B%5D=TDAP&sc%5Bv%5D%5B%5D=TDAP&sc%5Bv%5D%5B%5D=TDAPIPV&sc%5Bv%5D%5B%5D=TDIPV&sc%5Bv%5D%5B%5D=TT&sc%5Bv%5D%5B%5D=TYPHOID&sc%5Bv%5D%5B%5D=TYPHOIDHEPA&sc%5Bv%5D%5B%5D=VARICELLA&sc%5Bv%5D%5B%5D=VITA&sc%5Bv%5D%5B%5D=VITAMINA&sc%5Bv%5D%5B%5D=YF&sc%5Bv%5D%5B%5D=ZOSTER&sc%5BOK%5D=OK'

r = requests.get(url_to_scrape)

soup = BeautifulSoup(r.text, "lxml")
# print(soup)
countries = {}
country_index = 0

print(1)
for table_row in soup.select('table .odd'):
    #print(table_row)
    table_cells = table_row.findAll('td')
    print(table_cells[0])
    vaccine_index = 0
    vaccines = {}

    if len(table_cells) > 0:
        while True:
            vaccine_details = []
            for i in range(0, 5):
                if i < 3:
                    pass
                else:
                    print(i)
                    vaccine_details.append(table_cells[i].text.strip())
            vaccines[table_cells[vaccine_index].text.strip()] = vaccine_details
            country_index += 1
            if table_cells[country_index - 1] != '':
                break

    countries[table_cells[country_index - 1].text.strip()] = vaccines

    # print(vaccine_details)

    time.sleep(1)


for k, v in countries.items():
    print(k, v)


