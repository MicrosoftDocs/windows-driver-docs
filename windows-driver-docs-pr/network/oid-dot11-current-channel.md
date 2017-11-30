---
title: OID_DOT11_CURRENT_CHANNEL
author: windows-driver-content
description: OID_DOT11_CURRENT_CHANNEL
ms.assetid: 85f75cd8-ae9f-4dca-be9c-39e1c824d48c
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_CURRENT_CHANNEL Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_CURRENT\_CHANNEL


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_CURRENT\_CHANNEL object identifier (OID) requests that the miniport driver set the IEEE 802.11 **dot11CurrentChannel** or **dot11CurrentPrimaryChannel** management information base (MIB) object to the specified value for the current PHY type on the 802.11 station.

For the **dot11\_phy\_type\_ht** and **dot11\_phy\_type\_vht** PHY types, the OID sets the value of the **dot11CurrentPrimaryChannel** MIB object. For the **dot11\_phy\_type\_ht** operating in the 2.4 GHz band, the OID also sets the value of the **dot11CurrentChannel** MIB object.

When queried, this OID requests that the miniport driver return the value of the **dot11CurrentChannel** or **dot11CurrentPrimaryChannel** MIB object for the current PHY type. For the **dot11\_phy\_type\_ht** and **dot11\_phy\_type\_vht** PHY types, the miniport queries the **dot11CurrentPrimaryChannel** MIB object.

The **dot11CurrentChannel** MIB object defines the current operating frequency channel used by the PHY for transmit and receive operations. For more information about frequency channels, refer to clause 16.4.6.3 of the [IEEE 802.11-2012 standard](http://standards.ieee.org/getieee802/download/802.11-2012.pdf).

The **dot11CurrentPrimaryChannel** MIB object defines the location of the primary 20 MHz channel. For more information about this MIB object, see clause 20.4.2 of the [IEEE 802.11-2012 standard](http://standards.ieee.org/getieee802/download/802.11-2012.pdf) and clause 22.3.14 of IEEE Draft P802.11ac/D4.2.

For more information about 802.11n (HT) operation, refer to clause 10.15 of the [IEEE 802.11-2012 standard](http://standards.ieee.org/getieee802/download/802.11-2012.pdf).

For more information about 802.11ac operation, refer to clause 10.39 of IEEE Draft P802.11ac/D4.2.

The data type for OID\_DOT11\_CURRENT\_CHANNEL is a ULONG value that specifies the channel number.

This OID is valid only for the following PHY types:

-   Direct-sequence spread spectrum (DSSS) PHY (**dot11\_phy\_type\_dsss**).
-   High-rate DSSS (HRDSSS) PHY (**dot11\_phy\_type\_hrdsss**).
-   Extended-rate PHY (ERP) (**dot11\_phy\_type\_erp**).
-   High-Throughput (HT) PHY (**dot11\_phy\_type\_ht**).
-   Very High-Throughput (VHT) PHY (**dot11\_phy\_type\_vht**).

If the current PHY type is not set to one of these valid PHY types, the miniport driver must fail the query request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

**Note**  Support for OID\_DOT11\_CURRENT\_CHANNEL is mandatory if the NIC supports any of these valid PHY types. For more information about how the miniport driver specifies its list of supported PHY types, see [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](oid-dot11-supported-phy-types.md).

 

If the miniport driver is operating in the Extensible Station (ExtSTA) mode, the miniport driver fails a set request of OID\_DOT11\_CURRENT\_CHANNEL under the following conditions:

-   If the NIC is in a powered-off state, the miniport driver must fail the request by returning NDIS\_STATUS\_POWER\_STATE\_INVALID from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. For more information about power states, see [OID\_DOT11\_NIC\_POWER\_STATE](oid-dot11-nic-power-state.md).

-   If the 802.11 station is performing a scan request, the miniport driver can fail the set request by returning NDIS\_STATUS\_DOT11\_MEDIA\_IN\_USE from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. For more information about scan requests, see [OID\_DOT11\_SCAN\_REQUEST](oid-dot11-scan-request.md).

    The miniport driver can fail the set request if the 802.11 station is unable to change channels while performing the scan request.

-   If the miniport driver has enabled automatic PHY configuration, it can fail the set request if the 802.11 station manages the PHY-layer configuration. In this situation, the driver returns NDIS\_STATUS\_DOT11\_AUTO\_CONFIG\_ENABLED from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

    For more information about automatic PHY configuration, see [OID\_DOT11\_AUTO\_CONFIG\_ENABLED](oid-dot11-auto-config-enabled.md).

If the miniport driver is operating in Extensible Station (ExtSTA) mode, the current PHY type is determined through the ExtSTA **msDot11CurrentPhyID** MIB object. This MIB object specifies the index of the current PHY type within the 802.11 station's list of supported PHY types. For more information about **msDot11CurrentPhyID**, see [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md).

If the miniport driver is in Extensible Access Point (ExtAP) mode, the driver is responsible for implementing regulatory domain support in the NIC. The driver should therefore treat any channel or frequency set by the operating system in OID\_DOT11\_CURRENT\_CHANNEL or [OID\_DOT11\_CURRENT\_FREQUENCY](oid-dot11-current-frequency.md) to be only a suggestion. In response to query calls to these OIDs, the driver should return the actual channel or frequency values that the NIC is using. Whenever the driver adopts a channel or frequency, or it has started an AP, it should call the [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) function to make a [**DOT11\_PHY\_FREQUENCY\_ADOPTED\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff548735) indication to the operating system.

If the miniport driver supports the functionality of multiple MAC entities through [virtualization](https://msdn.microsoft.com/library/windows/hardware/ff571041), the driver should not return NDIS\_STATUS\_DOT11\_MEDIA\_IN\_USE if the medium is blocked by another MAC.

When the PHY is operating in 802.11n or 802.11ac mode, the miniport driver must report the primary channel when it completes the following:

-   Packet receive indications. For more information, see [Media-Specific OOB Data for Received 802.11 Packets](https://msdn.microsoft.com/library/windows/hardware/ff559169).

-   [Native 802.11 status indications](https://msdn.microsoft.com/library/windows/hardware/ff560685) that report channel information, such as [**DOT11\_PHY\_FREQUENCY\_ADOPTED\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff548735).
-   Query requests of OID\_DOT11\_CURRENT\_CHANNEL.

-   Query requests of [OID\_DOT11\_ENUM\_BSS\_LIST](oid-dot11-enum-bss-list.md).

    In this case, the miniport driver reports the primary channel in the **PhySpecificInfo** member of the [**DOT11\_BSS\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff547665) structure. The driver returns this structure when it completes the query request of OID\_DOT11\_ENUM\_BSS\_LIST.

For more information about 802.11ac 20/40/80/160/80+80 MHz mode, refer to the [IEEE P802.11ac standard (under development)](http://www.ieee802.org/11/Reports/tgac_update.md).

**Note**  When the miniport driver receives an [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) method request the miniport driver must reset the **dot11CurrentChannel** and **dot11CurrentPrimaryChannel** MIB objects to their default values under the following conditions:
-   When MIB values for the MAC and/or PHY are reset to their default values only if **bSetDefaultMIB** is set to TRUE.
-   When MAC or PHY values are affected by the value of the **dot11ResetType** member.

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_CURRENT_CHANNEL%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


