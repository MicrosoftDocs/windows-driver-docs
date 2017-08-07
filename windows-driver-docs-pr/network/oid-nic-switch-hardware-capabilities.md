---
title: OID\_NIC\_SWITCH\_HARDWARE\_CAPABILITIES
author: windows-driver-content
description: An overlying driver issues an object identifier (OID) query request of OID\_NIC\_SWITCH\_HARDWARE\_CAPABILITIES to obtain the hardware capabilities of the NIC switch in the network adapter.
ms.assetid: 2c417a16-68e1-4754-88a5-8bac4653e05d
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_NIC_SWITCH_HARDWARE_CAPABILITIES Network Drivers Starting with Windows Vista
---

# OID\_NIC\_SWITCH\_HARDWARE\_CAPABILITIES


An overlying driver issues an object identifier (OID) query request of OID\_NIC\_SWITCH\_HARDWARE\_CAPABILITIES to obtain the hardware capabilities of the NIC switch in the network adapter.

After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](ndis-nic-switch-capabilities.md) structure.

Remarks
-------

The [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](ndis-nic-switch-capabilities.md) structure contains information about the hardware capabilities of a NIC switch on the network adapter. These capabilities can include the hardware capabilities that are currently disabled by the INF file settings or through the **Advanced** properties page.

**Note**  All the capabilities of the specified NIC switch are returned through an OID query request of OID\_NIC\_SWITCH\_HARDWARE\_CAPABILITIES, regardless of whether a capability is enabled or disabled.

 

Starting with NDIS 6.20, miniport drivers supply the NIC switch hardware capabilities when its [*MiniportInitializeEx*](miniportinitializeex.md) function is called. The driver initializes an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](ndis-nic-switch-capabilities.md) structure with the NIC switch hardware capabilities and sets the **HardwareNicSwitchCapabilities** member of the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](ndis-miniport-adapter-hardware-assist-attributes.md) structure to a pointer to the **NDIS\_NIC\_SWITCH\_CAPABILITIES** structure. The miniport driver then calls the [**NdisMSetMiniportAttributes**](ndismsetminiportattributes.md) function and sets the *MiniportAttributes* parameter to a pointer to an **NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES** structure.

**Note**  Starting with NDIS 6.30, miniport drivers that support the single root I/O virtualization (SR-IOV) interface must register the hardware capabilities of the NIC switch. Drivers register these capabilities by calling [**NdisMSetMiniportAttributes**](ndismsetminiportattributes.md).

 

### Return Status Codes

NDIS handles the OID query request of OID\_NIC\_SWITCH\_HARDWARE\_CAPABILITIES request for miniport drivers, and returns one of the following status codes:

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
<td><p>The request completed successfully. The <strong>InformationBuffer</strong> points to an [<strong>NDIS_NIC_SWITCH_CAPABILITIES</strong>](ndis-nic-switch-capabilities.md) structure.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_NOT_SUPPORTED</p></td>
<td><p>The miniport driver either does not support the single root I/O virtualization (SR-IOV) interface or is not enabled to use the interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is less than sizeof([<strong>NDIS_NIC_SWITCH_CAPABILITIES</strong>](ndis-nic-switch-capabilities.md)). NDIS sets the <strong>DATA.QUERY_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](ndis-oid-request.md) structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="even">
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
<td><p>Supported in NDIS 6.20 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_BIND\_PARAMETERS**](ndis-bind-parameters.md)

[**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](ndis-miniport-adapter-hardware-assist-attributes.md)

[**NDIS\_NIC\_SWITCH\_CAPABILITIES**](ndis-nic-switch-capabilities.md)

[**NDIS\_OID\_REQUEST**](ndis-oid-request.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_NIC_SWITCH_HARDWARE_CAPABILITIES%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


