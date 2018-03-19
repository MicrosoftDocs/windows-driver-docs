---
Description: You can view USB ETW event traces using Microsoft Network Monitor, also referred to as Netmon.
title: USB ETW traces in Netmon
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# USB ETW traces in Netmon


You can view USB ETW event traces using Microsoft Network Monitor, also referred to as Netmon. Netmon does not parse the trace automatically. It requires USB ETW parsers. USB ETW parsers are text files, written in Network Monitor Parser Language (NPL), that describe the structure of USB ETW event traces. The parsers also define USB-specific columns and filters. These parsers make Netmon the best tool for analyzing USB ETW traces.

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
<td><p>[How to install Netmon and USB ETW Parsers](how-to-install-netmon-and-the-netmon-usb-parser.md)</p></td>
<td><p>This topic provides installation information about Netmon and the USB ETW parsers.</p></td>
</tr>
<tr class="even">
<td><p>[How to view a USB ETW trace in Netmon](how-to-examining-a-trace-file-by-using-netmon.md)</p></td>
<td><p>This topic describes how to example a event trace file by using Netmon.</p></td>
</tr>
<tr class="odd">
<td><p>[Debugging USB device issues by using ETW events](best-practices--debugging-usb-device-problems.md)</p></td>
<td><p>This topic provides tips for debugging USB device problems by using ETW events.</p></td>
</tr>
<tr class="even">
<td><p>[Case Study: Troubleshooting an unknown USB device by using ETW and Netmon](case-study--troubleshooting-an-unknown-usb-device-by-using-etw-and-netmon.md)</p></td>
<td><p>This topic provides an example of how to use USB ETW and Netmon to troubleshoot a USB device that Windows does not recognize.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[USB Event Tracing for Windows](usb-event-tracing-for-windows.md)  



