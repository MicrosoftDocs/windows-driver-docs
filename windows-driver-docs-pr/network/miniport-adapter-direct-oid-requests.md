---
title: Miniport Adapter Direct OID Requests
description: Miniport Adapter Direct OID Requests
ms.assetid: 63ced5a3-0c83-4952-aa0e-c3c654b3f241
keywords:
- direct OID request interface WDK networking
- direct OID request path WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miniport Adapter Direct OID Requests





To support the direct OID request path, miniport drivers provide *MiniportXxx* function entry points in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure and NDIS provides **NdisM*Xxx*** functions for miniport drivers.

The *direct OID request interface* is similar to the standard OID request interface. For example, the [**NdisMDirectOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563582) and [*MiniportDirectOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559371) functions are similar to the [**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622) and [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) functions.

**Note**  NDIS 6.1 supports specific OIDs for use with the direct OID request interface. OIDs that existed before NDIS 6.1 and some NDIS 6.1 OIDs are not supported. To determine if an OID can be used in the direct OIDs interface, see the OID reference page. 

Miniport drivers must be able to handle direct OID requests that are not serialized. Unlike the standard OID request interface, NDIS does not serialize direct OID requests with other requests that are sent with the direct OID interface or with the standard OID request interface. Also, miniport drivers must be able to handle direct OID requests at IRQL &lt;= DISPATCH\_LEVEL.

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff559371" data-raw-source="[&lt;em&gt;MiniportDirectOidRequest&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559371)"><em>MiniportDirectOidRequest</em></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff559416" data-raw-source="[&lt;em&gt;MiniportOidRequest&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559416)"><em>MiniportOidRequest</em></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff559335" data-raw-source="[&lt;em&gt;MiniportCancelDirectOidRequest&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559335)"><em>MiniportCancelDirectOidRequest</em></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff559339" data-raw-source="[&lt;em&gt;MiniportCancelOidRequest&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559339)"><em>MiniportCancelOidRequest</em></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563582" data-raw-source="[&lt;strong&gt;NdisMDirectOidRequestComplete&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563582)"><strong>NdisMDirectOidRequestComplete</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563622" data-raw-source="[&lt;strong&gt;NdisMOidRequestComplete&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563622)"><strong>NdisMOidRequestComplete</strong></a></p></td>
</tr>
</tbody>
</table>

 

 

 





