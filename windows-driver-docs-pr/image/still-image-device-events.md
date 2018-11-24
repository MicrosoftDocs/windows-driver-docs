---
title: Still Image Device Events
description: Still Image Device Events
ms.assetid: 5f9be89c-8442-4894-b2f6-a4d3558464bf
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Still Image Device Events





A *still image device event* is a device-level occurrence that upper-level software should be notified about, if that software has requested such notification. The user-mode minidriver is responsible for defining most device events and delivering notifications when an event occurs. In general, events indicate that upper-level software is going to be required to perform some action.

A typical still image device event is the detection of a push button being pressed. For example, a scanner might provide a user with separate buttons to initiate scanning text and photographs. When a button is pressed, upper-level software will be needed in order to display or store the image. The still image event monitor detects that the event has occurred (using the [IStiDevice COM interface](istidevice-com-interface.md)) and can call a still image application that was previously registered (using the [IStillImage COM interface](istillimage-com-interface.md)).

Still image device events are represented by GUIDs. In *sti.h*, Microsoft defines the following still image device events:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Event GUID</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>GUID_DeviceArrivedLaunch</strong></p></td>
<td><p>A still image device has just been attached to the system.</p></td>
</tr>
<tr class="even">
<td><p><strong>GUID_ScanImage</strong></p></td>
<td><p>An image should be scanned into the computer.</p></td>
</tr>
<tr class="odd">
<td><p><strong>GUID_ScanFaxImage</strong></p></td>
<td><p>An image should be scanned into the computer and then faxed.</p></td>
</tr>
<tr class="even">
<td><p><strong>GUID_ScanPrintImage</strong></p></td>
<td><p>An image should be scanned into the computer and then printed.</p></td>
</tr>
<tr class="odd">
<td><p><strong>GUID_STIUserDefined1</strong></p></td>
<td><p>A user-definable button has been pressed.</p></td>
</tr>
<tr class="even">
<td><p><strong>GUID_STIUserDefined2</strong></p></td>
<td><p>A user-definable button has been pressed.</p></td>
</tr>
<tr class="odd">
<td><p><strong>GUID_STIUserDefined3</strong></p></td>
<td><p>A user-definable button has been pressed.</p></td>
</tr>
</tbody>
</table>

 

Developers of user-mode minidrivers should use these predefined event GUIDs whenever possible. If these GUIDs are not appropriate, GUIDs for device-specific events must be defined.

To define a still image device event, you must:

-   Specify a GUID for each event.

-   Include each GUID in the user-mode driver's INF file.

Within the driver's INF file, each GUID specification must include either an asterisk (meaning "all applications") or a list of specific applications, indicating which applications should be started when the event occurs. The still image event monitor uses this list to provide default assignments of applications to events. The user can modify these assignments with the Scanners and Cameras Control Panel.

### Event Notification

The driver must monitor the device (using either asynchronous I/O or polling) to determine when the event associated with each GUID occurs. Depending on device capabilities, the driver can notify clients of the occurrence of device events either asynchronously or by responding to a request to poll the device. All drivers that are capable of delivering notification of device events (by either method) must set the STI\_GENCAP\_NOTIFICATIONS flag in the device's [**STI\_DEV\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff548380) structure. Drivers that support polling, and not asynchronous notification, must also set the STI\_GENCAP\_POLLING\_NEEDED flag in the same structure. (These capabilities must also be indicated using the **Capabilities** keyword in [INF files for still image devices](inf-files-for-still-image-devices.md).)

If a driver supports asynchronous notification of events, the event monitor calls [**IStiUSD::SetNotificationHandle**](https://msdn.microsoft.com/library/windows/hardware/ff543840) to request notifications and to supply an event handle. When a device event occurs, the driver must notify the event monitor by calling **SetEvent** (see the Microsoft Windows SDK documentation), using the event handle as an argument. The client can then call [**IStiUSD::GetNotificationData**](https://msdn.microsoft.com/library/windows/hardware/ff543821) to obtain the event's GUID.

If polling is required, the event monitor calls [**IStiUSD::GetStatus**](https://msdn.microsoft.com/library/windows/hardware/ff543823) to poll the driver, which must in turn poll the device and return results in an [**STI\_DEVICE\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff548369) structure.

 

 




