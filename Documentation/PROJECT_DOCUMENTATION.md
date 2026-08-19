# Project Documentation
# A/B Testing — Landing Page Conversion & Business Impact

## 1. Executive Summary
This project evaluates an A/B experiment comparing an existing landing page with a new landing page. The objective is to determine whether the new experience improves conversion and creates meaningful business value.

Conversion increased from 11.87% in the control group to 17.95% in the treatment group, a 6.08 percentage-point improvement and 51.18% relative uplift. A two-proportion z-test produced a z-statistic of -46.28 and p-value below 0.001.

The 95% confidence interval for the treatment-minus-control conversion difference is +5.82 to +6.33 percentage points.

At the observed treatment population, approximately 8,966 incremental conversions were observed versus the control benchmark, corresponding to approximately $337.8K estimated incremental revenue using the observed treatment AOV.

The recommendation is to roll out the new landing page subject to production validation and continued KPI monitoring.

## 2. Business Context
The company introduced a new landing page and needs to decide whether the new experience should replace the existing version.

The decision requires more than a simple conversion comparison. We need to establish statistical evidence, quantify business impact, check segment consistency, and provide an actionable recommendation.

## 3. Stakeholder Requirements
1. Compare conversion between old and new pages.
2. Test statistical significance.
3. Compare revenue per user and AOV.
4. Examine device, gender, and location segments.
5. Examine session duration and pages visited.
6. Estimate incremental conversions and revenue.
7. Provide a rollout recommendation.

## 4. Data Understanding
The dataset contains 294,478 user sessions and 12 columns.

| Column | Business Meaning |
|---|---|
| user_id | User identifier |
| timestamp | Session timestamp |
| group | Control or treatment assignment |
| landing_page | Old or new page |
| converted | Conversion indicator |
| age | User age |
| gender | User gender |
| location | User location |
| session_duration | Session duration |
| pages_visited | Pages viewed |
| device_type | Device used |
| purchase_amount | Purchase amount |

## 5. Data Validation
Validation completed before analysis:
- 294,478 rows
- 12 columns
- 0 missing values
- 0 duplicate rows
- Timestamp converted to datetime
- Conversion validated as binary
- Group and landing-page distributions checked
- Categorical distributions checked

The observed experiment mapping is Control → old_page and Treatment → new_page.

## 6. Exploratory Data Analysis

### 6.1 Conversion
Control: 17,444 / 146,926 = 11.87%

Treatment: 26,484 / 147,552 = 17.95%

Absolute difference: +6.08 percentage points

Relative uplift: +51.18%

### 6.2 Revenue
Control revenue: $654,227.55

Treatment revenue: $997,938.36

Revenue/user:
- Control: $4.45
- Treatment: $6.76

AOV:
- Control: $37.50
- Treatment: $37.68

Interpretation: revenue per user increases substantially while AOV remains almost unchanged, indicating that additional conversions are the primary contributor to the revenue improvement.

### 6.3 Engagement
Session duration:
- Control: 5.0037
- Treatment: 5.0006

Pages visited:
- Control: 4.0153
- Treatment: 4.0238

Interpretation: engagement is broadly unchanged.

### 6.4 Device
Treatment conversion was higher for Desktop, Mobile, and Tablet.

### 6.5 Gender
Treatment conversion was higher for Female, Male, and Other.

### 6.6 Location
Treatment conversion was higher across Australia, Canada, Germany, India, Pakistan, UK, and US.

## 7. Hypothesis Testing

### Test Selection
The primary outcome is binary (converted/not converted), there are two independent experiment groups, and the business question directly compares two conversion proportions. Given the very large sample sizes, a two-proportion z-test is appropriate.

A chi-square test could also be used for the 2×2 categorical relationship, but the two-proportion z-test directly expresses the business question as a comparison of conversion rates.

### Hypotheses
**H0:** Control and treatment conversion rates are equal.

**H1:** Control and treatment conversion rates are different.

α = 0.05

### Results
- Z-statistic: -46.28
- P-value: < 0.001
- Decision: Reject H0

Conclusion: there is strong statistical evidence that the treatment conversion rate is higher than the control conversion rate.

## 8. Confidence Interval
95% CI for treatment minus control conversion rate:

**+5.82 to +6.33 percentage points**

The interval does not include zero and is entirely positive.

## 9. Business Impact

### Incremental Conversions
Treatment users = 147,552

Expected conversions at control rate = 17,518

Actual treatment conversions = 26,484

Estimated incremental conversions = **8,966**

### Estimated Incremental Revenue
Treatment AOV = $37.68

Estimated incremental revenue = 8,966 × $37.68 = **approximately $337,846**

This is an estimate at the observed experiment scale.

## 10. Driver / Root-Cause Interpretation
The controlled experiment is intended to isolate the treatment effect if randomization was valid.

Additional analysis found:
- Consistent treatment improvement across devices, gender, and location.
- Session duration approximately unchanged.
- Pages visited approximately unchanged.
- AOV approximately unchanged.

The dataset lacks CTA clicks, checkout starts, scroll depth, form errors, and detailed funnel events. Therefore, no specific UI element can be claimed as the root cause.

The strongest defensible conclusion is that the new landing page increases conversion and that the revenue improvement is primarily driven by additional conversions.

## 11. Recommendation
**Recommend rollout of the new landing page, subject to normal production validation.**

The decision is supported by the significant conversion improvement, positive confidence interval, broad segment consistency, incremental conversions, and estimated revenue impact.

Post-launch, monitor conversion rate, revenue/user, AOV, segment performance, traffic mix, and engagement.

## 12. Power BI Dashboard

### Page 1 — Executive A/B Test Overview
Purpose: What happened?
- Total users
- Old/new conversion
- Uplift
- Avg pages visited
- Avg session duration
- Revenue/user
- Device analysis
- Location analysis

### Page 2 — User & Segment Analysis
Purpose: Who is affected and did behavior change?
- Gender conversion
- Session duration
- Pages visited
- AOV

### Page 3 — Experiment Impact & Business Decision
Purpose: Is the result statistically reliable and what should the business do?
- Z-test result
- P-value
- 95% CI
- Incremental conversions
- Estimated incremental revenue
- Key findings
- Recommendation

## 13. Limitations
1. No detailed page-level interaction data.
2. No specific UI element can be identified as root cause.
3. Incremental revenue is an estimate.
4. Future revenue requires validation of future traffic and representativeness.
5. Segment analysis is descriptive unless specifically powered for subgroup causal testing.
6. The analysis assumes valid random assignment and no major experimental violations.

## 14. Technical Stack
Python, Pandas, NumPy, Statsmodels, Power BI, Power Query, DAX, Jupyter/VS Code, Git/GitHub.

## 15. Final Outcome
The new landing page increased conversion from 11.87% to 17.95%, representing a 51.18% relative uplift. The result is statistically significant and the estimated treatment impact is +5.82 to +6.33 percentage points. At the observed treatment scale, the analysis estimates approximately 8,966 incremental conversions and $337.8K incremental revenue.

Recommended action: roll out the new landing page and monitor post-launch KPIs.
