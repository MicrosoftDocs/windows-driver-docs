---
title: SIO_ADDRESS_LIST_CHANGE
description: SIO_ADDRESS_LIST_CHANGE
ms.assetid: d451208d-c850-4f2f-9ee0-d34139454ed4
ms.date: 08/08/2017
keywords: 
 -SIO_ADDRESS_LIST_CHANGE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# SIO\_ADDRESS\_LIST\_CHANGE


The SIO\_ADDRESS\_LIST\_CHANGE socket I/O control operation notifies a WSK application when there has been a change to the list of local transport addresses for a socket's address family. This socket I/O control operation applies to all socket types.

To be notified when there has been a change to the list of local transport addresses for a socket's address family, a WSK application calls the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function with the following parameters.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>RequestType</em></p></td>
<td><p><strong>WskIoctl</strong></p></td>
</tr>
<tr class="even">
<td><p><em>ControlCode</em></p></td>
<td><p>SIO_ADDRESS_LIST_CHANGE</p></td>
</tr>
<tr class="odd">
<td><p><em>Level</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>InputSize</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><em>InputBuffer</em></p></td>
<td><p>NULL</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSize</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><em>OutputBuffer</em></p></td>
<td><p>NULL</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSizeReturned</em></p></td>
<td><p>NULL</p></td>
</tr>
</tbody>
</table>

A WSK application must specify a pointer to an IRP when calling the **WskControlSocket** function to be notified of a change to the list of local transport addresses for a socket's address family. The WSK subsystem queues the IRP and returns STATUS\_PENDING. If a change is made to the list of local transport addresses for the socket's address family, the WSK subsystem completes the IRP. When the IRP's completion routine is called, the WSK application can use the [**SIO\_ADDRESS\_LIST\_QUERY**](sio-address-list-query.md) socket I/O control operation to query the new list of local transport addresses for the socket's address family.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ws2def.h (include Wsk.h)</td>
</tr>
</tbody>
</table>

 

 




