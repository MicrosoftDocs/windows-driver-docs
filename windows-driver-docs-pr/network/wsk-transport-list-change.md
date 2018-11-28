---
title: WSK_TRANSPORT_LIST_CHANGE
description: WSK_TRANSPORT_LIST_CHANGE
ms.assetid: 3b12d692-467c-4d31-bd2a-bb6e34d87fde
ms.date: 07/18/2017
keywords:
 - WSK_TRANSPORT_LIST_CHANGE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WSK\_TRANSPORT\_LIST\_CHANGE


A WSK application uses the WSK\_TRANSPORT\_LIST\_CHANGE client control operation to receive notification if the list of available network transports changes.

To receive notification of when the list of available network transports changes, a WSK application calls the [**WskControlClient**](https://msdn.microsoft.com/library/windows/hardware/ff571126) function with the following parameters.

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
<td><p><em>ControlCode</em></p></td>
<td><p>WSK_TRANSPORT_LIST_CHANGE</p></td>
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
<tr class="odd">
<td><p><em>Irp</em></p></td>
<td><p>A pointer to an IRP that is queued by the WSK subsystem until the list of available network transports changes. The WSK subsystem will complete the IRP after either a new network transport is added or an existing network transport is removed.</p></td>
</tr>
</tbody>
</table>

An IRP is required for this client control operation.

The WSK subsystem will cancel any pending IRPs if the WSK application calls [**WskDeregister**](https://msdn.microsoft.com/library/windows/hardware/ff571128) to detach itself from the WSK subsystem.

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
<td>Wsk.h (include Wsk.h)</td>
</tr>
</tbody>
</table>

 

 




