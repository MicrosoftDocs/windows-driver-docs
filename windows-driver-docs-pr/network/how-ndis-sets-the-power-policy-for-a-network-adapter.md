---
title: How NDIS Sets the Power Policy for a Network Adapter
description: How NDIS Sets the Power Policy for a Network Adapter
ms.assetid: ede0e33d-16f9-45ec-9e9d-b188f6360b2f
keywords:
- network interface cards WDK networking , power policy
- NICs WDK networking , power policy
- power policy WDK networking
- DEVICE_CAPABILITIES
- OID_PNP_CAPABILITIES
- device power policy owner WDK networking
- power management WDK NDIS miniport , power policy
- user input WDK power management
- power management WDK NDIS miniport , user input
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How NDIS Sets the Power Policy for a Network Adapter





NDIS serves as the device power policy owner for each network device. As such, NDIS sets and administers the power policy for each network device. For more information about managing device power policy, see [Managing Device Power Policy](https://msdn.microsoft.com/library/windows/hardware/ff554355).

NDIS uses the following information to set the power policy for a NIC:

-   The [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure that the bus driver returns in response to an [**IRP\_MN\_QUERY\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664) request that NDIS issued.

-   The miniport driver's response to an [OID\_PNP\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569774) request issued by NDIS.

-   User input from the user interface (UI).

### <a href="" id="using-the-device-capabilities-structure"></a>Using the DEVICE\_CAPABILITIES Structure

When a NIC is enumerated, NDIS queries the NIC's capabilities by issuing, in addition to other requests, an [**IRP\_MN\_QUERY\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664) request. In response to this request, the bus driver returns a [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure. NDIS copies this structure and uses the following information from this structure when setting the power policy for the NIC.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543085" data-raw-source="[DeviceD1 and DeviceD2](https://msdn.microsoft.com/library/windows/hardware/ff543085)">DeviceD1 and DeviceD2</a></p></td>
<td align="left"><p>TRUE if the device supports the D1 power state.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543085" data-raw-source="[DeviceD1 and DeviceD2](https://msdn.microsoft.com/library/windows/hardware/ff543085)">DeviceD1 and DeviceD2</a></p></td>
<td align="left"><p>TRUE if the device supports the D2 power state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565609" data-raw-source="[WakeFromD0, WakeFromD1, WakeFromD2, and WakeFromD3](https://msdn.microsoft.com/library/windows/hardware/ff565609)">WakeFromD0, WakeFromD1, WakeFromD2, and WakeFromD3</a></p></td>
<td align="left"><p>TRUE if the device can respond to an external wake signal while in the D0 power state.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565609" data-raw-source="[WakeFromD0, WakeFromD1, WakeFromD2, and WakeFromD3](https://msdn.microsoft.com/library/windows/hardware/ff565609)">WakeFromD0, WakeFromD1, WakeFromD2, and WakeFromD3</a></p></td>
<td align="left"><p>TRUE if the device can respond to an external wake signal while in the D1 power state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565609" data-raw-source="[WakeFromD0, WakeFromD1, WakeFromD2, and WakeFromD3](https://msdn.microsoft.com/library/windows/hardware/ff565609)">WakeFromD0, WakeFromD1, WakeFromD2, and WakeFromD3</a></p></td>
<td align="left"><p>TRUE if the device can respond to an external wake signal while in the D2 power state.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565609" data-raw-source="[WakeFromD0, WakeFromD1, WakeFromD2, and WakeFromD3](https://msdn.microsoft.com/library/windows/hardware/ff565609)">WakeFromD0, WakeFromD1, WakeFromD2, and WakeFromD3</a></p></td>
<td align="left"><p>TRUE if the device can respond to an external wake signal while in the D3 power state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543087" data-raw-source="[DeviceState](https://msdn.microsoft.com/library/windows/hardware/ff543087)">DeviceState</a><strong>[PowerSystemMaximum]</strong></p></td>
<td align="left"><p>Specifies the highest-powered device state that this device can maintain for each system power state, from <strong>PowerSystemUnspecified</strong> to <strong>PowerSystemShutdown</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564538" data-raw-source="[SystemWake](https://msdn.microsoft.com/library/windows/hardware/ff564538)">SystemWake</a></p></td>
<td align="left"><p>Specifies lowest-powered system power state (S0 through S4) from which the device can signal a wake event.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543091" data-raw-source="[DeviceWake](https://msdn.microsoft.com/library/windows/hardware/ff543091)">DeviceWake</a></p></td>
<td align="left"><p>Specifies lowest-powered device power state (D0 through D3) from which the device can signal a wake event.</p></td>
</tr>
</tbody>
</table>

 

NDIS uses the DEVICE\_CAPABILITIES information to determine if:

-   Both the system and the NIC support power management, and if so, which device power states the NIC can be in for each system power state.

-   Both the system and the NIC support wake-on-LAN, and if so, from which device power states the NIC can wake the system.

**WakeFromD0** through **WakeFromD3** indicate the device power states from which the NIC can wake the system.

The **DeviceState** array indicates, for each system power state, the highest-powered device power state in which the NIC can be and still support that system power state. For example, consider the following array values.

```cpp
DeviceState[PowerSystemWorking] PowerDeviceD0
DeviceState[PowerSystemSleeping1] PowerDeviceD1
DeviceState[PowerSystemSleeping2] PowerDeviceD2
DeviceState[PowerSystemSleeping3] PowerDeviceD2
DeviceState[PowerSystemHibernate] PowerDeviceD3
DeviceState[PowerSystemShutdown] PowerDeviceD3
```

As indicated by the preceding array of sample values, when the system is in system power state S1, the NIC can be in device power state D1, D2, or D3. When the system is in system power state S2 or S3, the NIC can be in device power state D2 or D3.

To determine whether both the system and NIC support wake-on-LAN, NDIS examines both the **SystemWake** and **DeviceWake** members. If both **SystemWake** and **DeviceWake** are set to **PowerSystemUnspecified**, NDIS treats the NIC as capable of power management. In this case, or if the miniport driver set the NDIS\_ATTRIBUTE\_NO\_HALT\_ON\_SUSPEND flag during initialization, NDIS subsequently issues the miniport driver an [OID\_PNP\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569774) request to obtain more information about the NIC's wake-up capabilities.

### <a href="" id="using-oid-pnp-capabilities"></a>Using OID\_PNP\_CAPABILITIES

After a miniport driver successfully returns from its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, NDIS sends an OID\_PNP\_CAPABILITIES request to the driver if either of the following is true:

-   Both the **SystemWake** and **DeviceWake** members of the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure that is returned by the bus driver are *not* set to **PowerSystemUnspecified**.

-   The miniport driver set the NDIS\_ATTRIBUTE\_NO\_HALT\_ON\_SUSPEND flag when it called [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) during initialization.

Note that NDIS issues an OID\_PNP\_CAPABILITIES request regardless of whether the user has enabled wake-on-LAN in the user interface.

If the miniport driver returns NDIS\_STATUS\_SUCCESS in response to a query of [OID\_PNP\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569774), NDIS treats the miniport driver as power management-capable. If the miniport driver returns NDIS\_STATUS\_NOT\_SUPPORTED, NDIS treats the miniport driver as an old miniport driver that is not power management-capable. For more information about power management for such drivers, see [Power Management for Old Miniport Drivers](power-management-for-old-miniport-drivers.md).

A miniport driver that succeeds an OID\_PNP\_CAPABILITIES request returns the following information to NDIS in response to the request:

-   The lowest device power state from which the NIC can wake the system on receipt of a Magic Packet.

-   The lowest device power state from which the NIC can wake the system on receipt of a network frame that contains a pattern that the protocol driver specifies.

As soon as NDIS gets this information, it determines, for each system power state, the device power states to which it can set the NIC if wake-on-LAN is enabled by the user in the UI. If there are no allowable low-power device states from which the NIC can generate a wake-up signal (that is, if all the low-power device power states specified in the **DeviceState** array of DEVICE\_CAPABILITIES structures are lower than lowest device power states from which the NIC can wake the system), NDIS makes the **Allow the device to bring the computer out of standby** option in the **Power Management** tab unavailable for the NIC. Then, the user cannot enable wake-on-LAN.

**Note**  Wake-on-LAN is possible only if both the NIC and the system are power management-capable. If the system is not power management-capable, NDIS will not query a NIC's power management capabilities.

 

### Using User Input

For a power management-capable NIC, Microsoft Windows 2000 and later versions provide the following options in the **Power Management** tab of a NIC's **Properties** dialog box:

**Allow the computer to turn off this device to save power**

**Allow the device to bring the computer out of standby**

The first option is selected by default to enable power management for the NIC. If the user clears the option, NDIS treats the NIC as an old NIC with regard to power management. For more information, see [Power Management for Old Miniport Drivers](power-management-for-old-miniport-drivers.md).

The second option is clear by default. If NDIS determines that there is no allowable low-power state from which the NIC can generate a wake-up signal, NDIS makes the second option unavailable. For example, if the **DeviceState** array member of the DEVICE\_CAPABILITIES structure indicates that the NIC must be in D3 for all low-power system states, and if **DeviceWake** indicates that the lowest-powered device state from which the NIC can wake the system is D2, then NDIS shades makes the second check box unavailable.

In addition to the preceding two options, Windows XP and Windows Vista provide a third option in the **Power Management** tab for a NIC:

**Only allow management stations to bring the computer out of standby**

This option, which is subordinate to the second option that is described earlier, is available only if:

-   The user selected the second option to enable wake-on-LAN.

-   The miniport driver, in responding to the [OID\_PNP\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569774), indicated that the NIC could wake the system on receipt of a Magic Packet.

The **Only allow management stations to bring the computer out of standby** option is clear by default. The user can select this option to specify that only the receipt of a Magic Packet will cause the NIC to generate a wake-up signal to the system.

Whenever a user selects or clears a power management option for a NIC, the system notifies NDIS of the change. NDIS writes the new setting to the registry so that the changed setting persists across restarts.

 

 





