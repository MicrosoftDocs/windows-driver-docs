---
title: Managing Device Power Policy
description: Managing Device Power Policy
ms.assetid: f6f9ab40-4d51-4181-ac11-ff7af42370af
keywords: ["device power policy WDK kernel", "power policy WDK kernel", "device power policy owners WDK kernel", "function drivers WDK power management", "device power states WDK kernel", "initial device power state WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Managing Device Power Policy





Just as the power manager maintains and administers power policy for the system, one driver in the device stack for each device maintains and administers power policy for the device. This driver is the *device power policy owner* for the device.

The device power policy owner is the driver that has the most information about the device usage and power state. It need not physically be able to set the device registers to power the device on and off, but it must be able to determine when the device is in use, when it is idle, and when it should change power state.

Typically, the function driver for a device is its power policy owner, although for some devices another driver or system component might assume this role. For more information about the types of drivers involved in power management, see [Types of WDM Drivers](types-of-wdm-drivers.md).

Some drivers act as the function driver for one device (creating an FDO) and the bus driver (creating a PDO) for an enumerated child device. In its Dispatch routines for power and PnP IRPs, such a driver must distinguish its handling of IRPs sent to the FDO and those sent to the PDO.

For example, the driver for a SCSI adapter might perform the roles of function driver (creating an FDO) for the adapter itself and bus driver (creating a PDO) for the disks attached to the adapter. In its capacity as function driver/policy owner for the SCSI adapter, this driver receives system IRPs and requests device IRPs for the SCSI adapter. In its capacity as bus driver for the disks, it handles and completes device IRPs that specify the disk PDOs it creates. Just because the driver owns power policy for one device (FDO) does not mean that it owns power policy for the child device (PDO).

The device power policy owner is responsible for the following:

-   Setting the initial power state of the device to D0 by calling [**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765) as it handles the Plug and Play manager's [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request.

    Devices should power on as needed; for example, a device must power on to handle an I/O request. The device power policy owner is responsible for determining when its device is needed, ensuring that device power is on, and setting the correct device power state. The typical device should be powered on by the time the PnP start-device IRP has completed.

    As a general rule, most devices should be powered off when not in use, even when the system is in the working state.

-   Sending a device power request in response to a system power request by calling [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734).

    For example, when the policy owner receives a system set-power IRP, it sends a device set-power IRP. Most devices enter D3 when the system enters any sleeping state. The **DeviceState** array in the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure lists the highest-powered state the device can maintain for each system power state. (See [Reporting Device Power Capabilities](reporting-device-power-capabilities.md).)

-   Detecting when the device is idle and putting it to sleep to conserve energy.

    Either the power manager or the device policy owner can detect an idle device and send a device power IRP to change its state. For more information, see [Detecting an Idle Device](detecting-an-idle-device.md).

-   Returning its device to the working state when required.

    When an I/O request arrives for a sleeping device, the device's drivers should return it to the working state.

-   Enabling and disabling wake-up for its device when requested.

    The device power policy owner sends and cancels wait/wake IRPs, as described in [Supporting Devices that Have Wake-Up Capabilities](supporting-devices-that-have-wake-up-capabilities.md).

 

 




