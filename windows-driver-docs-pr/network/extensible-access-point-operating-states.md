---
title: Extensible Access Point Operating States
description: Extensible Access Point Operating States
ms.assetid: 4a5436ed-0de9-4e93-8453-aea2d5bb7afd
keywords: ["extensible access point WDK Native 802.11 , operating states"]
---

# Extensible Access Point Operating States


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The Extensible Access Point (ExtAP) operation mode, available beginning with Windows 7, consists of the following states:

<a href="" id="initialization--init-"></a>**Initialization (INIT)**  
In this state, the 802.11 station is configured to serve as an 802.11 access point. New AP profile settings can be configured only if the NIC is in the INIT state.

During initialization, the 802.11 miniport driver must load the Native 802.11 Operational **msDot11NICPowerState** management information base (MIB) object on each PHY. This MIB object specifies the power state of the current PHY type on the 802.11 station. The corresponding radio must remain off until this setting is loaded and applied. The NIC can then change the radio state based on the value of **msDot11NICPowerState**.

If the value of **msDot11NICPowerState** is **FALSE**, the corresponding radio must remain off until **msDot11NICPowerState** is set to **TRUE** by [OID\_DOT11\_NIC\_POWER\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569392).

In addition, any 802.11 MAC or PHY extensions developed by the independent hardware vendor (IHV) can be configured in this state.

When the NIC is operating in the ExtAP INIT state, it can receive OIDs listed in the "ExtAP INIT" column of [Native 802.11 Extensible AP OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560596). During initialization, the NIC can receive additional OIDs, as listed in [OID\_DOT11\_START\_AP\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569418).

For more information about initialization requirements, see the following topics:

[Native 802.11 Miniport Driver Initialization](native-802-11-miniport-driver-initialization.md)

[OID\_DOT11\_START\_AP\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569418)

<a href="" id="operation--op-"></a>**Operation (OP)**
In this state, the 802.11 station is connected to or is attempting to connect to a BSS network. Only a few MAC- or PHY-layer attributes, such as 802.11 fragmentation and request-to-send (RTS) threshold values, can be configured in this state.

When the NIC is operating in the ExtAP OP state, it can receive NDIS OIDs listed in the "ExtAP OP" column of [Native 802.11 Extensible AP OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560596).

The NIC driver must turn off the radio when the NIC driver is halted. For an NDIS 6.0 or later miniport, the NDIS [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) handler is called to halt the NIC. For more information, see [Halting a Miniport Adapter](halting-a-miniport-adapter.md).

The miniport driver must support the following transitions between operating states:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Operating State Transition</th>
<th align="left">Operating System Action</th>
<th align="left">Miniport Driver Response</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>INIT to OP</p></td>
<td align="left"><p>Operating system sets [OID_DOT11_START_AP_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569418).</p></td>
<td align="left"><p>Driver configures the NIC to start the infrastructure network and to serve as an access point.</p></td>
</tr>
<tr class="even">
<td align="left"><p>OP to INIT</p></td>
<td align="left"><p>Operating system sets [OID_DOT11_RESET_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409).</p></td>
<td align="left"><p>Driver resets the specified IEEE layers of the 802.11 station and transitions to the INIT state.</p></td>
</tr>
</tbody>
</table>

 

 

 





