---
title: Receive Side Throttle in NDIS 6.20
description: Receive Side Throttle in NDIS 6.20
ms.assetid: dc8d0f32-37ee-4383-864d-7d814d37c3c8
keywords:
- NDIS 6.20 WDK , receive-side throttle
- receive-side throttle (RST) WDK NDIS 6.20
- RST WDK NDIS 6.20
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receive Side Throttle in NDIS 6.20





NDIS 6.20 introduces receive-side throttle (RST) enhancements to reduce the possibility of disruptions during media playback in multimedia applications. RST support is mandatory for NDIS 6.20 and later drivers.

If an NDIS driver spends too much time at dispatch IRQ level in a deferred procedure call (DPC), it increases the scheduling latency for multimedia application threads and might cause disruptions during media playback. To improve media playback with NDIS 6.20 and later drivers, NDIS can control the number of packets that a miniport driver indicates in a receive DPC.

## Related topics


[*MiniportInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559395)

[*MiniportInterruptDPC*](https://msdn.microsoft.com/library/windows/hardware/ff559398)

[*MiniportMessageInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559407)

[*MiniportMessageInterruptDPC*](https://msdn.microsoft.com/library/windows/hardware/ff559411)

[**NDIS\_RECEIVE\_THROTTLE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567241)

[**NdisMQueueDpcEx**](https://msdn.microsoft.com/library/windows/hardware/ff563640)

 

 






