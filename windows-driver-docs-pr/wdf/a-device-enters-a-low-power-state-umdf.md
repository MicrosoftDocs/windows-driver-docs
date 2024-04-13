---
title: A Device Enters a Low-Power State (UMDF 1)
description: A Device Enters a Low-Power State
keywords:
- power management scenarios WDK UMDF, entering a low-power state
- low-power state scenario WDK UMDF
ms.date: 04/20/2017
---

# A Device Enters a Low-Power State (UMDF 1)


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

A device leaves its working (D0) state and enters a low-power state if one of the following occurs:

-   The device is idle (that is, not being accessed) and is capable of entering a low-power idle state while the system remains in its working (S0) state.

-   The system's power state has changed from its working (S0) state to a low-power state. (Drivers can call [**IWDFDevice2::GetSystemPowerAction**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice2-getsystempoweraction) to determine the reason for the change in the system's power state.)

For each UMDF-based function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is highest in the driver stack:

1.  If the driver is using self-managed I/O, the framework calls the driver's [**IPnpCallbackSelfManagedIo::OnSelfManagedIoSuspend**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagediosuspend) callback function.

2.  The framework stops all of the device's power-managed I/O queues and calls their [**IPnpCallbackSelfManagedIo::OnSelfManagedIoStop**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagediostop) callback functions (if they exist).

3.  If the driver is the device's power policy owner, the framework calls its [**IPowerPolicyCallbackWakeFromS0::OnArmWakeFromS0**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipowerpolicycallbackwakefroms0-onarmwakefroms0) or [**IPowerPolicyCallbackWakeFromSx::OnArmWakeFromSx**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipowerpolicycallbackwakefromsx-onarmwakefromsx) callback function.

4.  The framework calls the driver's [**IPnpCallback::OnD0Exit**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallback-ond0exit) callback function (if it exists).

To see a diagram that shows these steps, see the orderly removal figure in [A User Unplugs a Device](a-user-unplugs-a-device.md).

 

