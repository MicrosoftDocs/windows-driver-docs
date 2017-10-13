---
title: OID_GEN_RECEIVE_HASH
author: windows-driver-content
description: As a query, NDIS and overlying drivers use the OID\_GEN\_RECEIVE\_HASH OID to obtain the current receive hash calculation settings of a miniport adapter.
ms.assetid: be120dab-c98d-418f-8777-e2fb37b774a1
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_RECEIVE_HASH Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_RECEIVE_HASH%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


