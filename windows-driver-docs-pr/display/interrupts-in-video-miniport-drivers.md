---
title: Interrupts in Video Miniport Drivers
description: Interrupts in Video Miniport Drivers
ms.assetid: bf84a3fb-860a-4647-ac34-93f3a22b166b
keywords: ["video miniport drivers WDK Windows 2000 , interrupts", "interrupts WDK video miniport", "HwVidInterrupt"]
---

# Interrupts in Video Miniport Drivers


## <span id="ddk_interrupts_in_video_miniport_drivers_gg"></span><span id="DDK_INTERRUPTS_IN_VIDEO_MINIPORT_DRIVERS_GG"></span>


A video miniport driver for an adapter that generates interrupts must implement a [*HwVidInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff567349) routine. The miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff556159) routine should initialize the **HwInterrupt** member of the [**VIDEO\_HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff570505) structure to point to the interrupt handler.

The video port driver sets up an interrupt object for the video miniport driver if the adapter generates interrupts. Because the interrupt object is created and managed by the video port driver, a video miniport driver writer needs no further information about interrupt objects.

If the miniport driver's [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) function finds that the video adapter does not actually generate interrupts or that it cannot determine a valid interrupt vector/level for the adapter, *HwVidFindAdapter* should set both **InterruptLevel** and **InterruptVector** in the [**VIDEO\_PORT\_CONFIG\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff570531) structure to zero.

When *HwVidFindAdapter* returns control, the video port driver checks the interrupt configuration members in VIDEO\_PORT\_CONFIG\_INFO and, if both are zero, does not connect an interrupt for the miniport driver. Explicitly setting both interrupt configuration members to zero in *HwVidFindAdapter* disables the [*HwVidInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff567349) entry point, if any, that was set up by the miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff556159) function.

Note that *HwVidInterrupt* can access the miniport driver's device extension since it is nonpaged. Depending on the design of the miniport driver, it might be impossible for other driver functions to share the device extension or a particular area of the device extension with *HwVidInterrupt* safely.

For example, suppose the miniport driver's [*HwVidStartIO*](https://msdn.microsoft.com/library/windows/hardware/ff567367) function is accessing the device extension when the adapter interrupts, *HwVidInterrupt* is run on another processor, and *HwVidInterrupt* also accesses the device extension. If such a situation might occur, *HwVidStartIO* should call [**VideoPortSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff570372) with a driver-supplied [*HwVidSynchronizeExecutionCallback*](https://msdn.microsoft.com/library/windows/hardware/ff567369) function.

A video miniport driver should adhere to the following two rules:

1.  Whenever the miniport driver and hardware are in any state other than D0, the hardware *never* generates an interrupt.

2.  Because of Rule 1, a device driver ISR should *never* act on an interrupt if the power state is D3 (it should return **FALSE**).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Interrupts%20in%20Video%20Miniport%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




