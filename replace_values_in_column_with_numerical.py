all_data['LotShape'] = all_data.replace({
    "LotShape": {
        "Reg": 0,
        "IR1": 1,
        "IR2": 2,
        "IR3": 3,
    }
})

all_data[''] = all_data.replace({
    "": {
    	"None": 1,
        "": 2,
        "": 3,
        "": 4,
        "": 5,
    }
})