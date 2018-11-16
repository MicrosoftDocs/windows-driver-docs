---
title: OID_GEN_RECEIVE_SCALE_PARAMETERS
description: As a query, NDIS and overlying drivers can use the OID_GEN_RECEIVE_SCALE_PARAMETERS OID to query the current receive side scaling (RSS) parameters of a NIC.
ms.assetid: a54190f7-0d2e-4f85-84c2-05fc9ec4994a
ms.date: 08/08/2017
keywords: 
 -OID_GEN_RECEIVE_SCALE_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_RECEIVE\_SCALE\_PARAMETERS


As a query, NDIS and overlying drivers can use the OID\_GEN\_RECEIVE\_SCALE\_PARAMETERS OID to query the current receive side scaling (RSS) parameters of a NIC. NDIS returns an [**NDIS\_RECEIVE\_SCALE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567228) structure that defines the current RSS parameters.

As a set, NDIS and overlying drivers use the OID\_GEN\_RECEIVE\_SCALE\_PARAMETERS OID to set the current RSS parameters of a NIC. The miniport driver receives an NDIS\_RECEIVE\_SCALE\_PARAMETERS structure that defines the RSS parameters.

> [!NOTE]
> In RSSv2, this OID is only used to query current RSS parameters of a given scaling entity. For miniport drivers that support RSSv2, see [OID_GEN_RECEIVE_SCALE_PARAMETERS_V2](oid-gen-receive-scale-parameters-v2.md) for setting RSS parameters other than the indirection table.

Remarks
-------

For NDIS miniport drivers, the query is not requested and the set is required for drivers that support RSS. NDIS handles the query for miniport drivers.

The TCP/IP driver configures IPv4 and IPv6 with a single OID set request of OID\_GEN\_RECEIVE\_SCALE\_PARAMETERS. That is, when the stack should enable RSS for both IPv4 and IPv6, it sets both of the corresponding flags in the **HashInformation** member of the [**NDIS\_RECEIVE\_SCALE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567228) structure and sends one OID request. Also, IPv4 and IPv6 use the same secret key and the key will always be 40 bytes, even if only IPv4 is enabled.

The underlying miniport adapter must use the most recent OID\_GEN\_RECEIVE\_SCALE\_PARAMETERS OID settings it has received. For example, if the miniport gets an OID\_GEN\_RECEIVE\_SCALE\_PARAMETERS OID with the IPv4 hash types missing, it must disable IPv4 RSS if it was previously enabled.

**Note**  An overlying driver can use the [OID\_GEN\_RECEIVE\_HASH](oid-gen-receive-hash.md) OID to enable and configure hash calculations on received frames without enabling RSS.

 

**Note**  Protocol drivers must disable receive hash calculations ([OID\_GEN\_RECEIVE\_HASH](oid-gen-receive-hash.md)) before they enable RSS. If RSS is enabled, a protocol driver disables RSS before it enables receive hash calculations. A miniport driver should fail a set request with **NDIS\_STATUS\_INVALID\_OID** or **NDIS\_STATUS\_NOT\_SUPPORTED** to enable RSS if OID\_GEN\_RECEIVE\_HASH is currently enabled.

 

**Note**  The indirection table and secret key are appended after the [**NDIS\_RECEIVE\_SCALE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567228) structure members. For more information about the indirection table and secret key, see **NDIS\_RECEIVE\_SCALE\_PARAMETERS**.

 

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
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_RECEIVE\_SCALE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567228)

[OID\_GEN\_RECEIVE\_HASH](oid-gen-receive-hash.md)

 

 




