---
title: Detecting Child Devices
description: Detecting Child Devices
keywords:
- video miniport drivers WDK Windows 2000 , child devices
- child devices WDK video miniport , detecting
- detecting child devices WDK video miniport
- HwVidGetVideoChildDescriptor
ms.date: 04/20/2017
---

# Detecting Child Devices


## <span id="ddk_detecting_child_devices_gg"></span><span id="DDK_DETECTING_CHILD_DEVICES_GG"></span>


You must implement [*HwVidGetVideoChildDescriptor*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_get_child_descriptor) in your miniport driver for the Plug and Play manager to be able to detect child devices of a graphics adapter.

By default, [*HwVidGetVideoChildDescriptor*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_get_child_descriptor) cannot be called until after the parent device is started; that is, *HwVidGetVideoChildDescriptor* cannot be called until after [*HwVidFindAdapter*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_find_adapter) has completed. To override this default, thus allowing child enumeration to occur at any time, you can set the **AllowEarlyEnumeration** member of [**VIDEO\_HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/video/ns-video-_video_hw_initialization_data) to **TRUE**.

Some devices generate an interrupt when new hardware is connected to the system or when existing hardware is disconnected from the system. To handle such an interrupt, the miniport driver should do the following:

-   Implement a DPC ([**HwVidDpcRoutine**](/windows-hardware/drivers/ddi/video/nc-video-pminiport_dpc_routine)) that calls [**VideoPortEnumerateChildren**](/windows-hardware/drivers/ddi/video/nf-video-videoportenumeratechildren).

-   Implement an interrupt handler ([*HwVidInterrupt*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_interrupt)) that calls [**VideoPortQueueDpc**](/windows-hardware/drivers/ddi/video/nf-video-videoportqueuedpc) to queue the DPC when an interrupt on the device occurs.

[**VideoPortEnumerateChildren**](/windows-hardware/drivers/ddi/video/nf-video-videoportenumeratechildren) forces the reenumeration of the adapter's child devices by causing the miniport driver's [*HwVidGetVideoChildDescriptor*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_get_child_descriptor) function to be called for each of the parent device's children. The Plug and Play manager will update the relationship between the parent device and its children accordingly.

 

