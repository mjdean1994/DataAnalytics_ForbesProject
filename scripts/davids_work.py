

#===============================================


#plt.figure()
#cmpl_df['MILES'].plot(kind='box')
#plt.gcf()
#cmpl_df['MILES'].describe()

col_miles = cmpl_df['MILES'].dropna();


#cmpl_df[(cmpl_df['MILES'] >= 99) & (cmpl_df['MILES'] <= 101)]["MILES"]
#cmpl_df[(cmpl_df['MILES'] < 0)]["MILES"]

clean_miles = cmpl_df[(cmpl_df["MILES"] >= 0) & (cmpl_df["MILES"] < 300000)]["MILES"]

#print('10% - {0}'.format(col_miles.quantile(0.1)));
print('25% - {0}'.format(clean_miles.quantile(0.25)));
print('50% - {0}'.format(clean_miles.quantile(0.5)));
print('75% - {0}'.format(clean_miles.quantile(0.90)));

print(clean_miles.describe())

clean_df = cmpl_df[(cmpl_df["MILES"] >= 0) & (cmpl_df["MILES"] < 300000)]

plt.figure()
clean_miles.hist(bins=20)
#clean_df.plot(kind='scatter', x='MILES', y='OCCURENCES');
plt.title("Fig 5 - Milage at Failure")
plt.ylabel('Number of Failures', fontsize=12)
plt.xlabel('Miles at Failure', fontsize=12)
plt.gcf()



#===============================================



clean_df = cmpl_df[(cmpl_df["MILES"] >= 0) & (cmpl_df["MILES"] < 300000)]

plt.figure()
clean_df.plot(kind='scatter', x='MILES', y='OCCURENCES');
plt.title("Fig 5 - Number of Failures per Mile at Failure")
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Miles at Failure', fontsize=12)
plt.gcf()

#create_box_graph(clean_df, col_x='MILES', col_y='OCCURENCES', num_bins=10);



#===============================================


bin_df = pd.cut(clean_df['MILES'],bins)

plt.figure()
bin_df.value_counts().hist(bins=20)
plt.title("Fig 5 - Failed Component Count")
plt.ylabel('Number of Occurrences', fontsize=12)
plt.gcf()



#===============================================


