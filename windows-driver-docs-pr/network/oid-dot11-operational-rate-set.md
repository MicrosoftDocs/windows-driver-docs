---
title: OID_DOT11_OPERATIONAL_RATE_SET
author: windows-driver-content
description: OID_DOT11_OPERATIONAL_RATE_SET
ms.assetid: 4b22c1b2-1046-4e1c-880c-ab748f3ce1b0
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_OPERATIONAL_RATE_SET Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_OPERATIONAL\_RATE\_SET


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_OPERATIONAL\_RATE\_SET object identifier (OID) requests that the miniport driver set the operational data rates to the specified value.

When queried, this OID requests that the miniport driver return the set of operational data rates.

The data type for OID\_DOT11\_OPERATIONAL\_RATE\_SET is the [**DOT11\_RATE\_SET**](https://msdn.microsoft.com/library/windows/hardware/ff548759) structure, based on the IEEE 802.11 **dot11OperationalRateSet** management information base (MIB) object.

The operational rate set of the 802.11 station defines the rates at which the station can transmit data. The 802.11 station specifies the rates it supports in the Supported Rates information element (IE) of various 802.11 management frames, such as Beacon and Probe Response frames. For more information about the Supported Rates IE, refer to Clause 8.4.2.3 of the IEEE 802.11-2012 standard.

The 802.11 station also uses the operational rate set to determine whether it can connect to a BSS based on the Supported Rates IE from Beacons or Probe Response frames received within the BSS network. For more information about this process, refer to Clause 6.3 of the IEEE 802.11-2012 standard.

If the 802.11 station has not completed a scan request when OID\_DOT11\_OPERATIONAL\_RATE\_SET is set, it must use the specified operational rate set for the next 802.11 Probe Request frame that it transmits.

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

 

 




