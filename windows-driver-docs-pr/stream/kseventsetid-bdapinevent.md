---
title: KSEVENTSETID\_BdaPinEvent
description: KSEVENTSETID\_BdaPinEvent
ms.assetid: f81b9973-f4ae-4b39-a4e1-bbaff21c5d41
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSEVENTSETID\_BdaPinEvent


## <span id="ddk_kseventsetid_bdapinevent_ks"></span><span id="DDK_KSEVENTSETID_BDAPINEVENT_KS"></span>


KSEVENTSETID\_BdaPinEvent is the BDA pin event set. It is used for notifying filters or applications that requested notification of events related to a specific pin.

The following events are available:

<span id="KSEVENT_BDA_PIN_CONNECTED"></span><span id="ksevent_bda_pin_connected"></span>[**KSEVENT\_BDA\_PIN\_CONNECTED**](ksevent-bda-pin-connected.md)  
Notifies when a pin becomes connected.

<span id="KSEVENT_BDA_PIN_DISCONNECTED"></span><span id="ksevent_bda_pin_disconnected"></span>[**KSEVENT\_BDA\_PIN\_DISCONNECTED**](ksevent-bda-pin-disconnected.md)  
Notifies when a pin becomes disconnected.

### Comments

The network provider filter uses this event set to register for notification of events related to pins as those events occur.

If a BDA minidriver does not define this event set, then the BDA support library adds support when a pin is created by either the **BdaCreatePin** or **BdaInitFilter** function.

If a BDA minidriver defines its own handlers for this event set, then the minidriver is responsible for signaling the events in this event set to notify filters or plugins that previously requested notification.

 

 





