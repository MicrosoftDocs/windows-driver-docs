---
title: Performance Tip Completing Requests During HwStartIo
description: Performance Tip Completing Requests During HwStartIo
ms.assetid: b1a3feff-ca18-4757-a336-c70ada998ba9
---

# Performance Tip: Completing Requests During HwStartIo


By completing outstanding I/O requests that are ready for completion in its [**HwStorStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557423) routine, a miniport can spend less time at device IRQL (DIRQL), which improves system responsiveness, and also take advantage of new Storport optimizations that further improve system responsiveness and I/O throughput. The point is to try to spend as little time as possible in an interrupt handler. To take advantage of the new Storport optimizations, a miniport:

-   Must enable DPC redirection via [**StorPortInitializePerfOpts**](https://msdn.microsoft.com/library/windows/hardware/ff567114)

-   Must use [**StorPortNotification (NotificationType = RequestComplete)**](https://msdn.microsoft.com/library/windows/hardware/ff567446) while in its [**HwStorStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557423) routine to notify Storport of completed I/O requests

-   Should indicate its intention to do completion-during-StartIo by setting the STOR\_PERF\_OPTIMIZE\_FOR\_COMPLETION\_DURING\_STARTIO flag in its call to the [**StorPortInitializePerfOpts**](https://msdn.microsoft.com/library/windows/hardware/ff567114) routine

-   Must determine the characteristics of the workload (for example, request size and throughput) that should be present before the optimization is applied.

While in its [**HwStorStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557423) routine, a miniport should check for completed requests after starting the requested I/O operation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Performance%20Tip:%20Completing%20Requests%20During%20HwStartIo%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




