---
title: Protocol Driver Direct OID Requests
description: Protocol Driver Direct OID Requests
ms.assetid: 387d27de-3214-4f93-8f45-9a2f28e5036f
keywords:
- direct OID request interface WDK networking
- direct OID request path WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Protocol Driver Direct OID Requests





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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570259" data-raw-source="[&lt;strong&gt;ProtocolDirectOidRequestComplete&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570259)"><strong>ProtocolDirectOidRequestComplete</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570264" data-raw-source="[&lt;strong&gt;ProtocolOidRequestComplete&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570264)"><strong>ProtocolOidRequestComplete</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561746" data-raw-source="[&lt;strong&gt;NdisDirectOidRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561746)"><strong>NdisDirectOidRequest</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563710" data-raw-source="[&lt;strong&gt;NdisOidRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563710)"><strong>NdisOidRequest</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561621" data-raw-source="[&lt;strong&gt;NdisCancelDirectOidRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561621)"><strong>NdisCancelDirectOidRequest</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561622" data-raw-source="[&lt;strong&gt;NdisCancelOidRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561622)"><strong>NdisCancelOidRequest</strong></a></p></td>
</tr>
</tbody>
</table>

 

 

 





