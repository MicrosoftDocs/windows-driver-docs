---
title: IoCompletion Routines for Device Power IRPs
description: IoCompletion Routines for Device Power IRPs
ms.assetid: c275fcba-5fa9-427c-8d7e-2339563985e4
keywords: ["IoCompletion routines", "power IRPs WDK kernel , device changes", "state transitions WDK power management", "device state transitions WDK power management", "working state returns WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# IoCompletion Routines for Device Power IRPs





After the bus driver completes the IRP, the I/O manager calls the [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routines registered by higher-level drivers as they passed the IRP down the stack.

Whenever a device enters the D0 state, each of its drivers should set an *IoCompletion* routine that performs most of the tasks required to return it to the working state. Drivers should set an *IoCompletion* routine for any transition to the D0 state, whether the device is returning from a sleeping state or entering D0 at system start-up. The following figure shows the tasks such an *IoCompletion* routine should perform.

![diagram illustrating the device power-up iocompletion routine](images/d0-comp.png)

These tasks include:

-   Restoring device power state or reinitializing the device, as required, and preparing to handle any I/O queued by drivers while the device was not in the working state

-   Calling [**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765) to notify the power manager that the device is in the D0 power state.

-   Calling [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) to receive the next power IRP, if the driver did not originally send the current power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only).

-   Freeing memory allocated for the device context.

-   Calling [**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560) to free the lock that the driver acquired in its [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine when it received the IRP.

-   Returning STATUS\_SUCCESS.

The bus driver does not power up the device until it or higher drivers must communicate with the device.

When its device enters a sleeping state, a driver should set an *IoCompletion* routine that calls [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) (Windows Server 2003, Windows XP, and Windows 2000 only) and releases the remove lock. Remember that a driver cannot access its device while the device is in a sleeping state.

 

 




