---
title: WSK\_TRANSPORT\_LIST\_CHANGE
description: WSK\_TRANSPORT\_LIST\_CHANGE
MS-HAID:
- 'wskref\_5f822cc9-8250-4133-a28b-e198d5d2c572.xml'
- 'netvista.wsk\_transport\_list\_change'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3b12d692-467c-4d31-bd2a-bb6e34d87fde
keywords: ["WSK_TRANSPORT_LIST_CHANGE Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- WSK_TRANSPORT_LIST_CHANGE
api_location:
- Wsk.h
api_type:
- HeaderDef
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

 

```

```

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WSK_TRANSPORT_LIST_CHANGE%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




