Team mTurk - Image Bounding Scoring
================

Our scoring metric measures the accuracy of the bounding box by
calculating the ucledian distance of the Turkers bounds to the correct
bounding. Therefor a **lower score is better**. When the treatment
should cause a negative reaction, the score should increase if our
hypothesis is correct.

``` r
# Read in all the data, we'll use the 'experiment_no' to pull the results from each experiment. 
d <- fread("./data/experiment_all/experiment_results.csv")
```

``` r
# None of our experiments required creating multiple bounding boxes on a single image.
# We are assuming the extra bounding boxes are mistakes and taking the better score.
remove_extra_bounding_boxes <- function(d) {
  good_scores <- d[,  .(bounding_box_score = min(bounding_box_score), count = .N), keyby=.(WorkerId, ImageId, experiment_no, in_treatment)] %>% .[count<2, ]
  d[good_scores, on=.(WorkerId, ImageId, experiment_no, bounding_box_score, in_treatment)]
}

d <- remove_extra_bounding_boxes(d)
```

# Sanity Check

``` r
d[, .(count=.N, mean_score=mean(bounding_box_score, na.rm=T), std_dev=sd(bounding_box_score, na.rm=T)), keyby=.(experiment_no, is_pilot, in_treatment)]
```

    ##     experiment_no is_pilot in_treatment count mean_score   std_dev
    ##  1:             1        1            0   397  137.60402 295.29711
    ##  2:             1        1            1   396  136.39470 296.29412
    ##  3:             2        1            0   187   15.25847  36.79851
    ##  4:             2        1            1   189   17.09362  42.27343
    ##  5:             3        0            0    48   19.02776  23.08104
    ##  6:             3        0            1    47   22.71446  36.73351
    ##  7:             4        0            0    93   40.35981 139.47131
    ##  8:             4        0            1    94   14.51884  25.36227
    ##  9:             5        0            0    96   13.55187  23.01864
    ## 10:             5        0            1    97   11.61424  11.00214

# Experiment 1, our first pilot

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

We were not able to trust any ETA, but we could at least see the
variance, which was exceptionally high.

``` r
# Block the results by user taking their mean score
worker_mean_score <- d[experiment_no==1, .(score = mean(bounding_box_score), in_treatment = as.integer(median(in_treatment))), keyby=WorkerId]

worker_mean_score[, plot(score, col=(in_treatment+1))]
```

![](team_mturk_experiments_files/figure-gfm/unnamed-chunk-4-1.png)<!-- -->

    ## NULL

``` r
worker_mean_score[, plot(log(score), col=(in_treatment+1))]
```

![](team_mturk_experiments_files/figure-gfm/unnamed-chunk-4-2.png)<!-- -->

    ## NULL

``` r
summary(worker_mean_score[, .(score)])
```

    ##      score        
    ##  Min.   :  5.003  
    ##  1st Qu.: 25.938  
    ##  Median :119.894  
    ##  Mean   :135.288  
    ##  3rd Qu.:178.160  
    ##  Max.   :994.601  
    ##  NA's   :1

``` r
worker_mean_score[, .(mean_score=mean(score, na.rm=T), std_dev=sd(score, na.rm=T)), keyby=.(in_treatment)]
```

    ##    in_treatment mean_score  std_dev
    ## 1:            0   146.7838 125.4300
    ## 2:            1   118.8101 190.9985

``` r
#e1_mod_1 <- worker_mean_score[, lm(score ~ in_treatment)]
#summary(e1_mod_1)
```

``` r
#TODO Gauge if effort decreases with more HITTs
```

# Experiment 2, our second pilot

With the first pilot behind us, we decided we needed to focus on
increasing our statistical power and hypothesized that having more
subjects with fewer experiments would provide more statistical power.

``` r
d[experiment_no==2, plot(bounding_box_score, col=(in_treatment+1))]
```

![](team_mturk_experiments_files/figure-gfm/unnamed-chunk-7-1.png)<!-- -->

    ## NULL

``` r
d[experiment_no==2, plot(log(bounding_box_score), col=(in_treatment+1))]
```

![](team_mturk_experiments_files/figure-gfm/unnamed-chunk-7-2.png)<!-- -->

    ## NULL

``` r
summary(d[experiment_no==2, .(bounding_box_score)])
```

    ##  bounding_box_score
    ##  Min.   :  1.423   
    ##  1st Qu.:  5.054   
    ##  Median :  8.320   
    ##  Mean   : 16.178   
    ##  3rd Qu.: 13.498   
    ##  Max.   :489.540   
    ##  NA's   :3

``` r
d[experiment_no==2, .(mean_score=mean(bounding_box_score, na.rm=T), std_dev=sd(bounding_box_score, na.rm=T)), keyby=.(in_treatment)]
```

    ##    in_treatment mean_score  std_dev
    ## 1:            0   15.25847 36.79851
    ## 2:            1   17.09362 42.27343

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

Even with a p-value of 0.655, this was progress. Our coeffecient for in
treatment was still more likely due to random noise than not.

# Experiment 3

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
    ## -22.406 -14.676  -8.505   0.150 195.088 
    ## 
    ## Coefficients:
    ##                                  Estimate Std. Error t value Pr(>|t|)
    ## (Intercept)                         7.435     15.479   0.480    0.632
    ## in_treatment                        4.201      6.334   0.663    0.509
    ## as.factor(mousetrackpad)mouse      13.162     15.522   0.848    0.399
    ## as.factor(mousetrackpad)trackpad   -3.176     18.999  -0.167    0.868
    ## 
    ## Residual standard error: 30.3 on 88 degrees of freedom
    ##   (3 observations deleted due to missingness)
    ## Multiple R-squared:  0.03076,    Adjusted R-squared:  -0.002285 
    ## F-statistic: 0.9308 on 3 and 88 DF,  p-value: 0.4294

# Experiment 4, More data

``` r
#e4_mod_1 <- d[experiment_no %in% c(3,4), lm(bounding_box_score ~ in_treatment+as.factor(mousetrackpad)+as.factor(income)+as.factor(age)+as.factor(edu))]
e4_mod_1 <- d[experiment_no %in% c(3,4), lm(bounding_box_score ~ in_treatment+as.factor(mousetrackpad))]
summary(e4_mod_1)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment + as.factor(mousetrackpad))
    ## 
    ## Residuals:
    ##    Min     1Q Median     3Q    Max 
    ## -61.46 -21.98  -9.48  -2.07 978.22 
    ## 
    ## Coefficients:
    ##                                  Estimate Std. Error t value Pr(>|t|)
    ## (Intercept)                         47.57      29.96   1.588    0.113
    ## in_treatment                       -15.91      10.06  -1.582    0.115
    ## as.factor(mousetrackpad)mouse      -18.29      30.02  -0.609    0.543
    ## as.factor(mousetrackpad)other      -27.15      88.75  -0.306    0.760
    ## as.factor(mousetrackpad)trackpad    16.64      33.78   0.493    0.623
    ## 
    ## Residual standard error: 83.54 on 272 degrees of freedom
    ##   (5 observations deleted due to missingness)
    ## Multiple R-squared:  0.02468,    Adjusted R-squared:  0.01034 
    ## F-statistic: 1.721 on 4 and 272 DF,  p-value: 0.1456

``` r
e4_mod_1 <- d[experiment_no %in% c(3,4), lm(bounding_box_score ~ in_treatment+as.factor(monitor))]
summary(e4_mod_1)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment + as.factor(monitor))
    ## 
    ## Residuals:
    ##    Min     1Q Median     3Q    Max 
    ## -82.00 -17.03  -9.66  -1.48 923.25 
    ## 
    ## Coefficients:
    ##                               Estimate Std. Error t value Pr(>|t|)   
    ## (Intercept)                    261.160     81.864   3.190  0.00159 **
    ## in_treatment                   -11.593      9.947  -1.166  0.24484   
    ## as.factor(monitor)cellphone   -206.268     87.804  -2.349  0.01954 * 
    ## as.factor(monitor)largescreen -243.141     82.687  -2.941  0.00356 **
    ## as.factor(monitor)midsize     -232.912     82.376  -2.827  0.00505 **
    ## as.factor(monitor)notsure     -246.041     91.662  -2.684  0.00772 **
    ## as.factor(monitor)smalllaptop -234.780     82.614  -2.842  0.00483 **
    ## as.factor(monitor)tablet      -176.908     83.939  -2.108  0.03599 * 
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 81.86 on 269 degrees of freedom
    ##   (5 observations deleted due to missingness)
    ## Multiple R-squared:  0.07372,    Adjusted R-squared:  0.04962 
    ## F-statistic: 3.059 on 7 and 269 DF,  p-value: 0.004093

``` r
e4_mod_1 <- d[experiment_no %in% c(3,4), lm(bounding_box_score ~ in_treatment+as.factor(didbf))]
summary(e4_mod_1)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment + as.factor(didbf))
    ## 
    ## Residuals:
    ##    Min     1Q Median     3Q    Max 
    ## -58.39 -23.06 -12.21  -3.12 971.09 
    ## 
    ## Coefficients:
    ##                          Estimate Std. Error t value Pr(>|t|)  
    ## (Intercept)                 66.35      30.06   2.207   0.0281 *
    ## in_treatment               -17.37      10.21  -1.702   0.0898 .
    ## as.factor(didbf)dontknow   -51.18      36.08  -1.419   0.1571  
    ## as.factor(didbf)no         -40.41      31.60  -1.279   0.2021  
    ## as.factor(didbf)yes        -29.94      30.23  -0.990   0.3229  
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 83.79 on 272 degrees of freedom
    ##   (5 observations deleted due to missingness)
    ## Multiple R-squared:  0.01882,    Adjusted R-squared:  0.00439 
    ## F-statistic: 1.304 on 4 and 272 DF,  p-value: 0.2687

``` r
d[experiment_no %in% c(3,4), as.factor(didbf)]
```

    ##   [1] no       yes      yes      yes      no       yes      dontknow
    ##   [8] dontknow yes      yes      yes      yes      yes      yes     
    ##  [15] yes               yes      yes      no       yes      yes     
    ##  [22] yes      yes      yes               no       no       yes     
    ##  [29] yes      yes      yes      no       no       yes      yes     
    ##  [36] yes      dontknow dontknow yes      yes      yes      yes     
    ##  [43] yes      no       yes      yes      yes      yes      yes     
    ##  [50] yes      yes      dontknow yes      no       yes      no      
    ##  [57] no       no       no       yes      yes      yes      yes     
    ##  [64] yes      yes      yes      yes      yes      yes      dontknow
    ##  [71] yes      yes      no       dontknow yes      yes      yes     
    ##  [78] yes      no                yes      yes      yes      yes     
    ##  [85] no       yes      yes      yes      yes      yes      no      
    ##  [92] yes      yes      yes      no       yes      yes      dontknow
    ##  [99]          yes      yes      yes      yes      yes      no      
    ## [106] yes      yes      yes      yes      yes      yes      yes     
    ## [113] yes      yes      yes      yes      no       no       yes     
    ## [120]          yes      no       yes      yes      yes      yes     
    ## [127] dontknow          yes      yes      yes      yes      yes     
    ## [134] no       yes      yes      yes      yes      yes      yes     
    ## [141] no       yes      yes      yes      yes      yes      yes     
    ## [148] yes      yes      yes      dontknow yes      yes      yes     
    ## [155] no       yes      no       yes      no       dontknow yes     
    ## [162] yes      yes      yes      no       no       yes      yes     
    ## [169] yes      dontknow no       yes      no       yes      yes     
    ## [176] yes      no       yes      yes      yes      no       no      
    ## [183] no       no       yes      yes      no       yes      yes     
    ## [190] yes      yes      yes      yes      yes      dontknow yes     
    ## [197] dontknow yes      yes      dontknow no       yes      yes     
    ## [204] yes      yes      no       no       yes      no       no      
    ## [211] no       yes      yes      yes      yes      yes      yes     
    ## [218] yes      yes      no       dontknow yes      yes      yes     
    ## [225] yes      yes      yes               yes      no               
    ## [232] dontknow yes      yes      no       yes      yes      no      
    ## [239] no       yes      yes      yes      yes      no       yes     
    ## [246] yes      yes      yes      yes      yes      yes      no      
    ## [253] yes      no       yes      no       no       yes      yes     
    ## [260] yes      yes      yes      yes      no       yes      yes     
    ## [267] yes      yes      no       yes      yes      no       no      
    ## [274] no       yes      yes      yes      yes      yes      yes     
    ## [281] no       yes     
    ## Levels:  dontknow no yes

``` r
e4_mod_1 <- d[experiment_no %in% c(3,4), lm(bounding_box_score ~ in_treatment+as.factor(age))]
summary(e4_mod_1)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment + as.factor(age))
    ## 
    ## Residuals:
    ##    Min     1Q Median     3Q    Max 
    ## -35.08 -21.24 -11.82  -4.47 975.93 
    ## 
    ## Coefficients:
    ##                      Estimate Std. Error t value Pr(>|t|)   
    ## (Intercept)            261.16      83.21   3.139  0.00188 **
    ## in_treatment           -15.36      10.08  -1.524  0.12874   
    ## as.factor(age)21to30  -229.58      83.57  -2.747  0.00642 **
    ## as.factor(age)31to40  -223.33      84.13  -2.655  0.00841 **
    ## as.factor(age)4150    -228.50      85.67  -2.667  0.00811 **
    ## as.factor(age)lt21    -248.02      88.29  -2.809  0.00533 **
    ## as.factor(age)over50  -249.11      89.94  -2.770  0.00600 **
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 83.21 on 270 degrees of freedom
    ##   (5 observations deleted due to missingness)
    ## Multiple R-squared:  0.03956,    Adjusted R-squared:  0.01822 
    ## F-statistic: 1.854 on 6 and 270 DF,  p-value: 0.08903

``` r
e4_mod_1 <- d[experiment_no %in% c(3,4), lm(bounding_box_score ~ in_treatment+factor(edu, exclude=NA))]
summary(e4_mod_1)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment + factor(edu, 
    ##     exclude = NA))
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -117.01  -21.38  -12.72   -3.41  972.81 
    ## 
    ## Coefficients:
    ##                                          Estimate Std. Error t value
    ## (Intercept)                                144.15      59.50   2.423
    ## in_treatment                               -15.00      10.22  -1.467
    ## factor(edu, exclude = NA)fouryearcollege  -109.46      59.68  -1.834
    ## factor(edu, exclude = NA)highschool       -119.04      62.71  -1.898
    ## factor(edu, exclude = NA)lthighschool     -129.98      83.84  -1.550
    ## factor(edu, exclude = NA)masterorabove    -109.25      60.70  -1.800
    ## factor(edu, exclude = NA)somecollege      -119.03      60.22  -1.977
    ##                                          Pr(>|t|)  
    ## (Intercept)                                0.0161 *
    ## in_treatment                               0.1435  
    ## factor(edu, exclude = NA)fouryearcollege   0.0677 .
    ## factor(edu, exclude = NA)highschool        0.0587 .
    ## factor(edu, exclude = NA)lthighschool      0.1222  
    ## factor(edu, exclude = NA)masterorabove     0.0730 .
    ## factor(edu, exclude = NA)somecollege       0.0491 *
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 83.84 on 270 degrees of freedom
    ##   (5 observations deleted due to missingness)
    ## Multiple R-squared:  0.02485,    Adjusted R-squared:  0.003179 
    ## F-statistic: 1.147 on 6 and 270 DF,  p-value: 0.3355

``` r
e4_mod_1 <- d[experiment_no %in% c(3,4), lm(bounding_box_score ~ in_treatment+as.factor(income))]
summary(e4_mod_1)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment + as.factor(income))
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -112.36  -20.42  -11.46    2.10  952.65 
    ## 
    ## Coefficients:
    ##                             Estimate Std. Error t value Pr(>|t|)  
    ## (Intercept)                  148.796     58.683   2.536   0.0118 *
    ## in_treatment                 -17.276      9.995  -1.728   0.0851 .
    ## as.factor(income)10ktolt30k -127.381     59.139  -2.154   0.0321 *
    ## as.factor(income)gt30klt60k  -93.946     59.215  -1.587   0.1138  
    ## as.factor(income)gt60klt90k -125.628     59.989  -2.094   0.0372 *
    ## as.factor(income)gt90k      -112.901     61.213  -1.844   0.0662 .
    ## as.factor(income)lt10k      -123.900     59.606  -2.079   0.0386 *
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 82.69 on 270 degrees of freedom
    ##   (5 observations deleted due to missingness)
    ## Multiple R-squared:  0.05146,    Adjusted R-squared:  0.03038 
    ## F-statistic: 2.441 on 6 and 270 DF,  p-value: 0.02578

# Experiment 5, threats don’t work

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
