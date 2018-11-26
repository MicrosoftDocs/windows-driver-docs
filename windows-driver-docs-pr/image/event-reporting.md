---
title: Event Reporting
description: Event Reporting
ms.assetid: 4c3ffa7e-d0b3-483c-9f6b-3fe8ae997cf0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Event Reporting





The WIA architecture enables a still image device to notify the WIA minidriver when some action on the device occurs. For example, a scanner might have a push-button on its front panel, enabling the user to initiate a scan directly from the device. The WIA minidriver must be notified of this event so it can notify the WIA service. All running applications that have registered to receive this event are notified. Furthermore, if an application has registered to be started as a result of this event prior to the event, the WIA service starts that application.

The WIA architecture supports interrupt events and polled events. For more information about these events, see [WIA Driver Event Support](wia-driver-event-support.md).

 

 




