---
title: Distinguishing Fast Startup from Wake-from-Hibernation
description: Starting with Windows 8, a fast startup mode is available to start a computer in less time than is typically required for a traditional, cold startup.
ms.assetid: 1768F739-619A-441F-B270-029DD1F72953
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Distinguishing Fast Startup from Wake-from-Hibernation


Starting with Windows 8, a fast startup mode is available to start a computer in less time than is typically required for a traditional, cold startup. A fast startup is a hybrid combination of a cold startup and a wake-from-hibernation startup. Frequently, kernel-mode device drivers need to distinguish fast startups from wake-from-hibernation so that their devices behave as users expect. To make this distinction, drivers can use information that is available in [system power IRPs](power-irps-for-the-system.md).

During a cold startup, the boot loader constructs a kernel memory image by loading the sections of the Windows kernel file into memory and linking them. Next, the kernel configures core system functions, enumerates the devices attached to the computer, and loads drivers for them.

In contrast, a fast startup simply loads the hibernation file (Hiberfil.sys) into memory to restore the previously saved image of the Windows kernel and loaded drivers. A fast startup tends to take significantly less time than a cold startup.

To prepare for a fast startup, Windows performs a hybrid shutdown sequence that combines elements of a full shutdown sequence and a prepare-for-hibernation sequence. First, as in a full shutdown, Windows closes all applications and logs off all user sessions. At this stage, the system state is similar to that of a computer that has just started up—no applications are running, but the Windows kernel is loaded and the system session is running. Next, the power manager sends system power IRPs to device drivers to tell them to prepare their devices to enter hibernation. Finally, Windows saves the kernel memory image (including the loaded kernel-mode drivers) in Hiberfil.sys and shuts down the computer.

By default, Windows 8 uses a fast startup in place of a cold startup. Users can typically ignore the differences between fast and cold startups, but, to meet users' expectations, fast startups should behave the same as cold startups. In particular, the devices attached to the computer should be configured the same for a fast startup as they would be for a cold startup.

If the driver for a device configures the device differently depending on whether a cold startup or a wake-from-hibernation occurred, this driver should, after a fast startup, configure the device as though a cold startup (instead of a wake-from-hibernation) occurred. For example, the system-supplied NDIS driver disables miniport wake capabilities on a fast startup but not on a wake-from-hibernation.

To distinguish a fast startup from a wake-from-hibernation, a driver can inspect the information in the system set-power ([**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744)) IRP that informs the driver that the computer has entered the S0 (working) state. The driver's [I/O stack location](https://msdn.microsoft.com/library/windows/hardware/ff550659) in this IRP contains a **Power** member, which is a structure that contains power-related information. Starting with Windows Vista, the **Power** member structure contains a **SystemPowerStateContext** member, which is a [**SYSTEM\_POWER\_STATE\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/jj835780) structure that contains information about the previous system power states. This information is encoded in bit fields in the **SYSTEM\_POWER\_STATE\_CONTEXT** structure.

Most of the bit fields in the **SYSTEM\_POWER\_STATE\_CONTEXT** structure are reserved for system use and are opaque to drivers. However, this structure contains two bit fields, **TargetSystemState** and **EffectiveSystemState**, that can be read by drivers to determine whether a fast startup or a wake-from-hibernation occurred.

The **TargetSystemState** and **EffectiveSystemState** bit fields are set to [**SYSTEM\_POWER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff564565) enumeration values. If **TargetSystemState** = **PowerSystemHibernate** and **EffectiveSystemState** = **PowerSystemHibernate**, a wake-from-hibernation occurred. However, if **TargetSystemState** = **PowerSystemHibernate** and **EffectiveSystemState** = **PowerSystemShutdown**, a fast startup occurred.

The **TargetSystemState** bit field specifies the last system power state transition for which the driver received a system power IRP before the computer shut down or entered hibernation. The **EffectiveSystemState** bit field indicates the effective previous system power state of the device, as perceived by the user. The **TargetSystemState** and **EffectiveSystemState** values might not match if, for example, the driver received notification of a pending system transition to the hibernation state, but a hybrid shutdown subsequently occurred.

For more information, see [**SYSTEM\_POWER\_STATE\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/jj835780).

 

 




