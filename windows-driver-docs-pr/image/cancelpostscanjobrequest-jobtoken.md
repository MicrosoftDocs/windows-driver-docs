---
title: CancelPostScanJobRequest.JobToken
description: CancelPostScanJobRequest.JobToken
MS-HAID:
- 'dsm\_ref\_dsp\_34ad6d02-ee38-4a3c-a2fe-a525d5cd4cb2.xml'
- 'image.cancelpostscanjobrequest\_jobtoken'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d232fc80-20dc-4d47-9b3e-e15a0cf24273
keywords: ["CancelPostScanJobRequest.JobToken"]
---

# CancelPostScanJobRequest.JobToken


The **JobToken** element contains a GUID value that uniquely identifies a post-scan job.

A DSM device sends a DSMscan server a **CreatePostScanJobRequest** message to request the creation of a post-scan job. If the request succeeds, the scan server generates a new job token and sends the device a **CreatePostScanJobResponse** message that contains the job token. The device and server use the job token to identify the job in subsequent communications.

This element has no child elements.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20CancelPostScanJobRequest.JobToken%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




