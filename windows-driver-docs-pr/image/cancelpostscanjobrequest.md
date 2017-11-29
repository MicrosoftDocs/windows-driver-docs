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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20CancelPostScanJobRequest%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




