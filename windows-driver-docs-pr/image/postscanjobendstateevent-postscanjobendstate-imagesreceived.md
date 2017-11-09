---
title: PostScanJobEndStateEvent.PostScanJobEndState.ImagesReceived
description: PostScanJobEndStateEvent.PostScanJobEndState.ImagesReceived
MS-HAID:
- 'dsm\_ref\_dsp\_a5d2c024-9a40-4229-a7d1-e9ee623dce36.xml'
- 'image.postscanjobendstateevent\_postscanjobendstate\_imagesreceived'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b043f34b-e43a-4dcd-a606-0f45a49f66d0
keywords: ["PostScanJobEndStateEvent.PostScanJobEndState.ImagesReceived"]
---

# PostScanJobEndStateEvent.PostScanJobEndState.ImagesReceived


The **ImagesReceived** element contains an integer count of the image files received by a post-scan job.

The **ImagesReceived** element contains the number of image files that a DSM device has thus far sent to a DSM scan server during the course of a post-scan job.

In response to a message from a DSM device, a DSMscan server sends a message that contains the job elements requested by the device. The device can request a **JobStatus** element that includes an **ImagesReceived** element.

When a post-scan job completes, the DSM scan server sends the WSD Scan device a **PostScanJobEndStateEvent** message that contains information about the completion status of the job. This message contains a **PostScanJobEndState** element that includes an **ImagesReceived** element.

This element has no sub- elements.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20PostScanJobEndStateEvent.PostScanJobEndState.ImagesReceived%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




