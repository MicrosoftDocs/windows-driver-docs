---
title: OID_DOT11_TEMP_TYPE
author: windows-driver-content
description: OID_DOT11_TEMP_TYPE
ms.assetid: dbfcb23a-5c59-4c03-acd8-46d61b71ab21
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_TEMP_TYPE Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_TEMP\_TYPE


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_TEMP\_TYPE object identifier (OID) requests that the miniport driver return the value of the IEEE 802.11 **dot11TempType** management information base (MIB) object for the current PHY type on the 802.11 station.

This MIB object specifies the operating temperature range of the current PHY type.

The data type for OID\_DOT11\_TEMP\_TYPE is the [**DOT11\_TEMP\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff548806) enumeration.

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

 

 




