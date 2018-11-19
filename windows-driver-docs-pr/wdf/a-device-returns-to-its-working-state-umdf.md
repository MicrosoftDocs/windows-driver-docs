---
title: A Device Returns to Its Working State
description: A Device Returns to Its Working State
ms.assetid: 2b192eea-f731-4d61-be19-95724bf7b04a
keywords:
- power management scenarios WDK UMDF , device returning to its working state
- device returning to working state scenario WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# A Device Returns to Its Working State


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

A device that is in a low-power state returns to its working state if one of the following occurs:

-   The device detects an external event and triggers a wake signal on its bus. The kernel-mode bus driver detects the wake signal.

-   The device has been idle and a driver calls [**IWDFDevice2::StopIdle**](https://msdn.microsoft.com/library/windows/hardware/ff556948).

-   The system's power state has changed from a low-power state to its working (S0) state.

In each of these situations, the kernel-mode bus driver restores the device (a child device of the bus) to its working (D0) state.

For each UMDF-based function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is lowest in the driver stack:

1.  The framework calls the driver's [**IPnpCallback::OnD0Entry**](https://msdn.microsoft.com/library/windows/hardware/ff556799) callback function (if it exists).

2.  If the driver is the device's power policy owner, the framework calls its [**IPowerPolicyCallbackWakeFromS0::OnDisarmWakeFromS0**](https://msdn.microsoft.com/library/windows/hardware/ff556819) or [**IPowerPolicyCallbackWakeFromSx::OnDisarmWakeFromSx**](https://msdn.microsoft.com/library/windows/hardware/ff556828) callback function.

3.  The framework restarts all of the device's power-managed I/O queues and calls their [**IQueueCallbackIoResume::OnIoResume**](https://msdn.microsoft.com/library/windows/hardware/ff556865) callback functions (if necessary).

4.  If the driver is using self-managed I/O, the framework calls the driver's [**IPnpCallbackSelfManagedIo::OnSelfManagedIoRestart**](https://msdn.microsoft.com/library/windows/hardware/ff556785) callback function.

To see a diagram that shows these steps, see [A User Plugs in a Device](a-user-plugs-in-a-device.md).

 

 





