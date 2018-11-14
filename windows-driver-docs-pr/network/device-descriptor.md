---
title: Device Descriptor
description: Device Descriptor
ms.assetid: 5c533053-6a4e-4c28-a87d-562791298d5c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Descriptor





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
<th align="left">Offset</th>
<th align="left">Field</th>
<th align="left">Size</th>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>bLength</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x12</p></td>
<td align="left"><p>Size of this descriptor, in bytes</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>bDescriptorType</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x01</p></td>
<td align="left"><p>DEVICE descriptor</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>bcdUSB</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>0x0110</p></td>
<td align="left"><p>1.1 - current revision of USB spec</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>bDeviceClass</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x02</p></td>
<td align="left"><p>Communication Device Class</p></td>
</tr>
<tr class="odd">
<td align="left"><p>5</p></td>
<td align="left"><p>bDeviceSubClass</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x00</p></td>
<td align="left"><p>Unused</p></td>
</tr>
<tr class="even">
<td align="left"><p>6</p></td>
<td align="left"><p>bDeviceProtocol</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x00</p></td>
<td align="left"><p>Unused</p></td>
</tr>
<tr class="odd">
<td align="left"><p>7</p></td>
<td align="left"><p>bMaxPacketSize0</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x08</p></td>
<td align="left"><p>Max packet size on control pipe</p></td>
</tr>
<tr class="even">
<td align="left"><p>8</p></td>
<td align="left"><p>idVendor</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>0xXXXX</p></td>
<td align="left"><p>Vendor ID</p></td>
</tr>
<tr class="odd">
<td align="left"><p>10</p></td>
<td align="left"><p>idProduct</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>0xXXXX</p></td>
<td align="left"><p>Product ID</p></td>
</tr>
<tr class="even">
<td align="left"><p>12</p></td>
<td align="left"><p>bcdDevice</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>0xXXXX</p></td>
<td align="left"><p>Device Release Code</p></td>
</tr>
<tr class="odd">
<td align="left"><p>14</p></td>
<td align="left"><p>iManufacturer</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x01</p></td>
<td align="left"><p>Index of manufacturer string</p></td>
</tr>
<tr class="even">
<td align="left"><p>15</p></td>
<td align="left"><p>iProduct</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x02</p></td>
<td align="left"><p>Index of product string</p></td>
</tr>
<tr class="odd">
<td align="left"><p>16</p></td>
<td align="left"><p>iSerialNumber</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x03</p></td>
<td align="left"><p>Index of device serial number string</p></td>
</tr>
<tr class="even">
<td align="left"><p>17</p></td>
<td align="left"><p>bNumConfigurations</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x01</p></td>
<td align="left"><p>One configuration</p></td>
</tr>
</tbody>
</table>

 

 

 





