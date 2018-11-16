---
title: Performance Tip Completing Requests During HwStartIo
description: Performance Tip Completing Requests During HwStartIo
ms.assetid: b1a3feff-ca18-4757-a336-c70ada998ba9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Performance Tip: Completing Requests During HwStartIo


By completing outstanding I/O requests that are ready for completion in its [**HwStorStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557423) routine, a miniport can spend less time at device IRQL (DIRQL), which improves system responsiveness, and also take advantage of new Storport optimizations that further improve system responsiveness and I/O throughput. The point is to try to spend as little time as possible in an interrupt handler. To take advantage of the new Storport optimizations, a miniport:

-   Must enable DPC redirection via [**StorPortInitializePerfOpts**](https://msdn.microsoft.com/library/windows/hardware/ff567114)

-   Must use [**StorPortNotification (NotificationType = RequestComplete)**](https://msdn.microsoft.com/library/windows/hardware/ff567446) while in its [**HwStorStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557423) routine to notify Storport of completed I/O requests

-   Should indicate its intention to do completion-during-StartIo by setting the STOR\_PERF\_OPTIMIZE\_FOR\_COMPLETION\_DURING\_STARTIO flag in its call to the [**StorPortInitializePerfOpts**](https://msdn.microsoft.com/library/windows/hardware/ff567114) routine

-   Must determine the characteristics of the workload (for example, request size and throughput) that should be present before the optimization is applied.

While in its [**HwStorStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557423) routine, a miniport should check for completed requests after starting the requested I/O operation.

 

 




