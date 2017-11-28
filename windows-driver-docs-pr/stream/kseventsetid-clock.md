---
title: KSEVENTSETID\_Clock
description: Clients can request to be notified of clock state events on a clock by registering these events with the clock's file object KSEVENT\_CLOCK\_INTERVAL\_MARKKSEVENT\_CLOCK\_POSITION\_MARKWhen a client submits the IOCTL\_KS\_ENABLE\_EVENT request to register for event notification, it submits as a data buffer the structure documented in the EventData section of each event reference page.
ms.assetid: a411f83a-0361-4db6-9617-7c8588739cb4
keywords: ["KSEVENTSETID_Clock Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENTSETID_Clock
api_type:
- NA
---

# KSEVENTSETID\_Clock


Clients can request to be notified of clock state events on a clock by registering these events with the clock's file object:

[**KSEVENT\_CLOCK\_INTERVAL\_MARK**](ksevent-clock-interval-mark.md)

[**KSEVENT\_CLOCK\_POSITION\_MARK**](ksevent-clock-position-mark.md)

When a client submits the IOCTL\_KS\_ENABLE\_EVENT request to register for event notification, it submits as a data buffer the structure documented in the **EventData** section of each event reference page.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSEVENTSETID_Clock%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




