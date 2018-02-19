---
title: POS events
description: POS events
ms.assetid: '1123b789-c0ee-4490-9081-79c08fc31417'
---

POS events
==========

This section describes the events that are passed from the device driver to the Point of Service (POS) API layer by using [ReadFile](http://go.microsoft.com/fwlink/p/?LinkId=314125). When an application successfully claims a device through the POS API, the runtime will maintain a continuous read operation against the device driver to receive events. The I/O is message-based. That is, [ReadFile](http://go.microsoft.com/fwlink/p/?LinkId=314125) needs to pass in a buffer sufficiently large enough to read in the current event. The driver retains the message until a read request with a sufficient output buffer to read the entire message is made.

## In this section


[ReleaseDeviceRequested](releasedevicerequested.md)
[StatusUpdated](statusupdated.md)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bpos\pos%5D:%20POS%20events%20%20RELEASE:%20%282/18/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




