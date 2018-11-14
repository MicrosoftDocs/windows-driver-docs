---
title: Handling Removable Child Devices
description: Handling Removable Child Devices
ms.assetid: 0edc0331-7178-4986-b818-9f1ee8f12995
keywords:
- removable child devices WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Removable Child Devices


A video miniport driver should detect when a removable child device is changed with another like device so the driver can prevent Plug and Play (PnP) from using the data of the original child device. For example, the video miniport driver should detect when the user switches monitors.

If Extended Display Information Data (EDID) for the attached monitor changes between successive calls to the video miniport driver's [*HwVidGetVideoChildDescriptor*](https://msdn.microsoft.com/library/windows/hardware/ff567341) function, instead of tearing down the original monitor stack and building a new stack for the new monitor, the video port driver modifies the state of the current stack. Although the graphics subsystem can determine the new monitor's capabilities, because the original stack was not torn down, other operating system components (such as, PnP) use the capability data of the original monitor.

A video miniport driver can detect a change to the attached monitor and perform one of the following operations to prevent PnP from using the data of the original monitor:

1.  The video miniport driver can report that no monitor is present in order to force the tear down of the former monitor stack. Then, to force the video port driver to re-enumerate child devices in order to report the new monitor, the video miniport driver calls the [**VideoPortEnumerateChildren**](https://msdn.microsoft.com/library/windows/hardware/ff570297) function. The video miniport driver should call **VideoPortEnumerateChildren** to schedule the re-enumeration of child devices only after the first enumeration that reports that the monitor is disconnected completes.

2.  On appropriate computer and monitor configurations (see the following exception), the video miniport driver can respond to its [*HwVidGetVideoChildDescriptor*](https://msdn.microsoft.com/library/windows/hardware/ff567341) function by returning the new monitor's information in the buffer that the *pChildDescriptor* parameter of *HwVidGetVideoChildDescriptor* points to. However, the video miniport driver must specify a 32-bit [*device ID*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-id) for the new monitor in the variable that the *UId* parameter points to. This value must be different from the value that the video miniport driver used for the former monitor.

For an Advanced Configuration and Power Interface (ACPI) enumerated monitor, the first mechanism is generally preferable because 32-bit device IDs are tied to the BIOS implementation. Therefore, specifying a different 32-bit device ID might not be possible.

 

 





