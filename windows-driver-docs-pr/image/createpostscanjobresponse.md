---
title: CreatePostScanJobResponse
description: CreatePostScanJobResponse
MS-HAID:
- 'dsm\_ref\_dsp\_bafc0138-e7eb-4b26-9264-3958e508370b.xml'
- 'image.createpostscanjobresponse'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9c3bda26-d306-4fbd-9884-11b404c5e761
keywords: ["CreatePostScanJobResponse"]
---

# CreatePostScanJobResponse


The **CreatePostScanJobResponse** element is a response to a request from a client to start a post-scan job.

A DSM scan server sends a message that contains a **CreatePostScanJobResponse** element in response to a **CreatePostScanJobRequest** message received from a DSM device. The message from the scan server acknowledges receipt of the request from the device to create a post-scan job.

If the requested operation fails, the scan server sends the device an error message instead of a **CreatePostScanJobResponse** message. For more information about error messages, see WS-DSP Operation Error Reporting.

The **CreatePostScanJobResponse** element supports the following sub-element:

[CreatePostScanJobResponse.JobToken](createpostscanjobresponse-jobtoken.md)

For an example of using the **CreatePostScanJobResponse** element, see [CreatePostScanJobResponse Example](createpostscanjobresponse-example.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20CreatePostScanJobResponse%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




