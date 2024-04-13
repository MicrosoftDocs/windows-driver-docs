---
title: WDI Selective Suspend capability registration
description: The following is a flow diagram for registering the USB Selective Suspend capability.
ms.date: 03/02/2023
---

# WDI Selective Suspend capability registration


The following is a flow diagram for registering the USB Selective Suspend capability.

![wdi selective suspend capability registration.](images/wdi-register-usb-selective-suspend-flow.png)

AdapterCap(PM(ss)), \*SelectiveSuspend, **LeIdleNotificationHandler**, and **LeCancelIdleNotificationHandler** must be true or valid for WDI to register that WLAN supports Selective Suspend.

When WDI decides that Selective Suspend can be supported, WDI also registers an optional handler to NDIS.

## Related topics


[*MiniportWdiCancelIdleNotification*](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-miniport_wdi_cancel_idle_notification)

[*MiniportWdiIdleNotification*](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-miniport_wdi_idle_notification)

 

