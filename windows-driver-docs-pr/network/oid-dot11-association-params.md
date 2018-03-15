---
title: OID_DOT11_ASSOCIATION_PARAMS
author: windows-driver-content
description: OID_DOT11_ASSOCIATION_PARAMS
ms.assetid: 3d9af740-2efa-4a9e-a3e0-0af5c6745aac
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_ASSOCIATION_PARAMS Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_ASSOCIATION\_PARAMS


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_ASSOCIATION\_PARAMS OID requests that the miniport driver append a list of additional information elements (IEs) to the association request that the NIC sends to an access point in an infrastructure BSS network.

**Note**  Support for this OID is mandatory.

 

The data type for this OID is the [**DOT11\_ASSOCIATION\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff547648) structure.

When this OID is set, the NIC must behave as follows:

-   If the ExtSTA is in the INIT state, the NIC must complete the request.

-   If the ExtSTA is in the OP state, the NIC must fail the request and return error code NDIS\_STATUS\_INVALID\_STATE.

The NIC should place additional IEs at the end of the association request unless the additional IEs would cause the size of the frame to exceed the MAC management protocol data unit (MMPDU) limit. In this case, the NIC can discard the new additional IEs.

If the additional IEs are successfully added to the association request, the miniport driver should include these additional IEs in the association request frames that it reports in the [**DOT11\_ASSOCIATION\_COMPLETION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff547647) structure.

The miniport driver should clear its copy of the information in the association request if the **bSetDefaultMIB** member of the [DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) structure is **TRUE** and an OID\_DOT11\_RESET\_REQUEST method request is made to reset the MAC layer of the 802.11 station.

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


[**DOT11\_ASSOCIATION\_COMPLETION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff547647)

[**DOT11\_ASSOCIATION\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff547648)

[OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




