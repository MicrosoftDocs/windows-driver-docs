---
title: EndPostScanJobRequest
description: EndPostScanJobRequest
ms.assetid: e110e921-a5d0-4c6e-9d7e-0b5157b44716
keywords: ["EndPostScanJobRequest"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# EndPostScanJobRequest


The **EndPostScanJobRequest** element requests the end of a post-scan job.

A DSM device sends a message that contains an **EndPostScanJobRequest** element to a DSM scan server to indicate that the device has sent the last acquired image in the scanning job. In other words, the device has sent the final [SendImageRequest](sendimagerequest.md) message to the scan server, and the scan server has responded with a final [SendImageResponse](sendimageresponse.md) message. In response to the **EndPostScanJobRequest** message from the device, the scan server sends an [EndPostScanJobResponse](endpostscanjobresponse.md) message to acknowledge the request. Later, when the scan server finishes processing the last image, it sends the device a [PostScanJobEndStateEvent](postscanjobendstateevent.md) message.

The **EndPostScanJobRequest** element supports the following sub-element:

[EndPostScanJobRequest.JobToken](emailconfig.md)

For an example of using the **EndPostScanJobRequest** element, see [EndPostScanJobRequest Example](endpostscanjobrequest-example.md)

 

 





