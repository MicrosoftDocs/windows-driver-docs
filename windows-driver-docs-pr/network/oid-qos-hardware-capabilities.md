---
title: OID\_QOS\_HARDWARE\_CAPABILITIES
author: windows-driver-content
description: An overlying driver issues an object identifier (OID) query request of OID\_QOS\_HARDWARE\_CAPABILITIES to obtain the NDIS Quality of Service (QoS) hardware capabilities of a network adapter.
ms.assetid: 50D93F3F-DEA0-4D7D-8866-4155EED8D8BC
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_QOS_HARDWARE_CAPABILITIES Network Drivers Starting with Windows Vista
---

# OID\_QOS\_HARDWARE\_CAPABILITIES


An overlying driver issues an object identifier (OID) query request of OID\_QOS\_HARDWARE\_CAPABILITIES to obtain the NDIS Quality of Service (QoS) hardware capabilities of a network adapter.

After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure contains a pointer to an [**NDIS\_QOS\_CAPABILITIES**](ndis-qos-capabilities.md) structure.

**Note**  This OID query request is handled by NDIS for miniport drivers that support the IEEE 802.1 Data Center Bridging (DCB) interface.

 

Remarks
-------

The [**NDIS\_QOS\_CAPABILITIES**](ndis-qos-capabilities.md) structure contains information about the NDIS QoS hardware capabilities of a network adapter. These capabilities can include hardware capabilities that are currently disabled by INF file settings or through the **Advanced** properties page.

**Note**  All the NDIS QoS hardware capabilities of a network adapter are returned through an OID query request of OID\_QOS\_HARDWARE\_CAPABILITIES, regardless of whether a capability is enabled or disabled.

 

Miniport drivers registers the NDIS QoS hardware capabilities of a network adapter when its [*MiniportInitializeEx*](miniportinitializeex.md) function is called. The driver registers these capabilities by following these steps:

1.  The driver initializes an [**NDIS\_QOS\_CAPABILITIES**](ndis-qos-capabilities.md) structure with the NDIS QoS hardware capabilities.

2.  The driver sets the **HardwareQosCapabilities** member of the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](ndis-miniport-adapter-hardware-assist-attributes.md) structure to a pointer to the [**NDIS\_QOS\_CAPABILITIES**](ndis-qos-capabilities.md) structure.

3.  The miniport driver then calls the [**NdisMSetMiniportAttributes**](ndismsetminiportattributes.md) function and sets the *MiniportAttributes* parameter to a pointer to an [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](ndis-miniport-adapter-hardware-assist-attributes.md) structure.

**Note**  NDIS does not report the NDIS QoS hardware capabilities of a network adapter to overlying protocol and filter drivers during the bind or attach operations.

 

For more information on how to register NDIS QoS capabilities, see [Registering NDIS QoS Capabilities](https://msdn.microsoft.com/library/windows/hardware/hh440188).

### Return Status Codes

NDIS handles the OID query request of OID\_QOS\_HARDWARE\_CAPABILITIES request for miniport drivers, and returns one of the following status codes.

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
<td><p>The miniport driver does not support the NDIS QoS interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is less than sizeof([<strong>NDIS_QOS_CAPABILITIES</strong>](ndis-qos-capabilities.md)). NDIS sets the <strong>DATA.QUERY_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](ndis-oid-request.md) structure to the minimum buffer size that is required.</p></td>
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
[*MiniportInitializeEx*](miniportinitializeex.md)

[**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](ndis-miniport-adapter-hardware-assist-attributes.md)

[**NdisMSetMiniportAttributes**](ndismsetminiportattributes.md)

[**NDIS\_OID\_REQUEST**](ndis-oid-request.md)

[**NDIS\_QOS\_CAPABILITIES**](ndis-qos-capabilities.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_QOS_HARDWARE_CAPABILITIES%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


