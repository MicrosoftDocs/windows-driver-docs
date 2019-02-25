---
title: Control Channel Characteristics
description: Control Channel Characteristics
ms.assetid: b289f21c-a53e-424c-be31-b7a869e335c4
keywords:
- Control Channel Characteristics
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Control Channel Characteristics





The Control channel for the device is its USB Control endpoint. A control message from the host to the device is sent as a SEND\_ENCAPSULATED\_COMMAND transfer. This transfer is defined in the following table.

<table style="width:100%;">
<colgroup>
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">BmRequestType</th>
<th align="left">bRequest</th>
<th align="left">wValue</th>
<th align="left">wIndex</th>
<th align="left">wLength</th>
<th align="left">Data</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x21</p></td>
<td align="left"><p>0x00</p></td>
<td align="left"><p>0x0000</p></td>
<td align="left"><p><em>bInterfaceNumber</em> field of Communication Class interface descriptor</p></td>
<td align="left"><p>Byte length of control message block</p></td>
<td align="left"><p>Control message block</p></td>
</tr>
</tbody>
</table>

 

The host does not continuously poll the USB Control endpoint for input control messages. Upon placing a control message on its Control endpoint, the device must return a notification on the Communication Class interface's Interrupt IN endpoint, which is polled by the host whenever the device can return control messages. The transfer from the device's interrupt IN endpoint to the host is a standard USB Interrupt IN transfer. The only defined device notification is the RESPONSE\_AVAILABLE notification, defined in the following table.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Offset (bytes)</th>
<th align="left">Length (bytes)</th>
<th align="left">Field</th>
<th align="left">Data</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>Notification</p></td>
<td align="left"><p>RESPONSE_AVAILABLE (0x00000001)</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>0</p></td>
</tr>
</tbody>
</table>

 

Upon receiving the RESPONSE\_AVAILABLE notification, the host reads the control message from the Control endpoint using a GET\_ENCAPSULATED\_RESPONSE transfer, defined in the following table.

<table style="width:100%;">
<colgroup>
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">bmRequestType</th>
<th align="left">bRequest</th>
<th align="left">wValue</th>
<th align="left">wIndex</th>
<th align="left">wLength</th>
<th align="left">Data</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0xA1</p></td>
<td align="left"><p>0x01</p></td>
<td align="left"><p>0x0000</p></td>
<td align="left"><p><em>bInterfaceNumber</em> field of Communication Class interface descriptor</p></td>
<td align="left"><p>0x0400 (this is the minimum byte length of the buffer posted by host)</p></td>
<td align="left"><p>Control message block</p></td>
</tr>
</tbody>
</table>

 

If for some reason the device receives a GET\_ENCAPSULATED\_RESPONSE and is unable to respond with a valid data on the Control endpoint, then it should return a one-byte packet set to 0x00, rather than stalling the Control endpoint.

 

 





