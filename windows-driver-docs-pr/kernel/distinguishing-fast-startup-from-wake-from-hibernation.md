---
title: Distinguishing Fast Startup from Wake-from-Hibernation
description: Starting with Windows 8, a fast startup mode is available to start a computer in less time than is typically required for a traditional, cold startup.
ms.localizationpriority: medium
ms.date: 05/10/2021
ms.custom: contperf-fy21q4
---

# Distinguishing Fast Startup from Wake-from-Hibernation


There are three startup modes in Windows:

* Cold (traditional)
* Wake-from-hibernation
* Fast (combines first two, introduced in Windows 8)

To distinguish fast startups from wake-from-hibernation, kernel-mode device drivers can examine [system power IRPs](power-irps-for-the-system.md).

During a cold startup, the boot loader constructs a kernel memory image by loading the sections of the Windows kernel file into memory and linking them. Next, the kernel configures core system functions, enumerates the devices attached to the computer, and loads drivers for them.

In contrast, a fast startup simply loads the hibernation file (Hiberfil.sys) into memory. A fast startup tends to take significantly less time than a cold startup.

To distinguish a fast startup from a wake-from-hibernation, a driver can inspect the information in the system set-power ([**IRP\_MN\_SET\_POWER**](./irp-mn-set-power.md)) IRP that informs the driver that the computer has entered the S0 (working) state. The driver's [I/O stack location](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) in this IRP contains a **Power** member, which is a structure that contains power-related information. Starting with Windows Vista, the **Power** member structure contains a **SystemPowerStateContext** member, which is a [**SYSTEM\_POWER\_STATE\_CONTEXT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_system_power_state_context) structure that contains information about the previous system power states. This information is encoded in bit fields in the **SYSTEM\_POWER\_STATE\_CONTEXT** structure.

Most of the bit fields in the **SYSTEM\_POWER\_STATE\_CONTEXT** structure are reserved for system use and are opaque to drivers. However, this structure contains two bit fields, **TargetSystemState** and **EffectiveSystemState**, that can be read by drivers to determine whether a fast startup or a wake-from-hibernation occurred.

The **TargetSystemState** and **EffectiveSystemState** bit fields are set to [**SYSTEM\_POWER\_STATE**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_system_power_state) enumeration values. If **TargetSystemState** = **PowerSystemHibernate** and **EffectiveSystemState** = **PowerSystemHibernate**, a wake-from-hibernation occurred.

However, if **TargetSystemState** = **PowerSystemShutdown** and **EffectiveSystemState** = **PowerSystemHibernate**, a fast startup occurred.

The **TargetSystemState** bit field specifies the last system power state transition for which the driver received a system power IRP before the computer shut down or entered hibernation. The **EffectiveSystemState** bit field indicates the effective previous system power state of the device, as perceived by the user. The **TargetSystemState** and **EffectiveSystemState** values might not match if, for example, the driver received notification of a pending system transition to the hibernation state, but a hybrid shutdown subsequently occurred.

For more information, see [**SYSTEM\_POWER\_STATE\_CONTEXT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_system_power_state_context).

## Preparing for fast startup

To prepare for a fast startup, Windows performs a full shutdown sequence and saves a hibernation file.

1. First, as in a full shutdown, Windows closes all applications and logs off all user sessions. At this stage, no applications are running, but the Windows kernel is loaded and the system session is running.
2. Next, the power manager sends system power IRPs to device drivers to tell them to prepare their devices to enter hibernation.
3. Finally, Windows saves the kernel memory image (including the loaded kernel-mode drivers) in Hiberfil.sys and shuts down the computer.

If the driver for a device configures the device differently depending on whether a cold startup or a wake-from-hibernation occurred, this driver should, after a fast startup, configure the device as though a cold startup occurred. For example, the system-supplied NDIS driver disables miniport wake capabilities on a fast startup but not on a wake-from-hibernation.

