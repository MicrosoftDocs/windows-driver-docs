---
title: OID_GEN_RECEIVE_HASH
description: As a query, NDIS and overlying drivers use the OID_GEN_RECEIVE_HASH OID to obtain the current receive hash calculation settings of a miniport adapter.
ms.assetid: be120dab-c98d-418f-8777-e2fb37b774a1
ms.date: 08/08/2017
keywords: 
 -OID_GEN_RECEIVE_HASH Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_RECEIVE\_HASH


As a query, NDIS and overlying drivers use the OID\_GEN\_RECEIVE\_HASH OID to obtain the current receive hash calculation settings of a miniport adapter. NDIS returns an [**NDIS\_RECEIVE\_HASH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567190) structure that contains the current receive hash settings.

As a set, NDIS and overlying drivers use the OID\_GEN\_RECEIVE\_HASH OID to configure the receive hash calculations on a miniport adapter. The miniport driver receives an NDIS\_RECEIVE\_HASH\_PARAMETERS structure.

Remarks
-------

For NDIS miniport drivers, the query is not requested.

Support for this OID set is optional for miniport drivers, including those that support RSS.

An overlying driver can use the OID\_GEN\_RECEIVE\_HASH OID to enable and configure hash calculations on received frames without enabling RSS.

**Note**  Protocol drivers must disable receive hash calculations before they enable RSS. If RSS is enabled, a protocol driver disables RSS before it enables receive hash calculations. A miniport driver should fail a set request with **NDIS\_STATUS\_INVALID\_OID** or **NDIS\_STATUS\_NOT\_SUPPORTED** to enable receive hash calculations if [OID\_GEN\_RECEIVE\_SCALE\_PARAMETERS](oid-gen-receive-scale-parameters.md) is currently enabled.

 

**Note**  The secret key is appended after the [**NDIS\_RECEIVE\_HASH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567190) structure members.

 

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


[**NDIS\_RECEIVE\_HASH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567190)

 

 




