Team mTurk - Image Bounding Scoring
================

``` r
# Read the results from Mechanical Turk
#mturk_results_dt <- fread("../data/sample_openimages_output1.csv")

get_result_data <- function() {
  control <- fread("../data/pilot_1/Batch_3846852_batch_results_reg.csv")
  control[, in_treatment := 0]
  
  treatment <- fread("../data/pilot_1/Batch_3846847_batch_results_gov.csv")
  treatment[, in_treatment := 1]
  
  return(rbind(control, treatment))
}

mturk_results_dt <- get_result_data()
```

    ## Warning in fread("../data/pilot_1/Batch_3846852_batch_results_reg.csv"):
    ## Detected 33 column names but the data has 31 columns. Filling rows
    ## automatically. Set fill=TRUE explicitly to avoid this warning.

    ## Warning in fread("../data/pilot_1/Batch_3846847_batch_results_gov.csv"):
    ## Detected 33 column names but the data has 31 columns. Filling rows
    ## automatically. Set fill=TRUE explicitly to avoid this warning.

``` r
head(mturk_results_dt)
```

    ##                             HITId                      HITTypeId
    ## 1: 37NXA7GVTWOOG0I8I0TDMNSBSMSLVS 3AKE04YHPRJMSFDAM48Z0H4PATIZHQ
    ## 2: 37NXA7GVTWOOG0I8I0TDMNSBSMSLVS 3AKE04YHPRJMSFDAM48Z0H4PATIZHQ
    ## 3: 37NXA7GVTWOOG0I8I0TDMNSBSMSLVS 3AKE04YHPRJMSFDAM48Z0H4PATIZHQ
    ## 4: 37NXA7GVTWOOG0I8I0TDMNSBSMSLVS 3AKE04YHPRJMSFDAM48Z0H4PATIZHQ
    ## 5: 37NXA7GVTWOOG0I8I0TDMNSBSMSLVS 3AKE04YHPRJMSFDAM48Z0H4PATIZHQ
    ## 6: 37NXA7GVTWOOG0I8I0TDMNSBSMSLVS 3AKE04YHPRJMSFDAM48Z0H4PATIZHQ
    ##                                                                    Title
    ## 1: Est 2-to-3 minute job for 40 cents: Draw bounding box around 20 items
    ## 2: Est 2-to-3 minute job for 40 cents: Draw bounding box around 20 items
    ## 3: Est 2-to-3 minute job for 40 cents: Draw bounding box around 20 items
    ## 4: Est 2-to-3 minute job for 40 cents: Draw bounding box around 20 items
    ## 5: Est 2-to-3 minute job for 40 cents: Draw bounding box around 20 items
    ## 6: Est 2-to-3 minute job for 40 cents: Draw bounding box around 20 items
    ##                                         Description     Keywords Reward
    ## 1: Draw bounding boxes around the requested item(s) bounding box  $0.02
    ## 2: Draw bounding boxes around the requested item(s) bounding box  $0.02
    ## 3: Draw bounding boxes around the requested item(s) bounding box  $0.02
    ## 4: Draw bounding boxes around the requested item(s) bounding box  $0.02
    ## 5: Draw bounding boxes around the requested item(s) bounding box  $0.02
    ## 6: Draw bounding boxes around the requested item(s) bounding box  $0.02
    ##                    CreationTime MaxAssignments
    ## 1: Sat Nov 23 09:34:18 PST 2019             20
    ## 2: Sat Nov 23 09:34:18 PST 2019             20
    ## 3: Sat Nov 23 09:34:18 PST 2019             20
    ## 4: Sat Nov 23 09:34:18 PST 2019             20
    ## 5: Sat Nov 23 09:34:18 PST 2019             20
    ## 6: Sat Nov 23 09:34:18 PST 2019             20
    ##                                 RequesterAnnotation
    ## 1: BatchId:3846852;OriginalHitTemplateId:928390838;
    ## 2: BatchId:3846852;OriginalHitTemplateId:928390838;
    ## 3: BatchId:3846852;OriginalHitTemplateId:928390838;
    ## 4: BatchId:3846852;OriginalHitTemplateId:928390838;
    ## 5: BatchId:3846852;OriginalHitTemplateId:928390838;
    ## 6: BatchId:3846852;OriginalHitTemplateId:928390838;
    ##    AssignmentDurationInSeconds AutoApprovalDelayInSeconds
    ## 1:                        3600                      86400
    ## 2:                        3600                      86400
    ## 3:                        3600                      86400
    ## 4:                        3600                      86400
    ## 5:                        3600                      86400
    ## 6:                        3600                      86400
    ##                      Expiration NumberOfSimilarHITs LifetimeInSeconds
    ## 1: Sun Nov 24 09:34:18 PST 2019                  NA                NA
    ## 2: Sun Nov 24 09:34:18 PST 2019                  NA                NA
    ## 3: Sun Nov 24 09:34:18 PST 2019                  NA                NA
    ## 4: Sun Nov 24 09:34:18 PST 2019                  NA                NA
    ## 5: Sun Nov 24 09:34:18 PST 2019                  NA                NA
    ## 6: Sun Nov 24 09:34:18 PST 2019                  NA                NA
    ##                      AssignmentId       WorkerId AssignmentStatus
    ## 1: 33IZTU6J85J5AMGMSQWYBEYG6N0SXM A3RD75HSSMVHKM        Submitted
    ## 2: 34HJIJKLP9EU4C9G2AZYPQLPCWQ4VP  ABBMKMTKDC065        Submitted
    ## 3: 351SEKWQS4ZOELY0HTZ05YWIYG7MD3  AZIAQJWXTSFUX        Submitted
    ## 4: 35H6S234SEIRL5YFF7A0IQB4VZU655 A10HVCH6Y0N7SJ        Submitted
    ## 5: 3AUQQEL7U9BD5ORFJ9CWDNVCVK9V0Z A2FJ8YQ6VHGD2L        Submitted
    ## 6: 3BWI6RSP7KRALO5D9I8VSYHD33D7E6 A1FPCIKO68OQ63        Submitted
    ##                      AcceptTime                   SubmitTime
    ## 1: Sat Nov 23 09:35:35 PST 2019 Sat Nov 23 09:35:45 PST 2019
    ## 2: Sat Nov 23 09:34:39 PST 2019 Sat Nov 23 09:34:58 PST 2019
    ## 3: Sat Nov 23 09:37:24 PST 2019 Sat Nov 23 09:37:36 PST 2019
    ## 4: Sat Nov 23 09:36:24 PST 2019 Sat Nov 23 09:39:41 PST 2019
    ## 5: Sat Nov 23 09:34:19 PST 2019 Sat Nov 23 09:35:58 PST 2019
    ## 6: Sat Nov 23 09:38:13 PST 2019 Sat Nov 23 09:38:24 PST 2019
    ##                AutoApprovalTime ApprovalTime RejectionTime
    ## 1: Sun Nov 24 09:35:45 PST 2019           NA            NA
    ## 2: Sun Nov 24 09:34:58 PST 2019           NA            NA
    ## 3: Sun Nov 24 09:37:36 PST 2019           NA            NA
    ## 4: Sun Nov 24 09:39:41 PST 2019           NA            NA
    ## 5: Sun Nov 24 09:35:58 PST 2019           NA            NA
    ## 6: Sun Nov 24 09:38:24 PST 2019           NA            NA
    ##    RequesterFeedback WorkTimeInSeconds LifetimeApprovalRate
    ## 1:                NA                10             0% (0/0)
    ## 2:                NA                19             0% (0/0)
    ## 3:                NA                12             0% (0/0)
    ## 4:                NA               197             0% (0/0)
    ## 5:                NA                99             0% (0/0)
    ## 6:                NA                11             0% (0/0)
    ##    Last30DaysApprovalRate Last7DaysApprovalRate
    ## 1:               0% (0/0)              0% (0/0)
    ## 2:               0% (0/0)              0% (0/0)
    ## 3:               0% (0/0)              0% (0/0)
    ## 4:               0% (0/0)              0% (0/0)
    ## 5:               0% (0/0)              0% (0/0)
    ## 6:               0% (0/0)              0% (0/0)
    ##                                                                      Input.image_url
    ## 1: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/1002f337f91b7932.jpg
    ## 2: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/1002f337f91b7932.jpg
    ## 3: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/1002f337f91b7932.jpg
    ## 4: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/1002f337f91b7932.jpg
    ## 5: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/1002f337f91b7932.jpg
    ## 6: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/1002f337f91b7932.jpg
    ##                                           Answer.annotatedResult.boundingBoxes
    ## 1: [{""height"":252,""label"":""Car"",""left"":361,""top"":441,""width"":191}]
    ## 2: [{""height"":219,""label"":""Car"",""left"":369,""top"":450,""width"":160}]
    ## 3: [{""height"":218,""label"":""Car"",""left"":366,""top"":439,""width"":165}]
    ## 4: [{""height"":178,""label"":""Car"",""left"":360,""top"":464,""width"":159}]
    ## 5: [{""height"":202,""label"":""Car"",""left"":371,""top"":458,""width"":154}]
    ## 6: [{""height"":202,""label"":""Car"",""left"":368,""top"":459,""width"":169}]
    ##    Answer.annotatedResult.inputImageProperties.height
    ## 1:                                               1024
    ## 2:                                               1024
    ## 3:                                               1024
    ## 4:                                               1024
    ## 5:                                               1024
    ## 6:                                               1024
    ##    Answer.annotatedResult.inputImageProperties.width Approve Reject
    ## 1:                                              1024      NA     NA
    ## 2:                                              1024      NA     NA
    ## 3:                                              1024      NA     NA
    ## 4:                                              1024      NA     NA
    ## 5:                                              1024      NA     NA
    ## 6:                                              1024      NA     NA
    ##    in_treatment
    ## 1:            0
    ## 2:            0
    ## 3:            0
    ## 4:            0
    ## 5:            0
    ## 6:            0

``` r
mturk_results_dt[, sum(in_treatment)]
```

    ## [1] 400

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
    bounding_boxes_dt[, WorkTimeInSeconds := row[, WorkTimeInSeconds]]
  
    bounding_boxes_dt[, ImageId := row[, Input.image_url]] # Column renamed
    bounding_boxes_dt[, in_treatment := row[, in_treatment]]
    
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
```

    ## [1] "No rows"

``` r
score_mturk_results <- function() {
  
  score_results = c()

  # Iterate through the turker results
  for (i in 1:nrow(formatted_mturk_image_boundings_dt)) {
    
    formatted_mturk_image_boundings_row <- formatted_mturk_image_boundings_dt[i, ]
    tmp_scoring_results = c()
    
    # Find the correct bounding
    matched_images_dt <- image_coords_dt[ImageId == formatted_mturk_image_boundings_row[, ImageId], ]

    bounding_box_score <- score_bounding_box(matched_images_dt[, ], formatted_mturk_image_boundings_row[, ])
    score_results <- c(score_results, bounding_box_score)
    
  }
  score_results
}

#mturk_results_dt[, bounding_box_score := score_mturk_results()]

formatted_mturk_image_boundings_dt[, bounding_box_score := score_mturk_results()]

#setorder(formatted_mturk_image_boundings_dt, WorkerId)

print(formatted_mturk_image_boundings_dt[, c("HITId", "bounding_box_score", "WorkerId")])
```

    ##                               HITId bounding_box_score       WorkerId
    ##   1: 37NXA7GVTWOOG0I8I0TDMNSBSMSLVS           227.1781 A3RD75HSSMVHKM
    ##   2: 37NXA7GVTWOOG0I8I0TDMNSBSMSLVS           197.5538  ABBMKMTKDC065
    ##   3: 37NXA7GVTWOOG0I8I0TDMNSBSMSLVS           178.7525  AZIAQJWXTSFUX
    ##   4: 37NXA7GVTWOOG0I8I0TDMNSBSMSLVS           175.4531 A10HVCH6Y0N7SJ
    ##   5: 37NXA7GVTWOOG0I8I0TDMNSBSMSLVS           194.5826 A2FJ8YQ6VHGD2L
    ##  ---                                                                 
    ## 803: 3X4Q1O9UCK4UBVK9DU6P8QG219QO7K           997.8911  AE2N5QUSIL9JE
    ## 804: 3X4Q1O9UCK4UBVK9DU6P8QG219QO7K           998.7318 A3AFGG80UCEYNA
    ## 805: 3X4Q1O9UCK4UBVK9DU6P8QG219QO7K           993.6168 A2ZY1BYHGB34W5
    ## 806: 3X4Q1O9UCK4UBVK9DU6P8QG219QO7K           995.8732 A1FPCIKO68OQ63
    ## 807: 3X4Q1O9UCK4UBVK9DU6P8QG219QO7K           995.7909 A1Y0ABOUJUMCWW

``` r
fwrite(formatted_mturk_image_boundings_dt, "../data/pilot_1/pilot1_results.csv")
```
