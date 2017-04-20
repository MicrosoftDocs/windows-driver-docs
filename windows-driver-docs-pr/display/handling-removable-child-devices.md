---
title: Handling Removable Child Devices
description: Handling Removable Child Devices
ms.assetid: 0edc0331-7178-4986-b818-9f1ee8f12995
keywords:
- removable child devices WDK Windows 2000 display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling Removable Child Devices


A video miniport driver should detect when a removable child device is changed with another like device so the driver can prevent Plug and Play (PnP) from using the data of the original child device. For example, the video miniport driver should detect when the user switches monitors.

If Extended Display Information Data (EDID) for the attached monitor changes between successive calls to the video miniport driver's [*HwVidGetVideoChildDescriptor*](https://msdn.microsoft.com/library/windows/hardware/ff567341) function, instead of tearing down the original monitor stack and building a new stack for the new monitor, the video port driver modifies the state of the current stack. Although the graphics subsystem can determine the new monitor's capabilities, because the original stack was not torn down, other operating system components (such as, PnP) use the capability data of the original monitor.

A video miniport driver can detect a change to the attached monitor and perform one of the following operations to prevent PnP from using the data of the original monitor:

1.  The video miniport driver can report that no monitor is present in order to force the tear down of the former monitor stack. Then, to force the video port driver to re-enumerate child devices in order to report the new monitor, the video miniport driver calls the [**VideoPortEnumerateChildren**](https://msdn.microsoft.com/library/windows/hardware/ff570297) function. The video miniport driver should call **VideoPortEnumerateChildren** to schedule the re-enumeration of child devices only after the first enumeration that reports that the monitor is disconnected completes.

2.  On appropriate computer and monitor configurations (see the following exception), the video miniport driver can respond to its [*HwVidGetVideoChildDescriptor*](https://msdn.microsoft.com/library/windows/hardware/ff567341) function by returning the new monitor's information in the buffer that the *pChildDescriptor* parameter of *HwVidGetVideoChildDescriptor* points to. However, the video miniport driver must specify a 32-bit [*device ID*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-id) for the new monitor in the variable that the *UId* parameter points to. This value must be different from the value that the video miniport driver used for the former monitor.

For an Advanced Configuration and Power Interface (ACPI) enumerated monitor, the first mechanism is generally preferable because 32-bit device IDs are tied to the BIOS implementation. Therefore, specifying a different 32-bit device ID might not be possible.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Handling%20Removable%20Child%20Devices%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




