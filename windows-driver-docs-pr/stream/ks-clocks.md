---
title: KS Clocks
description: KS Clocks
keywords:
- kernel streaming WDK , clocks
- KS WDK , clocks
- clocks WDK kernel streaming
- time WDK kernel streaming
- time stamps WDK kernel streaming
ms.date: 04/20/2017
---

# KS Clocks





If you are writing an AVStream minidriver, refer to [AVStream Clocks](avstream-clocks.md).

Kernel streaming minidrivers support clock operations by providing callbacks for the properties in the set [KSPROPSETID\_Clock](./kspropsetid-clock.md). To learn how to do this, see [KS Properties](ks-properties.md).

A user-mode client can request to be notified when a clock reaches a certain time stamp, or to receive periodic notification that a fixed amount of time on the clock has elapsed. To do so, clients register [**KSEVENT\_CLOCK\_POSITION\_MARK**](./ksevent-clock-position-mark.md) and [**KSEVENT\_CLOCK\_INTERVAL\_MARK**](./ksevent-clock-interval-mark.md).

This section contains information about the following topics:

[Master Clocks](master-clocks.md)

[Default Clocks](default-clocks.md)

 

