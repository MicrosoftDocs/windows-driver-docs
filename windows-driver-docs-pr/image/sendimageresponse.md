---
title: SendImageResponse
description: SendImageResponse
ms.assetid: b850f63e-d9d3-4aa7-ba74-8d2914588796
keywords: ["SendImageResponse"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SendImageResponse


The **SendImageResponse** element is a response to a request from a client to send an image file to a post-scan job.

A DSM scan server sends a message that contains a **SendImageResponse** element in response to a message from a DSM device that contains a [SendImageRequest](sendimagerequest.md) element and an attached image file. The message from the scan server acknowledges receipt of the device's request and indicates that the post-scan job has received the image file.

If the requested operation fails, the scan server sends the device an error message instead of a **SendImageResponse** message. For more information about error messages, see [WS-DSP Operation Error Reporting](https://msdn.microsoft.com/library/windows/hardware/ff540619).

For an example of the **SendImageResponse** element, see [SendImageResponse Example](sendimageresponse-example.md).

 

 





