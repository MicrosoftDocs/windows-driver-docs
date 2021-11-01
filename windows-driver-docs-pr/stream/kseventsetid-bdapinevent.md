---
title: KSEVENTSETID_BdaPinEvent
description: KSEVENTSETID_BdaPinEvent is the BDA pin event set.
ms.date: 10/12/2021
ms.localizationpriority: medium
---

# KSEVENTSETID_BdaPinEvent

**KSEVENTSETID_BdaPinEvent** is the BDA pin event set. It is used for notifying filters or applications that requested notification of events related to a specific pin.

The following events are available:

[**KSEVENT_BDA_PIN_CONNECTED**](ksevent-bda-pin-connected.md)  
Notifies when a pin becomes connected.

[**KSEVENT_BDA_PIN_DISCONNECTED**](ksevent-bda-pin-disconnected.md)  
Notifies when a pin becomes disconnected.

## Comments

The network provider filter uses this event set to register for notification of events related to pins as those events occur.

If a BDA minidriver does not define this event set, then the BDA support library adds support when a pin is created by either the **BdaCreatePin** or **BdaInitFilter** function.

If a BDA minidriver defines its own handlers for this event set, then the minidriver is responsible for signaling the events in this event set to notify filters or plugins that previously requested notification.
