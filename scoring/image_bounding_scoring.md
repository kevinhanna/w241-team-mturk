Team mTurk - Image Bounding Scoring
================

``` r
# Read the results from Mechanical Turk
mturk_results_dt <- fread("../data/sample_openimages_output1.csv")
```

    ## Warning in fread("../data/sample_openimages_output1.csv"): Detected 33
    ## column names but the data has 31 columns. Filling rows automatically. Set
    ## fill=TRUE explicitly to avoid this warning.

``` r
head(mturk_results_dt)
```

    ##                             HITId                      HITTypeId
    ## 1: 3VQTAXTYN2KS3D99CPGNXHGZ46ABU5 3FRA5KKDL2PKKZUTPDY1K7J8LL529P
    ## 2: 36AZSFEYZ3ZSGSY9HFQST3IIIDJBVU 3FRA5KKDL2PKKZUTPDY1K7J8LL529P
    ## 3: 3GS542CVJUMSU54XD4UJYZTTHPE95B 3FRA5KKDL2PKKZUTPDY1K7J8LL529P
    ## 4: 367O8HRHKF7S31WW85B0A2S59H84SC 3FRA5KKDL2PKKZUTPDY1K7J8LL529P
    ## 5: 3A9LA2FRWRDUBU6QHM163ZI1T1VXHY 3FRA5KKDL2PKKZUTPDY1K7J8LL529P
    ## 6: 38B7Q9C28F4OD94BIN4OQ57TDKP96R 3FRA5KKDL2PKKZUTPDY1K7J8LL529P
    ##                                               Title
    ## 1: Draw bounding boxes around the requested item(s)
    ## 2: Draw bounding boxes around the requested item(s)
    ## 3: Draw bounding boxes around the requested item(s)
    ## 4: Draw bounding boxes around the requested item(s)
    ## 5: Draw bounding boxes around the requested item(s)
    ## 6: Draw bounding boxes around the requested item(s)
    ##                                         Description     Keywords Reward
    ## 1: Draw bounding boxes around the requested item(s) bounding box  $0.03
    ## 2: Draw bounding boxes around the requested item(s) bounding box  $0.03
    ## 3: Draw bounding boxes around the requested item(s) bounding box  $0.03
    ## 4: Draw bounding boxes around the requested item(s) bounding box  $0.03
    ## 5: Draw bounding boxes around the requested item(s) bounding box  $0.03
    ## 6: Draw bounding boxes around the requested item(s) bounding box  $0.03
    ##                    CreationTime MaxAssignments
    ## 1: Wed Nov 13 13:49:47 PST 2019              3
    ## 2: Wed Nov 13 13:49:47 PST 2019              3
    ## 3: Wed Nov 13 13:49:47 PST 2019              3
    ## 4: Wed Nov 13 13:49:47 PST 2019              3
    ## 5: Wed Nov 13 13:49:47 PST 2019              3
    ## 6: Wed Nov 13 13:49:47 PST 2019              3
    ##                                RequesterAnnotation
    ## 1: BatchId:258419;OriginalHitTemplateId:921587256;
    ## 2: BatchId:258419;OriginalHitTemplateId:921587256;
    ## 3: BatchId:258419;OriginalHitTemplateId:921587256;
    ## 4: BatchId:258419;OriginalHitTemplateId:921587256;
    ## 5: BatchId:258419;OriginalHitTemplateId:921587256;
    ## 6: BatchId:258419;OriginalHitTemplateId:921587256;
    ##    AssignmentDurationInSeconds AutoApprovalDelayInSeconds
    ## 1:                        3600                     259200
    ## 2:                        3600                     259200
    ## 3:                        3600                     259200
    ## 4:                        3600                     259200
    ## 5:                        3600                     259200
    ## 6:                        3600                     259200
    ##                      Expiration NumberOfSimilarHITs LifetimeInSeconds
    ## 1: Wed Nov 20 13:49:47 PST 2019                  NA                NA
    ## 2: Wed Nov 20 13:49:47 PST 2019                  NA                NA
    ## 3: Wed Nov 20 13:49:47 PST 2019                  NA                NA
    ## 4: Wed Nov 20 13:49:47 PST 2019                  NA                NA
    ## 5: Wed Nov 20 13:49:47 PST 2019                  NA                NA
    ## 6: Wed Nov 20 13:49:47 PST 2019                  NA                NA
    ##                      AssignmentId       WorkerId AssignmentStatus
    ## 1: 3ND9UOO81K1KUAIKO4PJHSSH671WL1 A3MMXRCOC1C30K        Submitted
    ## 2: 37Q970SNZE7EXMX7BPXZ0OGI2O0S1C A3MMXRCOC1C30K        Submitted
    ## 3: 3TAYZSBPLL7LM7F3UTXD57QNUUES2T A3MMXRCOC1C30K        Submitted
    ## 4: 3S4AW7T80BH8L8Z0EYJ0M09QME2L44 A3MMXRCOC1C30K        Submitted
    ## 5: 34PGFRQONOAEZKUKLJD61DFP2IWWJZ A3MMXRCOC1C30K        Submitted
    ## 6: 36NEMU28XFC40S05OGQYH5766CRWM3 A3MMXRCOC1C30K        Submitted
    ##                      AcceptTime                   SubmitTime
    ## 1: Wed Nov 13 13:52:02 PST 2019 Wed Nov 13 13:52:07 PST 2019
    ## 2: Wed Nov 13 13:52:10 PST 2019 Wed Nov 13 13:52:22 PST 2019
    ## 3: Wed Nov 13 13:52:33 PST 2019 Wed Nov 13 13:52:41 PST 2019
    ## 4: Wed Nov 13 13:50:39 PST 2019 Wed Nov 13 13:50:58 PST 2019
    ## 5: Wed Nov 13 13:51:15 PST 2019 Wed Nov 13 13:51:29 PST 2019
    ## 6: Wed Nov 13 13:52:22 PST 2019 Wed Nov 13 13:52:32 PST 2019
    ##                AutoApprovalTime ApprovalTime RejectionTime
    ## 1: Sat Nov 16 13:52:07 PST 2019           NA            NA
    ## 2: Sat Nov 16 13:52:22 PST 2019           NA            NA
    ## 3: Sat Nov 16 13:52:41 PST 2019           NA            NA
    ## 4: Sat Nov 16 13:50:58 PST 2019           NA            NA
    ## 5: Sat Nov 16 13:51:29 PST 2019           NA            NA
    ## 6: Sat Nov 16 13:52:32 PST 2019           NA            NA
    ##    RequesterFeedback WorkTimeInSeconds LifetimeApprovalRate
    ## 1:                NA                 5           100% (3/3)
    ## 2:                NA                12           100% (3/3)
    ## 3:                NA                 8           100% (3/3)
    ## 4:                NA                19           100% (3/3)
    ## 5:                NA                14           100% (3/3)
    ## 6:                NA                10           100% (3/3)
    ##    Last30DaysApprovalRate Last7DaysApprovalRate
    ## 1:             100% (3/3)              0% (0/0)
    ## 2:             100% (3/3)              0% (0/0)
    ## 3:             100% (3/3)              0% (0/0)
    ## 4:             100% (3/3)              0% (0/0)
    ## 5:             100% (3/3)              0% (0/0)
    ## 6:             100% (3/3)              0% (0/0)
    ##                                                                      Input.image_url
    ## 1: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/1002f337f91b7932.jpg
    ## 2: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/101fa29afd6608fc.jpg
    ## 3: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/10496f2878b93ee9.jpg
    ## 4: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/108eeb6df9f6b036.jpg
    ## 5: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/10a170e703878553.jpg
    ## 6: https://kstonedev.s3-us-west-2.amazonaws.com/W241/openimages/10e57672e496cc18.jpg
    ##                                           Answer.annotatedResult.boundingBoxes
    ## 1:                                                                          []
    ## 2:  [{""height"":72,""label"":""Car"",""left"":856,""top"":391,""width"":164}]
    ## 3: [{""height"":265,""label"":""Car"",""left"":117,""top"":315,""width"":746}]
    ## 4: [{""height"":178,""label"":""Car"",""left"":535,""top"":388,""width"":448}]
    ## 5: [{""height"":189,""label"":""Car"",""left"":293,""top"":326,""width"":378}]
    ## 6:  [{""height"":62,""label"":""Car"",""left"":319,""top"":409,""width"":118}]
    ##    Answer.annotatedResult.inputImageProperties.height
    ## 1:                                               1024
    ## 2:                                                576
    ## 3:                                                768
    ## 4:                                                740
    ## 5:                                                671
    ## 6:                                                680
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
    ##         top   bottom      left    right
    ## 1: 200.0000 400.0000 300.00000 500.0000
    ## 2: 329.2612 390.1553 723.84125 851.1337
    ## 3: 264.1915 487.9460  95.46937 721.1444
    ## 4:  10.0000  20.0000  10.00000  20.0000
    ## 5:  10.0000  20.0000  10.00000  20.0000
    ## 6:  10.0000  20.0000  10.00000  20.0000

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
```

    ## [1] "No rows"

``` r
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

print(mturk_results_dt[, c("HITId", "bounding_box_score")])
```

    ##                             HITId bounding_box_score
    ## 1: 3VQTAXTYN2KS3D99CPGNXHGZ46ABU5                 NA
    ## 2: 36AZSFEYZ3ZSGSY9HFQST3IIIDJBVU           330.8682
    ## 3: 3GS542CVJUMSU54XD4UJYZTTHPE95B           246.2046
    ## 4: 367O8HRHKF7S31WW85B0A2S59H84SC          1791.9873
    ## 5: 3A9LA2FRWRDUBU6QHM163ZI1T1VXHY          1293.8292
    ## 6: 38B7Q9C28F4OD94BIN4OQ57TDKP96R          1123.8405
    ## 7: 3KI0JD2ZU0HKZQGI3Q64C9GNIU176D          1250.9463
    ## 8: 322ZSN9Z5FJTI19BX5GQK7ORB0M4T1          1879.8637
