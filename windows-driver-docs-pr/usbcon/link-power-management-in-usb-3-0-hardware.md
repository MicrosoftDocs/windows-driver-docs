---
Description: This section provides information about certain limitations of the Universal Serial Bus (USB) 2.0 Selective Suspend mechanism.
title: Link power management in USB 3.0 hardware
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td><p>[Limitations of USB 2.0 Mechanism](limitations-of-usb-2-0-mechanism.md)</p></td>
<td><p>Describes the limitations of the Universal Serial Bus (USB) 2.0 Selective Suspend mechanism. It then provides an overview of the USB 3.0 Link Power Management (LPM) feature and how it can be used in conjunction with the Selective Suspend mechanism to reduce system power consumption. Finally, it lists the common pitfalls in LPM implementation in USB controllers, hubs, and devices.</p></td>
</tr>
<tr class="even">
<td><p>[USB 3.0 LPM Mechanism](usb-3-0-lpm-mechanism-.md)</p></td>
<td><p>This topic describes the USB 3.0 LPM mechanism.</p>
<p>There is an addendum to the official [USB 2.0 Specification](http://go.microsoft.com/fwlink/p/?linkid=230961) (USB2_LinkPowerMangement_ECN), which defines LPM for newer USB 2.0 hardware. This topic does not cover that USB 2.0 LPM mechanism. The purpose of this topic is to describe USB 3.0 LPM states, specifically U1 and U2.</p></td>
</tr>
<tr class="odd">
<td><p>[U1 and U2 Transitions](u1-and-u2-transitions.md)</p></td>
<td><p>This topic first describes the initial setup that is done by the software to enable U1 and U2 transitions, and then describes how these transitions occur in the hardware.</p></td>
</tr>
<tr class="even">
<td><p>[Common Hardware Problems with U1 or U2 Implementation](common-hardware-problems-with-u1-or-u2-implementation.md)</p></td>
<td><p>This topic discusses the LPM mechanism for saving power and described various common problems seen in current USB 3.0 hardware. USB-IF certification requires that devices, hubs, and controllers implement U1 and U2 correctly. The certification aims at enforcing that requirement through compliance tests. The Microsoft USB driver stack (included with Windows 8) takes full advantage of the U1 and U2 mechanism to achieve maximum power savings. Therefore problems such as those described in this topic will be seen more frequently. Those problems can lead to poor user experience and might prevent Windows from achieving the power savings offered by the USB 3.0 specification.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[Building USB devices for Windows](building-usb-devices-for-windows.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Link%20power%20management%20in%20USB%203.0%20hardware%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


