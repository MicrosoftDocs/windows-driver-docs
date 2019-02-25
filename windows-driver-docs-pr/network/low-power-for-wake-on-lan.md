---
title: Low Power for Wake on LAN
description: Low Power for Wake on LAN
ms.assetid: 9ab8fa19-e75a-4266-accf-4e8b2964f82e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Low Power for Wake on LAN





The wake on LAN (WOL) feature wakes the computer from a low power state when a network adapter detects a WOL event.

A miniport driver reports network adapter WOL capabilities during initialization. For more information about reporting WOL capabilities, see [Reporting Power Management Capabilities](reporting-power-management-capabilities.md).

Note that the lower power on the media disconnect (D3 on disconnect) feature is canceled when the computer enters a sleep state in order to prevent waking the computer when the link state is externally cycled; that is, when a switch is turned off and on. For more information about D3 on disconnect, see [Low Power on Media Disconnect](low-power-on-media-disconnect.md).

The following figure illustrates the sequence of events that occurs to set a network adapter to a low power state.

![diagram illustrating the sequence of events to set a nic to a low power state](images/d3onsleep.png)

When NDIS puts a network adapter in a low power state, the following sequence occurs:

1.  NDIS uses [OID\_PM\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569768) to enable wake on LAN and to disable wake on media connect. NDIS\_PM\_WAKE\_ON\_LINK\_CHANGE\_ENABLED is cleared in the **WakeUpFlags** member.

2.  NDIS uses [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) to notify the miniport driver of the new power state (D3).

3.  The miniport driver may indicate an unknown media connect state using the [**NDIS\_STATUS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567391) status indication. The **MediaConnectStateUnknown** value is set in the **MediaConnectState** member of the [**NDIS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh205390) structure. For more information, see the [**NDIS\_STATUS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567391) documentation.

4.  NDIS sends the PCI Express (PCIe) bus an [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) IRP to wait for a WOL event.

5.  NDIS sends the PCIe bus an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) IRP to set the bus to the D3 state.

The following figure illustrates the sequence of events that occurs to restore full power to a network adapter after a WOL event.

![diagram illustrating the sequence of events to restore full power to a nic after a wol event](images/d0onwol.png)

When the network adapter is waking the computer the following sequence occurs:

1.  The network adapter wakes the system by asserting WAKE\# on the PCIe bus or PME\# on the PCI bus.

2.  The bus completes the pending [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) IRP. The IRP is pending completion from the last step in the power down sequence.

3.  NDIS sets the bus to full power (D0) with the [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) IRP.

4.  NDIS notifies the miniport driver that the network adapter is at full power (D0) with the OID set request of [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780).

5.  The network adapter notifies NDIS of a media connect event with the [**NDIS\_STATUS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567391) status indication. The **MediaConnectStateConnected** value is set in the **MediaConnectState** member of the [**NDIS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh205390) structure.

Starting with NDIS 6.30, if the miniport driver supports [**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808) status indications, it must issue this status notification if the network adapter wakes the system. The driver issues this status notification while it is handling the OID set request of [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) for the transition to a full-power (D0) state.

For more information, see [NDIS Wake Reason Status Indications](ndis-wake-reason-status-indications.md).

 

 





