---
title: CancelPostScanJobRequest
description: CancelPostScanJobRequest
ms.assetid: 279cf004-a223-40e7-8ade-220fb1805b95
keywords: ["CancelPostScanJobRequest"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CancelPostScanJobRequest


The **CancelPostScanJobRequest** element is a request to cancel a post-scan job.

To cancel a post-scan job, a DSM device sends a message that contains a **CancelPostScanJobRequest** element to the DSM scan server. The scan server responds with a message that contains a **CancelPostScanJobResponse** element.

A **CancelPostScanJobRequest** contains a **JobToken** child element that identifies the post-scan job being canceled. The same user who previously submitted the **CreatePostScanJob** request that created the job must submit the job-cancellation request, and the job identifier specified by the **JobToken** element must be the same as in the earlier request. The scan server performs a *best effort* cancellation and does not delete any files that the filters have already processed in the post-scan job.

The **CancelPostScanJobRequest** element supports the following sub-element:

[CancelPostScanJobRequest.JobToken](cancelpostscanjobrequest-jobtoken.md)

For an example of how the **CancelPostScanJobRequest** element can be used in a SOAP message from a DSM device, see [CancelPostScanJobRequest Example](cancelpostscanjobrequest-example.md).

 

 





