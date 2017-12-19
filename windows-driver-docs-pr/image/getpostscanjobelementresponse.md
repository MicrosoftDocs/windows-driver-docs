---
title: GetPostScanJobElementResponse
description: GetPostScanJobElementResponse
ms.assetid: 564b2ce5-c041-4a71-b966-7eb0ca3365e6
keywords: ["GetPostScanJobElementResponse"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GetPostScanJobElementResponse


The **GetPostScanJobElementsResponse** element is a response to a request from a client to obtain a set of job elements from a post-scan job.

A DSM scan server sends a message that contains a **GetPostScanJobElementsResponse** element in response to a [GetPostScanJobElementRequest](getpostscanjobelementrequest.md) message received from a DSM device. The message from the scan server contains the job elements requested by the device.

The **Name** element is used to request Job elements.

If the requested operation fails, the scan server sends the device an error message instead of a **GetPostScanJobElementsResponse** message. For more information about error messages, see [WS-DSP Operation Error Reporting](https://msdn.microsoft.com/library/windows/hardware/ff540619).

The **GetPostScanJobElementsResponse** element supports the following sub-element:

[GetPostScanJobElementsResponse.JobElements](getpostscanjobelementsresponse-jobelements.md)

For an example of using the **GetPostScanJobElementsResponse** element, see [GetPostScanJobElementsResponse Example](getpostscanjobelementsresponse-example.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20GetPostScanJobElementResponse%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




