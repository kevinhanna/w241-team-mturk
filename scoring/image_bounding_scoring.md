Team mTurk - Image Bounding Scoring
================

``` r
# Read the results from Mechanical Turk
#mturk_results_dt <- fread("../data/sample_openimages_output1.csv")
mturk_results_dt <- fread("../data/Batch_3843733_batch_results.csv")
```

    ## Warning in fread("../data/Batch_3843733_batch_results.csv"): Detected 33
    ## column names but the data has 31 columns. Filling rows automatically. Set
    ## fill=TRUE explicitly to avoid this warning.

``` r
head(mturk_results_dt)
```

    ##                             HITId                      HITTypeId
    ## 1: 39AYGO6AGI2TPA6ST51KNNG1GMS6NB 3DQQATL6OWW6LD057T0U6XSV9BS4IA
    ## 2: 39AYGO6AGI2TPA6ST51KNNG1GMS6NB 3DQQATL6OWW6LD057T0U6XSV9BS4IA
    ## 3: 39AYGO6AGI2TPA6ST51KNNG1GMS6NB 3DQQATL6OWW6LD057T0U6XSV9BS4IA
    ## 4: 39AYGO6AGI2TPA6ST51KNNG1GMS6NB 3DQQATL6OWW6LD057T0U6XSV9BS4IA
    ## 5: 39AYGO6AGI2TPA6ST51KNNG1GMS6NB 3DQQATL6OWW6LD057T0U6XSV9BS4IA
    ## 6: 32TMVRKDHQGU7GFA4FJM8S6SV0N480 3DQQATL6OWW6LD057T0U6XSV9BS4IA
    ##                                                                    Title
    ## 1: Est 2-to-3 minute job for 35 cents: Draw bounding box around 20 items
    ## 2: Est 2-to-3 minute job for 35 cents: Draw bounding box around 20 items
    ## 3: Est 2-to-3 minute job for 35 cents: Draw bounding box around 20 items
    ## 4: Est 2-to-3 minute job for 35 cents: Draw bounding box around 20 items
    ## 5: Est 2-to-3 minute job for 35 cents: Draw bounding box around 20 items
    ## 6: Est 2-to-3 minute job for 35 cents: Draw bounding box around 20 items
    ##                                         Description     Keywords Reward
    ## 1: Draw bounding boxes around the requested item(s) bounding box  $0.02
    ## 2: Draw bounding boxes around the requested item(s) bounding box  $0.02
    ## 3: Draw bounding boxes around the requested item(s) bounding box  $0.02
    ## 4: Draw bounding boxes around the requested item(s) bounding box  $0.02
    ## 5: Draw bounding boxes around the requested item(s) bounding box  $0.02
    ## 6: Draw bounding boxes around the requested item(s) bounding box  $0.02
    ##                    CreationTime MaxAssignments
    ## 1: Wed Nov 20 21:03:26 PST 2019             25
    ## 2: Wed Nov 20 21:03:26 PST 2019             25
    ## 3: Wed Nov 20 21:03:26 PST 2019             25
    ## 4: Wed Nov 20 21:03:26 PST 2019             25
    ## 5: Wed Nov 20 21:03:26 PST 2019             25
    ## 6: Wed Nov 20 21:03:26 PST 2019             25
    ##                                 RequesterAnnotation
    ## 1: BatchId:3843733;OriginalHitTemplateId:928390838;
    ## 2: BatchId:3843733;OriginalHitTemplateId:928390838;
    ## 3: BatchId:3843733;OriginalHitTemplateId:928390838;
    ## 4: BatchId:3843733;OriginalHitTemplateId:928390838;
    ## 5: BatchId:3843733;OriginalHitTemplateId:928390838;
    ## 6: BatchId:3843733;OriginalHitTemplateId:928390838;
    ##    AssignmentDurationInSeconds AutoApprovalDelayInSeconds
    ## 1:                        3600                     259200
    ## 2:                        3600                     259200
    ## 3:                        3600                     259200
    ## 4:                        3600                     259200
    ## 5:                        3600                     259200
    ## 6:                        3600                     259200
    ##                      Expiration NumberOfSimilarHITs LifetimeInSeconds
    ## 1: Sat Nov 23 21:03:26 PST 2019                  NA                NA
    ## 2: Sat Nov 23 21:03:26 PST 2019                  NA                NA
    ## 3: Sat Nov 23 21:03:26 PST 2019                  NA                NA
    ## 4: Sat Nov 23 21:03:26 PST 2019                  NA                NA
    ## 5: Sat Nov 23 21:03:26 PST 2019                  NA                NA
    ## 6: Sat Nov 23 21:03:26 PST 2019                  NA                NA
    ##                      AssignmentId       WorkerId AssignmentStatus
    ## 1: 38SKSKU7R5FLGEW19VZWWIX6P70ILR A32318S1SI98GV        Submitted
    ## 2: 39LOEL67OWNBB4UZU3J5N79BMOT83I A2JKM9ZTUWHVPF        Submitted
    ## 3: 3AMYWKA6YF4DTF4XKM6ZRWBVBKZO67  A6381MY3CURAX        Submitted
    ## 4: 3EJJQNKU9VNWNHGU8XE7II5QVPYRHR  A9E9L9MWEZOPN        Submitted
    ## 5: 3TE3O85734QS8RDCPCB0VEZO62HR22 A2HUTXBZ4YCVYT        Submitted
    ## 6: 39DD6S19JTTT5YBJSD0EJIACCN0EZW A32318S1SI98GV        Submitted
    ##                      AcceptTime                   SubmitTime
    ## 1: Thu Nov 21 00:23:33 PST 2019 Thu Nov 21 00:24:22 PST 2019
    ## 2: Wed Nov 20 21:11:42 PST 2019 Wed Nov 20 21:11:56 PST 2019
    ## 3: Wed Nov 20 21:16:18 PST 2019 Wed Nov 20 21:34:34 PST 2019
    ## 4: Thu Nov 21 17:11:02 PST 2019 Thu Nov 21 17:11:16 PST 2019
    ## 5: Wed Nov 20 21:19:35 PST 2019 Wed Nov 20 21:39:47 PST 2019
    ## 6: Thu Nov 21 00:02:56 PST 2019 Thu Nov 21 00:04:07 PST 2019
    ##                AutoApprovalTime ApprovalTime RejectionTime
    ## 1: Sun Nov 24 00:24:22 PST 2019           NA            NA
    ## 2: Sat Nov 23 21:11:56 PST 2019           NA            NA
    ## 3: Sat Nov 23 21:34:34 PST 2019           NA            NA
    ## 4: Sun Nov 24 17:11:16 PST 2019           NA            NA
    ## 5: Sat Nov 23 21:39:47 PST 2019           NA            NA
    ## 6: Sun Nov 24 00:04:07 PST 2019           NA            NA
    ##    RequesterFeedback WorkTimeInSeconds LifetimeApprovalRate
    ## 1:                NA                49           100% (1/1)
    ## 2:                NA                14           100% (1/1)
    ## 3:                NA              1096           100% (1/1)
    ## 4:                NA                14           100% (1/1)
    ## 5:                NA              1212           100% (1/1)
    ## 6:                NA                71           100% (1/1)
    ##    Last30DaysApprovalRate Last7DaysApprovalRate
    ## 1:             100% (1/1)            100% (1/1)
    ## 2:             100% (1/1)            100% (1/1)
    ## 3:             100% (1/1)            100% (1/1)
    ## 4:             100% (1/1)            100% (1/1)
    ## 5:             100% (1/1)            100% (1/1)
    ## 6:             100% (1/1)            100% (1/1)
    ##                                                                      Input.image_url
    ## 1: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/1002f337f91b7932.jpg
    ## 2: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/1002f337f91b7932.jpg
    ## 3: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/1002f337f91b7932.jpg
    ## 4: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/1002f337f91b7932.jpg
    ## 5: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/1002f337f91b7932.jpg
    ## 6: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/101fa29afd6608fc.jpg
    ##                                           Answer.annotatedResult.boundingBoxes
    ## 1: [{""height"":204,""label"":""Car"",""left"":366,""top"":458,""width"":161}]
    ## 2: [{""height"":248,""label"":""Car"",""left"":341,""top"":425,""width"":221}]
    ## 3: [{""height"":193,""label"":""Car"",""left"":356,""top"":452,""width"":187}]
    ## 4: [{""height"":206,""label"":""Car"",""left"":362,""top"":443,""width"":163}]
    ## 5: [{""height"":200,""label"":""Car"",""left"":376,""top"":458,""width"":137}]
    ## 6:  [{""height"":73,""label"":""Car"",""left"":850,""top"":393,""width"":174}]
    ##    Answer.annotatedResult.inputImageProperties.height
    ## 1:                                               1024
    ## 2:                                               1024
    ## 3:                                               1024
    ## 4:                                               1024
    ## 5:                                               1024
    ## 6:                                                576
    ##    Answer.annotatedResult.inputImageProperties.width Approve Reject
    ## 1:                                              1024      NA     NA
    ## 2:                                              1024      NA     NA
    ## 3:                                              1024      NA     NA
    ## 4:                                              1024      NA     NA
    ## 5:                                              1024      NA     NA
    ## 6:                                              1024      NA     NA

``` r
# Read in the correct bounding cooridinates
image_coords_dt <- fread("../data/image_coords.csv")
head(image_coords_dt)
```

    ##                                                                              ImageId
    ## 1: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/1002f337f91b7932.jpg
    ## 2: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/101fa29afd6608fc.jpg
    ## 3: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/10496f2878b93ee9.jpg
    ## 4: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/108eeb6df9f6b036.jpg
    ## 5: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/10a170e703878553.jpg
    ## 6: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/10e57672e496cc18.jpg
    ##         top   bottom     left     right
    ## 1: 383.9058 570.9375 319.2192  473.9067
    ## 2: 391.0401 463.3597 858.8800 1009.9200
    ## 3: 313.5997 579.2003 113.2800  855.6800
    ## 4: 381.3960 560.6980 534.7891  981.4600
    ## 5: 338.7013 509.0125 306.5600  667.5200
    ## 6: 398.0020 471.0652 328.3200  424.3200

``` r
convert_mturk_bounding <- function(mturk_bounding_boxes) {
  # Mechanical Turk provides results with double-quoted JSON consisting of:
  #   height
  #   width
  #   top
  #   left
  #   label

  # Converts to top-left and bottom-right coords
  
  # Replace double-quotes (assumes there are no empty values)
  mturk_bounding_boxes <- gsub("\"\"", "\"", mturk_bounding_boxes)
  bounding_boxes_list <- fromJSON(mturk_bounding_boxes)
  
  # If there is no bounding boxes for this HIT, return NULL
  if (length(bounding_boxes_list) < 1) {
    print("No rows")
    return(NULL)
  }
    
  top_results_list <- c()
  bottom_results_list <- c()
  right_results_list <- c()
  left_results_list <- c()
  
  for (bounding_box in bounding_boxes_list) {
    top = as.integer(bounding_box$top)
    left = as.integer(bounding_box$left)
    bottom = as.integer(top + bounding_box$height)
    right = as.integer(left + bounding_box$width)

    top_results_list <- c(top_results_list, top)
    bottom_results_list <- c(bottom_results_list, bottom)
    right_results_list <- c(right_results_list, right)
    left_results_list <- c(left_results_list, left)
  }


  ret_dt <- data.table(
    top = top_results_list,
    bottom = bottom_results_list,
    right = right_results_list,
    left = left_results_list
  )
    
  return(ret_dt)
}

extract_image_bounding_data <- function(dt) {
  # Iterate through data.table, separate bounding boxes in to new rows in case there are multiple bounding boxes in any images. 
  
  results_dt <- data.table()
  
  for (i in 1:nrow(dt)) {
    row <- dt[i, ]

    bounding_boxes_dt <- convert_mturk_bounding(row[, Answer.annotatedResult.boundingBoxes])
    
    if (is.null(bounding_boxes_dt)) {
      bounding_boxes_dt <- data.table(
        top = NA,
        bottom = NA,
        left = NA,
        right = NA
      )
    }
    
    # Add attributes for the HIT to bounding boxes
    bounding_boxes_dt[, HITId := row[, HITId]]
    bounding_boxes_dt[, HITTypeId := row[, HITTypeId]]
    bounding_boxes_dt[, Reward := row[, Reward]]
    bounding_boxes_dt[, AssignmentDurationInSeconds := row[, AssignmentDurationInSeconds]]
    bounding_boxes_dt[, WorkerId := row[, WorkerId]]
    bounding_boxes_dt[, AssignmentStatus := row[, AssignmentStatus]]
    bounding_boxes_dt[, LifetimeApprovalRate := row[, LifetimeApprovalRate]]
    bounding_boxes_dt[, Last30DaysApprovalRate := row[, Last30DaysApprovalRate]]
    bounding_boxes_dt[, Last7DaysApprovalRate := row[, Last7DaysApprovalRate]]
    bounding_boxes_dt[, ImageId := row[, Input.image_url]] # Column renamed
    
    #bounding_boxes_dt[, bounding_box_score := -0.111]
    
    # Concatinate to results
    results_dt <- rbind(results_dt, bounding_boxes_dt)
  }
  
  return(results_dt)
}

score_bounding_box <- function(true_coords, turker_coords) {
  # Calculate the difference in the top-right and bottom-left points
  
  top = as.integer(true_coords[, top]) - turker_coords[, top]
  right = true_coords[, right] - turker_coords[, right]
  first_distance <- sqrt(top^2 + right^2)

  bottom = as.integer(true_coords[, bottom]) - turker_coords[, bottom]
  left = true_coords[, left] - turker_coords[, left]
  second_distance <- sqrt(bottom^2 + left^2)
  
  return(first_distance + second_distance)
  
}
```

``` r
# Prepare the mturk results
formatted_mturk_image_boundings_dt <- extract_image_bounding_data(mturk_results_dt)

score_mturk_results <- function() {
  
  scoring_results = c()
  
  # Iterate through the turker results
  for (i in 1:nrow(formatted_mturk_image_boundings_dt)) {
    
    formatted_mturk_image_boundings_row <- formatted_mturk_image_boundings_dt[i, ]
    tmp_scoring_results = c()
    
    # Find the correct bounding
    matched_images_dt <- image_coords_dt[ImageId == formatted_mturk_image_boundings_row[, ImageId], ]

    if (nrow(matched_images_dt) > 1) {
      #cat("Too many matched images for: (", nrow(matched_images_dt), ")", print(row[, ImageId]))
    }

    bounding_box_score <- score_bounding_box(matched_images_dt[, ], formatted_mturk_image_boundings_row[, ])
    scoring_results <- c(scoring_results, bounding_box_score)
    
    }
    
  scoring_results
}

mturk_results_dt[, bounding_box_score := score_mturk_results()]
```

    ## Warning in `[.data.table`(mturk_results_dt, , `:=`(bounding_box_score,
    ## score_mturk_results())): Supplied 116 items to be assigned to 115 items of
    ## column 'bounding_box_score' (1 unused)

``` r
setorder(mturk_results_dt, WorkerId)

print(mturk_results_dt[, c("HITId", "bounding_box_score", "WorkerId")])
```

    ##                               HITId bounding_box_score       WorkerId
    ##   1: 39AYGO6AGI2TPA6ST51KNNG1GMS6NB          189.30560 A2HUTXBZ4YCVYT
    ##   2: 32TMVRKDHQGU7GFA4FJM8S6SV0N480           20.71133 A2HUTXBZ4YCVYT
    ##   3: 3W3RSPVVHV9O3LT8DAJ8Q1QSED9ULY           17.92858 A2HUTXBZ4YCVYT
    ##   4: 3SMIWMMK74N4EF57HOQAZC78CKDWUT         1020.61403 A2HUTXBZ4YCVYT
    ##   5: 3O0M2G5VD9KULLYK97P08O13F6549P           27.96188 A2HUTXBZ4YCVYT
    ##  ---                                                                 
    ## 111: 3PIOQ99R814ERLWTPNZN3TUHJ89UN0           55.12650  A9E9L9MWEZOPN
    ## 112: 3ZLW647WBODY35UHOK52OW1JV0Z23A           36.85807  A9E9L9MWEZOPN
    ## 113: 3V7ICJJA0DYD9EDH7R3WZUWT3684BZ          994.48915  A9E9L9MWEZOPN
    ## 114: 3O0M2G5VD9KULLYK97P08O13F6549P           11.31961   ALJNN2WJURB3
    ## 115: 3B623HUYK78D91HLUGF46VMY9GPS8U           15.93497   ALJNN2WJURB3

``` r
fwrite(mturk_results_dt, "../data/pilot1_results.csv")
```
