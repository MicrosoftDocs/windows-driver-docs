---
title: When to Implement a HwVidSynchronizeExecutionCallback Routine
description: When to Implement a HwVidSynchronizeExecutionCallback Routine
ms.assetid: d33736ca-aff2-421b-a8cc-d09eba76ff7f
keywords:
- video miniport drivers WDK Windows 2000 , interrupts
- interrupts WDK video miniport
- HwVidSynchronizeExecutionCallback
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# When to Implement a HwVidSynchronizeExecutionCallback Routine


## <span id="ddk_when_to_implement_a_hwvidsynchronizeexecutioncallback_routine_gg"></span><span id="DDK_WHEN_TO_IMPLEMENT_A_HWVIDSYNCHRONIZEEXECUTIONCALLBACK_ROUTINE_GG"></span>


Miniport drivers for adapters that do not generate interrupts seldom call [**VideoPortSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff570372) with a [*HwVidSynchronizeExecutionCallback*](https://msdn.microsoft.com/library/windows/hardware/ff567369) function.

In fact, even miniport drivers that have a [*HwVidInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff567349) function do not necessarily have a *HwVidSynchronizeExecutionCallback* function. Because the video port driver does not send a request to a miniport driver's [*HwVidStartIO*](https://msdn.microsoft.com/library/windows/hardware/ff567367) function until it completes processing of the preceding request (see [Processing Video Requests (Windows 2000 Model)](processing-video-requests--windows-2000-model-.md) for more information), miniport drivers rarely call **VideoPortSynchronizeExecution**.

There are two possible uses for a miniport driver's *HwVidSynchronizeExecutionCallback* function:

-   To access the adapter registers using the miniport driver's device extension for a driver function other than the *HwVidInterrupt* function.

    When the *HwVidSynchronizeExecutionCallback* function is given control, interrupts from the adapter are masked off so the miniport driver's *HwVidInterrupt* function cannot change state in the device extension while the *HwVidSynchronizeExecutionCallback* function is running in an SMP machine.

-   To write commands to the adapter registers or ports very quickly if the adapter requires it.

    When the *HwVidSynchronizeExecutionCallback* function is given control, almost all system interrupts are masked off, so the *HwVidSynchronizeExecutionCallback* function cannot be preempted by a device (or even, a clock) interrupt.

    An *HwVidSynchronizeExecutionCallback* function *must* return control as quickly as possible.

With the first type of [*HwVidSynchronizeExecutionCallback*](https://msdn.microsoft.com/library/windows/hardware/ff567369) function, the miniport driver calls [**VideoPortSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff570372) with the *Priority* set to **VpMediumPriority**. With the second type of *HwVidSynchronizeExecutionCallback* function, the miniport driver also makes this call with the *Priority* set to **VpMediumPriority** if the driver has no [*HwVidInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff567349) function. Otherwise, such a miniport driver makes this call with the *Priority* set to **VpHighPriority**.

In general, a miniport driver should *not* call **VideoPortSynchronizeExecution** with the second type of *HwVidSynchronizeExecutionCallback* function unless the driver designer has no other alternative: that is, unless the adapter is such that it must be programmed with system interrupts masked off. Otherwise, the miniport driver should call **VideoPortSynchronizeExecution** with the *Priority* set to **VpLowPriority**.

A *HwVidSynchronizeExecutionCallback* function, like a *HwVidInterrupt* function, cannot be pageable and cannot call certain **VideoPort***Xxx* functions without bringing down the system. For a summary of **VideoPort***Xxx* functions that the *HwVidSynchronizeExecutionCallback* function can call safely, see [*HwVidInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff567349).

 

 





