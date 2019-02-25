---
title: Handling IRP_MN_SET_POWER for System Power States
description: Handling IRP_MN_SET_POWER for System Power States
ms.assetid: 21e8e8a7-ca77-445b-a49e-28a53f431a26
keywords: ["IRP_MN_SET_POWER", "system power states WDK kernel , IRP_MN_SET_POWER", "set-power IRPs WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling IRP\_MN\_SET\_POWER for System Power States





The power manager sends a power IRP that specifies the minor code [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) and a system power state for one of the following reasons:

-   To change the system power state.

-   To reaffirm the current power state after a failed [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) request.

Through the I/O manager, the power manager sends the IRP to the top driver in the device stack at each PnP device node. The IRP notifies all drivers in the stack of the correct system power state.

To ensure an orderly start-up, the power manager sequences system power-up IRPs so that parent devices have the opportunity to power up before their children do. The power manager does not query before sending a system power-up IRP.

Similarly, to ensure that the computer sleeps or shuts down in an orderly way, the power manager sends system IRPs that specify sleep, hibernation, or shutdown in a defined sequence, so that devices farther from the root power down before devices nearer the root. Whenever possible, the power manager queries before sending such an IRP. For more information, see [Handling IRP\_MN\_QUERY\_POWER for System Power States](handling-irp-mn-query-power-for-system-power-states.md).

The system power IRP is not a direct request to change power state — it is a notification. A driver must not change the power state of its device as a direct response to the *system* power IRP; a driver changes its device's power state only in response to a *device* power IRP. (The device power policy owner sends the device power IRP; see [Handling a System Set-Power IRP in a Device Power Policy Owner](handling-a-system-set-power-irp-in-a-device-power-policy-owner.md).)

Even if the device is already in a device power state that is valid for the requested system power state, each driver must nevertheless pass the system set-power IRP to the next-lower driver, until it reaches the bus driver. Only the bus driver is allowed to complete this IRP.

How a driver handles this IRP depends upon its role in the device stack, as described in the following sections:

[Handling a System Set-Power IRP in a Device Power Policy Owner](handling-a-system-set-power-irp-in-a-device-power-policy-owner.md)

[Handling a System Set-Power IRP in a Bus Driver](handling-a-system-set-power-irp-in-a-bus-driver.md)

[Handling a System Set-Power IRP in a Filter Driver](handling-a-system-set-power-irp-in-a-filter-driver.md)

A driver cannot fail an **IRP\_MN\_SET\_POWER** request to set the system power state. The power manager ignores any failure status returned for this IRP.

 

 




