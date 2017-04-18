---
title: HID Clients
author: windows-driver-content
description: The HID Clients are drivers, services or applications that communicate using the HID API and often represent a specific type of device (for example a sensor, a keyboard, or a mouse).
ms.assetid: C97E1F63-0CA5-42F3-A139-48E830F2E2B7
keywords: ["HID clients", "drivers", "services", "HID API", "HID Collection"]
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20HID%20Clients%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


