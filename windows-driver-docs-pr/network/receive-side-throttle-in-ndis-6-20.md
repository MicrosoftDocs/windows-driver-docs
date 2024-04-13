---
title: Receive Side Throttle in NDIS 6.20
description: Receive Side Throttle in NDIS 6.20
keywords:
- NDIS 6.20 WDK , receive-side throttle
- receive-side throttle (RST) WDK NDIS 6.20
- RST WDK NDIS 6.20
ms.date: 03/02/2023
---

# Receive Side Throttle in NDIS 6.20





NDIS 6.20 introduces receive-side throttle (RST) enhancements to reduce the possibility of disruptions during media playback in multimedia applications. RST support is mandatory for NDIS 6.20 and later drivers.

If an NDIS driver spends too much time at dispatch IRQ level in a deferred procedure call (DPC), it increases the scheduling latency for multimedia application threads and might cause disruptions during media playback. To improve media playback with NDIS 6.20 and later drivers, NDIS can control the number of packets that a miniport driver indicates in a receive DPC.

## Related topics


[*MiniportInterrupt*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_isr)

[*MiniportInterruptDPC*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_interrupt_dpc)

[*MiniportMessageInterrupt*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_message_interrupt)

[*MiniportMessageInterruptDPC*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_message_interrupt_dpc)

[**NDIS\_RECEIVE\_THROTTLE\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_receive_throttle_parameters)

[**NdisMQueueDpcEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismqueuedpcex)

 

