---
title: OID\_DOT11\_HARDWARE\_PHY\_STATE
author: windows-driver-content
description: OID\_DOT11\_HARDWARE\_PHY\_STATE
ms.assetid: 74ddc4d9-166c-4e80-996e-b63cab7938aa
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_HARDWARE_PHY_STATE Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_HARDWARE\_PHY\_STATE


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_HARDWARE\_PHY\_STATE object identifier (OID) requests that the miniport driver return the value of the Extensible Station (ExtSTA) **msDot11HardwarePHYState** management information base (MIB) object.

The **msDot11HardwarePHYState** MIB object defines the power state of the current PHY type on the 802.11 station.

The data type for OID\_DOT11\_HARDWARE\_PHY\_STATE is a BOOLEAN value. A value of **TRUE** indicates that the PHY is turned on.

Some 802.11 NICs support a hardware setting on the computer for turning the PHY on or off. The OID\_DOT11\_HARDWARE\_PHY\_STATE OID queries power state of the current PHY type based on the hardware setting.

When OID\_DOT11\_HARDWARE\_PHY\_STATE is queried, the miniport driver must set the returned BOOLEAN value as follows:

-   If the NIC does support a hardware setting, the value must be **FALSE** (if the PHY is turned off) or **TRUE** (if the PHY is turned on).

-   If the NIC does not support a hardware setting, the value must be **TRUE**.

Software settings for the PHY power state are made through the Native 802.11 Operational **msDot11NICPowerState** MIB variable. For more information about this MIB variable, see [OID\_DOT11\_NIC\_POWER\_STATE](oid-dot11-nic-power-state.md).

The 802.11 station must set the PHY's power state based on the **msDot11NICPowerState** and **msDot11HardwarePHYState** MIB variables in the following way:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>msDot11NICPowerState value</th>
<th>msDot11HardwarePHYState value</th>
<th>PHY power state</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>TRUE</strong></p></td>
<td><p><strong>TRUE</strong></p></td>
<td><p>Turned on</p></td>
</tr>
<tr class="even">
<td><p><strong>FALSE</strong></p></td>
<td><p><strong>TRUE</strong></p></td>
<td><p>Turned off</p></td>
</tr>
<tr class="odd">
<td><p><strong>TRUE</strong></p></td>
<td><p><strong>FALSE</strong></p></td>
<td><p>Turned off</p></td>
</tr>
<tr class="even">
<td><p><strong>FALSE</strong></p></td>
<td><p><strong>FALSE</strong></p></td>
<td><p>Turned off</p></td>
</tr>
</tbody>
</table>

 

The current PHY type is determined through the ExtSTA **msDot11CurrentPhyID** MIB object. This MIB object specifies the index (ID) of the current PHY type within the 802.11 station's list of supported PHY types. For more information about this MIB object, see [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md).

The miniport driver must make an [NDIS\_STATUS\_DOT11\_PHY\_STATE\_CHANGED](ndis-status-dot11-phy-state-changed.md) indication whenever the value of the **msDot11HardwarePHYState** MIB object changes.

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_HARDWARE_PHY_STATE%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


