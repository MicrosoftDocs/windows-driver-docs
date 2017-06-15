---
title: Handling IRP\_MN\_SET\_POWER for System Power States
author: windows-driver-content
description: Handling IRP\_MN\_SET\_POWER for System Power States
MS-HAID:
- 'PwrMgmt\_694616ba-6383-4e06-80cc-6688ac72dd1f.xml'
- 'kernel.handling\_irp\_mn\_set\_power\_for\_system\_power\_states'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 21e8e8a7-ca77-445b-a49e-28a53f431a26
keywords: ["IRP_MN_SET_POWER", "system power states WDK kernel , IRP_MN_SET_POWER", "set-power IRPs WDK power management"]
---

# Handling IRP\_MN\_SET\_POWER for System Power States


## <a href="" id="ddk-handling-irp-mn-set-power-for-system-power-states-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20IRP_MN_SET_POWER%20for%20System%20Power%20States%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


