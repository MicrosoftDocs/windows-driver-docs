---
title: GetPostScanJobElementRequest
description: GetPostScanJobElementRequest
ms.assetid: 37f6e28f-57c8-4f49-baed-2ba83dfdeda7
keywords: ["GetPostScanJobElementRequest"]
---

# GetPostScanJobElementRequest


The **GetPostScanJobElementsRequest** element requests a set of job elements from a post-scan job.

A DSM device sends a message that contains a **GetPostScanJobElementRequest** element to the DSM scan server to obtain a collection of job elements. In response, the scan server sends the device a message that contains a [GetPostScanJobElementResponse](getpostscanjobelementresponse.md) element. The response from the scan server contains the job elements requested in the message from the device.

The **Name** element is used to request Job elements.

The **GetPostScanJobElementsRequest** supports the following sub-elements:

[GetPostScanJobElementsRequest.JobToken](getpostscanjobelementsrequest-jobtoken.md)

[GetPostScanJobElementsRequest.RequestedElements](getpostscanjobelementsrequest-requestedelements.md)

For an example of using the **GetPostScanJobElementsRequest** element, see [GetPostScanJobElementsRequest Example](getpostscanjobelementsrequest-example.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20GetPostScanJobElementRequest%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




