---
title: WSK_CACHE_SD
description: WSK_CACHE_SD
ms.date: 07/18/2017
ms.topic: reference
keywords:
 - WSK_CACHE_SD Network Drivers Starting with Windows Vista
---

# WSK\_CACHE\_SD


A WSK application uses the WSK\_CACHE\_SD client control operation to obtain a cached copy of a security descriptor that can be passed to the [**WskSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_socket), [**WskSocketConnect**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_socket_connect), and [**WskControlSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket) functions.

To obtain a cached copy of a security descriptor, a WSK application calls the [**WskControlClient**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_client) function with the following parameters.

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
<td><p>WSK_CACHE_SD</p></td>
</tr>
<tr class="even">
<td><p><em>InputSize</em></p></td>
<td><p>sizeof(PSECURITY_DESCRIPTOR)</p></td>
</tr>
<tr class="odd">
<td><p><em>InputBuffer</em></p></td>
<td><p>A pointer to a PSECURITY_DESCRIPTOR-typed variable. This variable contains a pointer to the SECURITY_DESCRIPTOR structure that defines the uncached security descriptor that is being cached.</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSize</em></p></td>
<td><p>sizeof(PSECURITY_DESCRIPTOR)</p></td>
</tr>
<tr class="odd">
<td><p><em>OutputBuffer</em></p></td>
<td><p>A pointer to a PSECURITY_DESCRIPTOR-typed variable. This variable receives a pointer to a SECURITY_DESCRIPTOR structure that describes the cached security descriptor.</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSizeReturned</em></p></td>
<td><p><strong>NULL</strong></p></td>
</tr>
<tr class="odd">
<td><p><em>Irp</em></p></td>
<td><p><strong>NULL</strong></p></td>
</tr>
</tbody>
</table>

A WSK application must release the cached copy of the security descriptor by using the [**WSK\_RELEASE\_SD**](wsk-release-sd.md) client control operation when the security descriptor is no longer needed.

See the reference page for the [SECURITY_DESCRIPTOR](/windows/win32/api/winnt/ns-winnt-security_descriptor) structure for more information.

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

 

