---
title: PostScanJobStatusEvent.JobStatus.FilterStatuses.FilterStatus.FilterState
description: PostScanJobStatusEvent.JobStatus.FilterStatuses.FilterStatus.FilterState
ms.assetid: 56d290bc-91fd-460f-a27a-a5286a8597a3
keywords: ["PostScanJobStatusEvent.JobStatus.FilterStatuses.FilterStatus.FilterState"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PostScanJobStatusEvent.JobStatus.FilterStatuses.FilterStatus.FilterState


The **FilterState** element contains a token that indicates the state of a filter in a post-scan job.

The **FilterState** element supports the following values:

<span id="Pending"></span><span id="pending"></span><span id="PENDING"></span>**Pending**  
The filter is waiting to process image data from the post-scan job.

<span id="Processing"></span><span id="processing"></span><span id="PROCESSING"></span>**Processing**  
The filter is processing image data from the post-scan job.

<span id="Canceled"></span><span id="canceled"></span><span id="CANCELED"></span>**Canceled**  
Image processing by this filter has been canceled.

<span id="CompletedSuccessfully"></span><span id="completedsuccessfully"></span><span id="COMPLETEDSUCCESSFULLY"></span>**CompletedSuccessfully**  
Image processing by this filter completed successfully.

<span id="CompletedWithErrors"></span><span id="completedwitherrors"></span><span id="COMPLETEDWITHERRORS"></span>**CompletedWithErrors**  
Image processing by this filter completed with errors.

<span id="CompletedWithWarnings"></span><span id="completedwithwarnings"></span><span id="COMPLETEDWITHWARNINGS"></span>**CompletedWithWarnings**  
Image processing by this filter completed with warnings.

This element has no sub-elements.

 

 





