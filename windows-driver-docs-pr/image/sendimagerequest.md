---
title: SendImageRequest
description: SendImageRequest
ms.assetid: fda4926f-5d37-4515-9a13-ef27a607a8fd
keywords: ["SendImageRequest"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# SendImageRequest


The **SendImageRequest** element is a request to send an image file to a post-scan job.

A DSM device sends a message that contains a **SendImageRequest** element to a DSM scan server to add an image to the current post-scan job. The image data is attached to the message. In response, the scan server sends a message that contains a [SendImageResponse](sendimageresponse.md) element to the device.

A DSM device starts a post-scan job by sending a message that contains a [CreatePostScanJobRequest](createpostscanjobrequest.md) element to a DSM scan server. For each document that the user scans, the device sends the scan server a message that contains a **SendImageRequest** element and a document image. The scan server processes and stores each image according to the instructions in the scan process. After sending the final image, the device sends the scan server a message that contains an [EndPostScanJobRequest](endpostscanjobrequest.md) element to inform the scan server that all of the images for the post-scan job have been sent.

The **SendImageRequest** element supports the following sub-elements:

[SendImageRequest.JobToken](sendimagerequest-jobtoken.md)

[SendImageRequest.DocumentDescription](sendimagerequest-documentdescription.md)

[SendImageRequest.ImageData](sendimagerequest-imagedata.md)

For an example of using the **SendImageRequest** element, see [SendImageRequest Example](sendimagerequest-example.md).

 

 





