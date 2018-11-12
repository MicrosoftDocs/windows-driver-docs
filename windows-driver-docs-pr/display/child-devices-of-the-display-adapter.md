---
title: Child Devices of the Display Adapter
description: Child Devices of the Display Adapter
ms.assetid: 9fd20e1a-db98-4571-8fc4-6d33fd0e2f16
keywords:
- video present networks WDK display , display adapter child devices
- VidPN WDK display , display adapter child devices
- child devices WDK video present network
- display adapter child devices WDK video present network
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Child Devices of the Display Adapter


A child device of the display adapter is a device on the display adapter that is enumerated as a child by the display miniport driver. All child devices of the display adapter are on-board; monitors and other external devices that connect to the display adapter are not considered child devices.

The display miniport driver's [**DxgkDdiQueryChildRelations**](https://msdn.microsoft.com/library/windows/hardware/ff559750) function is responsible for enumerating child devices of the display adapter. During the enumeration, the display miniport driver assigns each child device a type and a hot-plug detection (HPD) awareness value. The type is one of the [**DXGK\_CHILD\_DEVICE\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff561008) enumerators:

-   **TypeVideoOutput**

-   **TypeOther**

The HPD awareness value is one of the [**DXGK\_CHILD\_DEVICE\_HPD\_AWARENESS**](https://msdn.microsoft.com/library/windows/hardware/ff561006) enumerators:

-   **HpdAwarenessAlwaysConnected**

-   **HpdAwarenessInterruptible**

-   **HpdAwarenessPolled**

The following table gives some examples of devices that have various types and HPD awareness values.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">HpdAwareness</th>
<th align="left">VideoOutput</th>
<th align="left">Other</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>AlwaysConnected</strong></p></td>
<td align="left"><p>Output for integrated LCD panel on a desktop computer</p></td>
<td align="left"><p>TV tuner</p>
<p>cross bar switch</p>
<p>MPEG2 codec</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Interruptible</strong></p></td>
<td align="left"><p>DVI</p>
<p>HDMI</p>
<p>Output for integrated LCD panel on a portable computer</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Polled</strong></p></td>
<td align="left"><p>S-video</p>
<p>HD15</p></td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

The operating system uses one of several strategies, depending on the HPD awareness value, to determine whether an external device is connected to a child device. The following table briefly describes how the operating system determines the connection status of devices with various HPD awareness values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">HpdAwareness</th>
<th align="left">How operating system determines connection status</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>AlwaysConnected</p></td>
<td align="left"><p>The operating system knows the child device is always present. No external device is ever connected to or disconnected from the child device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Interruptible</p></td>
<td align="left"><p>The operating system is notified when an external display device is connected to or disconnected from the child device. (The display panel on a portable computer is considered connected when the lid is open and disconnected when the lid is closed.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Polled</p></td>
<td align="left"><p>The operating system asks whether an external display device is connected to the child device.</p></td>
</tr>
</tbody>
</table>

 

 

 





