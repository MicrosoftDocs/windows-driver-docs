---
title: Performance Tip Completing Requests During HwStartIo
description: Performance Tip Completing Requests During HwStartIo
ms.date: 04/20/2017
---

# Performance Tip: Completing Requests During HwStartIo


By completing outstanding I/O requests that are ready for completion in its [**HwStorStartIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_startio) routine, a miniport can spend less time at device IRQL (DIRQL), which improves system responsiveness, and also take advantage of new Storport optimizations that further improve system responsiveness and I/O throughput. The point is to try to spend as little time as possible in an interrupt handler. To take advantage of the new Storport optimizations, a miniport:

-   Must enable DPC redirection via [**StorPortInitializePerfOpts**](/windows-hardware/drivers/ddi/storport/nf-storport-storportinitializeperfopts)

-   Must use [**StorPortNotification (NotificationType = RequestComplete)**](/windows-hardware/drivers/ddi/storport/nf-storport-storportnotification) while in its [**HwStorStartIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_startio) routine to notify Storport of completed I/O requests

-   Should indicate its intention to do completion-during-StartIo by setting the STOR\_PERF\_OPTIMIZE\_FOR\_COMPLETION\_DURING\_STARTIO flag in its call to the [**StorPortInitializePerfOpts**](/windows-hardware/drivers/ddi/storport/nf-storport-storportinitializeperfopts) routine

-   Must determine the characteristics of the workload (for example, request size and throughput) that should be present before the optimization is applied.

While in its [**HwStorStartIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_startio) routine, a miniport should check for completed requests after starting the requested I/O operation.

 

