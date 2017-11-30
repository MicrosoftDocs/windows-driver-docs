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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20SendImageResponse%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




