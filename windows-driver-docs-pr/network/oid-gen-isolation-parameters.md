---
title: OID\_GEN\_ISOLATION\_PARAMETERS
author: windows-driver-content
description: NDIS and overlying drivers issue an object identifier (OID) request of OID\_GEN\_ISOLATION\_PARAMETERS to obtain the multi-tenancy configuration (isolation) parameters that are set on a VM network adapter's port.
ms.assetid: 68E89349-4907-4241-9C50-B13C75273F0D
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_ISOLATION_PARAMETERS Network Drivers Starting with Windows Vista
---

# OID\_GEN\_ISOLATION\_PARAMETERS


NDIS and overlying drivers issue an object identifier (OID) request of OID\_GEN\_ISOLATION\_PARAMETERS to obtain the multi-tenancy configuration (isolation) parameters that are set on a VM network adapter's port.

Although each routing domain is configured separately on the port, this OID returns parameters for all of the routing domains in a single query.

An overlying driver should issue this OID in two steps:

1.  Io query the required buffer size, issue the OID query with the **Size** member of the **Header** member of the [**NDIS\_ISOLATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn383679) structure set to **NDIS\_SIZEOF\_NDIS\_ISOLATION\_PARAMETERS\_REVISION\_1**. (See **NDIS\_STATUS\_INVALID\_LENGTH** below.)
2.  Issue the OID with an **InformationBuffer** of the required size.

If the OID query request is completed successfully, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer. This buffer contains the following data, in order:

1.  An [**NDIS\_ISOLATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn383679) structure

2.  One or more [**NDIS\_ROUTING\_DOMAIN\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383681) structures, one for each routing domain

3.  One or more [**NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383684) structures, grouped by routing domain

In each [**NDIS\_ROUTING\_DOMAIN\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383681) structure, the **FirstIsolationInfoEntryOffset** member contains the offset from the beginning of the OID information buffer (that is, the beginning of the buffer that the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure points to) to the first [**NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383684) for that routing domain. The offset in the **NextIsolationInfoEntryOffset** member of the last structure in the list is zero.

If no multi-tenancy configuration parameters are set on the VM network adapter, the network adapter miniport driver sets the **DATA.QUERY\_INFORMATION.BytesWritten** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to zero and returns **NDIS\_STATUS\_SUCCESS**. In this case, the data within the **DATA.QUERY\_INFORMATION.InformationBuffer** member is not modified by the miniport driver.

Remarks
-------

### Return Status Codes

The VM network adapter miniport driver returns one of the following status codes for this OID request:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>NDIS_STATUS_SUCCESS</strong></p></td>
<td><p>The OID request completed successfully.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_INVALID_LENGTH</strong></p></td>
<td><p>The length of the information buffer is too small to return the requested information. The VM network adapter miniport driver sets the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size, in bytes, that is required.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_FAILURE</strong></p></td>
<td><p>The request failed for other reasons.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p>Supported in NDIS 6.40 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_ISOLATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn383679)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_ROUTING\_DOMAIN\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383681)

[**NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383684)

[**NDIS\_STATUS\_ISOLATION\_PARAMETERS\_CHANGE**](ndis-status-isolation-parameters-change.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_ISOLATION_PARAMETERS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


