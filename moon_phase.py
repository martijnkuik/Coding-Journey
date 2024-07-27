from collections import defaultdict

def moon_phase():
    return input("What type of Moon is there? ") 

moon_mapping = defaultdict(
    lambda: "There is no such moon phase", 
    { 
        "New Moon"         : "🌑", 
        "Waxing Crescent"  : "🌒", 
        "First Quarter"    : "🌓",
        "Waxing Gibbous"   : "🌔",
        "Full Moon"        : "🌕",
        "Waning Gibbous"   : "🌖", 
        "Last Quarter"     : "🌗",
        "Waning Crescent"  : "🌘"
    }
)

print(moon_mapping[moon_phase()])