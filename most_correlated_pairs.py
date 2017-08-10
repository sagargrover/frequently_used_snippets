c = df.corr().abs()

s = c.unstack()
so = s.order(kind="quicksort")

print so