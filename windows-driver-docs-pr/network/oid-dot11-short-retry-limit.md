---
title: OID_DOT11_SHORT_RETRY_LIMIT
author: windows-driver-content
description: OID_DOT11_SHORT_RETRY_LIMIT
ms.assetid: ccf0f3ef-179d-4b9c-b98a-c942e4e37f59
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_SHORT_RETRY_LIMIT Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_SHORT\_RETRY\_LIMIT


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_SHORT\_RETRY\_LIMIT object identifier (OID) requests that the miniport driver return the value of the IEEE 802.11 **dot11ShortRetryLimit** management information base (MIB) object.

The **dot11ShortRetryLimit** MIB object specifies the maximum number of retransmission attempts made by the 802.11 station for MAC service data unit (MSDU) packets with lengths less than or equal to the value of the IEEE 802.11 **dot11RTSThreshold** MIB object. For more information about the **dot11RTSThreshold** MIB object, see [OID\_DOT11\_RTS\_THRESHOLD](oid-dot11-rts-threshold.md).

The data type for this OID is a ULONG value from 1 through 255.

When the 802.11 station exceeds the number of maximum number of retransmission attempts defined by the **dot11ShortRetryLimit** MIB object, it must do the following:

-   Discard the packet.

-   If the miniport driver is operating in Extensible Station (ExtSTA) mode, it must increment the **ullFailedCount** member of the DOT11\_STATISTICS structure. For more information about this structure, see [OID\_DOT11\_STATISTICS](oid-dot11-statistics.md).

The default value for the **dot11ShortRetryLimit** MIB object is seven. The miniport driver must set the MIB object to this default through its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function or when reset through [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md).

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

 

 




