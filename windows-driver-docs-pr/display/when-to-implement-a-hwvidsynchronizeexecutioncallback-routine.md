---
title: Implementing a HwVidSynchronizeExecutionCallback Routine
description: When to Implement a HwVidSynchronizeExecutionCallback Routine
keywords:
- video miniport drivers WDK Windows 2000 , interrupts
- interrupts WDK video miniport
- HwVidSynchronizeExecutionCallback
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# Implementing a HwVidSynchronizeExecutionCallback Routine

Miniport drivers for adapters that do not generate interrupts seldom call [**VideoPortSynchronizeExecution**](/windows-hardware/drivers/ddi/video/nf-video-videoportsynchronizeexecution) with a [*HwVidSynchronizeExecutionCallback*](/windows-hardware/drivers/ddi/video/nc-video-pminiport_synchronize_routine) function.

In fact, even miniport drivers that have a [*HwVidInterrupt*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_interrupt) function do not necessarily have a *HwVidSynchronizeExecutionCallback* function. Because the video port driver does not send a request to a miniport driver's [*HwVidStartIO*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_start_io) function until it completes processing of the preceding request (see [Processing Video Requests (Windows 2000 Model)](processing-video-requests--windows-2000-model-.md) for more information), miniport drivers rarely call **VideoPortSynchronizeExecution**.

There are two possible uses for a miniport driver's *HwVidSynchronizeExecutionCallback* function:

-   To access the adapter registers using the miniport driver's device extension for a driver function other than the *HwVidInterrupt* function.

    When the *HwVidSynchronizeExecutionCallback* function is given control, interrupts from the adapter are masked off so the miniport driver's *HwVidInterrupt* function cannot change state in the device extension while the *HwVidSynchronizeExecutionCallback* function is running in an SMP machine.

-   To write commands to the adapter registers or ports very quickly if the adapter requires it.

    When the *HwVidSynchronizeExecutionCallback* function is given control, almost all system interrupts are masked off, so the *HwVidSynchronizeExecutionCallback* function cannot be preempted by a device (or even, a clock) interrupt.

    An *HwVidSynchronizeExecutionCallback* function *must* return control as quickly as possible.

With the first type of [*HwVidSynchronizeExecutionCallback*](/windows-hardware/drivers/ddi/video/nc-video-pminiport_synchronize_routine) function, the miniport driver calls [**VideoPortSynchronizeExecution**](/windows-hardware/drivers/ddi/video/nf-video-videoportsynchronizeexecution) with the *Priority* set to **VpMediumPriority**. With the second type of *HwVidSynchronizeExecutionCallback* function, the miniport driver also makes this call with the *Priority* set to **VpMediumPriority** if the driver has no [*HwVidInterrupt*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_interrupt) function. Otherwise, such a miniport driver makes this call with the *Priority* set to **VpHighPriority**.

In general, a miniport driver should *not* call **VideoPortSynchronizeExecution** with the second type of *HwVidSynchronizeExecutionCallback* function unless the driver designer has no other alternative: that is, unless the adapter is such that it must be programmed with system interrupts masked off. Otherwise, the miniport driver should call **VideoPortSynchronizeExecution** with the *Priority* set to **VpLowPriority**.

A *HwVidSynchronizeExecutionCallback* function, like a *HwVidInterrupt* function, cannot be pageable and cannot call certain **VideoPort***Xxx* functions without bringing down the system. For a summary of **VideoPort***Xxx* functions that the *HwVidSynchronizeExecutionCallback* function can call safely, see [*HwVidInterrupt*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_interrupt).

 

