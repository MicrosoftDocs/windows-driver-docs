---
title: OID\_DOT11\_SHORT\_RETRY\_LIMIT
author: windows-driver-content
description: OID\_DOT11\_SHORT\_RETRY\_LIMIT
ms.assetid: ccf0f3ef-179d-4b9c-b98a-c942e4e37f59
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_SHORT_RETRY_LIMIT Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_SHORT\_RETRY\_LIMIT


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_SHORT\_RETRY\_LIMIT object identifier (OID) requests that the miniport driver return the value of the IEEE 802.11 **dot11ShortRetryLimit** management information base (MIB) object.

The **dot11ShortRetryLimit** MIB object specifies the maximum number of retransmission attempts made by the 802.11 station for MAC service data unit (MSDU) packets with lengths less than or equal to the value of the IEEE 802.11 **dot11RTSThreshold** MIB object. For more information about the **dot11RTSThreshold** MIB object, see [OID\_DOT11\_RTS\_THRESHOLD](oid-dot11-rts-threshold.md).

The data type for this OID is a ULONG value from 1 through 255.

When the 802.11 station exceeds the number of maximum number of retransmission attempts defined by the **dot11ShortRetryLimit** MIB object, it must do the following:

-   Discard the packet.

-   If the miniport driver is operating in Extensible Station (ExtSTA) mode, it must increment the **ullFailedCount** member of the DOT11\_STATISTICS structure. For more information about this structure, see [OID\_DOT11\_STATISTICS](oid-dot11-statistics.md).

The default value for the **dot11ShortRetryLimit** MIB object is seven. The miniport driver must set the MIB object to this default through its [*MiniportInitializeEx*](miniportinitializeex.md) function or when reset through [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md).

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_SHORT_RETRY_LIMIT%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


