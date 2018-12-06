---
title: Communication Class Interface
description: Communication Class Interface
ms.assetid: b0414d0e-6e1b-4d84-8ca4-40a59fb1b099
keywords:
- communication
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Communication Class Interface





The Communication Class interface is described by a USB interface descriptor, three class-specific descriptors, and an endpoint descriptor for the notification endpoint. The notification endpoint descriptor is a standard USB Interrupt-type IN endpoint descriptor whose **wMaxPacketSize** field is 8 bytes. The following table defines the prominent fields of the Communication Class interface descriptor.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Offset (bytes)</th>
<th align="left">Field</th>
<th align="left">Size (bytes)</th>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>5</p></td>
<td align="left"><p>bInterfaceClass</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>02h</p></td>
<td align="left"><p>Communication Interface Class code.</p></td>
</tr>
<tr class="even">
<td align="left"><p>6</p></td>
<td align="left"><p>bInterfaceSubClass</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>02h</p></td>
<td align="left"><p>Communication Interface Class SubClass code for Abstract Control Model.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>7</p></td>
<td align="left"><p>bInterfaceProtocol</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>FFh</p></td>
<td align="left"><p>Communication Interface Class Protocol code for vendor specific protocol.</p></td>
</tr>
</tbody>
</table>

 

 

 





