---
title: OID_DOT11_ACTIVE_PHY_LIST
author: windows-driver-content
description: OID_DOT11_ACTIVE_PHY_LIST
ms.assetid: d285248b-aae8-440c-a63f-9acdf7379eb1
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_ACTIVE_PHY_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_ACTIVE\_PHY\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_ACTIVE\_PHY\_LIST object identifier (OID) requests that the miniport driver return the value of the Extensible Station (ExtSTA) **msDot11ActivePhyList** management information base (MIB) object.

The **msDot11ActivePhyList** MIB object specifies the PHYs on the 802.11 station that it can use for transmitting and receiving packets over the current basic service set (BSS) network connection. The miniport driver specifies the active PHY list when it makes an [NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION](ndis-status-dot11-association-completion.md) indication. This list must not change during the lifetime of the BSS network connection.

Each entry in the **msDot11ActivePhyList** MIB object is a PHY identifier (IDs), which can be one of the following:

-   An index into the table of supported PHYs as defined by the Native 802.11 Operational **msDot11SupportedPhyTypes** MIB object. For more information about PHY IDs and the **msDot11SupportedPhyTypes** MIB object, see [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](oid-dot11-supported-phy-types.md).

-   A PHY ID with the value of DOT11\_PHY\_ID\_ANY and is the wildcard PHY ID. If the **msDot11ActivePhyList** MIB object contains the wildcard PHY ID, the 802.11 station can use any supported PHY to operate in the BSS network.

The **msDot11ActivePhyList** MIB object does not define the PHY IDs that can be used by the 802.11 station for scan operations. The PHY IDs that the 802.11 station uses for scanning are specified when [OID\_DOT11\_SCAN\_REQUEST](oid-dot11-scan-request.md) is set.

The data type for this OID is the [**DOT11\_PHY\_ID\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff548738) structure.

When this OID is queried, the miniport driver must do the following:

-   If the 802.11 station is not connected to a BSS network, fail the query request by returning NDIS\_STATUS\_INVALID\_STATE from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   Verify that the **InformationBuffer** member of its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's *OidRequest* parameter is large enough to return the desired PHY ID list. For more information about this procedure, see [**DOT11\_PHY\_ID\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff548738).

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
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




