import numpy as np
import pandas as pd

df=pd.read_csv(r"D:\Data Analytics Projects\AB testing\Data\AB Testing Data.csv")
'''

print(df.head(3))
#Data Validation 


print("Row count")
print("rows",df.shape[0])
print("\nColumn count")
print("columns",df.shape[1])

print("\nINFO")
print(df.info())
print("\nDESCRIBE")
print(df.describe())


df['timestamp']=pd.to_datetime(df['timestamp'])
print(df.info())


missing_values=df.isnull().sum()
print(f"\nnull values,{missing_values}")

duplicates=df['user_id'].duplicated().sum()
print(f"\nduplicates{duplicates}")


for col in ["group", "landing_page", "converted","gender", "location", "device_type"]:
    print(f"\n{col}")
    print(df[col].value_counts(dropna='False'))  


print(
    pd.crosstab(
        df["group"],
        df["landing_page"]
    )
)

print(
    pd.crosstab(
        df["converted"],
        df["purchase_amount"] > 0
    )
)

'''

# Analysis and EDA


conversion_analysis = (df.groupby(['group','landing_page']).agg(
    total_user=('user_id','count'),
    converted_user=('converted','sum'),
    total_revenue=('purchase_amount','sum')
).reset_index()
)

conversion_analysis['conversion_rate'] = (
    conversion_analysis['converted_user'] 
    / conversion_analysis['total_user'] *100)

print(conversion_analysis)


control_rate = conversion_analysis.loc[
    conversion_analysis['group']=='control',
    "conversion_rate"].iloc[0]

treatment_rate = conversion_analysis.loc[
    conversion_analysis['group']=='treatment',
    'conversion_rate'].iloc[0]

print(control_rate)



absolute_difference =  treatment_rate - control_rate

relative_uplift = (
    (treatment_rate - control_rate)
    / control_rate
    * 100
)



print("Conversion_rate:\t",control_rate)
print("Treatmen_rate:\t",treatment_rate)
print("Absolute_difference:\t",absolute_difference)
print("Relative_uplift:\t",relative_uplift)  



revenue_analysis = (df.groupby('group').agg(
       total_users=("user_id", "count"),
          converted_users=("converted", "sum"),
          total_revenue=("purchase_amount", "sum")
      )
      .reset_index()
)

revenue_analysis['revenue_per_user'] =(
     revenue_analysis['total_revenue']
     / revenue_analysis['total_users']
)


revenue_analysis['AOV']=(
    revenue_analysis['total_revenue']
    / revenue_analysis['converted_users']
)

print(revenue_analysis) 


engagement_analysis = ( df.groupby('group').agg(
    avg_session_duration=('session_duration','mean'),
    median_session_duration=('session_duration','median'),
    avg_page_visited=('pages_visited','mean'),
    median_page_visites=('pages_visited','median')
).reset_index()
)
print(engagement_analysis) 


device_analysis = (df.groupby(['landing_page','device_type']).agg(
    users=('user_id','count'),
    conversion=('converted','sum')
).reset_index()
)
device_analysis["conversion_rate"] = (
    device_analysis["conversion"]
    / device_analysis["users"]
    * 100
)
print(device_analysis)




gender_analysis = (df.groupby(['gender','group']).agg(
    users=('user_id','count'),
    conversion=('converted','sum')
).reset_index()
)

gender_analysis['conversion_rate']=(
    gender_analysis['conversion'] 
    / gender_analysis['users']*100)

print(gender_analysis)


location_analysis = (df.groupby(['location','group']).agg(
    users=('user_id','count'),
    conversion=('converted','sum')
)
)

location_analysis['conversion_rate']=(location_analysis['conversion']
                                      /location_analysis['users'])*100
print(location_analysis)

'''
# stastical test
H₀ — Null hypothesis

There is no difference in conversion rate between the Old Page and New Page.

In simple terms:
Old conversion = New conversion

H₁ — Alternative hypothesis

There is a difference in conversion rate between the Old Page and New Page.

Old conversion ≠ New conversion

Significance level α = 0.05 '''

from statsmodels.stats.proportion import proportions_ztest
converted = [
    df[df["group"] == "control"]["converted"].sum(),
    df[df["group"] == "treatment"]["converted"].sum()
]

users = [
    (df["group"] == "control").sum(),
    (df["group"] == "treatment").sum()
]

z_value,p_value = proportions_ztest(count=converted,nobs=users,alternative='two-sided')
alpha = 0.05


print("Converted users:", converted)
print("Total users:", users)
print("Z-statistic:", z_value)
print("P-value:", p_value)

if p_value < alpha:
    print("\nResult: Reject the Null Hypothesis")
else:
    print("\nResult: Fail to Reject the Null Hypothesis")


#confidence interval




from statsmodels.stats.proportion import confint_proportions_2indep

control_converted = 17444
control_users = 146926

treatment_converted = 26484
treatment_users = 147552

ci_low, ci_high = confint_proportions_2indep(
    treatment_converted,
    treatment_users,
    control_converted,
    control_users,
    method="wald"
)

print("95% CI Lower:", ci_low)
print("95% CI Upper:", ci_high)



#incremental_conversion

control_rate = 17444 / 146926
treatment_conversions = 26484
treatment_users = 147552

expected_conversions = treatment_users * control_rate

incremental_conversions = (
    treatment_conversions - expected_conversions
)

print("Expected conversions at control rate:",
      round(expected_conversions))

print("Actual treatment conversions:",
      treatment_conversions)

print("Incremental conversions:",
      round(incremental_conversions))

#revenue_conversion

treatment_aov = 997938.36 / 26484

incremental_conversions = 8966

incremental_revenue = incremental_conversions * treatment_aov

print("Treatment AOV:", round(treatment_aov, 2))
print("Estimated incremental revenue:",
      round(incremental_revenue, 2))



