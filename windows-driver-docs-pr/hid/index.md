---
title: HID drivers
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


This section introduces Human Interface Devices (or HID). For more information about HID concepts, see the official [HID specification](http://www.usb.org/developers/hidpage/HID1_11.pdf). 

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
<td><p><a href="what-s-new-in-hid.md" data-raw-source="[What&#39;s New in HID](what-s-new-in-hid.md)">What&#39;s New in HID</a></p></td>
<td></td>
</tr>
<tr class="even">
<td><p><a href="introduction-to-hid-concepts.md" data-raw-source="[Introduction to HID Concepts](introduction-to-hid-concepts.md)">Introduction to HID Concepts</a></p></td>
<td><p>This section introduces Human Interface Devices (or HID). Typically, these are devices that humans use to directly control the operation of computer systems.</p></td>
</tr>
<tr class="odd">
<td><p><a href="hid-architecture.md" data-raw-source="[HID Architecture](hid-architecture.md)">HID Architecture</a></p></td>
<td><p>The architecture of the HID driver stack in Windows is built on the class driver named <em>hidclass.sys</em>.</p></td>
</tr>
<tr class="even">
<td><p><a href="hid-clients-supported-in-windows.md" data-raw-source="[HID Clients Supported in Windows](hid-clients-supported-in-windows.md)">HID Clients Supported in Windows</a></p></td>
<td><p>Windows supports the following top-level collections:</p></td>
</tr>
<tr class="odd">
<td><p><a href="hid-transports-supported-in-windows.md" data-raw-source="[HID Transports Supported in Windows](hid-transports-supported-in-windows.md)">HID Transports Supported in Windows</a></p></td>
<td><p>Windows supports the following transports.</p></td>
</tr>
<tr class="even">
<td><p><a href="hid-clients.md" data-raw-source="[HID Clients](hid-clients.md)">HID Clients</a></p></td>
<td><p>The HID Clients are drivers, services or applications that communicate using the HID API and often represent a specific type of device (for example: a sensor, a keyboard, or a mouse). They identify the device via a hardware ID or a specific HID Collection and communicate with the HID Collection via HID API.</p></td>
</tr>
<tr class="odd">
<td><p><a href="hid-transports.md" data-raw-source="[HID Transports](hid-transports.md)">HID Transports</a></p></td>
<td><p>Descriptions of HID transports supported in current and previous versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p><a href="non-hid-legacy-devices.md" data-raw-source="[Non-HID legacy devices](non-hid-legacy-devices.md)">Non-HID legacy devices</a></p></td>
<td><p>This section describes drivers, transports, and filter-drivers for non-HID keyboards and mice. These devices primarily run on the PS/2 transport.</p></td>
</tr>
</tbody>
</table>

 

 

 




