---
title: WSK_TRANSPORT_LIST_QUERY
description: WSK_TRANSPORT_LIST_QUERY
ms.date: 07/18/2017
keywords:
 - WSK_TRANSPORT_LIST_QUERY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WSK\_TRANSPORT\_LIST\_QUERY


A WSK application uses the WSK\_TRANSPORT\_LIST\_QUERY client control operation to retrieve a list of available network transports that can be specified when creating a new socket.

To retrieve a list of available network transports, a WSK application calls the [**WskControlClient**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_client) function with the following parameters.

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
<td><p>WSK_TRANSPORT_LIST_QUERY</p></td>
</tr>
<tr class="even">
<td><p><em>InputSize</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><em>InputBuffer</em></p></td>
<td><p><strong>NULL</strong></p></td>
</tr>
<tr class="even">
<td><p><em>OutputSize</em></p></td>
<td><p>The size, in bytes, of the array of structures that is pointed to by the <em>OutputBuffer</em> parameter</p></td>
</tr>
<tr class="odd">
<td><p><em>OutputBuffer</em></p></td>
<td><p>A pointer to an array of <a href="/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_transport" data-raw-source="[&lt;strong&gt;WSK_TRANSPORT&lt;/strong&gt;](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_transport)"><strong>WSK_TRANSPORT</strong></a> structures that receives the list of available network transports</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSizeReturned</em></p></td>
<td><p>A pointer to a SIZE_T-typed variable that receives the number of bytes of data that are copied into the array of structures that is pointed to by the <em>OutputBuffer</em> parameter</p></td>
</tr>
<tr class="odd">
<td><p><em>Irp</em></p></td>
<td><p><strong>NULL</strong></p></td>
</tr>
</tbody>
</table>

A WSK application can specify zero in the *OutputSize* parameter and **NULL** in the *OutputBuffer* parameter to determine the size of the array of [**WSK\_TRANSPORT**](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_transport) structures, in bytes, that is required to contain the complete list of available network transports. In such a situation, the call to the [**WskControlClient**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_client) function returns STATUS\_BUFFER\_OVERFLOW, and the variable that is pointed to by the *OutputSizeReturned* parameter contains the required buffer size. The application can then allocate a buffer that is large enough to contain the complete list of available network transports and can call the **WskControlClient** function a second time, specifying the parameters that are shown in the preceding table.

The *Irp* parameter must be **NULL** for this client control operation.

## Requirements

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

