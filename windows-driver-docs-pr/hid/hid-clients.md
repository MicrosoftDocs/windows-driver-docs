---
title: HID Clients
description: The HID Clients are drivers, services or applications that communicate using the HID API and often represent a specific type of device (for example a sensor, a keyboard, or a mouse).
ms.assetid: C97E1F63-0CA5-42F3-A139-48E830F2E2B7
keywords:
- HID clients
- drivers
- services
- HID API
- HID Collection
ms.date: 04/20/2017
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
<td><p><a href="hid-usages.md" data-raw-source="[HID Usages](hid-usages.md)">HID Usages</a></p></td>
<td><p><em>HID usages</em> identify the intended use of HID controls and what the controls actually measure.</p></td>
</tr>
<tr class="even">
<td><p><a href="hid-collections.md" data-raw-source="[HID Collections](hid-collections.md)">HID Collections</a></p></td>
<td><p>A <em>HID collection</em> is a meaningful grouping of HID controls and their respective <a href="hid-usages.md" data-raw-source="[HID usages](hid-usages.md)">HID usages</a>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="opening-hid-collections.md" data-raw-source="[Opening HID collections](opening-hid-collections.md)">Opening HID collections</a></p></td>
<td><p>This section describes how a HID Client can communicate with the HID Class driver (HIDClass) to operate the device’s HID collections.</p></td>
</tr>
<tr class="even">
<td><p><a href="handling-hid-reports.md" data-raw-source="[Handling HID Reports](handling-hid-reports.md)">Handling HID Reports</a></p></td>
<td><p>This section describes the mechanisms that user-mode applications and kernel-mode drivers use for handling <a href="introduction-to-hid-concepts.md" data-raw-source="[HID reports](introduction-to-hid-concepts.md)">HID reports</a>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="freeing-resources.md" data-raw-source="[Freeing Resources](freeing-resources.md)">Freeing Resources</a></p></td>
<td><p>User-mode applications and kernel-mode drivers that are HID clients should always free any resources that are no longer required.</p></td>
</tr>
<tr class="even">
<td><p><a href="installing-hid-clients.md" data-raw-source="[Installing HID clients](installing-hid-clients.md)">Installing HID clients</a></p></td>
<td><p>This section describes the following requirements for installing HIDClass devices in Microsoft Windows.</p></td>
</tr>
<tr class="odd">
<td><p><a href="hidclass-hardware-ids-for-top-level-collections.md" data-raw-source="[HIDClass Hardware IDs for Top-Level Collections](hidclass-hardware-ids-for-top-level-collections.md)">HIDClass Hardware IDs for Top-Level Collections</a></p></td>
<td><p>This section specifies the hardware IDs that the HID class driver generates for top-level collections.</p></td>
</tr>
<tr class="even">
<td><p><a href="keyboard-and-mouse-hid-client-drivers.md" data-raw-source="[Keyboard and mouse HID client drivers](keyboard-and-mouse-hid-client-drivers.md)">Keyboard and mouse HID client drivers</a></p></td>
<td><p>This topic discusses keyboard and mouse HID client drivers. Keyboards and mice represent the first set of HID clients that were standardized in the HID Usage tables and implemented in Windows operating systems.</p></td>
</tr>
<tr class="odd">
<td><p><a href="sensor-hid-class-driver.md" data-raw-source="[Sensor HID class driver](sensor-hid-class-driver.md)">Sensor HID class driver</a></p></td>
<td><p>Starting with Windows 8, the Windows operating system includes an in-box sensor HID Class driver (SensorsHIDClassDriver.dll), that supports eleven types of sensors that communicate using the HID transport.</p></td>
</tr>
<tr class="even">
<td><p><a href="airplane-mode-radio-management.md" data-raw-source="[Airplane mode radio management](airplane-mode-radio-management.md)">Airplane mode radio management</a></p></td>
<td><p>Starting with Windows 8, the Windows operating system provides support via HID, for airplane mode radio management controls.</p></td>
</tr>
<tr class="odd">
<td><p><a href="display-brightness-control.md" data-raw-source="[Display brightness control](display-brightness-control.md)">Display brightness control</a></p></td>
<td><p>Starting with Windows 8, a standardized solution has been added to allow keyboards (external or embedded on laptops), to control a laptop’s or tablet’s screen brightness through HID.</p></td>
</tr>
</tbody>
</table>

 

 

 




