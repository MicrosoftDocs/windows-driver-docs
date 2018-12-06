---
title: SIO_WSK_REGISTER_EXTENSION
description: SIO_WSK_REGISTER_EXTENSION
ms.assetid: e7fd6d68-85e8-4c5f-b67f-2193d200130d
ms.date: 07/18/2017
keywords:
 - SIO_WSK_REGISTER_EXTENSION Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# SIO\_WSK\_REGISTER\_EXTENSION


The SIO\_WSK\_REGISTER\_EXTENSION socket I/O control operation allows a WSK application to register for an extension interface that is supported by the WSK subsystem. This socket I/O control operation applies to all socket types.

To register an extension interface, a WSK application calls the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function with the following parameters.

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
<td><p>SIO_WSK_REGISTER_EXTENSION</p></td>
</tr>
<tr class="odd">
<td><p><em>Level</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>InputSize</em></p></td>
<td><p>sizeof(WSK_EXTENSION_CONTROL_IN)</p></td>
</tr>
<tr class="odd">
<td><p><em>InputBuffer</em></p></td>
<td><p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff571167" data-raw-source="[&lt;strong&gt;WSK_EXTENSION_CONTROL_IN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff571167)"><strong>WSK_EXTENSION_CONTROL_IN</strong></a> structure. This structure contains a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568373" data-raw-source="[Network Programming Interface (NPI)](https://msdn.microsoft.com/library/windows/hardware/ff568373)">Network Programming Interface (NPI)</a> identifier for the extension interface and pointers to the dispatch table and to the context for the WSK application&#39;s implementation of the extension interface.</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSize</em></p></td>
<td><p>sizeof(WSK_EXTENSION_CONTROL_OUT)</p></td>
</tr>
<tr class="odd">
<td><p><em>OutputBuffer</em></p></td>
<td><p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff571168" data-raw-source="[&lt;strong&gt;WSK_EXTENSION_CONTROL_OUT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff571168)"><strong>WSK_EXTENSION_CONTROL_OUT</strong></a> structure. This structure receives a pointer to the dispatch table and a pointer to the context for the WSK subsystem&#39;s implementation of the extension interface.</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSizeReturned</em></p></td>
<td><p>NULL</p></td>
</tr>
</tbody>
</table>


A WSK application does not specify a pointer to an IRP when calling the **WskControlSocket** function to register an extension interface.

The contents of the dispatch table structures are extension interface-specific.

For more information about registering an extension interface, see [Registering an Extension Interface](https://msdn.microsoft.com/library/windows/hardware/ff570461).

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

 

 




