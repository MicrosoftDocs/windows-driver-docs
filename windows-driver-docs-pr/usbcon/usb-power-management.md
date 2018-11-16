---
Description: The topics in this section examine the ways in which the WDM power model interacts with the power management properties of USB devices.
title: Implementing power management in USB client drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td><p><a href="comparing-usb-device-states-to-wdm-device-states.md" data-raw-source="[USB Device Power States](comparing-usb-device-states-to-wdm-device-states.md)">USB Device Power States</a></p></td>
<td><p>This topic describes the WDM device states to use for USB device power states as specified in section 9.1 of the Universal Serial Bus 2.0 specification.</p></td>
</tr>
<tr class="even">
<td><p><a href="selective-suspend-in-usb-drivers-wdf.md" data-raw-source="[Selective suspend in USB drivers (WDF)](selective-suspend-in-usb-drivers-wdf.md)">Selective suspend in USB drivers (WDF)</a></p></td>
<td><p>A USB function driver supports runtime idle detection by implementing USB selective suspend. Here is content for driver developers about how to implement selective suspend in USB drivers that are based on the Windows® Driver Foundation (WDF).</p></td>
</tr>
<tr class="odd">
<td><p><a href="usb-selective-suspend.md" data-raw-source="[USB Selective Suspend](usb-selective-suspend.md)">USB Selective Suspend</a></p></td>
<td><p>This section provides information about choosing the correct mechanism for the selective suspend feature.</p></td>
</tr>
<tr class="even">
<td><p><a href="register-a-composite-driver.md" data-raw-source="[How to Register a Composite Driver](register-a-composite-driver.md)">How to Register a Composite Driver</a></p></td>
<td><p>This topic describes how a driver of a USB multi-function device, called a composite driver, can register and unregister the composite device with the underlying USB driver stack. The Microsoft-provided driver, Usbccgp.sys, is the default composite driver that is loaded by Windows. The procedure in this topic applies to a custom Windows Driver Model (WDM)-based composite driver that replaces Usbccgp.sys.</p></td>
</tr>
<tr class="odd">
<td><p><a href="how-to--implement-remote-and-function-wake-support.md" data-raw-source="[How to Implement Function Suspend for a Composite Driver](how-to--implement-remote-and-function-wake-support.md)">How to Implement Function Suspend for a Composite Driver</a></p></td>
<td><p>This topic provides an overview of function suspend and function remote wake-up features for Universal Serial Bus (USB) 3.0 multi-function devices (composite devices). In this topic you will learn about implementing those features in a driver that controls a composite device. The topic applies to composite drivers that replace Usbccgp.sys.</p></td>
</tr>
<tr class="even">
<td><p><a href="remote-wakeup-of-usb-devices.md" data-raw-source="[Remote Wakeup of USB Devices](remote-wakeup-of-usb-devices.md)">Remote Wakeup of USB Devices</a></p></td>
<td><p>This topic describes best practices about implementing the remote wakeup capability in a client driver.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[USB Driver Development Guide](usb-driver-development-guide.md)  



