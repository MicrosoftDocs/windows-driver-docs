---
Description: The topics in this section examine the ways in which the WDM power model interacts with the power management properties of USB devices.
title: Implementing power management in USB client drivers
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Implementing power management in USB client drivers


The topics in this section examine the ways in which the WDM power model interacts with the power management properties of USB devices.

Power management abilities of USB devices that comply with the Universal Serial Bus (USB) specification have a rich and complex set of power management features. It is important to understand how these features interact with the Windows Driver Model (WDM), and in particular how Microsoft Windows has adapted standard USB features to support the system wakeup architecture.

For information about WDM power management in kernel-mode drivers, see [Implementing Power Management](https://msdn.microsoft.com/library/windows/hardware/ff547131).

USB client drivers based on kernel-mode driver framework (KMDF) and user-mode driver framework (UMDF) should use the mechanisms supported by the base technology and respective frameworks for managing power for a USB device. For information about managing power in KMDF-based client drivers, see [Supporting PnP and Power Management in Your Driver](https://msdn.microsoft.com/library/windows/hardware/ff544686); for UMDF-based client drivers, see [PnP and Power Management in UMDF-based Drivers](https://msdn.microsoft.com/library/windows/hardware/ff560449).

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[USB Device Power States](comparing-usb-device-states-to-wdm-device-states.md)</p></td>
<td><p>This topic describes the WDM device states to use for USB device power states as specified in section 9.1 of the Universal Serial Bus 2.0 specification.</p></td>
</tr>
<tr class="even">
<td><p>[Selective suspend in USB drivers (WDF)](selective-suspend-in-usb-drivers-wdf.md)</p></td>
<td><p>A USB function driver supports runtime idle detection by implementing USB selective suspend. Here is content for driver developers about how to implement selective suspend in USB drivers that are based on the Windows® Driver Foundation (WDF).</p></td>
</tr>
<tr class="odd">
<td><p>[USB Selective Suspend](usb-selective-suspend.md)</p></td>
<td><p>This section provides information about choosing the correct mechanism for the selective suspend feature.</p></td>
</tr>
<tr class="even">
<td><p>[How to Register a Composite Driver](register-a-composite-driver.md)</p></td>
<td><p>This topic describes how a driver of a USB multi-function device, called a composite driver, can register and unregister the composite device with the underlying USB driver stack. The Microsoft-provided driver, Usbccgp.sys, is the default composite driver that is loaded by Windows. The procedure in this topic applies to a custom Windows Driver Model (WDM)-based composite driver that replaces Usbccgp.sys.</p></td>
</tr>
<tr class="odd">
<td><p>[How to Implement Function Suspend for a Composite Driver](how-to--implement-remote-and-function-wake-support.md)</p></td>
<td><p>This topic provides an overview of function suspend and function remote wake-up features for Universal Serial Bus (USB) 3.0 multi-function devices (composite devices). In this topic you will learn about implementing those features in a driver that controls a composite device. The topic applies to composite drivers that replace Usbccgp.sys.</p></td>
</tr>
<tr class="even">
<td><p>[Remote Wakeup of USB Devices](remote-wakeup-of-usb-devices.md)</p></td>
<td><p>This topic describes best practices about implementing the remote wakeup capability in a client driver.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[USB Driver Development Guide](usb-driver-development-guide.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Implementing%20power%20management%20in%20USB%20client%20drivers%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


