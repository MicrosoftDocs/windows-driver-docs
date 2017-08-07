---
title: OID\_RECEIVE\_FILTER\_MOVE\_FILTER
author: windows-driver-content
description: An overlying driver issues an object identifier (OID) set request of OID\_RECEIVE\_FILTER\_MOVE\_FILTER to move a previously configured receive filter.
ms.assetid: CC899ABD-EE6B-4932-889F-984C8B5A403F
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_RECEIVE_FILTER_MOVE_FILTER Network Drivers Starting with Windows Vista
---

# OID\_RECEIVE\_FILTER\_MOVE\_FILTER


An overlying driver issues an object identifier (OID) set request of OID\_RECEIVE\_FILTER\_MOVE\_FILTER to move a previously configured receive filter. Receive filters are moved from one virtual port (VPort) to a different VPort.

Overlying drivers issue this OID set request to the miniport driver for the network adapter's PCIe Physical Function (PF). This OID set request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_MOVE\_FILTER\_PARAMETERS**](ndis-receive-filter-move-filter-parameters.md) structure.

Remarks
-------

NDIS validates the members of the [**NDIS\_RECEIVE\_FILTER\_MOVE\_FILTER\_PARAMETERS**](ndis-receive-filter-move-filter-parameters.md) structure before it forwards the OID set request to the PF miniport driver.

The PF miniport driver must handle this OID set request atomically. The driver must be able to configure the network adapter to simultaneously remove the filter from a receive queue and VPort and set it on a different receive queue and VPort.

For more information, see [Moving a Receive Filter to a Virtual Port](https://msdn.microsoft.com/library/windows/hardware/hh464102).

### Return Status Codes

The PF miniport driver returns one of the following status codes for the OID set request of OID\_RECEIVE\_FILTER\_MOVE\_FILTER.

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
<td><p>NDIS_STATUS_SUCCESS</p></td>
<td><p>The OID request completed successfully.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_NOT_SUPPORTED</p></td>
<td><p>The PF miniport driver either does not support the single root I/O virtualization (SR-IOV) interface or is not enabled to use the interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_PARAMETER</p></td>
<td><p>One or more of the members of the [<strong>NDIS_RECEIVE_FILTER_MOVE_FILTER_PARAMETERS</strong>](ndis-receive-filter-move-filter-parameters.md) structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is less than sizeof([<strong>NDIS_RECEIVE_FILTER_MOVE_FILTER_PARAMETERS</strong>](ndis-receive-filter-move-filter-parameters.md)). The PF miniport driver must set the <strong>DATA.SET_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](ndis-oid-request.md) structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_FAILURE</p></td>
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
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[**NDIS\_OID\_REQUEST**](ndis-oid-request.md)

[**NDIS\_RECEIVE\_FILTER\_MOVE\_FILTER\_PARAMETERS**](ndis-receive-filter-move-filter-parameters.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_RECEIVE_FILTER_MOVE_FILTER%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


