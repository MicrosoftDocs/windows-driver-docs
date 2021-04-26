---
title: Changing State on the Adapter
description: Changing State on the Adapter
keywords:
- video adapter state changes WDK video miniport
- states WDK video miniport
- adapter states WDK video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Changing State on the Adapter


## <span id="ddk_changing_state_on_the_adapter_gg"></span><span id="DDK_CHANGING_STATE_ON_THE_ADAPTER_GG"></span>


The miniport driver must not permanently change the state of the adapter until its [*HwVidInitialize*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_initialize) routine is called. Miniport driver routines called before *HwVidInitialize*, such as [*HwVidFindAdapter*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_find_adapter), should not change the state of any video adapter unnecessarily and must not change the state of any video adapter permanently.

While [*HwVidFindAdapter*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_find_adapter) runs, the HAL has control of the video adapter so it can write information to the screen in the early stages of the system boot process. If *HwVidFindAdapter*'s attempt to identify its adapter affects an adapter's state, this routine should restore the original state immediately so that on return from *HwVidFindAdapter* the HAL can continue to display boot-up messages.

For example, [*HwVidFindAdapter*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_find_adapter) should defer determining the DAC type of an adapter to the [*HwVidInitialize*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_initialize) function, because making this determination does not affect whether the miniport driver will be loaded but does change the state of the adapter permanently.

 

