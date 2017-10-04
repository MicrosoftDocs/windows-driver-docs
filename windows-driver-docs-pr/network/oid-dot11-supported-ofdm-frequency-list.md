---
title: OID_DOT11_SUPPORTED_OFDM_FREQUENCY_LIST
author: windows-driver-content
description: OID\_DOT11\_SUPPORTED\_OFDM\_FREQUENCY\_LIST
ms.assetid: d6b22bc7-27c2-44cb-8f33-17e04596e0b1
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_SUPPORTED_OFDM_FREQUENCY_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_SUPPORTED\_OFDM\_FREQUENCY\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_SUPPORTED\_OFDM\_FREQUENCY\_LIST OID requests that the miniport driver returns the list of channel center frequencies that the 802.11 station can operate with.

The data type for this OID is the [**DOT11\_SUPPORTED\_OFDM\_FREQUENCY\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff548800) structure.

You can use this OID to indicate to the operating system any frequency channels that should be scanned for conformance with performance specifications. The operating system does not use these OIDs during routine operation of the 802.11 station.

The OID MIB object is only valid for the following PHY types:

-   Orthogonal frequency division multiplexing (OFDM) PHY.
-   High-throughput (HT) 802.11n PHY or very high-throughput (VHT) 802.11ac PHY when operating in the 5-GHz band.

If the current PHY type is not set to **dot11\_phy\_type\_ofdm**, **dot11\_phy\_type\_ht**, or **dot11\_phy\_type\_vht**, the miniport driver must fail the query request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

Support for this OID is optional, unless the station reports to the operating system that it supports the **dot11\_phy\_type\_ofdm** PHY type. In this case support for this OID is mandatory.

If the miniport driver is operating in Extensible Station (ExtSTA) mode, the current PHY type is determined through the ExtSTA **msDot11CurrentPhyID** management information base (MIB) object. This MIB object specifies the index of the current PHY type within the 802.11 station's list of supported PHY types. For more information about **msDot11CurrentPhyID**, see [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md).

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
<td><p>Available in Windows 7 and later versions of the Windows operating systems.</p></td>
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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_SUPPORTED_OFDM_FREQUENCY_LIST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


