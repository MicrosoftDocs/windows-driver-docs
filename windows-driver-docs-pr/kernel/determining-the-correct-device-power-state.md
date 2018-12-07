---
title: Determining the Correct Device Power State
description: Determining the Correct Device Power State
ms.assetid: 4acefe93-1d7a-4c12-8701-03c2a8929591
keywords: ["DEVICE_CAPABILITIES structure", "correct device power states WDK power management", "device power states WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Determining the Correct Device Power State





The power policy owner checks the [**DeviceState**](devicestate.md) array in the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure to determine the valid range of device power states for each system power state. The array lists the highest device power state the underlying device can support for each system power state.

When choosing a specific state from this range, consider the following:

-   Most devices enter the D0 state when the system enters the S0 state.

-   Most devices enter the D3 state when the system enters any sleeping state. However, a device that is enabled for wake-up might be required to enter D1 or D2 instead, if it supports such states. For further information, see [Reporting Device Power Capabilities](reporting-device-power-capabilities.md).

-   Special rules apply for the device that will hold the hibernation file. If the system IRP requests **PowerSystemHibernate**, the device that will hold the hibernation file must not power off. The power policy owner for such a device should request device power state D3 and save context, but the device's drivers must not power off the device.

If the system IRP requests **PowerSystemShutdown**, the driver should check the POWER\_ACTION value at **Irp-&gt;Parameters.Power.ShutdownType** to determine the reason for the state change. For further information, see [System Power Actions](system-power-actions.md).

The device power policy owner must send a device set-power IRP for each system set-power IRP, even if the device is already in the correct device power state. If the driver previously suspended device operations in response to a query-power IRP, the set-power IRP notifies it to stop queuing IRPs and return to normal operation for its current power state. The only exception occurs when the device is in the D3 state; in this case, the driver need not send an additional [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request for D3.

 

 




