---
title: Miniport Driver Hardware Reset
description: Miniport Driver Hardware Reset
ms.assetid: d5209809-039c-4ac2-afdf-1f5144307850
keywords:
- network interface cards WDK networking , resetting
- NICs WDK networking , resetting
- resetting NIC
- MiniportResetEx
- hardware resets WDK NDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miniport Driver Hardware Reset





A miniport driver must register a [*MiniportResetEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_reset) function with [**NdisMRegisterMiniportDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismregisterminiportdriver).

*MiniportResetEx* can complete synchronously or asynchronously with a call to [**NdisMResetComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismresetcomplete)(see the following figure).

![diagram illustrating resetting a network interface card](images/207-09.png)

*MiniportResetEx* should:

-   Disable further interrupts.

-   Clear out the data that is associated with any sends in progress. For example, on a ring buffer for a bus-master direct memory access (DMA) device, the pointers to send buffers should be cleared. Deserialized and connection-oriented miniport drivers must return NDIS\_STATUS\_REQUEST\_ABORTED for any queued send requests.

-   Restore the hardware state and the miniport driver's internal state to the state that existed before the reset operation.

The miniport driver is responsible for restoring the hardware state of the device except for multicast addresses, packet filters, task offload settings, and wake up patterns. These setting are restored by either the miniport driver or NDIS. The miniport driver determines who is responsible for restoring these settings by returning a Boolean value in the *AddressingReset* parameter.

If the miniport driver returns **FALSE** in the *AddressingReset* parameter, the miniport driver restores its multicast addresses, packet filters, task offload settings, and wake up patterns to their initial state. If the miniport driver returns **TRUE** in *AddressingReset*, NDIS calls a connectionless miniport driver's [*MiniportOidRequest*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_oid_request) function or a connection-oriented miniport driver's [**MiniportCoOidRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_co_oid_request) function to set the following configuration settings:

-   The network packet filter through a set request of [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-current-packet-filter).

-   The multicast address list through a set request of [OID\_802\_3\_MULTICAST\_LIST](https://docs.microsoft.com/windows-hardware/drivers/network/oid-802-3-multicast-list).

-   Task offload encapsulation settings through a set request of [OID\_OFFLOAD\_ENCAPSULATION](https://docs.microsoft.com/windows-hardware/drivers/network/oid-offload-encapsulation).

-   Power management wake-up patterns through a set request of [OID\_PNP\_ADD\_WAKE\_UP\_PATTERN](https://docs.microsoft.com/windows-hardware/drivers/network/oid-pnp-add-wake-up-pattern).
    **Note**  Starting with NDIS 6.20, wake-up patterns set through [OID\_PM\_ADD\_WOL\_PATTERN](https://docs.microsoft.com/windows-hardware/drivers/network/oid-pm-add-wol-pattern) must be restored by the miniport driver.

     

## Related topics


[Adapter States of a Miniport Driver](adapter-states-of-a-miniport-driver.md)

[Miniport Adapter States and Operations](miniport-adapter-states-and-operations.md)

[Miniport Driver Reset and Halt Functions](https://docs.microsoft.com/previous-versions/windows/hardware/network/ff564064(v=vs.85))

 

 






