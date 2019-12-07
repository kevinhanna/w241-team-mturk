Team mTurk - Motivating Quality Work
================
Kevin Hanna, Kevin Stone, Changjing Zhao

  - [Motivating Quality Work](#motivating-quality-work)
      - [What motivates crowdsourced workers to do quality
        work?](#what-motivates-crowdsourced-workers-to-do-quality-work)
      - [Our Experiments](#our-experiments)
      - [Experiment 1, our first pilot](#experiment-1-our-first-pilot)
      - [Experiment 2, our second pilot](#experiment-2-our-second-pilot)

## Motivating Quality Work

### What motivates crowdsourced workers to do quality work?

Our scoring metric measures the accuracy of the bounding box by
calculating the euclidean distance of the Turkers bounds to the correct
bounding. Therefor a **lower score is better**. When the treatment
should cause a negative reaction, the score should increase if our
hypothesis is correct.

### Our Experiments

1.  Pilot - Bound 20 images with negative treatment (Government
    Surveillance)
2.  Pilot - Bound a single image with negative treatment (Government
    Surveillance)
3.  Experiment - Bound a single image with positive treatment (Potential
    future work)
4.  Experiment - Increase subjects for experiment 3
5.  Experiment - Bound a single image with negative treatment, reward 2
    cents (Threat of not paying for poor performance)
6.  Experiment - Bound a single image with negative treatment, increased
    reward to 5 cents (Threat of not paying for poor performance)

<table>

<thead>

<tr>

<th style="text-align:right;">

experiment\_no

</th>

<th style="text-align:right;">

is\_pilot

</th>

<th style="text-align:right;">

in\_treatment

</th>

<th style="text-align:right;">

count

</th>

<th style="text-align:right;">

mean\_score

</th>

<th style="text-align:right;">

std\_dev

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:right;">

1

</td>

<td style="text-align:right;">

1

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

397

</td>

<td style="text-align:right;">

137.60402

</td>

<td style="text-align:right;">

295.29711

</td>

</tr>

<tr>

<td style="text-align:right;">

1

</td>

<td style="text-align:right;">

1

</td>

<td style="text-align:right;">

1

</td>

<td style="text-align:right;">

396

</td>

<td style="text-align:right;">

136.39470

</td>

<td style="text-align:right;">

296.29412

</td>

</tr>

<tr>

<td style="text-align:right;">

2

</td>

<td style="text-align:right;">

1

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

187

</td>

<td style="text-align:right;">

15.25847

</td>

<td style="text-align:right;">

36.79851

</td>

</tr>

<tr>

<td style="text-align:right;">

2

</td>

<td style="text-align:right;">

1

</td>

<td style="text-align:right;">

1

</td>

<td style="text-align:right;">

189

</td>

<td style="text-align:right;">

17.09362

</td>

<td style="text-align:right;">

42.27343

</td>

</tr>

<tr>

<td style="text-align:right;">

3

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

48

</td>

<td style="text-align:right;">

19.02776

</td>

<td style="text-align:right;">

23.08104

</td>

</tr>

<tr>

<td style="text-align:right;">

3

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

1

</td>

<td style="text-align:right;">

47

</td>

<td style="text-align:right;">

22.71446

</td>

<td style="text-align:right;">

36.73351

</td>

</tr>

<tr>

<td style="text-align:right;">

4

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

93

</td>

<td style="text-align:right;">

40.35981

</td>

<td style="text-align:right;">

139.47131

</td>

</tr>

<tr>

<td style="text-align:right;">

4

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

1

</td>

<td style="text-align:right;">

94

</td>

<td style="text-align:right;">

14.51884

</td>

<td style="text-align:right;">

25.36227

</td>

</tr>

<tr>

<td style="text-align:right;">

5

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

96

</td>

<td style="text-align:right;">

13.55187

</td>

<td style="text-align:right;">

23.01864

</td>

</tr>

<tr>

<td style="text-align:right;">

5

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

1

</td>

<td style="text-align:right;">

97

</td>

<td style="text-align:right;">

11.61424

</td>

<td style="text-align:right;">

11.00214

</td>

</tr>

<tr>

<td style="text-align:right;">

6

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

94

</td>

<td style="text-align:right;">

13.56319

</td>

<td style="text-align:right;">

20.70507

</td>

</tr>

<tr>

<td style="text-align:right;">

6

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

1

</td>

<td style="text-align:right;">

92

</td>

<td style="text-align:right;">

13.15357

</td>

<td style="text-align:right;">

17.04807

</td>

</tr>

<tr>

<td style="text-align:right;">

7

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

191

</td>

<td style="text-align:right;">

13.17927

</td>

<td style="text-align:right;">

16.12633

</td>

</tr>

<tr>

<td style="text-align:right;">

7

</td>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

1

</td>

<td style="text-align:right;">

181

</td>

<td style="text-align:right;">

21.52917

</td>

<td style="text-align:right;">

98.68055

</td>

</tr>

</tbody>

</table>

<table>

<thead>

<tr>

<th style="text-align:left;">

</th>

<th style="text-align:left;">

bounding\_box\_score

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

Min. : 1.000

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

1st Qu.: 6.681

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

Median : 12.414

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

Mean : 60.752

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

3rd Qu.: 27.917

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

Max. :1284.400

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

NA’s :18

</td>

</tr>

</tbody>

</table>

### Experiment 1, our first pilot

For our pilot, we gave the Turkers a negative treatment and asked that
they draw a single bounding box on each of 20 images. We first collected
some information about the subject through a survey and then randomly
assigned those subjects to treatment and control. Our primary goal was
to understand how our scoring scheme worked, gauge level of variance we
should expect in future experiments and test if our covariates collected
from our survey were helpful. We had high attrition and due to a
misunderstanding of the Mechanical Turk platform, our assignments to
treatment and control failed and we ended up with Turkers not in our
experiment in our results, and many ended up in both treatment and
control.

We were not able to trust any ATE, but we could at least see the
variance, which was exceptionally high.

![](team_mturk_experiments_files/figure-gfm/plot_experiment_1-1.png)<!-- -->

<table>

<thead>

<tr>

<th style="text-align:left;">

</th>

<th style="text-align:left;">

mean\_worker\_score

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

Min. : 5.003

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

1st Qu.: 25.938

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

Median :119.894

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

Mean :135.288

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

3rd Qu.:178.160

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

Max. :994.601

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

NA’s :1

</td>

</tr>

</tbody>

</table>

<table>

<thead>

<tr>

<th style="text-align:right;">

in\_treatment

</th>

<th style="text-align:right;">

mean\_score

</th>

<th style="text-align:right;">

std\_dev

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

146.7838

</td>

<td style="text-align:right;">

125.4300

</td>

</tr>

<tr>

<td style="text-align:right;">

1

</td>

<td style="text-align:right;">

118.8101

</td>

<td style="text-align:right;">

190.9985

</td>

</tr>

</tbody>

</table>

``` r
#TODO Gauge if effort decreases with more HITTs
```

### Experiment 2, our second pilot

With the first pilot behind us, we decided we needed to focus on
increasing our statistical power and hypothesized that having more
subjects with fewer experiments would provide more statistical power.

![](team_mturk_experiments_files/figure-gfm/plot_experiment_2-1.png)<!-- -->

<table>

<thead>

<tr>

<th style="text-align:left;">

</th>

<th style="text-align:left;">

bounding\_box\_score

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

Min. : 1.423

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

1st Qu.: 5.054

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

Median : 8.320

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

Mean : 16.178

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

3rd Qu.: 13.498

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

Max. :489.540

</td>

</tr>

<tr>

<td style="text-align:left;">

</td>

<td style="text-align:left;">

NA’s :3

</td>

</tr>

</tbody>

</table>

<table>

<thead>

<tr>

<th style="text-align:right;">

in\_treatment

</th>

<th style="text-align:right;">

mean\_score

</th>

<th style="text-align:right;">

std\_dev

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:right;">

0

</td>

<td style="text-align:right;">

15.25847

</td>

<td style="text-align:right;">

36.79851

</td>

</tr>

<tr>

<td style="text-align:right;">

1

</td>

<td style="text-align:right;">

17.09362

</td>

<td style="text-align:right;">

42.27343

</td>

</tr>

</tbody>

</table>

Even with a p-value of 0.655, this was progress. Our coefficient for in
treatment was still more likely due to random noise than not.

#### 2.1 Power Test

    ## 
    ##      Two-sample t test power calculation 
    ## 
    ##               n = 5756.986
    ##           delta = 1.835148
    ##              sd = 39.59534
    ##       sig.level = 0.05
    ##           power = 0.8
    ##     alternative = one.sided
    ## 
    ## NOTE: n is number in *each* group

To achieve the statistical power of 0.8 at the 0.05 confidence-level
with the variance we had in this experiement, we would require nearly
5,800 subjects in both control and treatment.

#### 2.2 Analysis

With this pilot, the only covariate we had was the amount of time each
Turker spent on the task. And working time acts as a control explaining
away some of the variance reducing the p-value for our target feature
from 0.45 to 0.39.

``` r
e2_mod_1 <- d[experiment_no==2, lm(bounding_box_score ~ in_treatment)]
e2_mod_2 <- d[experiment_no==2, lm(bounding_box_score ~ in_treatment+WorkTimeInSeconds)]

stargazer(e2_mod_1,  e2_mod_2,
          type = 'latex', header = FALSE, table.placement = 'h', report=('vc*p'),
          add.lines = list(c("Data Subset", "All", "All", "$x==1$")),
          column.labels=c("Target Alone", "With WorkInSeconds Control"))
```

\=============================================== Dependent variable:  
————————— WorkTimeInSeconds  
———————————————– in\_treatment -7.720  
p = 0.663

Constant 86.059\*\*\*  
p = 0.000

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Data Subset All Observations 376 R2 0.001 Adjusted R2 -0.002 Residual Std. Error 171.347 (df = 374) F Statistic 0.191 (df = 1; 374) =============================================== Note: *p\<0.1; **p\<0.05; ***p\<0.01                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| The results suggest the negative treatment caused Turkers to spend less time on the task, but the p-value is far from statistically significant again.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| \#\#\#\# 2.3 Learnings from our second experiment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| The estimated 11,600 subjects required to achieve the statistical power we needed was far too many, With a p-value of 0.389, even with the 11,600 subjects, we weren’t likely to find a statistically significant ATE. We need to change our experiment and collect more covariates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| \#\#\# Experiment 3, incentive of future work.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| In both of our pilots, we used a treatment which we hypothesized would cause the Turkers in treatment to work less hard, and the ATE was positive, which in our scoring means the bounding was less accurate. We also wanted to test if a positive treatment would have a larger ATE, so the Turkers in treatment were told we were looking for Turkers to perform some future work with the hypothesis that if the Turkers though of the task as a test with the incentive of future work they would try harder. So we ran a small experiment to test this theory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| \#\#\#\# 3.1 Simple regression analysis                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| \`\`\`r e3\_mod\_1 \<- d\[experiment\_no==3, lm(bounding\_box\_score \~ in\_treatment)\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| stargazer(e3\_mod\_1, e2\_mod\_1, type = ‘text’, header = FALSE, table.placement = ‘h’, report=(’vc\*p’), add.lines = list(c(“Data Subset”, “All”, “All”, “\(x==1\)”)), column.labels=c(“Incentivized”, “Negative Treatment”)) \`\`\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `## ## ========================================================== ##                              Dependent variable: ##                     -------------------------------------- ##                               bounding_box_score ##                        Incentivized    Negative Treatment ##                            (1)                 (2) ## ---------------------------------------------------------- ## in_treatment              3.687               1.835 ##                         p = 0.563           p = 0.656 ## ## Constant                19.028***           15.258*** ##                        p = 0.00004         p = 0.00000 ## ## ---------------------------------------------------------- ## Data Subset                All                 All ## Observations                92                 373 ## R2                        0.004               0.001 ## Adjusted R2               -0.007             -0.002 ## Residual Std. Error  30.379 (df = 90)   39.638 (df = 371) ## F Statistic         0.338 (df = 1; 90) 0.200 (df = 1; 371) ## ========================================================== ## Note:                          *p<0.1; **p<0.05; ***p<0.01`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| The first look was disappointing, the last p-value had gone up from 0.45 in the previous experiment to 0.563 in this, but we only used a quarter the number of subjects. More concerning is the change in the treatment was estimated to change the direction of the coeffecient, and it is still positive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \#\#\#\# 3.2 Analysis with covariates                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| In this experiment we asked the Turkers to answer some questions about the device they were using, their experience doing these types of tasks and some demographic info.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| \`\`\`r e3\_mod\_2 \<- d\[experiment\_no==3, lm(bounding\_box\_score \~ in\_treatment+as.factor(monitor))\] e3\_mod\_3 \<- d\[experiment\_no==3, lm(bounding\_box\_score \~ in\_treatment+as.factor(didbf))\] e3\_mod\_4 \<- d\[experiment\_no==3, lm(bounding\_box\_score \~ in\_treatment+as.factor(age))\] e3\_mod\_5 \<- d\[experiment\_no==3, lm(bounding\_box\_score \~ in\_treatment+as.factor(edu))\] e3\_mod\_6 \<- d\[experiment\_no==3, lm(bounding\_box\_score \~ in\_treatment+as.factor(income))\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| stargazer(e3\_mod\_1, e3\_mod\_2, e3\_mod\_3, e3\_mod\_4, e3\_mod\_5, e3\_mod\_6, type = ‘text’, header = FALSE, table.placement = ‘h’, report=(’vc\*p’), add.lines = list(c(“Data Subset”, “All”, “All”, “\(x==1\)”)), column.labels=c(“Target Alone”, “Monitor size”, “Did task before”, “Age”, “Education”, “Income”)) \`\`\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `## ## ===================================================================================================================================================== ##                                                                                 Dependent variable: ##                               ----------------------------------------------------------------------------------------------------------------------- ##                                                                                 bounding_box_score ##                                  Target Alone        Monitor size       Did task before            Age              Education            Income ##                                      (1)                  (2)                 (3)                  (4)                 (5)                (6) ## ----------------------------------------------------------------------------------------------------------------------------------------------------- ## in_treatment                        3.687                7.794               4.708                2.681               3.280              -0.015 ##                                   p = 0.563            p = 0.231           p = 0.470            p = 0.640           p = 0.613          p = 0.999 ## ## as.factor(monitor)largescreen                         -66.462*** ##                                                       p = 0.0004 ## ## as.factor(monitor)midsize                             -60.451*** ##                                                       p = 0.0005 ## ## as.factor(monitor)smalllaptop                         -57.383*** ##                                                        p = 0.002 ## ## as.factor(monitor)tablet                               -35.061* ##                                                        p = 0.064 ## ## as.factor(didbf)no                                                           7.732 ##                                                                            p = 0.612 ## ## as.factor(didbf)yes                                                          8.810 ##                                                                            p = 0.535 ## ## as.factor(age)31to40                                                                             -9.611 ##                                                                                                 p = 0.372 ## ## as.factor(age)41to50                                                                            97.704*** ##                                                                                                p = 0.00001 ## ## as.factor(age)lt21                                                                               -12.327 ##                                                                                                 p = 0.653 ## ## as.factor(edu)highschool                                                                                             -17.099 ##                                                                                                                     p = 0.438 ## ## as.factor(edu)masterorabove                                                                                          -14.161 ##                                                                                                                     p = 0.154 ## ## as.factor(edu)somecollege                                                                                            -15.051 ##                                                                                                                     p = 0.216 ## ## as.factor(income)gt30klt60k                                                                                                              7.338 ##                                                                                                                                        p = 0.371 ## ## as.factor(income)gt60klt90k                                                                                                              -3.268 ##                                                                                                                                        p = 0.762 ## ## as.factor(income)gt90k                                                                                                                   19.021 ##                                                                                                                                        p = 0.160 ## ## as.factor(income)lt10k                                                                                                                   -8.956 ##                                                                                                                                        p = 0.404 ## ## Constant                          19.028***            72.889***             9.539              18.250***           22.433***          18.375*** ##                                  p = 0.00004          p = 0.00004          p = 0.474           p = 0.00003         p = 0.00001         p = 0.002 ## ## ----------------------------------------------------------------------------------------------------------------------------------------------------- ## Data Subset                          All                  All                 x==1 ## Observations                          92                  92                   90                  92                   92                 92 ## R2                                  0.004                0.200               0.014                0.240               0.045              0.056 ## Adjusted R2                         -0.007               0.153               -0.021               0.205               0.001              0.001 ## Residual Std. Error            30.379 (df = 90)    27.850 (df = 86)     29.643 (df = 86)    26.982 (df = 87)     30.255 (df = 87)   30.251 (df = 86) ## F Statistic                   0.338 (df = 1; 90) 4.297*** (df = 5; 86) 0.393 (df = 3; 86) 6.879*** (df = 4; 87) 1.021 (df = 4; 87) 1.021 (df = 5; 86) ## ===================================================================================================================================================== ## Note:                                                                                                                     *p<0.1; **p<0.05; ***p<0.01` |
| The only covariate which seemed to act as any type of control was the education question, though it wasn’t very significant. However, all of the coeffecients for the screensize question were negative, and by a fairly significant ammount. The baseline value was cellphone, which can be significantly smaller than all the other types of screens. So we tested that on its own.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| \=============================================================== Dependent variable: —————————————- bounding\_box\_score Target Alone Used Cellphone (1) (2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

in\_treatment 3.687 2.239  
p = 0.563 p = 0.710

monitor == “cellphone” 58.789\*\*\*  
p = 0.001

Constant 19.028\*\*\* 17.803\*\*\*  
p = 0.00004 p = 0.00005

|                                                                                                                                                                                                                                                                                                                                   |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Subset All All Observations 92 92 R2 0.004 0.123 Adjusted R2 -0.007 0.104 Residual Std. Error 30.379 (df = 90) 28.655 (df = 89) F Statistic 0.338 (df = 1; 90) 6.268\*\*\* (df = 2; 89) =============================================================== Note: *p\<0.1; **p\<0.05; ***p\<0.01                                 |
| If the subject is using a cellphone to do the task, their accuracy goes down (score increases), which is intuitive. Having cellphone as a control decreases the p-value from 0.56 to 0.33. With more data, this could be quite a bit lower. But it still doesn’t explain why subjects with more incentive are doing a poorer job. |
| As with the previous experiment, we also analyzed how the treatment affected the amount of time they spent on the task.                                                                                                                                                                                                           |
| \========================================================== Dependent variable: ————————————– WorkTimeInSeconds Incentivized Negative Treatment (1) (2)                                                                                                                                                                           |

in\_treatment 22.983 -7.720  
p = 0.766 p = 0.663

Constant 377.208\*\*\* 86.059\*\*\*  
p = 0.000 p = 0.000

|                                                                                                                                                                                                                                                                                                                                                            |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Subset All All Observations 95 376 R2 0.001 0.001 Adjusted R2 -0.010 -0.002 Residual Std. Error 374.924 (df = 93) 171.347 (df = 374) F Statistic 0.089 (df = 1; 93) 0.191 (df = 1; 374) ========================================================== Note: *p\<0.1; **p\<0.05; ***p\<0.01                                                               |
| The regression shows those in treatment on average spent 23 seconds more time, this alone is concerning, as the task itself shouldn’t take that much time.                                                                                                                                                                                                 |
| ![](team_mturk_experiments_files/figure-gfm/experiment_3_summary_time-1.png)<!-- -->                                                                                                                                                                                                                                                                       |
| There are alot of values suggesting that Turkers are not conentrating on our task, it could be they are spawning multiple tabs. Regardless, working time is not helpful for our experiment.                                                                                                                                                                |
| \#\#\#\# 3.1 Power Test                                                                                                                                                                                                                                                                                                                                    |
| With a lot of speculation about whether our statistical significance would go up with more data, we tested that theory by doing a power calculation.                                                                                                                                                                                                       |
| `## ##      Two-sample t test power calculation ## ##               n = 834.1739 ##           delta = 3.686703 ##              sd = 30.26851 ##       sig.level = 0.05 ##           power = 0.8 ##     alternative = one.sided ## ## NOTE: n is number in *each* group`                                                                                    |
| The power calculation when using the negative treatment, telling those in treatment that they were doing work for a government surveillance system estimated we needed 5,800 subjects. Using an incentive of possible future work as the treatment, the ATE has less variance, and estimated that we only need 835 subjects to get 0.80 statistical power. |
| \#\#\# Experiment 4, More data                                                                                                                                                                                                                                                                                                                             |
| To improve the statistical power from Experiment 3, we are adding more data and sending out another 100 control tasks to Turkers and 100 with the same treatment.                                                                                                                                                                                          |
| \#TODO covariate balance check, demographic info show how random it is.                                                                                                                                                                                                                                                                                    |
| \========================================================== Dependent variable: ————————————– bounding\_box\_score n=100 + n=200 n=100 (1) (2)                                                                                                                                                                                                             |

in\_treatment -15.895 3.687  
p = 0.116 p = 0.563

Constant 33.046\*\*\* 19.028\*\*\*  
p = 0.00001 p = 0.00004

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Subset All All Observations 277 92 R2 0.009 0.004 Adjusted R2 0.005 -0.007 Residual Std. Error 83.748 (df = 275) 30.379 (df = 90) F Statistic 2.494 (df = 1; 275) 0.338 (df = 1; 90) ========================================================== Note: *p\<0.1; **p\<0.05; ***p\<0.01                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| The results are much better, adding another 200 subjects helped decrease the p-value from 0.56 to 0.12, and our ATE is -15.9, a negative number means the bounding boxes from treatment are more accurate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| \`\`\`r \#e4\_mod\_2 \<- d\[experiment\_no %in% c(3,4), lm(bounding\_box\_score \~ in\_treatment+is\_mobile+tried=(monitor=="" & mousetrackpad==""))\] \#summary(e4\_mod\_2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| \#e4\_mod\_2 \<- d\[experiment\_no %in% c(3,4), .(tried=as.numeric(is.na(monitor) & is.na(mousetrackpad)), bounding\_box\_score, in\_treatment, is\_mobile, WorkTimeInSeconds)\] %\>% \# .\[, lm(bounding\_box\_score \~ in\_treatment+is\_mobile+tried)\] \#summary(e4\_mod\_2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| \#e4\_mod\_2 \<- d\[experiment\_no %in% c(3,4), .(tried=as.numeric(is.na(monitor)), bounding\_box\_score, in\_treatment, is\_mobile, Reward)\] %\>% \# .\[, lm(bounding\_box\_score \~ in\_treatment+is\_mobile+tried)\] \#summary(e4\_mod\_2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| e4\_mod\_2 \<- d\[experiment\_no %in% c(3,4), lm(bounding\_box\_score \~ in\_treatment+is\_mobile)\] stargazer(e4\_mod\_1, e4\_mod\_2, type = ‘text’, header = FALSE, table.placement = ‘h’, report=(’vc\*p’), add.lines = list(c(“Data Subset”, “All”, “All”, “\(x==1\)”)), column.labels=c(“Target Alone”, “Cellphone”)) \`\`\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `## ## ============================================================== ##                                Dependent variable: ##                     ------------------------------------------ ##                                 bounding_box_score ##                        Target Alone           Cellphone ##                             (1)                  (2) ## -------------------------------------------------------------- ## in_treatment              -15.895              -14.181 ##                          p = 0.116            p = 0.155 ## ## is_mobile                                     50.409*** ##                                               p = 0.003 ## ## Constant                 33.046***            27.285*** ##                         p = 0.00001           p = 0.0002 ## ## -------------------------------------------------------------- ## Data Subset                 All                  All ## Observations                277                  277 ## R2                         0.009                0.041 ## Adjusted R2                0.005                0.034 ## Residual Std. Error  83.748 (df = 275)    82.547 (df = 274) ## F Statistic         2.494 (df = 1; 275) 5.812*** (df = 2; 274) ## ============================================================== ## Note:                              *p<0.1; **p<0.05; ***p<0.01` |
| \`\`\`r \#e4\_mod\_3 \<- d\[experiment\_no %in% c(3,4), lm(bounding\_box\_score \~ in\_treatment+factor(monitor))\] \#e4\_mod\_4 \<- d\[experiment\_no %in% c(3,4), lm(bounding\_box\_score \~ in\_treatment+factor(didbf))\] \#e4\_mod\_5 \<- d\[experiment\_no %in% c(3,4), lm(bounding\_box\_score \~ in\_treatment+factor(age))\] \#e4\_mod\_6 \<- d\[experiment\_no %in% c(3,4), lm(bounding\_box\_score \~ in\_treatment+factor(edu))\] \#e4\_mod\_7 \<- d\[experiment\_no %in% c(3,4), lm(bounding\_box\_score \~ in\_treatment+factor(income))\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| \#stargazer(e4\_mod\_3, e4\_mod\_4, e4\_mod\_5, e4\_mod\_6, e4\_mod\_7, \# type = ‘text’, header = FALSE, table.placement = ‘h’, report=(’vc\*p’), \# add.lines = list(c(“Data Subset”, “All”, “All”, “\(x==1\)”))) \`\`\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| \#\#\#\# 4.1 Power Test                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \`\`\`r e4\_ate = d\[experiment\_no %in% c(3, 4) & in\_treatment == 1, mean(bounding\_box\_score, na.rm=T)\] - d\[experiment\_no %in% c(3, 4) & in\_treatment == 0, mean(bounding\_box\_score, na.rm=T)\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| e4\_sd = d\[experiment\_no %in% c(3, 4), sd(bounding\_box\_score, na.rm=T)\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| power.t.test(delta=abs(e4\_ate), sd=e4\_sd, sig.level = 0.05, power = 0.80, alternative = “one.sided”, n = NULL) \`\`\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `## ##      Two-sample t test power calculation ## ##               n = 345.7973 ##           delta = 15.89495 ##              sd = 83.97393 ##       sig.level = 0.05 ##           power = 0.8 ##     alternative = one.sided ## ## NOTE: n is number in *each* group`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \`\`\`r power\_curve \<- function(x) { result = c()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| for (i in 1:length(x)) { new\_n \<- power.t.test(delta=abs(e4\_ate), sd=e4\_sd, sig.level = 0.05, power = NULL, alternative = “one.sided”, n = x\[i\])\[“power”\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| result \<- c(result, new\_n) }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| return(result) }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| sig\_curve \<- function(x) { result = c()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| for (i in 1:length(x)) { new\_n \<- power.t.test(delta=abs(e4\_ate), sd=e4\_sd, sig.level = NULL, power = 0.8, alternative = “one.sided”, n = x\[i\])\[“sig.level”\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| result \<- c(result, new\_n) }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| return(result) }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| delta\_curve \<- function(x) { result = c()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| for (i in 1:length(x)) { new\_n \<- power.t.test(delta=x\[i\], sd=e4\_sd, sig.level = 0.05, power = 0.8, alternative = “one.sided”, n = NULL)\[“n”\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| result \<- c(result, new\_n) }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| return(result) } curve(power\_curve(x), 10, 1000) \`\`\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ![](team_mturk_experiments_files/figure-gfm/unnamed-chunk-7-1.png)<!-- -->                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `r #curve(sig_curve(x), 10, 1000) #curve(delta_curve(x), 5, 20)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| \#\#\# Experiment 5, threats don’t work                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `r e5_mod_1 <- d[experiment_no == 5, lm(bounding_box_score ~ in_treatment)] summary(e5_mod_1)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `## ## Call: ## lm(formula = bounding_box_score ~ in_treatment) ## ## Residuals: ##     Min      1Q  Median      3Q     Max ## -12.005  -7.388  -4.123   0.854 193.311 ## ## Coefficients: ##              Estimate Std. Error t value Pr(>\|t\|) ## (Intercept)    13.552      1.848   7.334 6.38e-12 *** ## in_treatment   -1.938      2.606  -0.743    0.458 ## --- ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1 ## ## Residual standard error: 18.01 on 189 degrees of freedom ##   (2 observations deleted due to missingness) ## Multiple R-squared:  0.002916,   Adjusted R-squared:  -0.00236 ## F-statistic: 0.5527 on 1 and 189 DF,  p-value: 0.4582`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| \#\#\# Experiment 6, threats still don’t work                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `r e6_mod_1 <- d[experiment_no == 6, lm(bounding_box_score ~ in_treatment)] summary(e6_mod_1)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `## ## Call: ## lm(formula = bounding_box_score ~ in_treatment) ## ## Residuals: ##    Min     1Q Median     3Q    Max ## -12.02  -8.64  -6.39  -1.38 107.83 ## ## Coefficients: ##              Estimate Std. Error t value Pr(>\|t\|) ## (Intercept)   13.5632     1.9581   6.927 6.99e-11 *** ## in_treatment  -0.4096     2.7842  -0.147    0.883 ## --- ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1 ## ## Residual standard error: 18.98 on 184 degrees of freedom ## Multiple R-squared:  0.0001176,  Adjusted R-squared:  -0.005317 ## F-statistic: 0.02164 on 1 and 184 DF,  p-value: 0.8832`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `r e6_mod_2 <- d[experiment_no %in% c(5,6), lm(bounding_box_score ~ in_treatment+(Reward == "$0.05"))] summary(e6_mod_2)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `## ## Call: ## lm(formula = bounding_box_score ~ in_treatment + (Reward == "$0.05")) ## ## Residuals: ##     Min      1Q  Median      3Q     Max ## -12.399  -8.042  -5.148  -0.011 193.690 ## ## Coefficients: ##                       Estimate Std. Error t value Pr(>\|t\|) ## (Intercept)            13.1730     1.6439   8.013 1.44e-14 *** ## in_treatment           -1.1838     1.9033  -0.622    0.534 ## Reward == "$0.05"TRUE   0.7731     1.9034   0.406    0.685 ## --- ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1 ## ## Residual standard error: 18.48 on 374 degrees of freedom ##   (2 observations deleted due to missingness) ## Multiple R-squared:  0.001484,   Adjusted R-squared:  -0.003855 ## F-statistic: 0.278 on 2 and 374 DF,  p-value: 0.7575`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| \#\#\# Experiment 7, Even MORE incentive data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| \====================================================================================================== Dependent variable: ———————————————————————————- bounding\_box\_score n=300 n=300 and cellphone n=700 n=700 and cellphone (1) (2) (3) (4)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

in\_treatment -15.895 -14.181 -2.020 -16.466  
p = 0.116 p = 0.155 p = 0.738 p = 0.105

is\_mobile 50.409\*\*\*  
p = 0.003

is\_cellphone 25.693  
p = 0.426

Constant 33.046\*\*\* 27.285\*\*\* 21.633\*\*\* 32.679\*\*\*  
p = 0.00001 p = 0.0002 p = 0.00000 p = 0.00001

-----

Data Subset All All x==1  
Observations 277 277 642 277  
R2 0.009 0.041 0.0002 0.011  
Adjusted R2 0.005 0.034 -0.001 0.004  
Residual Std. Error 83.748 (df = 275) 82.547 (df = 274) 76.188 (df =
640) 83.803 (df = 274) F Statistic 2.494 (df = 1; 275) 5.812\*\*\* (df =
2; 274) 0.113 (df = 1; 640) 1.565 (df = 2; 274)
======================================================================================================
Note: *p\<0.1; **p\<0.05; ***p\<0.01

``` r
e7_ate = d[experiment_no %in% c(3, 4, 7) & in_treatment == 1, mean(bounding_box_score, na.rm=T)] - d[experiment_no %in% c(3, 4, 7) & in_treatment == 0, mean(bounding_box_score, na.rm=T)]

e7_sd = d[experiment_no %in% c(3, 4, 7), sd(bounding_box_score, na.rm=T)]


power.t.test(delta=abs(e7_ate), 
             sd=e7_sd, 
             sig.level = 0.05,
             power = 0.80,
             alternative = "one.sided",
             n = NULL)
```

    ## 
    ##      Two-sample t test power calculation 
    ## 
    ##               n = 17560.84
    ##           delta = 2.020332
    ##              sd = 76.13563
    ##       sig.level = 0.05
    ##           power = 0.8
    ##     alternative = one.sided
    ## 
    ## NOTE: n is number in *each* group
