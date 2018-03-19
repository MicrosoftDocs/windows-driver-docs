---
title: OID_DOT11_CF_POLLABLE
author: windows-driver-content
description: OID_DOT11_CF_POLLABLE
ms.assetid: 1eb80044-5303-4f81-b821-59376f60ff34
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_CF_POLLABLE Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_CF\_POLLABLE


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_CF\_POLLABLE object identifier (OID) requests that the miniport driver return the value of the IEEE 802.11 **dot11CFPollable** management information base (MIB) object.

The **dot11CFPollable** MIB object specifies whether the 802.11 station supports the contention free (CF) access method and CF-Poll frames.

The data type for OID\_DOT11\_CF\_POLLABLE is a BOOLEAN value. A value of **TRUE** indicates that the 802.11 station supports CF-Poll frames.

**Note**  The MIB object is **TRUE** only if the 802.11 station can respond to a CF-Poll frame with an MPDU data frame within a short interframe space (SIFS) time.

 

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

 

 




