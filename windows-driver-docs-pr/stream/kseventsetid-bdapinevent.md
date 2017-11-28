---
title: KSEVENTSETID\_BdaPinEvent
description: KSEVENTSETID\_BdaPinEvent
ms.assetid: f81b9973-f4ae-4b39-a4e1-bbaff21c5d41
---

# KSEVENTSETID\_BdaPinEvent


## <span id="ddk_kseventsetid_bdapinevent_ks"></span><span id="DDK_KSEVENTSETID_BDAPINEVENT_KS"></span>


KSEVENTSETID\_BdaPinEvent is the BDA pin event set. It is used for notifying filters or applications that requested notification of events related to a specific pin.

The following events are available:

<span id="KSEVENT_BDA_PIN_CONNECTED"></span><span id="ksevent_bda_pin_connected"></span>[**KSEVENT\_BDA\_PIN\_CONNECTED**](ksevent-bda-pin-connected.md)  
Notifies when a pin becomes connected.

<span id="KSEVENT_BDA_PIN_DISCONNECTED"></span><span id="ksevent_bda_pin_disconnected"></span>[**KSEVENT\_BDA\_PIN\_DISCONNECTED**](ksevent-bda-pin-disconnected.md)  
Notifies when a pin becomes disconnected.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The network provider filter uses this event set to register for notification of events related to pins as those events occur.

If a BDA minidriver does not define this event set, then the BDA support library adds support when a pin is created by either the **BdaCreatePin** or **BdaInitFilter** function.

If a BDA minidriver defines its own handlers for this event set, then the minidriver is responsible for signaling the events in this event set to notify filters or plugins that previously requested notification.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSEVENTSETID_BdaPinEvent%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




