---
title: Protocol Implementation
description: Windows Precision Touchpads are expected to use the Human Interface Device (HID) protocol to communicate with the host. This topic describes how to implement the HID protocol for Windows Precision Touchpads.
ms.assetid: CCF82524-E64C-4A86-AB30-FFB07C64D03A
---

#  Protocol Implementation


Windows Precision Touchpads are expected to use the Human Interface Device (HID) protocol to communicate with the host. This topic describes how to implement the HID protocol for Windows Precision Touchpads.

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[Required HID Descriptors](windows-precision-touchpad-required-hid-descriptors.md)</p></td>
<td align="left"><p>This topic describes required Human Interface Devices (HID) descriptors for the Windows Precision Touchpad HID protocol implementation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Required HID Top-Level Collections](windows-precision-touchpad-required-hid-top-level-collections.md)</p></td>
<td align="left"><p>A Windows Precision Touchpad device shall expose 3 mandatory top-level collections; Windows Precision Touchpad, Mouse and Configuration. An optional (recommended) collection for firmware update can also be implemented.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Sample Report Descriptors](windows-precision-touchpad-sample-report-descriptors.md)</p></td>
<td align="left"><p>This topic provides sample report descriptors.</p></td>
</tr>
</tbody>
</table>

 

Before you read this document, you must have a good understanding of the HID protocol. The following documents include information about the protocol:

-   [Device Class Definition for Human Interface Devices (HID) Version 1.11](http://www.usb.org/developers/hidpage/HID1_11.pdf)

-   [HID Usage Tables](http://www.usb.org/developers/hidpage/Hut1_12v2.pdf)

-   [HID Over I2C Protocol Specification Version 1.0](http://msdn.microsoft.com/library/windows/hardware/hh852380)

Windows includes a HID class driver and corresponding HID I²C and HID USB miniport drivers; therefore, there is no need or allowance for any third-party drivers for Windows Precision Touchpads. You only need to report the usages that are described in this topic in the firmware for your Windows Precision Touchpad. Windows will use your firmware and its own HID drivers to enable mouse and gesture capabilities for your device and furnish Windows applications with access to your device.

A sample descriptor is included in [Windows Precision Touchpad Sample Report Descriptors](windows-precision-touchpad-sample-report-descriptors.md).

 

 




