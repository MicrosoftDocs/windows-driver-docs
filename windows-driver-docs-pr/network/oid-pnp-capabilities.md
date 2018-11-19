---
title: OID_PNP_CAPABILITIES
description: The OID_PNP_CAPABILITIES OID requests a miniport driver to return the wake-up capabilities of its network adapter or requests an intermediate driver to return the intermediate driver's wake-up capabilities.
ms.assetid: f2e3a867-d7d2-4d09-b84b-e8f8610b8535
ms.date: 08/08/2017
keywords: 
 -OID_PNP_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PNP\_CAPABILITIES


The OID\_PNP\_CAPABILITIES OID requests a miniport driver to return the wake-up capabilities of its network adapter or requests an intermediate driver to return the intermediate driver's wake-up capabilities. The wake-up capabilities are formatted as an **NDIS\_PNP\_CAPABILITIES** structure, which is defined as follows:

```C++
    typedef struct _NDIS_PNP_CAPABILITIES {
         ULONG Flags;
         NDIS_PM_WAKE_UP_CAPABILITIES WakeUpCapabilities;
    } NDIS_PNP_CAPABILITIES, *PNDIS_PNP_CAPABILITIES;  
```




The members of this structure contain the following information:

<a href="" id="flags"></a>**Flags**  
**NDIS\_DEVICE\_WAKE\_UP\_ENABLE**

NDIS sets this flag if the underlying miniport driver supports one or more wake-up capabilities. Protocol drivers can test this flag to determine whether an underlying miniport driver has wake-up capabilities. Miniport drivers should not access this flag.

<a href="" id="wakeupcapabilities"></a>**WakeUpCapabilities**  
An **NDIS\_PM\_WAKE\_UP\_CAPABILITIES** structure that specifies the wake-up capabilities of the miniport driver's network adapter. The **NDIS\_PM\_WAKE\_UP\_CAPABILITIES** structure is defined as follows:

```C++
typedef struct _NDIS_PM_WAKE_UP_CAPABILITIES {
         NDIS_DEVICE_POWER_STATE MinMagicPacketWakeUp;
         NDIS_DEVICE_POWER_STATE MinPatternWakeUp;
         NDIS_DEVICE_POWER_STATE MinLinkChangeWakeUp;
       } NDIS_PM_WAKE_UP_CAPABILITIES, *PNDIS_PM_WAKE_UP_CAPABILITIES;
```

The members of this structure contain the following information:

<a href="" id="minmagicpacketwakeup"></a>**MinMagicPacketWakeUp**  
Specifies the lowest device power state from which the miniport driver's network adapter can signal a wake-up on receipt of a magic packet. (A *magic packet* is a packet that contains 16 contiguous copies of the receiving network adapter's Ethernet address.) The device power state is specified as one of the following [**NDIS\_DEVICE\_POWER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/gg602135) values:

<a href="" id="ndisdevicestateunspecified"></a>**NdisDeviceStateUnspecified**  
The network adapter does not support magic-packet wake-ups.

<a href="" id="ndisdevicestated0"></a>**NdisDeviceStateD0**  
The network adapter can signal a magic-packet wake-up from device power state D0. Because D0 is the fully powered state, this does not cause a wake-up but can be used as a run-time event.

<a href="" id="ndisdevicestated1"></a>**NdisDeviceStateD1**  
The network adapter can signal a magic-packet wake-up from device power states D1 and D0.

<a href="" id="ndisdevicestated2"></a>**NdisDeviceStateD2**  
The network adapter can signal a magic-packet wake-up from device states D2, D1, and D0.

<a href="" id="ndisdevicestated3"></a>**NdisDeviceStateD3**  
The network adapter can signal a magic-packet wake-up from device power states D3, D2, D1, and D0.

<a href="" id="minpatternwakeup"></a>**MinPatternWakeUp**  
Specifies the lowest device power state from which the miniport driver's network adapter can signal a wake-up event on receipt of a network frame that contains a pattern specified by the protocol driver. The power state is specified as one of the following [**NDIS\_DEVICE\_POWER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/gg602135) values:

<a href="" id="ndisdevicestateunspecified"></a>**NdisDeviceStateUnspecified**  
The network adapter does not support pattern-match wake-ups.

<a href="" id="ndisdevicestated0"></a>**NdisDeviceStateD0**  
The network adapter can signal a pattern-match wake-up from device power state D0. Because D0 is the fully powered state, this does not cause a wake-up but can be used as a run-time event.

<a href="" id="ndisdevicestated1"></a>**NdisDeviceStateD1**  
The network adapter can signal a pattern-match wake-up from device power states D1 and D0.

<a href="" id="ndisdevicestated2"></a>**NdisDeviceStateD2**  
The network adapter can signal a pattern-match wake-up from device power states D2, D1, and D0.

<a href="" id="ndisdevicestated3"></a>**NdisDeviceStateD3**  
The network adapter can signal a pattern-match wake-up from device power states D3, D2, D1, and D0.

<a href="" id="minlinkchangewakeup"></a>**MinLinkChangeWakeUp**  
Reserved. NDIS ignores this member.

**For Miniport Drivers**

After the miniport driver completes initialization, both the protocol driver and NDIS can query the miniport driver with this OID to determine the following:

-   Whether the miniport driver is PM-aware.

-   The network adapter's capabilities of indicating network wake-up events.

If the miniport driver returns **NDIS\_STATUS\_SUCCESS** to a query of OID\_PNP\_CAPABILITIES, NDIS considers the miniport driver to be PM-aware. If the miniport driver returns **NDIS\_STATUS\_NOT\_SUPPORTED**, NDIS considers the miniport driver to be a legacy miniport driver that is not PM-aware.

When calling [**NdisMSetAttributesEx**](https://msdn.microsoft.com/library/windows/hardware/ff553623), a miniport driver that does not support wake-up capabilities but that can save and restore its network adapter state across a power-state transition can set the **NDIS\_ATTRIBUTE\_NO\_HALT\_ON\_SUSPEND** flag. Setting this flag prevents NDIS from calling the driver's *MiniportHalt* function before the system transitions to a low-power (sleeping) state. However, if the miniport driver returns **NDIS\_STATUS\_NOT\_SUPPORTED** in response to a query OID\_PNP\_CAPABILITIES, NDIS ignores the **NDIS\_ATTRIBUTE\_NO\_HALT\_ON\_SUSPEND** flag and halts the network adapter if the system goes into a low-power state.

A miniport driver's network adapter can support any combination of wake-up events, including no wake-up events. A miniport driver can still support power management even if its network adapter cannot not signal wake-up events. In this case, the only power management OIDs that the miniport driver supports in addition to OID\_PNP\_CAPABILITIES are [OID\_PNP\_QUERY\_POWER](oid-pnp-query-power.md) and [OID\_PNP\_SET\_POWER](oid-pnp-set-power.md).

If a miniport driver's network adapter does not support a particular wake-up event, the miniport driver should indicate an [**NDIS\_DEVICE\_POWER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/gg602135) value of **NdisDeviceStateUnspecified** for the wake-up event in the **NDIS\_PM\_WAKE\_UP\_CAPABILITIES** structure.

OID\_PNP\_CAPABILITIES only indicates the wake-up capabilities of a miniport driver' s network adapter; it does not enable such capabilities. [OID\_PNP\_ENABLE\_WAKE\_UP](oid-pnp-enable-wake-up.md) is used to enable a network adapter's wake-up capabilities.

**For Intermediate Drivers**

If the underlying network adapter is PM-aware, the intermediate driver should return **NDIS\_STATUS\_SUCCESS** to a query of OID\_PNP\_CAPABILITIES. In the **NDIS\_PM\_WAKE\_UP\_CAPABILITIES** structure returned by this OID, the intermediate driver should specify a device power state of **NdisDeviceStateUnspecified** for each wake-up capability ( **MinMagicPacketWakeUp** or **MinPatternWakeUp**). Such a response indicates that the intermediate driver is PM-aware but does not manage a physical device.

If the underlying network adapter is not PM-aware, the intermediate driver should return **NDIS\_STATUS\_NOT\_SUPPORTED** to a query of OID\_PNP\_CAPABILITIES.

**Note**  For information about how NDIS 6.20 and later miniport drivers report power management capabilities, see [Reporting Power Management Capabilities](https://msdn.microsoft.com/library/windows/hardware/ff570672).

 

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
<td><p>Supported in NDIS 6.0 and NDIS 6.1. For NDIS 6.20 and later, use <a href="oid-pm-current-capabilities.md" data-raw-source="[OID_PM_CURRENT_CAPABILITIES](oid-pm-current-capabilities.md)">OID_PM_CURRENT_CAPABILITIES</a> instead.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_DEVICE\_POWER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/gg602135)

[**NdisMSetAttributesEx**](https://msdn.microsoft.com/library/windows/hardware/ff553623)

[OID\_PM\_CURRENT\_CAPABILITIES](oid-pm-current-capabilities.md)

[OID\_PNP\_ENABLE\_WAKE\_UP](oid-pnp-enable-wake-up.md)

[OID\_PNP\_QUERY\_POWER](oid-pnp-query-power.md)

[OID\_PNP\_SET\_POWER](oid-pnp-set-power.md)

[Reporting Power Management Capabilities](https://msdn.microsoft.com/library/windows/hardware/ff570672)

 

 




