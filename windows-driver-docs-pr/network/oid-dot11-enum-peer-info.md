---
title: OID_DOT11_ENUM_PEER_INFO
author: windows-driver-content
description: OID_DOT11_ENUM_PEER_INFO
ms.assetid: d836f261-b335-4284-9d5b-79ebb9943a02
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_ENUM_PEER_INFO Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_ENUM\_PEER\_INFO


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_ENUM\_PEER\_INFO object identifier (OID) requests that the miniport driver return information on all peer stations within an infrastructure basic service set (BSS) network. The miniport driver must fill in the members of a DOT11\_PEER\_INFO\_LIST structure.

**Note**  Support for this OID is mandatory.

 

The data type for this OID is the [**DOT11\_PEER\_INFO\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff548719) structure.

The miniport driver must also verify that the input buffer is large enough to hold all the data in the DOT11\_PEER\_INFO\_LIST structure.

If the input buffer is not large enough, in the call to the NDIS [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function, set *OidRequest* . **Data** . **BytesNeeded** to the number of bytes required and return the status indication NDIS\_STATUS\_INVALID\_LENGTH so that the 802.11 framework can allocate a buffer of sufficient size before it makes the next function call.

If the input buffer is large enough to hold all the data in the DOT11\_PEER\_INFO\_LIST structure, the miniport driver must return a list of [**DOT11\_PEER\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff548713) structures and set *OidRequest*.**Data**.**BytesNeeded** to the number of bytes that the miniport driver returns.

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
<td><p>Available in Windows 7 and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




