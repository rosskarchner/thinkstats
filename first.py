import survey
table = survey.Pregnancies()
table.ReadRecords()

def avg_prg_length(records):
	s= sum([record.prglength for record in records])
	return float(s)/len(records)


first_p=[record for record in table.records if record.outcome==1 and record.birthord ==1]
other_p=[record for record in table.records if record.outcome==1 and record.birthord > 1]

first_avg=avg_prg_length(first_p)
other_avg=avg_prg_length(other_p)

print "live, first births", len(first_p), "(%s)" % first_avg
print "live, not first births", len(other_p),  "(%s)" % other_avg
print "difference in days (first-others)", (first_avg-other_avg ) * 7.0

