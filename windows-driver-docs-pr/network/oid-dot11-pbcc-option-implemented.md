---
title: OID_DOT11_PBCC_OPTION_IMPLEMENTED
author: windows-driver-content
description: OID_DOT11_PBCC_OPTION_IMPLEMENTED
ms.assetid: 38ef6940-05c1-42e4-a19e-68155f609239
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_PBCC_OPTION_IMPLEMENTED Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_PBCC\_OPTION\_IMPLEMENTED


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_PBCC\_OPTION\_IMPLEMENTED object identifier (OID) requests that the miniport driver return the value of the IEEE 802.11b **dot11PBCCOptionImplemented** management information base (MIB) object for the current PHY type on the 802.11 station.

The **dot11PBCCOptionImplemented** MIB object specifies whether the current PHY type supports enabled packet binary convolutional code (PBCC) modulation. For more information about PBCC modulation, refer to Clause 18.4.6.6 of the IEEE 802.11b-1999 standard.

The data type for OID\_DOT11\_PBCC\_OPTION\_IMPLEMENTED is a BOOLEAN value. A value of **TRUE** indicates that the current PHY type supports PBCC modulation.

The **dot11ERPPBCCOptionImplemented** MIB object is only valid for the following PHY types:

-   High-rate direct-sequence spread spectrum (HRDSS) PHY.

-   Extended-rate PHY (ERP).

If the current PHY type is not set to **dot11\_phy\_type\_hrdsss** or **dot11\_phy\_type\_erp**, the miniport driver must fail the query request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

If the miniport driver is operating in Extensible Station (ExtSTA) mode, the current PHY type is determined through the ExtSTA **msDot11CurrentPhyID** MIB object. This MIB object specifies the index of the current PHY type within the 802.11 station's list of supported PHY types. For more information about **msDot11CurrentPhyID**, see [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md).

**Note**  A Native 802.11 miniport driver that is designed to run on the Windows Vista or Windows Server 2008 operating systems must always reset this 802.11 MIB OID to its default value. This is the case regardless of the value of the **bSetDefaultMIB** member of the DOT11\_RESET\_REQUEST structure. This requirement applies to a miniport driver that, in a call to the **NdisMSetMiniportAttributes** function, sets **MiniportAttributes** -&gt; **Native\_802\_11\_Attributes** -&gt; **Header** -&gt; **Revision** to NDIS\_MINIPORT\_ADAPTER\_802\_11\_ATTRIBUTES\_REVISION\_1.

 

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


[Native 802.11 MIB OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560645)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




