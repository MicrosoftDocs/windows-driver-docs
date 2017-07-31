---
title: WSK_TRANSPORT_LIST_QUERY
author: windows-driver-content
description: WSK_TRANSPORT_LIST_QUERY
ms.assetid: feb6aed2-fac9-4d3f-a36b-f721c737aacf
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WSK_TRANSPORT_LIST_QUERY Network Drivers Starting with Windows Vista
---

# WSK\_TRANSPORT\_LIST\_QUERY


A WSK application uses the WSK\_TRANSPORT\_LIST\_QUERY client control operation to retrieve a list of available network transports that can be specified when creating a new socket.

To retrieve a list of available network transports, a WSK application calls the [**WskControlClient**](https://msdn.microsoft.com/library/windows/hardware/ff571126) function with the following parameters.

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
<td><p>A pointer to an array of [<strong>WSK_TRANSPORT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff571193) structures that receives the list of available network transports</p></td>
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

 

```

```

A WSK application can specify zero in the *OutputSize* parameter and **NULL** in the *OutputBuffer* parameter to determine the size of the array of [**WSK\_TRANSPORT**](https://msdn.microsoft.com/library/windows/hardware/ff571193) structures, in bytes, that is required to contain the complete list of available network transports. In such a situation, the call to the [**WskControlClient**](https://msdn.microsoft.com/library/windows/hardware/ff571126) function returns STATUS\_BUFFER\_OVERFLOW, and the variable that is pointed to by the *OutputSizeReturned* parameter contains the required buffer size. The application can then allocate a buffer that is large enough to contain the complete list of available network transports and can call the **WskControlClient** function a second time, specifying the parameters that are shown in the preceding table.

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WSK_TRANSPORT_LIST_QUERY%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


