cond = houseprice['LotFrontage'].isnull()
houseprice.LotFrontage[cond]=houseprice.SqrtLotArea[cond]