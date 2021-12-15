---
title: Interrupts in Video Miniport Drivers
description: Interrupts in Video Miniport Drivers
keywords:
- video miniport drivers WDK Windows 2000 , interrupts
- interrupts WDK video miniport
- HwVidInterrupt
ms.date: 04/20/2017
---

# Interrupts in Video Miniport Drivers


## <span id="ddk_interrupts_in_video_miniport_drivers_gg"></span><span id="DDK_INTERRUPTS_IN_VIDEO_MINIPORT_DRIVERS_GG"></span>


A video miniport driver for an adapter that generates interrupts must implement a [*HwVidInterrupt*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_interrupt) routine. The miniport driver's [**DriverEntry**](./driverentry-of-video-miniport-driver.md) routine should initialize the **HwInterrupt** member of the [**VIDEO\_HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/video/ns-video-_video_hw_initialization_data) structure to point to the interrupt handler.

The video port driver sets up an interrupt object for the video miniport driver if the adapter generates interrupts. Because the interrupt object is created and managed by the video port driver, a video miniport driver writer needs no further information about interrupt objects.

If the miniport driver's [*HwVidFindAdapter*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_find_adapter) function finds that the video adapter does not actually generate interrupts or that it cannot determine a valid interrupt vector/level for the adapter, *HwVidFindAdapter* should set both **InterruptLevel** and **InterruptVector** in the [**VIDEO\_PORT\_CONFIG\_INFO**](/windows-hardware/drivers/ddi/video/ns-video-_video_port_config_info) structure to zero.

When *HwVidFindAdapter* returns control, the video port driver checks the interrupt configuration members in VIDEO\_PORT\_CONFIG\_INFO and, if both are zero, does not connect an interrupt for the miniport driver. Explicitly setting both interrupt configuration members to zero in *HwVidFindAdapter* disables the [*HwVidInterrupt*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_interrupt) entry point, if any, that was set up by the miniport driver's [**DriverEntry**](./driverentry-of-video-miniport-driver.md) function.

Note that *HwVidInterrupt* can access the miniport driver's device extension since it is nonpaged. Depending on the design of the miniport driver, it might be impossible for other driver functions to share the device extension or a particular area of the device extension with *HwVidInterrupt* safely.

For example, suppose the miniport driver's [*HwVidStartIO*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_start_io) function is accessing the device extension when the adapter interrupts, *HwVidInterrupt* is run on another processor, and *HwVidInterrupt* also accesses the device extension. If such a situation might occur, *HwVidStartIO* should call [**VideoPortSynchronizeExecution**](/windows-hardware/drivers/ddi/video/nf-video-videoportsynchronizeexecution) with a driver-supplied [*HwVidSynchronizeExecutionCallback*](/windows-hardware/drivers/ddi/video/nc-video-pminiport_synchronize_routine) function.

A video miniport driver should adhere to the following two rules:

1.  Whenever the miniport driver and hardware are in any state other than D0, the hardware *never* generates an interrupt.

2.  Because of Rule 1, a device driver ISR should *never* act on an interrupt if the power state is D3 (it should return **FALSE**).

 

