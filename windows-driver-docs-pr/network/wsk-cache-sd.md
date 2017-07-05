---
title: WSK\_CACHE\_SD
description: WSK\_CACHE\_SD
MS-HAID:
- 'wskref\_87a859be-0370-44ac-b55e-89c241db1ae8.xml'
- 'netvista.wsk\_cache\_sd'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 60a4c7f9-d7e3-4378-b22b-93c69a9b8a37
keywords: ["WSK_CACHE_SD Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- WSK_CACHE_SD
api_location:
- Wsk.h
api_type:
- HeaderDef
---

# WSK\_CACHE\_SD


A WSK application uses the WSK\_CACHE\_SD client control operation to obtain a cached copy of a security descriptor that can be passed to the [**WskSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571149), [**WskSocketConnect**](https://msdn.microsoft.com/library/windows/hardware/ff571150), and [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) functions.

To obtain a cached copy of a security descriptor, a WSK application calls the [**WskControlClient**](https://msdn.microsoft.com/library/windows/hardware/ff571126) function with the following parameters.

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

 

```

```

A WSK application must release the cached copy of the security descriptor by using the [**WSK\_RELEASE\_SD**](wsk-release-sd.md) client control operation when the security descriptor is no longer needed.

For more information about the SECURITY\_DESCRIPTOR structure, see the reference page for SECURITY\_DESCRIPTOR in the Microsoft Windows SDK documentation.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WSK_CACHE_SD%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




