---
title: WDI Selective Suspend capability registration
description: The following is a flow diagram for registering the USB Selective Suspend capability.
ms.assetid: E4AE424F-2017-4111-B4C7-DF0BA6A40A15
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI Selective Suspend capability registration


The following is a flow diagram for registering the USB Selective Suspend capability.

![wdi selective suspend capability registration](images/wdi-register-usb-selective-suspend-flow.png)

AdapterCap(PM(ss)), \*SelectiveSuspend, **LeIdleNotificationHandler**, and **LeCancelIdleNotificationHandler** must be true or valid for WDI to register that WLAN supports Selective Suspend.

When WDI decides that Selective Suspend can be supported, WDI also registers an optional handler to NDIS.

## Related topics


[*MiniportWdiCancelIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/mt297560)

[*MiniportWdiIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/mt297563)

 

 






