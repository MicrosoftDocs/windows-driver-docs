---
title: OID_DOT11_CURRENT_PHY_ID
author: windows-driver-content
description: OID_DOT11_CURRENT_PHY_ID
ms.assetid: 1f551f19-01e7-4e12-8399-977589ffca32
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_CURRENT_PHY_ID Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_CURRENT\_PHY\_ID


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_CURRENT\_PHY\_ID object identifier (OID) requests that the miniport driver set the value of the Extensible Station (ExtSTA) **msDot11CurrentPhyID** management information base (MIB) object to the specified value.

When queried, OID\_DOT11\_CURRENT\_PHY\_ID requests that the miniport driver return the value of the **msDot11CurrentPhyID** MIB object.

The **msDot11CurrentPhyID** MIB object specifies the PHY identifier (ID) that the miniport driver uses when PHY-layer OIDs are set or queried. Examples of PHY-layer OIDs are:

-   [OID\_DOT11\_HARDWARE\_PHY\_STATE](oid-dot11-hardware-phy-state.md)

-   [OID\_DOT11\_CURRENT\_CHANNEL](oid-dot11-current-channel.md)

-   [OID\_DOT11\_DIVERSITY\_SUPPORT](oid-dot11-diversity-support.md)

A PHY ID is an index into the table of supported PHYS as defined by the Native 802.11 Operational **msDot11SupportedPhyTypes** MIB object. For more information about PHY IDs and the **msDot11SupportedPhyTypes** MIB object, see [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](oid-dot11-supported-phy-types.md).

When OID\_DOT11\_CURRENT\_PHY\_ID is set, the miniport driver must fail the request if the specified PHY ID is greater than or equal to the number of entries defined by the **msDot11SupportedPhyTypes** MIB object. In this situation, the miniport driver must return NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

The data type for this OID is a ULONG value. The default value of the **msDot11CurrentPhyID** MIB object is zero. The miniport driver must set this MIB object to its default if any of the following occurs:

-   The miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made to reset the MAC layer of the 802.11 station and the **bSetDefaultMIB** member of the DOT11\_RESET\_REQUEST structure is **TRUE**.

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

 

 




