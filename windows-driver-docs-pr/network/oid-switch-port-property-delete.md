---
title: OID\_SWITCH\_PORT\_PROPERTY\_DELETE
author: windows-driver-content
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_PORT\_PROPERTY\_DELETE to notify extensible switch extensions about the deletion of a policy property for an extensible switch port.
ms.assetid: BA8AB5D9-FF2C-4E16-B09F-B09E3EC19B90
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_SWITCH_PORT_PROPERTY_DELETE Network Drivers Starting with Windows Vista
---

# OID\_SWITCH\_PORT\_PROPERTY\_DELETE


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_PORT\_PROPERTY\_DELETE to notify extensible switch extensions about the deletion of a policy property for an extensible switch port.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure contains a pointer to a buffer that contains an [**NDIS\_SWITCH\_PORT\_PROPERTY\_DELETE\_PARAMETERS**](ndis-switch-port-property-delete-parameters.md) structure.

Remarks
-------

A forwarding extension can handle the OID set request of OID\_SWITCH\_PORT\_PROPERTY\_DELETE. All other types of extensions must call [**NdisFOidRequest**](ndisfoidrequest.md) to forward the OID request to the next extension in the extensible switch driver stack.

For guidelines on how to handle an OID set request of OID\_SWITCH\_PORT\_PROPERTY\_DELETE, see [Managing Port Policies](https://msdn.microsoft.com/library/windows/hardware/hh598202).

### Return Status Codes

If the forwarding extension completes the OID set request of OID\_SWITCH\_PORT\_PROPERTY\_DELETE, it returns one of the following status codes.

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
<td><p>The forwarding extension does not support the port policy.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_<em>Xxx</em></p></td>
<td><p>The OID request failed for other reasons.</p></td>
</tr>
</tbody>
</table>

 

If the forwarding extension does not complete the OID set request of OID\_SWITCH\_PORT\_PROPERTY\_DELETE, the request is completed by the underlying miniport edge of the extensible switch. The miniport edge returns the following status code.

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

[**NDIS\_SWITCH\_PORT\_PROPERTY\_CUSTOM**](ndis-switch-port-property-custom.md)

[**NDIS\_SWITCH\_PORT\_PROPERTY\_PARAMETERS**](ndis-switch-port-property-parameters.md)

[**NDIS\_SWITCH\_PORT\_PROPERTY\_VLAN**](ndis-switch-port-property-vlan.md)

[**NdisFOidRequest**](ndisfoidrequest.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SWITCH_PORT_PROPERTY_DELETE%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


