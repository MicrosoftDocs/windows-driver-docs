---
title: D1Latency, D2Latency, and D3Latency
description: D1Latency, D2Latency, and D3Latency
keywords: ["D1Latency", "D2Latency", "D3Latency"]
ms.date: 06/16/2017
---

# D1Latency, D2Latency, and D3Latency





The **D1Latency**, **D2Latency**, and **D3Latency** members of [**DEVICE\_CAPABILITIES**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_capabilities) contain the approximate time, in 100-microsecond units, that the device requires to return to the D0 state from each of the sleeping states. A driver should specify a latency time of zero for any device power state that it does not support.

 

