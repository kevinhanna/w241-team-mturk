Team mTurk - Image Bounding Scoring
================

``` r
# Read in the correct bounding cooridinates
pilot_d <- fread("../data/pilot_1/pilot1_results.csv")

# Remove bad image where bounding box not available
pilot_d <- pilot_d[ImageId != "https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/104b3a47edc67285.jpg",]
pilot_d <- pilot_d[ImageId != "https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/1002f337f91b7932.jpg",]


head(pilot_d)
```

    ##    top bottom right left                          HITId
    ## 1: 390    471  1024  856 3EHIMLB7GAHOJS35JM352HFW07IH8C
    ## 2: 394    459  1019  861 3EHIMLB7GAHOJS35JM352HFW07IH8C
    ## 3: 396    459  1024  859 3EHIMLB7GAHOJS35JM352HFW07IH8C
    ## 4: 395    462  1024  857 3EHIMLB7GAHOJS35JM352HFW07IH8C
    ## 5: 392    460  1020  859 3EHIMLB7GAHOJS35JM352HFW07IH8C
    ## 6: 392    474  1024  859 3EHIMLB7GAHOJS35JM352HFW07IH8C
    ##                         HITTypeId Reward AssignmentDurationInSeconds
    ## 1: 3AKE04YHPRJMSFDAM48Z0H4PATIZHQ  $0.02                        3600
    ## 2: 3AKE04YHPRJMSFDAM48Z0H4PATIZHQ  $0.02                        3600
    ## 3: 3AKE04YHPRJMSFDAM48Z0H4PATIZHQ  $0.02                        3600
    ## 4: 3AKE04YHPRJMSFDAM48Z0H4PATIZHQ  $0.02                        3600
    ## 5: 3AKE04YHPRJMSFDAM48Z0H4PATIZHQ  $0.02                        3600
    ## 6: 3AKE04YHPRJMSFDAM48Z0H4PATIZHQ  $0.02                        3600
    ##          WorkerId AssignmentStatus LifetimeApprovalRate
    ## 1: A2AZEEKX5O8J4N        Submitted             0% (0/0)
    ## 2: A2LAE3OM5OQ0WF        Submitted             0% (0/0)
    ## 3: A1ULHXPHPJRQVZ        Submitted             0% (0/0)
    ## 4: A2ZY1BYHGB34W5        Submitted             0% (0/0)
    ## 5:  AJY5G987IRT25        Submitted             0% (0/0)
    ## 6:  AE2N5QUSIL9JE        Submitted             0% (0/0)
    ##    Last30DaysApprovalRate Last7DaysApprovalRate WorkTimeInSeconds
    ## 1:               0% (0/0)              0% (0/0)                83
    ## 2:               0% (0/0)              0% (0/0)                31
    ## 3:               0% (0/0)              0% (0/0)                17
    ## 4:               0% (0/0)              0% (0/0)               251
    ## 5:               0% (0/0)              0% (0/0)                12
    ## 6:               0% (0/0)              0% (0/0)                13
    ##                                                                              ImageId
    ## 1: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/101fa29afd6608fc.jpg
    ## 2: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/101fa29afd6608fc.jpg
    ## 3: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/101fa29afd6608fc.jpg
    ## 4: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/101fa29afd6608fc.jpg
    ## 5: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/101fa29afd6608fc.jpg
    ## 6: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/101fa29afd6608fc.jpg
    ##    in_treatment bounding_box_score
    ## 1:            0           22.61808
    ## 2:            0           14.08984
    ## 3:            0           18.94323
    ## 4:            0           16.76657
    ## 5:            0           13.13188
    ## 6:            0           25.11612

``` r
pilot_d[, mean(bounding_box_score), keyby=WorkerId]
```

    ##           WorkerId         V1
    ##  1: A10HVCH6Y0N7SJ  78.942722
    ##  2: A10IJ2B94MS2MX  18.746941
    ##  3: A16VLS2Z2GYR29  16.568782
    ##  4: A18WFPSLFV4FKY  51.830631
    ##  5: A1A2NGCC4KVRB8  11.156743
    ##  6: A1FPCIKO68OQ63 108.964523
    ##  7: A1G85JMLZY7B28  60.681248
    ##  8:  A1L89JD0FAS0Q  77.899597
    ##  9: A1LFKPNCX23XN6  20.372598
    ## 10: A1NCO5A4JYHGKQ  14.791871
    ## 11: A1O4AAQX2KCD3N  21.379817
    ## 12: A1QRO7EU8B0J4U 150.688607
    ## 13: A1SM0IKQ4OTSCI 355.638338
    ## 14: A1ULHXPHPJRQVZ 114.305814
    ## 15: A1VMYCTZSIBP5J  25.726024
    ## 16: A1Y0ABOUJUMCWW 113.412765
    ## 17: A1ZJL7Q3MPFYJB 515.133404
    ## 18: A1ZRK6K5JUPJAV  28.601833
    ## 19: A255Z4TRTBZLKV 152.587667
    ## 20: A2848VESF5MRA8  20.409504
    ## 21: A2AI293TGSIILE  50.771482
    ## 22: A2AZEEKX5O8J4N  92.251362
    ## 23: A2CPJ227RHJRRZ 994.601532
    ## 24: A2D71F0L4OOTPK 226.457495
    ## 25: A2FJ8YQ6VHGD2L  66.285391
    ## 26: A2FZ88OU42EFC8  12.466715
    ## 27: A2G5GGLXD2KSZS 123.306066
    ## 28: A2H75L5IY3FR41 105.027310
    ## 29: A2JKM9ZTUWHVPF  80.723541
    ## 30: A2KFVSJQGOHZN8  20.653403
    ## 31: A2LAE3OM5OQ0WF  21.983845
    ## 32: A2LCRHTK0WQEOM  12.690492
    ## 33: A2RCBXJ6Q5I1C1  32.601284
    ## 34: A2U7U0A4G92GTR  11.911371
    ## 35: A2WTDVHVVORNDU  16.987211
    ## 36: A2Y0G20STAP4DC  21.398103
    ## 37: A2ZD05YZ9CKQ0D  17.470517
    ## 38: A2ZY1BYHGB34W5 215.878340
    ## 39: A2ZZW6KME1FUDU  43.377020
    ## 40: A30DUC2L6BI0D5  19.440695
    ## 41: A30N5H4N4C22N8 171.366391
    ## 42: A359WCYOJEO9IG  18.361851
    ## 43: A3720E38DB4LL7  25.653513
    ## 44: A376RKV87IXIVQ  13.244846
    ## 45: A37WQHTSP4WWK3  25.018781
    ## 46: A39Q5Z2B8IZ59C 125.229745
    ## 47: A3AFGG80UCEYNA 289.829048
    ## 48: A3DB4V3R2RXTKU 105.289490
    ## 49: A3G0UTSYPCMFBU  48.693799
    ## 50: A3JVT6LSQTTKVS   8.077917
    ## 51: A3M3CSJVL61LMM  13.907641
    ## 52: A3NBJ2WSWYJPWY 125.579148
    ## 53: A3OYVZSC9CXE5L 120.955843
    ## 54: A3PGUPNMOU5BPW  31.337911
    ## 55: A3RD75HSSMVHKM  93.194204
    ## 56: A3UXXT6KP7MIRG  54.730094
    ## 57:  A4GXHVTRGW5P8   5.003332
    ## 58:  A67D9ONK3AJZ8  43.583235
    ## 59:  ABBMKMTKDC065  89.653466
    ## 60:  AE2N5QUSIL9JE  84.401388
    ## 61:  AEDNG2VYAA8NX  91.444979
    ## 62:  AFDUTS29O99VG 203.978424
    ## 63:  AG4R08059MUPR 551.478957
    ## 64:  AGJTTK50503VZ 125.904105
    ## 65:  AJY5G987IRT25 123.131279
    ## 66:  ALQOIBJA35DZM 255.627057
    ## 67:  AMMUQ5FYIZ1GQ  45.380053
    ## 68:  AMO9QDNF1R150  80.934679
    ## 69:  AOMFEAWQHU3D8  14.778389
    ## 70:  APSKPVAHS522W  38.965961
    ## 71:  AV1GWUIPHJY7Q   7.869887
    ## 72:  AWITQJV4D1QA4 137.823349
    ## 73:  AXZBVDVY0VM3V  69.273556
    ## 74:  AZIAQJWXTSFUX  27.192540
    ##           WorkerId         V1

``` r
pilot_d[, mean(bounding_box_score, na.rm=T), keyby=in_treatment]
```

    ##    in_treatment       V1
    ## 1:            0 91.62462
    ## 2:            1 87.69042

``` r
mod <- pilot_d[, lm(bounding_box_score ~ in_treatment)]
summary(mod)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ in_treatment)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ##  -89.31  -73.78  -62.97  -46.44 1114.51 
    ## 
    ## Coefficients:
    ##              Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)    91.625     12.226   7.494 1.95e-13 ***
    ## in_treatment   -3.934     17.290  -0.228     0.82    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 232.9 on 724 degrees of freedom
    ## Multiple R-squared:  7.15e-05,   Adjusted R-squared:  -0.00131 
    ## F-statistic: 0.05177 on 1 and 724 DF,  p-value: 0.8201

``` r
t.test(pilot_d[in_treatment == 1, bounding_box_score], pilot_d[in_treatment == 0, bounding_box_score])
```

    ## 
    ##  Welch Two Sample t-test
    ## 
    ## data:  pilot_d[in_treatment == 1, bounding_box_score] and pilot_d[in_treatment == 0, bounding_box_score]
    ## t = -0.22754, df = 723.19, p-value = 0.8201
    ## alternative hypothesis: true difference in means is not equal to 0
    ## 95 percent confidence interval:
    ##  -37.87954  30.01114
    ## sample estimates:
    ## mean of x mean of y 
    ##  87.69042  91.62462

``` r
mod <- pilot_d[, lm(bounding_box_score ~ WorkTimeInSeconds)]
summary(mod)
```

    ## 
    ## Call:
    ## lm(formula = bounding_box_score ~ WorkTimeInSeconds)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ##  -90.93  -74.34  -62.45  -45.62 1117.22 
    ## 
    ## Coefficients:
    ##                   Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)       92.68907   10.56333   8.775   <2e-16 ***
    ## WorkTimeInSeconds -0.01982    0.03970  -0.499    0.618    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 232.9 on 724 degrees of freedom
    ## Multiple R-squared:  0.0003442,  Adjusted R-squared:  -0.001037 
    ## F-statistic: 0.2493 on 1 and 724 DF,  p-value: 0.6177

``` r
pilot_d[, mean(WorkTimeInSeconds, na.rm=T), keyby=in_treatment]
```

    ##    in_treatment       V1
    ## 1:            0 157.8375
    ## 2:            1 148.0028

``` r
mod <- pilot_d[, lm(WorkTimeInSeconds ~ in_treatment)]
summary(mod)
```

    ## 
    ## Call:
    ## lm(formula = WorkTimeInSeconds ~ in_treatment)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -153.84 -132.00 -108.42   86.91 1411.00 
    ## 
    ## Coefficients:
    ##              Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)   157.837     11.440  13.798   <2e-16 ***
    ## in_treatment   -9.835     16.178  -0.608    0.543    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 218 on 724 degrees of freedom
    ## Multiple R-squared:  0.0005102,  Adjusted R-squared:  -0.0008703 
    ## F-statistic: 0.3696 on 1 and 724 DF,  p-value: 0.5434

``` r
pilot_d[, mean(WorkTimeInSeconds)]
```

    ## [1] 152.9201

``` r
pilot_d[, .N, keyby=WorkerId]
```

    ##           WorkerId  N
    ##  1: A10HVCH6Y0N7SJ 33
    ##  2: A10IJ2B94MS2MX  2
    ##  3: A16VLS2Z2GYR29  4
    ##  4: A18WFPSLFV4FKY  2
    ##  5: A1A2NGCC4KVRB8  1
    ##  6: A1FPCIKO68OQ63 11
    ##  7: A1G85JMLZY7B28 30
    ##  8:  A1L89JD0FAS0Q 11
    ##  9: A1LFKPNCX23XN6  8
    ## 10: A1NCO5A4JYHGKQ  4
    ## 11: A1O4AAQX2KCD3N  7
    ## 12: A1QRO7EU8B0J4U  2
    ## 13: A1SM0IKQ4OTSCI  3
    ## 14: A1ULHXPHPJRQVZ 10
    ## 15: A1VMYCTZSIBP5J  2
    ## 16: A1Y0ABOUJUMCWW 10
    ## 17: A1ZJL7Q3MPFYJB  2
    ## 18: A1ZRK6K5JUPJAV  1
    ## 19: A255Z4TRTBZLKV 15
    ## 20: A2848VESF5MRA8  3
    ## 21: A2AI293TGSIILE  5
    ## 22: A2AZEEKX5O8J4N 34
    ## 23: A2CPJ227RHJRRZ  1
    ## 24: A2D71F0L4OOTPK  3
    ## 25: A2FJ8YQ6VHGD2L 19
    ## 26: A2FZ88OU42EFC8  6
    ## 27: A2G5GGLXD2KSZS 10
    ## 28: A2H75L5IY3FR41 23
    ## 29: A2JKM9ZTUWHVPF 26
    ## 30: A2KFVSJQGOHZN8  6
    ## 31: A2LAE3OM5OQ0WF  2
    ## 32: A2LCRHTK0WQEOM  3
    ## 33: A2RCBXJ6Q5I1C1  2
    ## 34: A2U7U0A4G92GTR  5
    ## 35: A2WTDVHVVORNDU  3
    ## 36: A2Y0G20STAP4DC  3
    ## 37: A2ZD05YZ9CKQ0D  7
    ## 38: A2ZY1BYHGB34W5 10
    ## 39: A2ZZW6KME1FUDU  3
    ## 40: A30DUC2L6BI0D5  7
    ## 41: A30N5H4N4C22N8 13
    ## 42: A359WCYOJEO9IG  3
    ## 43: A3720E38DB4LL7  6
    ## 44: A376RKV87IXIVQ  4
    ## 45: A37WQHTSP4WWK3  6
    ## 46: A39Q5Z2B8IZ59C  1
    ## 47: A3AFGG80UCEYNA 12
    ## 48: A3DB4V3R2RXTKU 27
    ## 49: A3G0UTSYPCMFBU 31
    ## 50: A3JVT6LSQTTKVS  1
    ## 51: A3M3CSJVL61LMM  1
    ## 52: A3NBJ2WSWYJPWY 18
    ## 53: A3OYVZSC9CXE5L 10
    ## 54: A3PGUPNMOU5BPW  1
    ## 55: A3RD75HSSMVHKM 35
    ## 56: A3UXXT6KP7MIRG 28
    ## 57:  A4GXHVTRGW5P8  1
    ## 58:  A67D9ONK3AJZ8  9
    ## 59:  ABBMKMTKDC065 14
    ## 60:  AE2N5QUSIL9JE 36
    ## 61:  AEDNG2VYAA8NX 18
    ## 62:  AFDUTS29O99VG  6
    ## 63:  AG4R08059MUPR  2
    ## 64:  AGJTTK50503VZ  9
    ## 65:  AJY5G987IRT25  9
    ## 66:  ALQOIBJA35DZM  4
    ## 67:  AMMUQ5FYIZ1GQ 26
    ## 68:  AMO9QDNF1R150 17
    ## 69:  AOMFEAWQHU3D8  9
    ## 70:  APSKPVAHS522W  9
    ## 71:  AV1GWUIPHJY7Q  1
    ## 72:  AWITQJV4D1QA4 11
    ## 73:  AXZBVDVY0VM3V  3
    ## 74:  AZIAQJWXTSFUX  6
    ##           WorkerId  N

``` r
pilot_d[, sum(in_treatment)]
```

    ## [1] 363

``` r
pilot_d[, mean(bounding_box_score), keyby=ImageId]
```

    ##                                                                               ImageId
    ##  1: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/101fa29afd6608fc.jpg
    ##  2: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/10496f2878b93ee9.jpg
    ##  3: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/108eeb6df9f6b036.jpg
    ##  4: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/10a170e703878553.jpg
    ##  5: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/10e57672e496cc18.jpg
    ##  6: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/116257e7260fdb51.jpg
    ##  7: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/117c0a56e9f25a6c.jpg
    ##  8: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/118ae565963194f2.jpg
    ##  9: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/11a5ec59de4bf422.jpg
    ## 10: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/11b13f14591a1541.jpg
    ## 11: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/11ca5d6eb7a78462.jpg
    ## 12: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/11cbd39c3b7f1cb0.jpg
    ## 13: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/11cc2d6f28ef43e8.jpg
    ## 14: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/11f2911acdd13dfc.jpg
    ## 15: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/120d043fcfb8d619.jpg
    ## 16: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/1242767b37ed4c77.jpg
    ## 17: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/125dab7404579318.jpg
    ## 18: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/1271622877a21c47.jpg
    ##            V1
    ##  1:  23.43752
    ##  2:  57.50680
    ##  3:  21.35954
    ##  4:  59.79267
    ##  5:  34.99101
    ##  6:  22.49589
    ##  7:  49.26748
    ##  8:  21.90156
    ##  9:  24.11292
    ## 10:  22.94632
    ## 11:  62.44282
    ## 12:  29.64071
    ## 13:  30.22750
    ## 14:  50.01161
    ## 15:  46.93291
    ## 16:  40.96663
    ## 17:  26.97933
    ## 18: 994.62794
