---
title: OID_DOT11_MPDU_MAX_LENGTH
author: windows-driver-content
description: OID_DOT11_MPDU_MAX_LENGTH
ms.assetid: f278f5ec-ad01-41e8-ab14-a245d46f127e
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_MPDU_MAX_LENGTH Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_MPDU\_MAX\_LENGTH


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_MPDU\_MAX\_LENGTH object identifier (OID) requests that the miniport driver return the value of the IEEE 802.11 **aMPDUMaxLength** attribute for the current PHY type on the 802.11 station.

The data type for this OID is a **ULONG** value.

The **aMPDUMaxLength** attribute defines the maximum length, in bytes, of a MAC protocol data unit (MPDU) frame that the PHY can transmit or receive. The following table lists the values of this attribute for the various 802.11 PHY types supported.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>PHY type</th>
<th>aMPDUMaxLength value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>dot11_phy_type_fhss</strong></p></td>
<td><p>4095 bytes</p></td>
</tr>
<tr class="even">
<td><p><strong>dot11_phy_type_dsss</strong></p></td>
<td><p>4-8191 bytes</p></td>
</tr>
<tr class="odd">
<td><p><strong>dot11_phy_type_irbaseband</strong></p></td>
<td><p>2500 bytes</p></td>
</tr>
<tr class="even">
<td><p><strong>dot11_phy_type_ofdm</strong></p></td>
<td><p>4095 bytes</p></td>
</tr>
<tr class="odd">
<td><p><strong>dot11_phy_type_hrdsss</strong></p></td>
<td><p>4095 bytes</p></td>
</tr>
<tr class="even">
<td><p><strong>dot11_phy_type_erp</strong></p></td>
<td><p>4095 bytes</p></td>
</tr>
</tbody>
</table>

 

**Note**  The **dot11\_phy\_type\_ht** and **dot11\_phy\_type\_vht** PHY types do not appear in the table, because they have no **aMPDUMaxLength** attribute.

 

If the miniport driver is operating in Extensible Station (ExtSTA) mode, the current PHY type is determined through the ExtSTA **msDot11CurrentPhyID** management information base (MIB) object. This MIB object specifies the index of the current PHY type within the 802.11 station's list of supported PHY types. For more information about this MIB object, see [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md).

If the **aMPDUMaxLength** value changes, the miniport driver must make a media-specific [NDIS\_STATUS\_DOT11\_MPDU\_MAX\_LENGTH\_CHANGED](ndis-status-dot11-mpdu-max-length-changed.md) indication. This indication notifies the operating system of the change in the maximum MPDU length supported on the 802.11 station.

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


[**DOT11\_PHY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff548741)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




