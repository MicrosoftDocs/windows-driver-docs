---
title: SendImageRequest
description: SendImageRequest
MS-HAID:
- 'dsm\_ref\_dsp\_803795c7-7639-465e-9614-19dc114ff21d.xml'
- 'image.sendimagerequest'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: fda4926f-5d37-4515-9a13-ef27a607a8fd
keywords: ["SendImageRequest"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20SendImageRequest%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




