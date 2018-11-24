---
title: OID_GEN_MEDIA_CONNECT_STATUS_EX
description: As a query, the OID_GEN_MEDIA_CONNECT_STATUS_EX OID returns the connection state of an interface. Windows Vista and laterSupported. NDIS 6.0 and later miniport driversNot requested. For NDIS interface providers only.
ms.assetid: 8239616c-788a-4073-8bbe-41f493a461de
ms.date: 08/08/2017
keywords: 
 -OID_GEN_MEDIA_CONNECT_STATUS_EX Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_MEDIA\_CONNECT\_STATUS\_EX


As a query, the OID\_GEN\_MEDIA\_CONNECT\_STATUS\_EX OID returns the connection state of an interface.

<a href="" id="windows-vista-and-later"></a>Windows Vista and later  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. For NDIS interface providers only.

Remarks
-------

NDIS uses this OID to query the connection state of an [NDIS network interface](https://msdn.microsoft.com/library/windows/hardware/ff566527) provider. Only NDIS interface providers, and therefore not miniport drivers or filter drivers, must support this OID as an OID request.

If the query succeeds, the interface provider returns NDIS\_STATUS\_SUCCESS, and the result of the query can be one of the values in the [**NET\_IF\_MEDIA\_CONNECT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff568744) enumeration.

Miniport drivers supply the media connect status during initialization and provide updates with status indications.

To specify the connection state in a miniport driver, set the **MediaConnectState** member of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure that the miniport driver passes to the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923)

[**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672)

[**NET\_IF\_MEDIA\_CONNECT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff568744)

[NDIS Network Interface OIDs](https://msdn.microsoft.com/library/windows/hardware/ff566545)

 

 




