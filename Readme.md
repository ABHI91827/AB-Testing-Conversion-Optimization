# A/B Testing — Landing Page Conversion & Business Impact

## Project Overview
This capstone analyzes an A/B test to determine whether a new website landing page improves conversion and business performance compared with the existing landing page.

The project follows an end-to-end Data Analyst workflow: business understanding, data validation, exploratory analysis, statistical hypothesis testing, segment analysis, business impact estimation, and Power BI reporting.

## Business Problem
The company introduced a new landing page and wants to determine whether it should replace the existing page.

The analysis evaluates:
- Conversion rate
- Revenue per user
- Statistical significance
- Segment consistency
- User engagement
- Incremental conversions and revenue
- Rollout recommendation

## Stakeholder Questions
1. Does the new landing page improve conversion?
2. Is the observed difference statistically significant?
3. Does higher conversion translate into higher revenue per user?
4. Is the improvement consistent across devices, genders, and locations?
5. Does the new page materially change user engagement?
6. What is the estimated incremental conversion and revenue impact?
7. Should the company roll out the new landing page?

## Dataset
294,478 user sessions and 12 columns.

| Column | Description |
|---|---|
| user_id | Unique user identifier |
| timestamp | Session timestamp |
| group | Control or treatment |
| landing_page | Old or new landing page |
| converted | 1 = converted, 0 = not converted |
| age | User age |
| gender | User gender |
| location | User location |
| session_duration | Session duration |
| pages_visited | Number of pages visited |
| device_type | Device used |
| purchase_amount | Purchase amount |

## Data Validation
- Rows: 294,478
- Columns: 12
- Missing values: 0
- Duplicate rows: 0
- Timestamp converted to datetime
- Conversion validated as binary
- Control/Treatment distribution checked
- Landing-page assignment checked
- Categorical distributions checked

Experiment mapping:
- Control → old_page
- Treatment → new_page

## Key EDA Results

### Conversion
| Metric | Control / Old | Treatment / New |
|---|---:|---:|
| Users | 146,926 | 147,552 |
| Converted | 17,444 | 26,484 |
| Conversion Rate | 11.87% | 17.95% |

- Absolute difference: +6.08 percentage points
- Relative uplift: +51.18%

### Revenue
| Metric | Control | Treatment |
|---|---:|---:|
| Total Revenue | $654,227.55 | $997,938.36 |
| Revenue/User | $4.45 | $6.76 |
| AOV | $37.50 | $37.68 |

AOV is almost unchanged, indicating that the revenue improvement is primarily associated with more users converting.

### Engagement
- Avg session duration: Control 5.0037 vs Treatment 5.0006
- Avg pages visited: Control 4.0153 vs Treatment 4.0238

Engagement is almost unchanged.

### Segment Analysis
Treatment conversion was higher across:
- Desktop, Mobile, Tablet
- Female, Male, Other
- Australia, Canada, Germany, India, Pakistan, UK, US

The improvement is broad rather than concentrated in one segment.

## Hypothesis Testing

A two-proportion z-test was selected because:
- Conversion is binary.
- There are two independent experiment groups.
- The analysis directly compares two conversion proportions.
- Sample sizes are very large.

**H0:** Control and treatment conversion rates are equal.

**H1:** Control and treatment conversion rates are different.

Significance level: α = 0.05

Results:
- Z-statistic: -46.28
- P-value: < 0.001
- Decision: Reject H0

Conclusion: the treatment conversion rate is statistically significantly higher than the control conversion rate.

## Confidence Interval
95% confidence interval for the treatment-minus-control conversion-rate difference:

**+5.82 to +6.33 percentage points**

The interval is entirely above zero.

## Business Impact
Treatment users: 147,552

Expected conversions at the control rate: 17,518

Actual treatment conversions: 26,484

Estimated incremental conversions: **8,966**

Treatment AOV: **$37.68**

Estimated incremental revenue: **approximately $337,846**

This is an estimate at the observed experiment scale and should not be treated as guaranteed future revenue.

## Driver / Root-Cause Interpretation
The experiment itself isolates the landing-page treatment if assignment was properly randomized and the experiment had no major violations.

Additional analysis found:
- Treatment improvement is consistent across devices, gender, and location.
- Session duration is almost unchanged.
- Pages visited are almost unchanged.
- AOV is almost unchanged.

The dataset does not contain CTA clicks, checkout steps, scroll depth, form errors, or detailed funnel events. Therefore, the project does not claim a specific UI element as the root cause.

The strongest supported interpretation is that the new landing page increases conversion, with the revenue improvement primarily driven by additional conversions rather than higher purchase value.

## Final Recommendation
**Recommend rollout of the new landing page, subject to normal production validation.**

Reasons:
- Conversion increased from 11.87% to 17.95%.
- Relative uplift: 51.18%.
- p-value < 0.001.
- 95% CI: +5.82 to +6.33 pp.
- Approximately 8,966 incremental conversions at the observed treatment scale.
- Estimated incremental revenue: approximately $337.8K.
- Improvement is consistent across major segments.

Post-rollout monitoring:
- Conversion rate
- Revenue per user
- AOV
- Segment-level conversion
- Traffic mix
- User engagement

## Power BI Dashboard

### Page 1 — Executive A/B Test Overview
Answers: **What happened?**
- Total users
- Conversion rates
- Conversion uplift
- Average pages visited
- Average session duration
- Revenue per user
- Conversion by device
- Conversion by location

### Page 2 — User & Segment Analysis
Answers: **Who is affected and did user behavior change?**
- Gender conversion
- Session duration
- Pages visited
- AOV

### Page 3 — Experiment Impact & Business Decision
Answers: **Is the result statistically reliable and what should the business do?**
- Statistical test
- Z-statistic
- P-value
- 95% confidence interval
- Incremental conversions
- Estimated incremental revenue
- Key findings
- Final recommendation

## Tools
- Python
- Pandas
- NumPy
- Statsmodels
- Power BI
- Power Query
- DAX
- Jupyter / VS Code
- Git / GitHub

## Limitations
- No detailed page-level interaction events.
- A specific UI element cannot be identified as the root cause.
- Incremental revenue is estimated from observed treatment AOV.
- Future revenue should not be extrapolated without validating traffic volume and population representativeness.
- Segment analysis is descriptive unless the experiment was specifically designed and powered for subgroup causal testing.
