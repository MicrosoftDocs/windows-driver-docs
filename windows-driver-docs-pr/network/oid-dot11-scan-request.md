---
title: OID_DOT11_SCAN_REQUEST
author: windows-driver-content
description: OID_DOT11_SCAN_REQUEST
ms.assetid: 84b62c71-f73c-4cb5-b00e-fb17d6b55851
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_SCAN_REQUEST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_SCAN\_REQUEST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_SCAN\_REQUEST object identifier (OID) requests that the 802.11 station perform a survey of all basic service set (BSS) networks within range of the NIC's radio. The 802.11 station performs the scan operation by using the parameters defined in the set request.

The data type for this OID is the [**DOT11\_SCAN\_REQUEST\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure.

When OID\_DOT11\_SCAN\_REQUEST is set, the miniport driver must fail the set request under the following conditions by returning the specified value from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Condition</th>
<th>Return value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>The <strong>uNumOfdot11SSIDs</strong> member of the [<strong>DOT11_SCAN_REQUEST_V2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure has a value greater than the value of <strong>uScanSSIDListSize</strong> that the driver previously returned through a query of [OID_DOT11_EXTSTA_CAPABILITY](oid-dot11-extsta-capability.md).</p>
<div class="alert">
<strong>Note</strong>  This condition is applicable only when the miniport driver is operating in Extensible Station (ExtSTA) mode.
</div>
<div>
 
</div></td>
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
</tr>
<tr class="even">
<td><p>The <strong>ChDescriptionType</strong> member of the [<strong>DOT11_SCAN_REQUEST_V2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure contains an invalid enumerator value.</p></td>
<td><p>NDIS_STATUS_BAD_VERSION</p></td>
</tr>
<tr class="odd">
<td><p>The <strong>dot11PhyType</strong> member of the [<strong>DOT11_PHY_TYPE_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548745) structure specifies a PHY type that is not supported by the 802.11 station.</p></td>
<td><p>NDIS_STATUS_BAD_VERSION</p></td>
</tr>
<tr class="even">
<td><p>The <strong>dot11PhyId</strong> member of the [<strong>DOT11_PHY_TYPE_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548745) structure is set to a value of DOT11_PHY_ID_ANY.</p></td>
<td><p>NDIS_STATUS_INVALID_DATA</p></td>
</tr>
<tr class="odd">
<td><p>The <strong>dot11PhyId</strong> member of the [<strong>DOT11_PHY_TYPE_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548745) structure is set to a value that is larger than the number of entries in the list of supported PHYs returned by the driver through a query of [OID_DOT11_SUPPORTED_PHY_TYPES](oid-dot11-supported-phy-types.md).</p></td>
<td><p>NDIS_STATUS_BAD_VERSION</p></td>
</tr>
<tr class="even">
<td><p>A scan initiated from a previous set of OID_DOT11_SCAN_REQUEST is not complete.</p></td>
<td><p>NDIS_STATUS_DOT11_MEDIA_IN_USE</p></td>
</tr>
<tr class="odd">
<td><p>The <strong>msDot11NICPowerState</strong> management information base (MIB) object is set to <strong>FALSE</strong>. For more information about this MIB object, see [OID_DOT11_NIC_POWER_STATE](oid-dot11-nic-power-state.md).</p></td>
<td><p>NDIS_STATUS_POWER_STATE_INVALID</p></td>
</tr>
<tr class="even">
<td><p>All of the PHYs in the list of PHY types are turned off through a hardware switch setting or proprietary software setting.</p></td>
<td><p>NDIS_STATUS_DOT11_POWER_STATE_INVALID</p></td>
</tr>
<tr class="odd">
<td><p>One or more of the PHYs in the list of PHY types are either not supported or have been disabled on the 802.11 station through a proprietary mechanism implemented by the independent hardware vendor (IHV).</p>
<p>This condition does not apply to PHYs disabled through a set request of [OID_DOT11_NIC_POWER_STATE](oid-dot11-nic-power-state.md).</p></td>
<td><p>NDIS_STATUS_UNSUPPORTED_MEDIA</p></td>
</tr>
<tr class="even">
<td><p>The list of PHY types includes a type that is not supported by the 802.11 station or contains a channel description that is not supported by the regulatory domain in which the station is operating.</p></td>
<td><p>NDIS_STATUS_BAD_VERSION</p></td>
</tr>
</tbody>
</table>

 

When performing the scan operation, the miniport driver and 802.11 station must follow the guidelines described in [Native 802.11 Scan Operations](https://msdn.microsoft.com/library/windows/hardware/ff560679). The miniport driver must not wait for the scan operation to finish before completing the set request. The driver must return NDIS\_STATUS\_SUCCESS from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function after initiating the scan operation.

If the miniport driver supports the functionality of multiple MAC entities through [virtualization](https://msdn.microsoft.com/library/windows/hardware/ff571041), the driver should not return NDIS\_STATUS\_DOT11\_MEDIA\_IN\_USE if the medium is blocked by another MAC.

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


[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




