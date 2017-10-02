---
title: OID_GEN_HD_SPLIT_CURRENT_CONFIG
author: windows-driver-content
description: As a query, overlying drivers or administrative utilities can use the OID\_GEN\_HD\_SPLIT\_CURRENT\_CONFIG OID to determine the current header-data split configuration of a miniport adapter.
ms.assetid: fc363227-1040-45bc-8c76-2ac61606d777
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_HD_SPLIT_CURRENT_CONFIG Network Drivers Starting with Windows Vista
---

# OID\_GEN\_HD\_SPLIT\_CURRENT\_CONFIG


As a query, overlying drivers or administrative utilities can use the OID\_GEN\_HD\_SPLIT\_CURRENT\_CONFIG OID to determine the current header-data split configuration of a miniport adapter. A system administrator can use the GUID that is associated with this OID through the WMI interface.

Remarks
-------

NDIS handles this OID on behalf of the miniport driver. NDIS maintains the current header-data split configuration information based on the miniport driver initialization attributes and the [**NDIS\_STATUS\_HD\_SPLIT\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567370) status indication.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains an [**NDIS\_HD\_SPLIT\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff565696) structure.

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
<td><p>Supported in NDIS 6.1 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_HD\_SPLIT\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff565696)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_STATUS\_HD\_SPLIT\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567370)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_HD_SPLIT_CURRENT_CONFIG%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


