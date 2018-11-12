---
title: Handling the Surprise Removal of a NIC
description: Handling the Surprise Removal of a NIC
ms.assetid: afd94749-8f2a-4cce-a646-1f616a845a0e
keywords:
- surprise removals WDK networking
- NICs WDK networking , surprise removals
- network interface cards WDK networking , surprise removals
- Plug and Play WDK NDIS miniport , surprise NIC removal
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling the Surprise Removal of a NIC





A surprise removal occurs when a user removes a network interface card (NIC) from a running system without notifying the system beforehand through the user interface (UI).

Miniport drivers for Windows Vista and later versions of the operating system should be able to handle surprise removals. In particular, NDIS miniport drivers with a Windows Driver Model (WDM) lower edge should be able to handle such events. If an NDIS-WDM miniport driver does not handle a surprise removal, any pending IRPs that the miniport driver sent to the underlying bus driver before the surprise removal cannot be completed.

For Windows Vista and later versions, a miniport driver (such as a miniport driver with a WDM lower edge) that does not control hardware directly should set the NDIS\_MINIPORT\_ATTRIBUTES\_SURPRISE\_REMOVE\_OK attribute flag when calling [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672). Setting this flag prevents a warning from being displayed when a user performs a surprise removal of a NIC. A miniport driver that cannot handle a surprise removal should not set this flag.

A miniport driver that supports surprise removal should itself attempt to detect a surprise removal during normal operations--outside of the context of [*MiniportDevicePnPEventNotify*](https://msdn.microsoft.com/library/windows/hardware/ff559369). After a NIC is removed, an attempt to read a NIC's I/O ports typically results in return values that have all bits set to one. If a miniport driver reads such a value, it should check for the presence of the hardware with a more conclusive test. For example, the miniport driver could write a value to an I/O port and then try to read the value from that port. The miniport driver could also check for valid values in the NIC's I/O registers. Detecting a surprise removal in such a way prevents the miniport driver from hanging in an infinite loop when it attempts to read a removed NIC's registers in an interrupt DPC.. A miniport driver that stops responding in this way stops NDIS from calling the driver's *MiniportDevicePnPEventNotify* function.

 

 





