---
title: Windows Kernel-Mode Power Manager
description: Windows Kernel-Mode Power Manager
ms.assetid: 2d39e43a-63a6-4474-a1ed-c24b4526a3f5
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Windows Kernel-Mode Power Manager


Windows uses power management technology to reduce power consumption for PCs in general and for battery-powered laptops in particular. For example, a Windows computer can be put in a sleep or hibernation state. A complex power management system for computer devices has evolved so that when the computer begins to shut down or go to lower power consumption, the attached devices can also be powered down in a proper manner so that no data is lost. But these devices need a warning that the power status in changing and they may also need to be part of a communications loop that tells the controlling device to wait until they can shut down properly.

The Windows kernel-mode power manager manages the orderly change in power status for all devices that support power state changes. This is often done through a complex stack of devices controlling other devices. Each controlling device is called a *node* and must have a driver that can handle the communication of power state changes up and down through a device stack.

If you are writing a driver that can be affected by power-state changes, you must be able to process the following types of information in your driver code:

-   System activity level.

-   System battery level.

-   Current requests to shut down, sleep, or hibernate.

-   User actions such as pressing a power button.

-   Control panel settings, such as automatically shutting down at 10 percent battery power.

The power manager handles these requests using IRPs. For more information about IRPs, see [Handling IRPs](handling-irps.md).

The power manager works in combination with policy management to handle power management and coordinate power events, and then generates power management IRPs. The power manager collects requests to change the power state, decides which order the devices must have their power state changed, and then send the appropriate IRPs to tell the appropriate drivers to make the changes (which in turn may tell subdevices to make the change as well). The policy manager monitors activity in the system and integrates user status, application status, and device driver status into power policy.

For more detailed information about power management, see [Power Management for Windows Drivers](implementing-power-management.md).

The power manager is considered a subcomponent of the I/O manager. For more information, see [Windows I/O Manager](windows-kernel-mode-i-o-manager.md).

Routines that provide a direct interface to the power manager are usually prefixed with "**Po**"; for example, **PoSetPowerState**. For a list of power manager routines, see [Power Manager Routines](https://msdn.microsoft.com/library/windows/hardware/ff559835).

The Windows Driver Frameworks (WDF) provides a set of libraries to make power management much easier. For more information about WDF, see [Kernel-Mode Driver Framework Overview](https://msdn.microsoft.com/library/windows/hardware/ff544296).

 

 




