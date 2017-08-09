---
title: OID\_DOT11\_FRAGMENTATION\_THRESHOLD
author: windows-driver-content
description: OID\_DOT11\_FRAGMENTATION\_THRESHOLD
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_FRAGMENTATION_THRESHOLD%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


