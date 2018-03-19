---
title: HID drivers
author: windows-driver-content
description: This section introduces Human Interface Devices (or HID). Typically, these are devices that humans use to directly control the operation of computer systems.
ms.assetid: 19aefe5f-d82a-411f-86ab-5d1d53191524
keywords:
- pointing devices WDK
- input devices WDK
- Human Interface Devices WDK
- HID WDK
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# HID drivers


This section introduces Human Interface Devices (or HID). Typically, these are devices that humans use to directly control the operation of computer systems.

The definition of HID started as a device class over USB. The goal at that time was to define a replacement to PS/2 and create an interface over USB, allowing the creation of a generic driver for HID devices like keyboards, mice, and game controllers. Prior to HID, devices had to conform to strictly defined protocols for mice and keyboards. All hardware innovations necessitated overloading the use of data in an existing protocol, or the creation of non-standard hardware that needed its own drivers. The vision of HID started with finding a way for providing basic support for these “boot mode” devices in the operating system, but still allowing hardware vendors to provide differentiation with extensible, standardized and easily programmable interfaces.

Today, HID devices include: alphanumeric displays, barcode readers, volume controls on speakers/headsets, auxiliary displays, sensors, and MRI’s (yes, in hospitals). In addition, many hardware vendors use HID for their proprietary devices.

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
<td><p>[What's New in HID](what-s-new-in-hid.md)</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>[Introduction to HID Concepts](introduction-to-hid-concepts.md)</p></td>
<td><p>This section introduces Human Interface Devices (or HID). Typically, these are devices that humans use to directly control the operation of computer systems.</p></td>
</tr>
<tr class="odd">
<td><p>[HID Architecture](hid-architecture.md)</p></td>
<td><p>The architecture of the HID driver stack in Windows is built on the class driver named <em>hidclass.sys</em>.</p></td>
</tr>
<tr class="even">
<td><p>[HID Clients Supported in Windows](hid-clients-supported-in-windows.md)</p></td>
<td><p>Windows supports the following top-level collections:</p></td>
</tr>
<tr class="odd">
<td><p>[HID Transports Supported in Windows](hid-transports-supported-in-windows.md)</p></td>
<td><p>Windows supports the following transports.</p></td>
</tr>
<tr class="even">
<td><p>[HID Clients](hid-clients.md)</p></td>
<td><p>The HID Clients are drivers, services or applications that communicate using the HID API and often represent a specific type of device (for example: a sensor, a keyboard, or a mouse). They identify the device via a hardware ID or a specific HID Collection and communicate with the HID Collection via HID API.</p></td>
</tr>
<tr class="odd">
<td><p>[HID Transports](hid-transports.md)</p></td>
<td><p>Descriptions of HID transports supported in current and previous versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>[Non-HID legacy devices](non-hid-legacy-devices.md)</p></td>
<td><p>This section describes drivers, transports, and filter-drivers for non-HID keyboards and mice. These devices primarily run on the PS/2 transport.</p></td>
</tr>
</tbody>
</table>

 

 

 




