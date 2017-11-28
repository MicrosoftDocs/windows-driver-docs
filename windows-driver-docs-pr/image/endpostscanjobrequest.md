---
title: EndPostScanJobRequest
description: EndPostScanJobRequest
ms.assetid: e110e921-a5d0-4c6e-9d7e-0b5157b44716
keywords: ["EndPostScanJobRequest"]
---

# EndPostScanJobRequest


The **EndPostScanJobRequest** element requests the end of a post-scan job.

A DSM device sends a message that contains an **EndPostScanJobRequest** element to a DSM scan server to indicate that the device has sent the last acquired image in the scanning job. In other words, the device has sent the final [SendImageRequest](sendimagerequest.md) message to the scan server, and the scan server has responded with a final [SendImageResponse](sendimageresponse.md) message. In response to the **EndPostScanJobRequest** message from the device, the scan server sends an [EndPostScanJobResponse](endpostscanjobresponse.md) message to acknowledge the request. Later, when the scan server finishes processing the last image, it sends the device a [PostScanJobEndStateEvent](postscanjobendstateevent.md) message.

The **EndPostScanJobRequest** element supports the following sub-element:

[EndPostScanJobRequest.JobToken](emailconfig.md)

For an example of using the **EndPostScanJobRequest** element, see [EndPostScanJobRequest Example](endpostscanjobrequest-example.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20EndPostScanJobRequest%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




