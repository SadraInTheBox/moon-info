from pylunar import MoonInfo

import datetime

now = datetime.datetime.today()

moon = MoonInfo((35, 41, 21.308), (51, 23, 22.561))

moon.update(now)

name = str(moon.phase_name())
name2 = name.replace("_", " ").lower()

def get_style(p : str):
    import phashe as pn
    if p.lower() == "new_moon":
        return pn.NEW_MOON
    elif p.lower() == "FIRST_QUARTER".lower():
        return pn.FIRST_QUARTER
    elif p.lower() == "WAXING_CRESCENT".lower():
        return pn.WAXING_CRESCENT
    elif p == "FULL_MOON":
        return pn.FULL_MOON
    elif p == "LAST_QUARTER":
        return pn.LAST_QUARTER
    elif p == "WANING_CRESCENT":
        return pn.WANING_CRESCENT
    elif p == "WAXING_GIBBOUS":
        return pn.WAXING_GIBBOUS
    elif p == "WANING_GIBBOUS":
        return pn.WANING_GIBBOUS
    elif p == "NEW_MOON":
        return pn.NWE_MOON
    elif p == "FIRST_QUARTER":
        return pn.FIRST_QUARTER
    else:
        return p

print(get_style(name))

print("age : " + str(round(moon.age())) + "\n")
#print(moon.is_visible())
print("phase name : " + name2 + "\n")

print("next phases names :")

for h in moon.next_four_phases():
    #n += 1
    o, t = h
    o = o.replace("_", " ")
    t = str(t).replace("(", "")
    t = t.replace(")", "")
    print("\t" + o + " in " + t)
