---
title: KSEVENT\_CONNECTION\_ENDOFSTREAM
description: The KSEVENT\_CONNECTION\_ENDOFSTREAM event allows a client to receive notification of an end of stream event.
ms.assetid: f6fb9408-9926-48e6-b2a4-2ba7e0251544
keywords: ["KSEVENT_CONNECTION_ENDOFSTREAM Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_CONNECTION_ENDOFSTREAM
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSEVENT\_CONNECTION\_ENDOFSTREAM


The **KSEVENT\_CONNECTION\_ENDOFSTREAM** event allows a client to receive notification of an end of stream event. This event occurs when a standard streaming header is used, when a buffer whose header has the KSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM variable completes processing. *Rendering* points must support this event so the end of stream event can be detected by the client.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSEVENT_CONNECTION_ENDOFSTREAM%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




