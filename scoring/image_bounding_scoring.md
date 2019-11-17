Team mTurk - Image Bounding Scoring
================

``` r
# Read the results from Mechanical Turk
mturk_results_dt <- fread("../data/sample_mturk_output.csv")
head(mturk_results_dt)
```

    ##                             HITId                      HITTypeId
    ## 1: 35A1YQPVFDFL56X0HY0WBSSW08D5IO 3FRA5KKDL2PKKZUTPDY1K7J8LL529P
    ## 2: 3GVPRXWRPGT0SABJ5RFT9C6SRE87I5 3FRA5KKDL2PKKZUTPDY1K7J8LL529P
    ## 3: 388FBO7JZQSBLVIBPGILRXM6HCAYNC 3FRA5KKDL2PKKZUTPDY1K7J8LL529P
    ##                                               Title
    ## 1: Draw bounding boxes around the requested item(s)
    ## 2: Draw bounding boxes around the requested item(s)
    ## 3: Draw bounding boxes around the requested item(s)
    ##                                         Description     Keywords Reward
    ## 1: Draw bounding boxes around the requested item(s) bounding box  $0.03
    ## 2: Draw bounding boxes around the requested item(s) bounding box  $0.03
    ## 3: Draw bounding boxes around the requested item(s) bounding box  $0.03
    ##                    CreationTime MaxAssignments
    ## 1: Sat Oct 26 10:21:19 PDT 2019              3
    ## 2: Sat Oct 26 10:21:19 PDT 2019              3
    ## 3: Sat Oct 26 10:21:19 PDT 2019              3
    ##                                RequesterAnnotation
    ## 1: BatchId:255778;OriginalHitTemplateId:921587256;
    ## 2: BatchId:255778;OriginalHitTemplateId:921587256;
    ## 3: BatchId:255778;OriginalHitTemplateId:921587256;
    ##    AssignmentDurationInSeconds AutoApprovalDelayInSeconds
    ## 1:                        3600                     259200
    ## 2:                        3600                     259200
    ## 3:                        3600                     259200
    ##                      Expiration NumberOfSimilarHITs LifetimeInSeconds
    ## 1: Sat Nov 02 10:21:19 PDT 2019                  NA                NA
    ## 2: Sat Nov 02 10:21:19 PDT 2019                  NA                NA
    ## 3: Sat Nov 02 10:21:19 PDT 2019                  NA                NA
    ##                      AssignmentId       WorkerId AssignmentStatus
    ## 1: 3C8HJ7UOP7T8UN5AZ3A5G91ONC0ZMX A3MMXRCOC1C30K        Submitted
    ## 2: 37W3JXSD6674U9PJ7JE9B0UDFKAWYU A3MMXRCOC1C30K        Submitted
    ## 3: 3OF2M9AATGND4Z57ERXP1W9KY75ZKS A3MMXRCOC1C30K        Submitted
    ##                      AcceptTime                   SubmitTime
    ## 1: Sat Oct 26 10:28:52 PDT 2019 Sat Oct 26 10:29:19 PDT 2019
    ## 2: Sat Oct 26 10:28:26 PDT 2019 Sat Oct 26 10:28:47 PDT 2019
    ## 3: Sat Oct 26 10:27:24 PDT 2019 Sat Oct 26 10:27:55 PDT 2019
    ##                AutoApprovalTime ApprovalTime RejectionTime
    ## 1: Tue Oct 29 10:29:19 PDT 2019           NA            NA
    ## 2: Tue Oct 29 10:28:47 PDT 2019           NA            NA
    ## 3: Tue Oct 29 10:27:55 PDT 2019           NA            NA
    ##    RequesterFeedback WorkTimeInSeconds LifetimeApprovalRate
    ## 1:                NA                27             0% (0/0)
    ## 2:                NA                21             0% (0/0)
    ## 3:                NA                31             0% (0/0)
    ##    Last30DaysApprovalRate Last7DaysApprovalRate
    ## 1:               0% (0/0)              0% (0/0)
    ## 2:               0% (0/0)              0% (0/0)
    ## 3:               0% (0/0)              0% (0/0)
    ##                                                                                                                                                          Input.image_url
    ## 1:                                                                                            https://www.publicdomainpictures.net/pictures/50000/velka/cars-on-road.jpg
    ## 2: https://zdnet4.cbsistatic.com/hub/i/r/2015/11/09/99b78749-8986-4597-bd7b-f57f7ffd5084/resize/770xauto/febbf6abb58f6d12f20808fa64f1883b/volvo-driverless-cars-road.jpg
    ## 3:                        https://previews.123rf.com/images/sparky2000/sparky20000603/sparky2000060300357/341699-a-beautiful-country-road-with-a-sprinkling-of-cars-.jpg
    ##                                                                                                                                                                                                                                                                                                                                                       Answer.annotatedResult.boundingBoxes
    ## 1: [{""height"":295,""label"":""Car"",""left"":1094,""top"":1017,""width"":326},{""height"":243,""label"":""Car"",""left"":641,""top"":1064,""width"":363},{""height"":132,""label"":""Car"",""left"":604,""top"":1001,""width"":200},{""height"":164,""label"":""Car"",""left"":430,""top"":990,""width"":190},{""height"":195,""label"":""Car"",""left"":204,""top"":990,""width"":231}]
    ## 2:                                                                                    [{""height"":52,""label"":""Car"",""left"":138,""top"":221,""width"":67},{""height"":73,""label"":""Car"",""left"":164,""top"":249,""width"":83},{""height"":99,""label"":""Car"",""left"":227,""top"":284,""width"":121},{""height"":153,""label"":""Car"",""left"":381,""top"":330,""width"":204}]
    ## 3:                                                                                     [{""height"":223,""label"":""Car"",""left"":189,""top"":395,""width"":295},{""height"":60,""label"":""Car"",""left"":546,""top"":421,""width"":76},{""height"":50,""label"":""Car"",""left"":619,""top"":421,""width"":57},{""height"":24,""label"":""Car"",""left"":805,""top"":319,""width"":24}]
    ##    Answer.annotatedResult.inputImageProperties.height
    ## 1:                                               1920
    ## 2:                                                513
    ## 3:                                                866
    ##    Answer.annotatedResult.inputImageProperties.width Approve Reject
    ## 1:                                              1606      NA     NA
    ## 2:                                               770      NA     NA
    ## 3:                                              1300      NA     NA

``` r
# Read in the correct bounding cooridinates
image_coords_dt <- fread("../data/image_coords.csv")
head(image_coords_dt)
```

    ##                                                                                                                                                                  ImageId
    ## 1:                                                                                            https://www.publicdomainpictures.net/pictures/50000/velka/cars-on-road.jpg
    ## 2: https://zdnet4.cbsistatic.com/hub/i/r/2015/11/09/99b78749-8986-4597-bd7b-f57f7ffd5084/resize/770xauto/febbf6abb58f6d12f20808fa64f1883b/volvo-driverless-cars-road.jpg
    ## 3:                        https://previews.123rf.com/images/sparky2000/sparky20000603/sparky2000060300357/341699-a-beautiful-country-road-with-a-sprinkling-of-cars-.jpg
    ##     top bottom right left
    ## 1: 1018   1322  1424 1084
    ## 2:  223    275   207  136
    ## 3:  393    618   484  189

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
image_boundings_dt <- extract_image_bounding_data(mturk_results_dt)

score_mturk_results <- function() {
  scoring_results = c()
  # Iterate through the correct bounding boxes and score the results
  for (i in 1:nrow(image_coords_dt)) {
    row <- image_coords_dt[i, ]
    tmp_scoring_results = c()
  
    matched_images_dt <- image_boundings_dt[ImageId == row[, ImageId], ]
  
    if (nrow(matched_images_dt) > 1) {
      #cat("Too many matched images for: (", nrow(matched_images_dt), ")", print(row[, ImageId]))
    }

    # In case there are multiple bounding boxes, we'll grab the best score
    for (i in 1:nrow(matched_images_dt)) {
      bounding_box_score <- score_bounding_box(row[, ], matched_images_dt[, ])
      tmp_scoring_results <- c(tmp_scoring_results, bounding_box_score)
    }
    scoring_results <- c(scoring_results, min(tmp_scoring_results))
  }
  scoring_results
}

mturk_results_dt[, bounding_box_score := score_mturk_results()]

print(mturk_results_dt[, c("HITId", "bounding_box_score")])
```

    ##                             HITId bounding_box_score
    ## 1: 35A1YQPVFDFL56X0HY0WBSSW08D5IO          18.265241
    ## 2: 3GVPRXWRPGT0SABJ5RFT9C6SRE87I5           5.656854
    ## 3: 388FBO7JZQSBLVIBPGILRXM6HCAYNC           2.000000
