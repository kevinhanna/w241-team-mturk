Team mTurk - Motivating Quality Work
================
Kevin Hanna, Kevin Stone, Changjing Zhao

  - [Motivating Quality Work](#motivating-quality-work)
      - [What motivates crowdsourced workers to do quality
        work?](#what-motivates-crowdsourced-workers-to-do-quality-work)
      - [Our Experiments](#our-experiments)
      - [Experiment 1, our first pilot](#experiment-1-our-first-pilot)
      - [Experiment 2, our second pilot](#experiment-2-our-second-pilot)
      - [Experiment 3, promise](#experiment-3-promise)
      - [Experiment 4, More data](#experiment-4-more-data)
      - [Experiment 5, threats don’t
        work](#experiment-5-threats-dont-work)
      - [Experiment 6, threats still don’t
        work](#experiment-6-threats-still-dont-work)

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

| experiment\_no | is\_pilot | in\_treatment | count | mean\_score |  std\_dev |
| -------------: | --------: | ------------: | ----: | ----------: | --------: |
|              1 |         1 |             0 |   397 |   137.60402 | 295.29711 |
|              1 |         1 |             1 |   396 |   136.39470 | 296.29412 |
|              2 |         1 |             0 |   187 |    15.25847 |  36.79851 |
|              2 |         1 |             1 |   189 |    17.09362 |  42.27343 |
|              3 |         0 |             0 |    48 |    19.02776 |  23.08104 |
|              3 |         0 |             1 |    47 |    22.71446 |  36.73351 |
|              4 |         0 |             0 |    93 |    40.35981 | 139.47131 |
|              4 |         0 |             1 |    94 |    14.51884 |  25.36227 |
|              5 |         0 |             0 |    96 |    13.55187 |  23.01864 |
|              5 |         0 |             1 |    97 |    11.61424 |  11.00214 |
|              6 |         0 |             0 |    94 |    13.56319 |  20.70507 |
|              6 |         0 |             1 |    92 |    13.15357 |  17.04807 |

Experiment Data Summary

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

![](team_mturk_experiments_files/figure-gfm/plot_experiment_1-1.png)<!-- -->![](team_mturk_experiments_files/figure-gfm/plot_experiment_1-2.png)<!-- -->

|  | mean\_worker\_score |
|  | :------------------ |
|  | Min. : 5.003        |
|  | 1st Qu.: 25.938     |
|  | Median :119.894     |
|  | Mean :135.288       |
|  | 3rd Qu.:178.160     |
|  | Max. :994.601       |
|  | NA’s :1             |

| in\_treatment | mean\_score | std\_dev |
| ------------: | ----------: | -------: |
|             0 |    146.7838 | 125.4300 |
|             1 |    118.8101 | 190.9985 |

``` r
#TODO Gauge if effort decreases with more HITTs
```

### Experiment 2, our second pilot

With the first pilot behind us, we decided we needed to focus on
increasing our statistical power and hypothesized that having more
subjects with fewer experiments would provide more statistical power.

![](team_mturk_experiments_files/figure-gfm/plot_experiment_2-1.png)<!-- -->![](team_mturk_experiments_files/figure-gfm/plot_experiment_2-2.png)<!-- -->

    ##  bounding_box_score
    ##  Min.   :  1.423   
    ##  1st Qu.:  5.054   
    ##  Median :  8.320   
    ##  Mean   : 16.178   
    ##  3rd Qu.: 13.498   
    ##  Max.   :489.540   
    ##  NA's   :3

| in\_treatment | mean\_score | std\_dev |
| ------------: | ----------: | -------: |
|             0 |    15.25847 | 36.79851 |
|             1 |    17.09362 | 42.27343 |

``` r
e2_mod_1 <- d[experiment_no==2, lm(bounding_box_score ~ in_treatment)]
summary(e2_mod_1)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment)
    ## 
    ## Residuals:
    ##    Min     1Q Median     3Q    Max 
    ## -15.27 -10.80  -7.74  -2.85 472.45 
    ## 
    ## Coefficients:
    ##              Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)    15.258      2.906   5.250 2.57e-07 ***
    ## in_treatment    1.835      4.105   0.447    0.655    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 39.64 on 371 degrees of freedom
    ##   (3 observations deleted due to missingness)
    ## Multiple R-squared:  0.0005385,  Adjusted R-squared:  -0.002156 
    ## F-statistic: 0.1999 on 1 and 371 DF,  p-value: 0.6551

Even with a p-value of 0.655, this was progress. Our coefficient for in
treatment was still more likely due to random noise than not.

#### 2.1 Power Test

``` r
e2_ate = d[experiment_no==2 & in_treatment == 1, mean(bounding_box_score, na.rm=T)] - d[experiment_no==2 & in_treatment == 0, mean(bounding_box_score, na.rm=T)]

e2_sd = d[experiment_no==2, sd(bounding_box_score, na.rm=T)]


power.t.test(delta=e2_ate, 
             sd=e2_sd, 
             sig.level = 0.05,
             power = 0.80,
             alternative = "one.sided",
             n = NULL)
```

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

### Experiment 3, promise

\#TODO demographic info show how random it is.

``` r
e3_mod_1 <- d[experiment_no==3, lm(bounding_box_score ~ in_treatment)]
summary(e3_mod_1)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -20.322 -14.375  -9.781  -1.417 197.172 
    ## 
    ## Coefficients:
    ##              Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)    19.028      4.385   4.339 3.73e-05 ***
    ## in_treatment    3.687      6.340   0.581    0.562    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 30.38 on 90 degrees of freedom
    ##   (3 observations deleted due to missingness)
    ## Multiple R-squared:  0.003742,   Adjusted R-squared:  -0.007327 
    ## F-statistic: 0.3381 on 1 and 90 DF,  p-value: 0.5624

``` r
e3_mod_2 <- d[experiment_no==3, lm(bounding_box_score ~ in_treatment+as.factor(mousetrackpad))]
summary(e3_mod_2)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment + as.factor(mousetrackpad))
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -22.645 -14.927  -9.188  -0.139 194.850 
    ## 
    ## Coefficients:
    ##                                  Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)                        20.386      4.612   4.421 2.89e-05 ***
    ## in_treatment                        4.651      6.586   0.706    0.482    
    ## as.factor(mousetrackpad)trackpad  -16.384     12.157  -1.348    0.181    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 30.81 on 85 degrees of freedom
    ##   (7 observations deleted due to missingness)
    ## Multiple R-squared:  0.02541,    Adjusted R-squared:  0.00248 
    ## F-statistic: 1.108 on 2 and 85 DF,  p-value: 0.3349

#### 3.1 Power Test

``` r
e3_ate = d[experiment_no==3 & in_treatment == 1, mean(bounding_box_score, na.rm=T)] - d[experiment_no==3 & in_treatment == 0, mean(bounding_box_score, na.rm=T)]

e3_sd = d[experiment_no==3, sd(bounding_box_score, na.rm=T)]


power.t.test(delta=e3_ate, 
             sd=e3_sd, 
             sig.level = 0.05,
             power = 0.80,
             alternative = "one.sided",
             n = NULL)
```

    ## 
    ##      Two-sample t test power calculation 
    ## 
    ##               n = 834.1739
    ##           delta = 3.686703
    ##              sd = 30.26851
    ##       sig.level = 0.05
    ##           power = 0.8
    ##     alternative = one.sided
    ## 
    ## NOTE: n is number in *each* group

### Experiment 4, More data

``` r
e4_mod_1 <- d[experiment_no %in% c(3,4), lm(bounding_box_score ~ in_treatment)]
summary(e4_mod_1)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment)
    ## 
    ## Residuals:
    ##    Min     1Q Median     3Q    Max 
    ## -30.80 -23.02 -12.37  -5.59 974.46 
    ## 
    ## Coefficients:
    ##              Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)    33.046      7.078   4.669 4.74e-06 ***
    ## in_treatment  -15.895     10.064  -1.579    0.115    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 83.75 on 275 degrees of freedom
    ##   (5 observations deleted due to missingness)
    ## Multiple R-squared:  0.008989,   Adjusted R-squared:  0.005385 
    ## F-statistic: 2.494 on 1 and 275 DF,  p-value: 0.1154

``` r
#d[experiment_no %in% c(1), .(sd(bounding_box_score)), keyby=WorkerId]
```

``` r
#e4_mod_2 <- d[experiment_no %in% c(3,4), lm(bounding_box_score ~ in_treatment+is_mobile+tried=(monitor=="" &   mousetrackpad==""))]
#summary(e4_mod_2)

e4_mod_2 <- d[experiment_no %in% c(3,4), .(tried=as.numeric(monitor=="" &   mousetrackpad==""), bounding_box_score, in_treatment, is_mobile, WorkTimeInSeconds)] %>% 
  .[, lm(bounding_box_score ~ in_treatment+is_mobile+tried)]
summary(e4_mod_2)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment + is_mobile + 
    ##     tried)
    ## 
    ## Residuals:
    ##    Min     1Q Median     3Q    Max 
    ## -74.74 -17.37  -8.55  -2.25 930.51 
    ## 
    ## Coefficients: (1 not defined because of singularities)
    ##              Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)    25.475      7.167   3.554 0.000447 ***
    ## in_treatment  -12.460      9.825  -1.268 0.205791    
    ## is_mobile      51.518     16.535   3.116 0.002031 ** 
    ## tried              NA         NA      NA       NA    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 81.47 on 273 degrees of freedom
    ##   (6 observations deleted due to missingness)
    ## Multiple R-squared:  0.0415, Adjusted R-squared:  0.03448 
    ## F-statistic:  5.91 on 2 and 273 DF,  p-value: 0.003072

``` r
e4_mod_2 <- d[experiment_no %in% c(3,4), .(tried=as.numeric(mousetrackpad==""), bounding_box_score, in_treatment, is_mobile, Reward)] %>% 
  .[, lm(bounding_box_score ~ in_treatment+is_mobile+tried)]
summary(e4_mod_2)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment + is_mobile + 
    ##     tried)
    ## 
    ## Residuals:
    ##    Min     1Q Median     3Q    Max 
    ## -79.68 -17.51  -8.75  -2.47 925.57 
    ## 
    ## Coefficients: (1 not defined because of singularities)
    ##              Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)    25.650      7.313   3.507 0.000531 ***
    ## in_treatment  -12.388     10.058  -1.232 0.219162    
    ## is_mobile      56.283     17.320   3.250 0.001304 ** 
    ## tried              NA         NA      NA       NA    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 82.33 on 266 degrees of freedom
    ##   (13 observations deleted due to missingness)
    ## Multiple R-squared:  0.04525,    Adjusted R-squared:  0.03807 
    ## F-statistic: 6.303 on 2 and 266 DF,  p-value: 0.002115

``` r
e4_mod_2 <- d[experiment_no %in% c(3,4), lm(bounding_box_score ~ in_treatment+is_mobile)]
summary(e4_mod_2)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment + is_mobile)
    ## 
    ## Residuals:
    ##    Min     1Q Median     3Q    Max 
    ## -75.44 -18.89  -8.88  -2.36 929.81 
    ## 
    ## Coefficients:
    ##              Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)    27.285      7.234   3.772 0.000199 ***
    ## in_treatment  -14.181      9.936  -1.427 0.154659    
    ## is_mobile      50.409     16.750   3.010 0.002860 ** 
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 82.55 on 274 degrees of freedom
    ##   (5 observations deleted due to missingness)
    ## Multiple R-squared:  0.0407, Adjusted R-squared:  0.0337 
    ## F-statistic: 5.812 on 2 and 274 DF,  p-value: 0.003371

``` r
stargazer(e3_mod_1, e4_mod_1, 
          type = 'text', header = FALSE, table.placement = 'h', 
          add.lines = list(c("Data Subset", "All", "All", "$x==1$")))
```

\========================================================== Dependent
variable:  
————————————– bounding\_box\_score  
(1) (2)  
———————————————————- in\_treatment 3.687 -15.895  
(6.340) (10.064)

Constant 19.028\*\*\* 33.046\*\*\*  
(4.385) (7.078)

|                                                                                                                                                                                                                                                                                           |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Subset All All Observations 92 277 R2 0.004 0.009 Adjusted R2 -0.007 0.005 Residual Std. Error 30.379 (df = 90) 83.748 (df = 275) F Statistic 0.338 (df = 1; 90) 2.494 (df = 1; 275) ========================================================== Note: *p\<0.1; **p\<0.05; ***p\<0.01 |
| `r stargazer(e4_mod_1, e4_mod_2, type = 'text', header = FALSE, table.placement = 'h', add.lines = list(c("Data Subset", "All", "All", "$x==1$")))`                                                                                                                                       |
| \============================================================== Dependent variable: —————————————— bounding\_box\_score (1) (2)                                                                                                                                                           |

in\_treatment -15.895 -14.181  
(10.064) (9.936)

is\_mobile 50.409\*\*\*  
(16.750)

Constant 33.046\*\*\* 27.285\*\*\*  
(7.078) (7.234)

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Subset All All Observations 277 277 R2 0.009 0.041 Adjusted R2 0.005 0.034 Residual Std. Error 83.748 (df = 275) 82.547 (df = 274) F Statistic 2.494 (df = 1; 275) 5.812\*\*\* (df = 2; 274) ============================================================== Note: *p\<0.1; **p\<0.05; ***p\<0.01                                                                                                                                                                                                                                                                                                            |
| \`\`\`r e4\_mod\_3 \<- d\[experiment\_no %in% c(3,4), lm(bounding\_box\_score \~ in\_treatment+factor(monitor, exclude=c(NA)))\] e4\_mod\_4 \<- d\[experiment\_no %in% c(3,4), lm(bounding\_box\_score \~ in\_treatment+factor(didbf, exclude=c(NA)))\] e4\_mod\_5 \<- d\[experiment\_no %in% c(3,4), lm(bounding\_box\_score \~ in\_treatment+factor(age, exclude=NA))\] e4\_mod\_6 \<- d\[experiment\_no %in% c(3,4), lm(bounding\_box\_score \~ in\_treatment+factor(edu, exclude=NA))\] e4\_mod\_7 \<- d\[experiment\_no %in% c(3,4), lm(bounding\_box\_score \~ in\_treatment+factor(income, exclude=NA))\] |
| stargazer(e4\_mod\_3, e4\_mod\_4, e4\_mod\_5, e4\_mod\_6, e4\_mod\_7, type = ‘text’, header = FALSE, table.placement = ‘h’, add.lines = list(c(“Data Subset”, “All”, “All”, “\(x==1\)”))) \`\`\`                                                                                                                                                                                                                                                                                                                                                                                                                 |
| \================================================================================================================================================== Dependent variable: —————————————————————————————————— bounding\_box\_score (1) (2) (3) (4) (5)                                                                                                                                                                                                                                                                                                                                                              |

in\_treatment -11.593 -15.436 -15.364 -13.246 -15.622  
(9.947) (10.358) (10.083) (10.205) (9.981)

factor(monitor, exclude = c(NA))largescreen -36.873  
(32.733)

factor(monitor, exclude = c(NA))midsize -26.643  
(31.902)

factor(monitor, exclude = c(NA))notsure -39.773  
(51.355)

factor(monitor, exclude = c(NA))smalllaptop -28.512  
(32.632)

factor(monitor, exclude = c(NA))tablet 29.360  
(36.186)

factor(didbf, exclude = c(NA))no 10.107  
(23.372)

factor(didbf, exclude = c(NA))yes 20.584  
(21.478)

factor(age, exclude = NA)31to40 6.252  
(12.684)

factor(age, exclude = NA)4150 1.080  
(20.540)

factor(age, exclude = NA)lt21 -18.433  
(30.134)

factor(age, exclude = NA)over50 -19.531  
(34.542)

factor(edu, exclude = NA)highschool -9.949  
(21.438)

factor(edu, exclude = NA)lthighschool -20.530  
(59.350)

factor(edu, exclude = NA)masterorabove 0.497  
(14.641)

factor(edu, exclude = NA)somecollege -9.642  
(12.514)

factor(income, exclude = NA)gt30klt60k 33.347\*\*\*  
(12.839)

factor(income, exclude = NA)gt60klt90k 1.730  
(15.998)

factor(income, exclude = NA)gt90k 14.138  
(20.109)

factor(income, exclude = NA)lt10k 3.463  
(14.509)

Constant 54.891\* 14.827 31.576\*\*\* 33.822\*\*\* 20.655\*\*  
(31.747) (20.399) (7.821) (8.470) (9.943)

-----

Data Subset All All x==1  
Observations 276 269 276 275 275  
R2 0.046 0.012 0.011 0.011 0.037  
Adjusted R2 0.025 0.001 -0.007 -0.008 0.019  
Residual Std. Error 81.864 (df = 269) 83.771 (df = 265) 83.205 (df =
270) 83.383 (df = 269) 82.269 (df = 269)  
F Statistic 2.179\*\* (df = 6; 269) 1.101 (df = 3; 265) 0.610 (df = 5;
270) 0.573 (df = 5; 269) 2.059\* (df = 5; 269)
==================================================================================================================================================
Note: *p\<0.1; **p\<0.05; ***p\<0.01

#### 4.1 Power Test

``` r
e4_ate = d[experiment_no %in% c(3, 4) & in_treatment == 1, mean(bounding_box_score, na.rm=T)] - d[experiment_no %in% c(3, 4) & in_treatment == 0, mean(bounding_box_score, na.rm=T)]

e4_sd = d[experiment_no %in% c(3, 4), sd(bounding_box_score, na.rm=T)]


power.t.test(delta=abs(e4_ate), 
             sd=e4_sd, 
             sig.level = 0.05,
             power = 0.80,
             alternative = "one.sided",
             n = NULL)
```

    ## 
    ##      Two-sample t test power calculation 
    ## 
    ##               n = 345.7973
    ##           delta = 15.89495
    ##              sd = 83.97393
    ##       sig.level = 0.05
    ##           power = 0.8
    ##     alternative = one.sided
    ## 
    ## NOTE: n is number in *each* group

``` r
power_curve <- function(x) {
  result = c()

  for (i in 1:length(x)) {
    new_n <- power.t.test(delta=abs(e4_ate), 
             sd=e4_sd, 
             sig.level = 0.05,
             power = NULL,
             alternative = "one.sided",
             n = x[i])["power"]
    
    result <- c(result, new_n)
  }
  
  return(result)
}

sig_curve <- function(x) {
  result = c()

  for (i in 1:length(x)) {
    new_n <- power.t.test(delta=abs(e4_ate), 
             sd=e4_sd, 
             sig.level = NULL,
             power = 0.8,
             alternative = "one.sided",
             n = x[i])["sig.level"]
    
    result <- c(result, new_n)
  }
  
  return(result)
}

delta_curve <- function(x) {
  result = c()

  for (i in 1:length(x)) {
    new_n <- power.t.test(delta=x[i], 
             sd=e4_sd, 
             sig.level = 0.05,
             power = 0.8,
             alternative = "one.sided",
             n = NULL)["n"]
    
    result <- c(result, new_n)
  }
  
  return(result)
}
curve(power_curve(x), 10, 1000)
```

![](team_mturk_experiments_files/figure-gfm/unnamed-chunk-13-1.png)<!-- -->

``` r
#curve(sig_curve(x), 10, 1000)
#curve(delta_curve(x), 5, 20)
```

### Experiment 5, threats don’t work

``` r
e5_mod_1 <- d[experiment_no == 5, lm(bounding_box_score ~ in_treatment)]
summary(e5_mod_1)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -12.005  -7.388  -4.123   0.854 193.311 
    ## 
    ## Coefficients:
    ##              Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)    13.552      1.848   7.334 6.38e-12 ***
    ## in_treatment   -1.938      2.606  -0.743    0.458    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 18.01 on 189 degrees of freedom
    ##   (2 observations deleted due to missingness)
    ## Multiple R-squared:  0.002916,   Adjusted R-squared:  -0.00236 
    ## F-statistic: 0.5527 on 1 and 189 DF,  p-value: 0.4582

### Experiment 6, threats still don’t work

``` r
e6_mod_1 <- d[experiment_no == 6, lm(bounding_box_score ~ in_treatment)]
summary(e6_mod_1)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment)
    ## 
    ## Residuals:
    ##    Min     1Q Median     3Q    Max 
    ## -12.02  -8.64  -6.39  -1.38 107.83 
    ## 
    ## Coefficients:
    ##              Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)   13.5632     1.9581   6.927 6.99e-11 ***
    ## in_treatment  -0.4096     2.7842  -0.147    0.883    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 18.98 on 184 degrees of freedom
    ## Multiple R-squared:  0.0001176,  Adjusted R-squared:  -0.005317 
    ## F-statistic: 0.02164 on 1 and 184 DF,  p-value: 0.8832

``` r
e6_mod_2 <- d[experiment_no %in% c(5,6), lm(bounding_box_score ~ in_treatment+(Reward == "$0.05"))]
summary(e6_mod_2)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment + (Reward == "$0.05"))
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -12.399  -8.042  -5.148  -0.011 193.690 
    ## 
    ## Coefficients:
    ##                       Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)            13.1730     1.6439   8.013 1.44e-14 ***
    ## in_treatment           -1.1838     1.9033  -0.622    0.534    
    ## Reward == "$0.05"TRUE   0.7731     1.9034   0.406    0.685    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 18.48 on 374 degrees of freedom
    ##   (2 observations deleted due to missingness)
    ## Multiple R-squared:  0.001484,   Adjusted R-squared:  -0.003855 
    ## F-statistic: 0.278 on 2 and 374 DF,  p-value: 0.7575
