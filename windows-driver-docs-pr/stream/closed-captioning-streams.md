---
title: Closed Captioning Streams
author: windows-driver-content
description: Closed Captioning Streams
MS-HAID:
- 'dvd-design\_23b9cd9a-c92a-4649-9bba-8ffad916d2b3.xml'
- 'stream.closed\_captioning\_streams'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ee6cfac6-c532-4e73-81b2-ee767d2d6a4d
keywords: ["closed captioning streams WDK DVD decoder", "group of pictures WDK DVD decoder", "GOP WDK DVD decoder"]
---

# Closed Captioning Streams


## <a href="" id="ddk-closed-captioning-streams-ksg"></a>


Support for closed captioning is required. The DVD decoder minidriver must provide closed captioning information for the Microsoft line 21 decoder filter. Implementations may not simply decode the closed captioning information inside the MPEG2 decoder and add it to the video stream. The DVD decoder minidriver must present the closed captioning pin as an output pin. After the stream is opened, the DVD decoder minidriver receives SRB\_READ\_DATA requests on the stream. The DVD decoder minidriver queues these requests until closed captioning data is available.

When a group of pictures (GOP) start code is processed in the video stream, the DVD decoder minidriver looks for user data (closed captioning information) and returns that information using one of the stream request blocks (SRBs) present on the closed captioning stream queue. All data discontinuity and format block changes should be propagated from the video pin to the closed captioning pin.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Closed%20Captioning%20Streams%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


