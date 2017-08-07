---
title: OID\_DOT11\_ASSOCIATION\_PARAMS
author: windows-driver-content
description: OID\_DOT11\_ASSOCIATION\_PARAMS
ms.assetid: 3d9af740-2efa-4a9e-a3e0-0af5c6745aac
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_ASSOCIATION_PARAMS Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_ASSOCIATION\_PARAMS


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_ASSOCIATION\_PARAMS OID requests that the miniport driver append a list of additional information elements (IEs) to the association request that the NIC sends to an access point in an infrastructure BSS network.

**Note**  Support for this OID is mandatory.

 

The data type for this OID is the [**DOT11\_ASSOCIATION\_PARAMS**](dot11-association-params.md) structure.

When this OID is set, the NIC must behave as follows:

-   If the ExtSTA is in the INIT state, the NIC must complete the request.

-   If the ExtSTA is in the OP state, the NIC must fail the request and return error code NDIS\_STATUS\_INVALID\_STATE.

The NIC should place additional IEs at the end of the association request unless the additional IEs would cause the size of the frame to exceed the MAC management protocol data unit (MMPDU) limit. In this case, the NIC can discard the new additional IEs.

If the additional IEs are successfully added to the association request, the miniport driver should include these additional IEs in the association request frames that it reports in the [**DOT11\_ASSOCIATION\_COMPLETION\_PARAMETERS**](dot11-association-completion-parameters.md) structure.

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


[**DOT11\_ASSOCIATION\_COMPLETION\_PARAMETERS**](dot11-association-completion-parameters.md)

[**DOT11\_ASSOCIATION\_PARAMS**](dot11-association-params.md)

[OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_ASSOCIATION_PARAMS%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


