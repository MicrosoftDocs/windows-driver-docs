---
title: Power management enhancements in NDIS 6.30
description: Introduces NDIS 6.30 power management enhancements to reduce computer power consumption
ms.date: 03/02/2023
---

# Power Management Enhancements in NDIS 6.30


NDIS 6.20 included power management new features and improvements to reduce computer power consumption. NDIS 6.30 extends the NDIS 6.20 power management support with the following capabilities, as described in [Power Management (NDIS 6.30)](power-management--ndis-6-30-.md):

### NDIS Packet Coalescing

Starting with NDIS 6.30, network adapters can support NDIS packet coalescing. This feature reduces the processing overhead and power consumption on a host system due to the reception of random broadcast or multicast packets.

For more information, see [NDIS Packet Coalescing](ndis-packet-coalescing.md).

### NDIS Selective Suspend

Starting with NDIS 6.30, the NDIS selective suspend interface allows NDIS to suspend an idle network adapter by transitioning the adapter to a low-power state. This enables the system to reduce the power overhead on the CPU and network adapter.

For more information, see [NDIS Selective Suspend](ndis-selective-suspend.md).

### NDIS Wake Reason Status Indications

Starting with NDIS 6.30, miniport drivers issue an NDIS wake reason status indication ([**NDIS\_STATUS\_PM\_WAKE\_REASON**](./ndis-status-pm-wake-reason.md)) to notify NDIS and overlying drivers about the reason for a system wake-up event. If the network adapter generates a wake-up event, the miniport driver immediately issues this NDIS status indication when the system resumes to a full-power state.

**Note**  Support for NDIS wake reason status indications is optional for Mobile Broadband (MB) miniport drivers.

 

For more information, see [NDIS Wake Reason Status Indications](overview-of-ndis-wake-reason-statue-indications.md).

### NDIS No Pause On Suspend

Starting with NDIS 6.30, miniport drivers can specify an attribute flag (**NDIS\_MINIPORT\_ATTRIBUTES\_NO\_PAUSE\_ON\_SUSPEND**) in the [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_registration_attributes) structure. The driver passes a pointer to this structure in its call to the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function.

If the miniport sets the **NDIS\_MINIPORT\_ATTRIBUTES\_NO\_PAUSE\_ON\_SUSPEND** attribute flag, NDIS does not call the miniport driver's [*MiniportPause*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pause) function before the object identifier (OID) request of [OID\_PNP\_SET\_POWER](./oid-pnp-set-power.md) is issued to the driver. When the miniport driver handles the OID request, it must not assume that it had been previously paused when preparing the miniport adapter for the transition to a low-power state.

For more information, see [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_registration_attributes).

 

