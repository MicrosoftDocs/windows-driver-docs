---
title: OID\_DOT11\_POWER\_MGMT\_REQUEST
author: windows-driver-content
description: OID\_DOT11\_POWER\_MGMT\_REQUEST
ms.assetid: 5b79d5e4-7b0a-4c70-93c6-957385356244
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_POWER_MGMT_REQUEST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_POWER\_MGMT\_REQUEST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_POWER\_MGMT\_REQUEST object identifier (OID) requests that the miniport driver set its Extensible Station (ExtSTA) **msDot11PowerSavingLevel** management information base (MIB) object to the specified data.

When queried, this OID requests that the miniport driver return the value of the **msDot11PowerSavingLevel** MIB object.

The **msDot11PowerSavingLevel** MIB object specifies the power management mode of the 802.11 station.

The data type for OID\_DOT11\_POWER\_MGMT\_REQUEST is a ULONG value, which specifies the level of power-saving activity performed by the 802.11 station.

The following power-saving levels are defined:

<a href="" id="dot11-power-saving-no-power-saving"></a>DOT11\_POWER\_SAVING\_NO\_POWER\_SAVING  
Specifies no power-saving activity performed by the 802.11 station.

**Note**  This is the default value for the **msDot11PowerSavingLevel** MIB object.

 

<a href="" id="dot11-power-saving-fast-psp"></a>DOT11\_POWER\_SAVING\_FAST\_PSP  
Specifies a power save polling (PSP) mode that uses the fastest power-saving mode. This power mode must provide the best combination of network performance and power usage.

<a href="" id="dot11-power-saving-max-psp"></a>DOT11\_POWER\_SAVING\_MAX\_PSP  
Specifies a PSP mode that uses the maximum (MAX) power saving capabilities. The MAX power save mode results in the greatest power savings for the radio on the 802.11 station.

<a href="" id="dot11-power-saving-maximum-level"></a>DOT11\_POWER\_SAVING\_MAXIMUM\_LEVEL  
Specifies a proprietary PSP mode implemented by the independent hardware vendor (IHV) that exceeds the DOT11\_POWER\_SAVING\_MAX\_PSP power-saving level.

**Note**  When the miniport driver receives an [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) method request the miniport driver must reset the **msDot11PowerSavingLevel** MIB object to its default value under the following conditions:
-   When MIB values for the MAC and/or PHY are reset to their default values only if **bSetDefaultMIB** is set to TRUE.
-   When MAC or PHY values are affected by the value of the **dot11ResetType** member.

 

The 802.11 station is required to support power-saving levels of DOT11\_POWER\_SAVING\_FAST\_PSP and DOT11\_POWER\_SAVING\_MAX\_PSP.

After the power-saving levels are changed to any value except DOT11\_POWER\_SAVING\_NO\_POWER\_SAVING, the 802.11 station must do the following:

-   If the 802.11 station is connected to a basic service set (BSS) network:

    -   If its transmit queue is not empty, announce its power management mode in the next packet it transmits. It does this by setting the Power Management subfield of the Frame Control field in the 802.11 MAC header of the transmitted frame.

        For more information about the Power Management subfield, refer to Clause 8.2.4.1.7 of the IEEE 802.11-2012 standard.

    -   If its transmit queue is empty, announce its power mode by creating and transmitting a frame containing only the 802.11 MAC header.

    -   After entering a power-save state, perform the power management procedures defined in Clause 10.2 of the IEEE 802.11-2012 standard.

-   If the 802.11 station is not connected to a BSS network:

    -   If the radio is turned on and the Native 802.11 Operational **msDot11NICPowerState** management information base (MIB) object is set to **TRUE**, turn off the radio and only turn on the radio when performing scan operations.

        For more information about the **msDot11NICPowerState** MIB object, see [OID\_DOT11\_NIC\_POWER\_STATE](oid-dot11-nic-power-state.md).

        For more information about scan operations, see [OID\_DOT11\_SCAN\_REQUEST](oid-dot11-scan-request.md).

    -   Retain the current value of the **msDot11NICPowerState** MIB object whenever the 802.11 station turns the radio off or on.

    -   When the radio is turned off or on, the miniport driver must not make an [NDIS\_STATUS\_DOT11\_PHY\_STATE\_CHANGED](ndis-status-dot11-phy-state-changed.md) indication.

The miniport driver must not change the power state of the 802.11 station when the driver's [*MiniportDevicePnPEventNotify*](https://msdn.microsoft.com/library/windows/hardware/ff559369) function is called for the **NdisDevicePnPEventPowerProfileChanged** event. The miniport driver must ignore this event and only make changes to the 802.11 station's power state when OID\_DOT11\_POWER\_MGMT\_REQUEST is set.

Starting with Windows 7, if the wireless adapter is set to a **Medium Power Saving** setting, the operating system enables DOT11\_POWER\_SAVING\_MAX\_PSP on the 802.11 station if one of the following is true:

-   The wireless adapter is not associated with an infrastructure network.

-   The wireless adapter is associated with an infrastructure network and the associated AP supports the Automatic Power Save Delivery (APSD) - Power Save mode.

**Note**  **Medium Power Saving** is the default **Power Saving Mode** behavior when the computer is in the **Balanced** power plan. These adapter settings are accessed through the **Power Options** control panel.

 

Starting with Windows 8, supporting Wi-Fi Direct requires that this OID is used to configure power level for all Wi-Fi Direct ports. The port availability period and power saving features are adapted to the power level requested.

When the power-saving level is set to DOT11\_POWER\_SAVING\_NO\_POWER\_SAVING the miniport should disable all power saving mechanisms on the WFD port, and provide the specific port maximum access to the radio.

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_POWER_MGMT_REQUEST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


