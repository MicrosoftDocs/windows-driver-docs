---
title: Porting I/O
description: Porting I/O
ms.assetid: D65B85C4-401F-4143-9626-5C16E24925A0
---

# Porting I/O


KMDF drivers handle I/O requests by creating one or more queues and associating one or more I/O event callback functions with each queue. To port a WDM driver’s I/O handling code to KMDF:

-   [Port I/O queues](creating-i-o-queues.md).

-   [Port I/O dispatch routines](porting-i-o-dispatch-routines-to-i-o-event-callback-functions.md) to I/O event callbacks.

-   [Revise code that handles completed requests](revise-completed-request-logic.md).

-   [Revise Canceled Request Logic](revise-canceled-request-logic.md).

-   [Revise Forward Request Logic](revise-forward-request-logic.md).

-   [Revise code that issues I/O requests](revise-code-that-issues-i-o-requests.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Porting%20I/O%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




