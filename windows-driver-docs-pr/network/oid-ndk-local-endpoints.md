---
title: OID_NDK_LOCAL_ENDPOINTS
author: windows-driver-content
description: As a query, NDIS and overlying drivers or user-mode applications use the OID\_NDK\_LOCAL\_ENDPOINTS OID to the list of active Network Direct listeners and shared endpoints on a miniport adapter.
ms.assetid: 93F077AF-7FEA-4F92-9784-B65ADCC16564
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_NDK_LOCAL_ENDPOINTS Network Drivers Starting with Windows Vista
---

# OID\_NDK\_LOCAL\_ENDPOINTS


As a query, NDIS and overlying drivers or user-mode applications use the OID\_NDK\_LOCAL\_ENDPOINTS OID to the list of active Network Direct listeners and shared endpoints on a miniport adapter.

NDIS 6.30 and later miniport drivers that provide NDK services must support this OID. Otherwise, this OID is optional.

Remarks
-------

NDIS issues this OID to obtain the list of active Network Direct listeners and shared endpoints from an adapter. The adapter is required to return the list of listeners and shared endpoints in the [**NDIS\_NDK\_LOCAL\_ENDPOINTS**](https://msdn.microsoft.com/library/windows/hardware/hh451563) structure at **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure.

This structure is variable-sized based on the number of local endpoints that are returned. The size of the local endpoint array, as element count, is specified in the **Count** member.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>None supported</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2012</p></td>
</tr>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_NDK\_LOCAL\_ENDPOINTS**](https://msdn.microsoft.com/library/windows/hardware/hh451563)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_NDK_LOCAL_ENDPOINTS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


