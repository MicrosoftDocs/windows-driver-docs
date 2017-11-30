---
title: OID_DOT11_NIC_POWER_STATE
author: windows-driver-content
description: OID_DOT11_NIC_POWER_STATE
ms.assetid: ed05b714-7cdf-4996-bc5d-ab9baa67e11b
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_NIC_POWER_STATE Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_NIC\_POWER\_STATE


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_NIC\_POWER\_STATE object identifier (OID) requests that the miniport driver set the Native 802.11 Operational **msDot11NICPowerState** management information base (MIB) object to the specified value.

When queried, this OID requests that the miniport driver return the value of the **msDot11NICPowerState** MIB object.

The **msDot11NICPowerState** MIB object specifies the power state of the current PHY type on the 802.11 station.

The miniport driver must retain the value of the **msDot11NICPowerState** MIB object through any of the following:

-   Resets of the 802.11 station through a method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md).

-   Resets of the miniport driver through a call to the driver's [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function.

-   Calls to the miniport driver's [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) or [*MiniportShutdownEx*](https://msdn.microsoft.com/library/windows/hardware/ff559449) function. The driver must restore the value of the **msDot11NICPowerState** MIB object and the power state of the current PHY type whenever the driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.

The data type for OID\_DOT11\_NIC\_POWER\_STATE is a BOOLEAN value. A value of **TRUE** indicates that the PHY is turned on. In response to a value of **FALSE**, the miniport driver can either turn off the radio only for the current PHY, or it can turn off the radios for all supported PHYs.

After OID\_DOT11\_NIC\_POWER\_STATE is set, the 802.11 station must do the following:

-   If the 802.11 station is performing an explicit scan operation initiated through a set of [OID\_DOT11\_SCAN\_REQUEST](oid-dot11-scan-request.md), fail the set request by returning NDIS\_STATUS\_DOT11\_MEDIA\_IN\_USE from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   After all PHYs that use the radio are turned off, turn off the radio.

The following points apply to a miniport driver operating in Extensible Station (ExtSTA) mode:

-   The current PHY type is determined through the ExtSTA **msDot11CurrentPhyID** MIB object. This MIB object specifies the index of the current PHY type within the 802.11 station's list of supported PHY types. For more information about this MIB object, see [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md).

-   If the value of the **msDot11NICPowerState** MIB object is changed when OID\_DOT11\_NIC\_POWER\_STATE is set, the miniport driver must make an [NDIS\_STATUS\_DOT11\_PHY\_STATE\_CHANGED](ndis-status-dot11-phy-state-changed.md) indication. The miniport driver must also make this indication if the value of the **msDot11NICPowerState** MIB object is changed through a proprietary interface or OID implemented by the independent hardware vendor (IHV).

-   Some 802.11 NICs support a hardware setting on the computer for turning the PHY on or off. The ExtSTA **msDot11HardwarePHYState** MIB variable specifies the current hardware setting for the PHY. The 802.11 station must set the PHY's power state based on the **msDot11NICPowerState** and **msDot11HardwarePHYState** MIB variables. For more information about the **msDot11HardwarePHYState** MIB variable, see [NDIS\_STATUS\_DOT11\_PHY\_STATE\_CHANGED](ndis-status-dot11-phy-state-changed.md).

If the value of the **msDot11NICPowerState** MIB object has not been previously set, the miniport driver must use a default value of **TRUE** for this MIB object.

**Note**  If the miniport driver supports the functionality of multiple MAC entities through [virtualization](https://msdn.microsoft.com/library/windows/hardware/ff571041), the following requirements apply:
-   The **msDot11NICPowerState** MIB object applies to the same PHY on all such MAC entities.

-   If the operating system enables or disables a PHY through an OID set on one of the MAC entities, the driver should apply that change to the PHY on all virtualized MAC entities. The driver should then send appropriate [NDIS\_STATUS\_DOT11\_PHY\_STATE\_CHANGED](ndis-status-dot11-phy-state-changed.md) indications for all MAC entities, both physical and virtual.

-   The driver should not return NDIS\_STATUS\_DOT11\_MEDIA\_IN\_USE if the medium is blocked by another MAC.

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_NIC_POWER_STATE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


