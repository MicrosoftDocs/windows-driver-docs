---
title: HID Clients
author: windows-driver-content
description: The HID Clients are drivers, services or applications that communicate using the HID API and often represent a specific type of device (for example a sensor, a keyboard, or a mouse).
ms.assetid: C97E1F63-0CA5-42F3-A139-48E830F2E2B7
keywords:
- HID clients
- drivers
- services
- HID API
- HID Collection
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# HID Clients


The HID Clients are drivers, services or applications that communicate using the HID API and often represent a specific type of device (for example: a sensor, a keyboard, or a mouse). They identify the device via a hardware ID or a specific HID Collection and communicate with the HID Collection via HID API.

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
<td><p>[HID Usages](hid-usages.md)</p></td>
<td><p><em>HID usages</em> identify the intended use of HID controls and what the controls actually measure.</p></td>
</tr>
<tr class="even">
<td><p>[HID Collections](hid-collections.md)</p></td>
<td><p>A <em>HID collection</em> is a meaningful grouping of HID controls and their respective [HID usages](hid-usages.md).</p></td>
</tr>
<tr class="odd">
<td><p>[Opening HID collections](opening-hid-collections.md)</p></td>
<td><p>This section describes how a HID Client can communicate with the HID Class driver (HIDClass) to operate the device’s HID collections.</p></td>
</tr>
<tr class="even">
<td><p>[Handling HID Reports](handling-hid-reports.md)</p></td>
<td><p>This section describes the mechanisms that user-mode applications and kernel-mode drivers use for handling [HID reports](introduction-to-hid-concepts.md).</p></td>
</tr>
<tr class="odd">
<td><p>[Freeing Resources](freeing-resources.md)</p></td>
<td><p>User-mode applications and kernel-mode drivers that are HID clients should always free any resources that are no longer required.</p></td>
</tr>
<tr class="even">
<td><p>[Installing HID clients](installing-hid-clients.md)</p></td>
<td><p>This section describes the following requirements for installing HIDClass devices in Microsoft Windows.</p></td>
</tr>
<tr class="odd">
<td><p>[HIDClass Hardware IDs for Top-Level Collections](hidclass-hardware-ids-for-top-level-collections.md)</p></td>
<td><p>This section specifies the hardware IDs that the HID class driver generates for top-level collections.</p></td>
</tr>
<tr class="even">
<td><p>[Keyboard and mouse HID client drivers](keyboard-and-mouse-hid-client-drivers.md)</p></td>
<td><p>This topic discusses keyboard and mouse HID client drivers. Keyboards and mice represent the first set of HID clients that were standardized in the HID Usage tables and implemented in Windows operating systems.</p></td>
</tr>
<tr class="odd">
<td><p>[Sensor HID class driver](sensor-hid-class-driver.md)</p></td>
<td><p>Starting with Windows 8, the Windows operating system includes an in-box sensor HID Class driver (SensorsHIDClassDriver.dll), that supports eleven types of sensors that communicate using the HID transport.</p></td>
</tr>
<tr class="even">
<td><p>[Airplane mode radio management](airplane-mode-radio-management.md)</p></td>
<td><p>Starting with Windows 8, the Windows operating system provides support via HID, for airplane mode radio management controls.</p></td>
</tr>
<tr class="odd">
<td><p>[Display brightness control](display-brightness-control.md)</p></td>
<td><p>Starting with Windows 8, a standardized solution has been added to allow keyboards (external or embedded on laptops), to control a laptop’s or tablet’s screen brightness through HID.</p></td>
</tr>
</tbody>
</table>

 

 

 




