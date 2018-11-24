---
Description: This section provides information about certain limitations of the Universal Serial Bus (USB) 2.0 Selective Suspend mechanism.
title: Link power management in USB 3.0 hardware
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Link power management in USB 3.0 hardware


This section provides information about certain limitations of the Universal Serial Bus (USB) 2.0 Selective Suspend mechanism. It provides guidelines for independent hardware vendors (IHVs) and original equipment manufacturers (OEMs) to implement power management for USB devices by using Link Power Management (LPM) in conjunction with Selective Suspend. It also provides information about common pitfalls in LPM implementation in USB controllers, hubs, and devices. This information applies to Windows 8 and later versions.

This section assumes that the reader is familiar with the following:

-   The official [USB 3.0 specification](http://www.usb.org/developers/docs/).
-   The [USB Selective Suspend](http://go.microsoft.com/fwlink/p/?linkid=230964) mechanism. The mechanism is described in the blog post, [Demystifying USB Selective Suspend](http://go.microsoft.com/fwlink/p/?linkid=230962).

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
<td><p><a href="limitations-of-usb-2-0-mechanism.md" data-raw-source="[Limitations of USB 2.0 Mechanism](limitations-of-usb-2-0-mechanism.md)">Limitations of USB 2.0 Mechanism</a></p></td>
<td><p>Describes the limitations of the Universal Serial Bus (USB) 2.0 Selective Suspend mechanism. It then provides an overview of the USB 3.0 Link Power Management (LPM) feature and how it can be used in conjunction with the Selective Suspend mechanism to reduce system power consumption. Finally, it lists the common pitfalls in LPM implementation in USB controllers, hubs, and devices.</p></td>
</tr>
<tr class="even">
<td><p><a href="usb-3-0-lpm-mechanism-.md" data-raw-source="[USB 3.0 LPM Mechanism](usb-3-0-lpm-mechanism-.md)">USB 3.0 LPM Mechanism</a></p></td>
<td><p>This topic describes the USB 3.0 LPM mechanism.</p>
<p>There is an addendum to the official <a href="http://go.microsoft.com/fwlink/p/?linkid=230961" data-raw-source="[USB 2.0 Specification](http://go.microsoft.com/fwlink/p/?linkid=230961)">USB 2.0 Specification</a> (USB2_LinkPowerMangement_ECN), which defines LPM for newer USB 2.0 hardware. This topic does not cover that USB 2.0 LPM mechanism. The purpose of this topic is to describe USB 3.0 LPM states, specifically U1 and U2.</p></td>
</tr>
<tr class="odd">
<td><p><a href="u1-and-u2-transitions.md" data-raw-source="[U1 and U2 Transitions](u1-and-u2-transitions.md)">U1 and U2 Transitions</a></p></td>
<td><p>This topic first describes the initial setup that is done by the software to enable U1 and U2 transitions, and then describes how these transitions occur in the hardware.</p></td>
</tr>
<tr class="even">
<td><p><a href="common-hardware-problems-with-u1-or-u2-implementation.md" data-raw-source="[Common Hardware Problems with U1 or U2 Implementation](common-hardware-problems-with-u1-or-u2-implementation.md)">Common Hardware Problems with U1 or U2 Implementation</a></p></td>
<td><p>This topic discusses the LPM mechanism for saving power and described various common problems seen in current USB 3.0 hardware. USB-IF certification requires that devices, hubs, and controllers implement U1 and U2 correctly. The certification aims at enforcing that requirement through compliance tests. The Microsoft USB driver stack (included with Windows 8) takes full advantage of the U1 and U2 mechanism to achieve maximum power savings. Therefore problems such as those described in this topic will be seen more frequently. Those problems can lead to poor user experience and might prevent Windows from achieving the power savings offered by the USB 3.0 specification.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[Building USB devices for Windows](building-usb-devices-for-windows.md)  



