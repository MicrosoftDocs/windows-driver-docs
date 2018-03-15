---
title: OID_DOT11_CURRENT_FREQUENCY
author: windows-driver-content
description: OID_DOT11_CURRENT_FREQUENCY
ms.assetid: 8e164bef-0a83-41cb-a287-82d67553a611
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_CURRENT_FREQUENCY Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_CURRENT\_FREQUENCY


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_CURRENT\_FREQUENCY object identifier (OID) requests that the miniport driver set the value of the IEEE 802.11a **dot11CurrentFrequency** management information base (MIB) object for the current PHY type on the 802.11 station.

When queried, OID\_DOT11\_CURRENT\_FREQUENCY requests that the miniport driver return the value of the **dot11CurrentFrequency** MIB object.

This MIB object defines the current operating frequency channel used by the PHY.

**Note**  Support for OID\_DOT11\_CURRENT\_FREQUENCY is mandatory if the NIC supports the **dot11\_phy\_type\_ofdm** PHY type. For more information about how the miniport driver specifies its list of supported PHY types, see [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](oid-dot11-supported-phy-types.md).

 

The data type for OID\_DOT11\_CURRENT\_FREQUENCYis a ULONG value from 0 through 200.

**Note**  If a service provided by the independent hardware vendor (IHV) is managing the wireless network profiles, the IHV can use whatever value range it supports.

 

The **dot11CurrentFrequency** MIB object is only valid for the orthogonal frequency division multiplexing (OFDM) PHY type. If the current PHY type is not set to **dot11\_phy\_type\_ofdm**, the miniport driver must fail the query request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

When OID\_DOT11\_CURRENT\_FREQUENCY is set, the miniport driver fails the request under the following conditions:

-   If the current PHY type is in a powered-off state, the miniport driver must fail the request by returning NDIS\_STATUS\_POWER\_STATE\_INVALID from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. For more information about power states, see [OID\_DOT11\_NIC\_POWER\_STATE](oid-dot11-nic-power-state.md).

-   If the 802.11 station is currently performing a scan request, the miniport driver must fail the set request by returning NDIS\_STATUS\_DOT11\_MEDIA\_IN\_USE from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. For more information about scan requests, see [OID\_DOT11\_SCAN\_REQUEST](oid-dot11-scan-request.md).

If the miniport driver is operating in the Extensible Station (ExtSTA) mode, it fails the set request of OID\_DOT11\_CURRENT\_FREQUENCY under the following conditions:

-   If the desired BSS type is **dot11\_BSS\_type\_infrastructure**, the miniport driver must fail the set request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. For more information about the desired BSS type, see [OID\_DOT11\_DESIRED\_BSS\_TYPE](oid-dot11-desired-bss-type.md).

-   If the miniport driver has enabled automatic PHY configuration, it can fail the set request if the 802.11 station manages the PHY-layer configuration. In this situation, the driver returns NDIS\_STATUS\_DOT11\_AUTO\_CONFIG\_ENABLED from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

    For more information about automatic PHY configuration, see [OID\_DOT11\_AUTO\_CONFIG\_ENABLED](oid-dot11-auto-config-enabled.md).

If the miniport driver is operating in ExtSTA mode, the current PHY type is determined through the ExtSTA **msDot11CurrentPhyID** MIB object. This MIB object specifies the index of the current PHY type within the 802.11 station's list of supported PHY types. For more information about **msDot11CurrentPhyID**, see [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md).

If the miniport driver supports the functionality of multiple MAC entities through [virtualization](https://msdn.microsoft.com/library/windows/hardware/ff571041), the driver should not return NDIS\_STATUS\_DOT11\_MEDIA\_IN\_USE if the medium is blocked by another MAC.

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

 

 




