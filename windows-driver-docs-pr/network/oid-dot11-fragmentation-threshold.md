---
title: OID_DOT11_FRAGMENTATION_THRESHOLD
author: windows-driver-content
description: OID_DOT11_FRAGMENTATION_THRESHOLD
ms.assetid: 4b2fe2e0-2a6d-4dbb-b46c-7de32f38a349
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_FRAGMENTATION_THRESHOLD Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_FRAGMENTATION\_THRESHOLD


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_FRAGMENTATION\_THRESHOLD object identifier (OID) requests that the miniport driver set the value of the IEEE 802.11 **dot11FragmentationThreshold** management information base (MIB) object to the specified value.

When queried, OID\_DOT11\_FRAGMENTATION\_THRESHOLD requests that the miniport driver return the value of the **dot11FragmentationThreshold** MIB object.

This MIB object specifies the current maximum size, in bytes, of the MAC protocol data unit (MPDU) frame that the PHY can transmit.

The 802.11 station fragments a MAC service data unit (MSDU) packet if the payload length (plus the 802.11 MAC header and trailer) exceeds the value of **dot11FragmentationThreshold**.

The data type for OID\_DOT11\_FRAGMENTATION\_THRESHOLD is a ULONG value that specifies the fragmentation threshold in bytes.

The **aMPDUMaxLength** attribute of the current PHY type on the 802.11 station determines the range of values for the **dot11FragmentationThreshold** MIB object, and is based on the following formula:

```
256 <= dot11FragmentationThreshold <= min(2346, aMPDUMaxLength PHY attribute)
```

When OID\_DOT11\_FRAGMENTATION\_THRESHOLD is set, the 802.11 station must do the following:

-   After the set request, use the new fragmentation threshold value on all MSDU packets issued by the operating system to the miniport driver's [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function.

-   Either use the new fragmentation threshold value on all MSDU packets that are pending in the station's transmit queue, or continue to use the old fragmentation threshold value for the pending MSDU packets.

When OID\_DOT11\_FRAGMENTATION\_THRESHOLD is set, the 802.11 station must not apply the new fragmentation threshold value on the MSDU packet that the station is transmitting.

The following points apply to a miniport driver operating in Extensible Station (ExtSTA) mode:

-   If the miniport driver has enabled automatic MAC configuration, it can fail the set request if the 802.11 station manages the MAC-layer configuration. In this situation, the driver returns NDIS\_STATUS\_DOT11\_AUTO\_CONFIG\_ENABLED from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

    For more information about the automatic MAC configuration, see [OID\_DOT11\_AUTO\_CONFIG\_ENABLED](oid-dot11-auto-config-enabled.md).

-   The current PHY type is determined through the ExtSTA **msDot11CurrentPhyID** MIB object. This MIB object specifies the index of the current PHY type within the 802.11 station's list of supported PHY types. For more information about **msDot11CurrentPhyID**, see [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md).

The default value for the **dot11FragmentationThreshold** MIB object depends on the IEEE 802.11 **aMPDUMaxLength** attribute of the current PHY type on the 802.11 station based on the following formula:

```
dot11FragmentationThreshold = min(2346, aMPDUMaxLength)
```

The miniport driver must set the **dot11FragmentationThreshold** MIB object to this default when all of the following apply:

-   A set request of [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md) changes the current PHY type.

-   The miniport driver initializes the current PHY type through its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made to reset the MAC layer of the 802.11 station and the **bSetDefaultMIB** member of the DOT11\_RESET\_REQUEST structure is **TRUE**.

For more information about the **aMPDUMaxLength** PHY attribute, see [OID\_DOT11\_MPDU\_MAX\_LENGTH](oid-dot11-mpdu-max-length.md).

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

 

 




