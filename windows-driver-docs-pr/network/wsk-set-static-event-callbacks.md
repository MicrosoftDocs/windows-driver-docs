---
title: WSK_SET_STATIC_EVENT_CALLBACKS
author: windows-driver-content
description: WSK_SET_STATIC_EVENT_CALLBACKS
ms.assetid: fa95bc7d-c7b2-4cca-a419-ef5eb2520976
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WSK_SET_STATIC_EVENT_CALLBACKS Network Drivers Starting with Windows Vista
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
<td><p>A pointer to a [<strong>WSK_EVENT_CALLBACK_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff571166) structure that specifies the desired event callback functions to be automatically enabled</p></td>
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

 

```

```

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WSK_SET_STATIC_EVENT_CALLBACKS%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


