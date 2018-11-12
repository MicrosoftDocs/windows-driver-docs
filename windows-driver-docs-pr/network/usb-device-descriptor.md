---
title: USB Device Descriptor
description: USB Device Descriptor
ms.assetid: ef2a3e43-0e55-4e8e-ad86-efcbe153c847
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB Device Descriptor





The device returns a USB Device Descriptor as defined in the USB Specification. The following table defines the prominent fields of the USB Device Descriptor.

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
<td align="left"><p>4</p></td>
<td align="left"><p>bDeviceClass</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>02h</p></td>
<td align="left"><p>Communication Device Class code.</p></td>
</tr>
<tr class="even">
<td align="left"><p>5</p></td>
<td align="left"><p>bDeviceSubClass</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>00h</p></td>
<td align="left"><p>Communication Device Subclass code, unused at this time.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>6</p></td>
<td align="left"><p>bDeviceProtocol</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>00h</p></td>
<td align="left"><p>Communication Device Protocol code, unused at this time.</p></td>
</tr>
</tbody>
</table>

 

 

 





