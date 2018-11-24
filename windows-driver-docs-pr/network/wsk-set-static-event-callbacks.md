---
title: WSK_SET_STATIC_EVENT_CALLBACKS
description: WSK_SET_STATIC_EVENT_CALLBACKS
ms.assetid: fa95bc7d-c7b2-4cca-a419-ef5eb2520976
ms.date: 07/18/2017
keywords:
 - WSK_SET_STATIC_EVENT_CALLBACKS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WSK\_SET\_STATIC\_EVENT\_CALLBACKS


A WSK application uses the WSK\_SET\_STATIC\_EVENT\_CALLBACKS client control operation to automatically enable certain event callback functions on every socket that it creates. The event callback functions that are enabled in this manner are always enabled and cannot be disabled or re-enabled later by the WSK application. However, if a WSK application always enables certain event callback functions on every socket that it creates, the application should use this method to automatically enable those event callback functions because it will yield much better performance.

If a WSK application uses the WSK\_SET\_STATIC\_EVENT\_CALLBACKS client control operation, it must do so before it creates any sockets.

To automatically enable certain event callback functions on every socket it creates, a WSK application calls the [**WskControlClient**](https://msdn.microsoft.com/library/windows/hardware/ff571126) function with the following parameters.

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
<td><p>WSK_SET_STATIC_EVENT_CALLBACKS</p></td>
</tr>
<tr class="even">
<td><p><em>InputSize</em></p></td>
<td><p>sizeof(WSK_EVENT_CALLBACK_CONTROL)</p></td>
</tr>
<tr class="odd">
<td><p><em>InputBuffer</em></p></td>
<td><p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff571166" data-raw-source="[&lt;strong&gt;WSK_EVENT_CALLBACK_CONTROL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff571166)"><strong>WSK_EVENT_CALLBACK_CONTROL</strong></a> structure that specifies the desired event callback functions to be automatically enabled</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSize</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><em>OutputBuffer</em></p></td>
<td><p><strong>NULL</strong></p></td>
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

A WSK application can specify a combination of event flags for different socket types in the **EventMask** member of the [**WSK\_EVENT\_CALLBACK\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff571166) structure. When the WSK application creates a new socket, the WSK subsystem will automatically enable the appropriate event callback functions for the specific [category](https://msdn.microsoft.com/library/windows/hardware/ff571093) of WSK socket that is being created.

For more information about the event flags for the standard WSK event callback functions, see [**SO\_WSK\_EVENT\_CALLBACK**](so-wsk-event-callback.md).

For more information about enabling and disabling a socket's event callback functions, see [Enabling and Disabling Event Callback Functions](https://msdn.microsoft.com/library/windows/hardware/ff548851).

The *Irp* parameter must be **NULL** for this client control operation.

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

 

 




