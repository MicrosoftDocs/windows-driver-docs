---
title: SIO_WSK_REGISTER_EXTENSION
description: SIO_WSK_REGISTER_EXTENSION
ms.date: 07/18/2017
keywords:
 - SIO_WSK_REGISTER_EXTENSION Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# SIO\_WSK\_REGISTER\_EXTENSION


The SIO\_WSK\_REGISTER\_EXTENSION socket I/O control operation allows a WSK application to register for an extension interface that is supported by the WSK subsystem. This socket I/O control operation applies to all socket types.

To register an extension interface, a WSK application calls the [**WskControlSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket) function with the following parameters.

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
<td><p>A pointer to a <a href="/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_extension_control_in" data-raw-source="[&lt;strong&gt;WSK_EXTENSION_CONTROL_IN&lt;/strong&gt;](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_extension_control_in)"><strong>WSK_EXTENSION_CONTROL_IN</strong></a> structure. This structure contains a pointer to the <a href="/windows-hardware/drivers/network/network-programming-interface" data-raw-source="[Network Programming Interface (NPI)](./network-programming-interface.md)">Network Programming Interface (NPI)</a> identifier for the extension interface and pointers to the dispatch table and to the context for the WSK application's implementation of the extension interface.</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSize</em></p></td>
<td><p>sizeof(WSK_EXTENSION_CONTROL_OUT)</p></td>
</tr>
<tr class="odd">
<td><p><em>OutputBuffer</em></p></td>
<td><p>A pointer to a <a href="/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_extension_control_out" data-raw-source="[&lt;strong&gt;WSK_EXTENSION_CONTROL_OUT&lt;/strong&gt;](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_extension_control_out)"><strong>WSK_EXTENSION_CONTROL_OUT</strong></a> structure. This structure receives a pointer to the dispatch table and a pointer to the context for the WSK subsystem's implementation of the extension interface.</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSizeReturned</em></p></td>
<td><p>NULL</p></td>
</tr>
</tbody>
</table>


A WSK application does not specify a pointer to an IRP when calling the **WskControlSocket** function to register an extension interface.

The contents of the dispatch table structures are extension interface-specific.

For more information about registering an extension interface, see [Registering an Extension Interface](./registering-an-extension-interface.md).

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

