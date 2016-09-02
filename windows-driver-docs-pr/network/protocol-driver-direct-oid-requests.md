---
title: Protocol Driver Direct OID Requests
description: Protocol Driver Direct OID Requests
ms.assetid: 387d27de-3214-4f93-8f45-9a2f28e5036f
keywords: ["direct OID request interface WDK networking", "direct OID request path WDK networking"]
---

# Protocol Driver Direct OID Requests


## <a href="" id="ddk-protocol-driver-direct-oid-requests-ng"></a>


To support the direct OID request path, protocol drivers provide *ProtocolXxx* function entry points in the [**NDIS\_PROTOCOL\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566825) structure and NDIS provides **Ndis*Xxx*** functions for protocol drivers.

The *direct OID request interface* is similar to the standard OID request interface. For example, the [**NdisDirectOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561746) and [**ProtocolDirectOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570259) functions are similar to the [**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710) and [**ProtocolOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570264) functions.

**Note**  NDIS 6.1 and later support specific OIDs for use with the direct OID request interface. OIDs that existed before NDIS 6.1 and some NDIS 6.1 OIDs are not supported. To determine if an OID can be used in the direct OIDs interface, see the OID reference page. For example, see the note in the [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569812) OID.

 

To support the direct OIDs request interface, use the documentation for the standard OID request interface. The following table shows the relationship between the functions in the direct OID request interface and the standard OID request interface.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Direct OID function</th>
<th align="left">Standard OID function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>ProtocolDirectOidRequestComplete</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570259)</p></td>
<td align="left"><p>[<strong>ProtocolOidRequestComplete</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570264)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NdisDirectOidRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561746)</p></td>
<td align="left"><p>[<strong>NdisOidRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563710)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NdisCancelDirectOidRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561621)</p></td>
<td align="left"><p>[<strong>NdisCancelOidRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561622)</p></td>
</tr>
</tbody>
</table>

 

 

 





