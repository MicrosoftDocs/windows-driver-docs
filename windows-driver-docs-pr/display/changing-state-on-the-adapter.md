---
title: Changing State on the Adapter
description: Changing State on the Adapter
ms.assetid: bf503a42-ac32-4d68-9ad9-afec69c5fe2a
keywords:
- video adapter state changes WDK video miniport
- states WDK video miniport
- adapter states WDK video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Changing State on the Adapter


## <span id="ddk_changing_state_on_the_adapter_gg"></span><span id="DDK_CHANGING_STATE_ON_THE_ADAPTER_GG"></span>


The miniport driver must not permanently change the state of the adapter until its [*HwVidInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff567345) routine is called. Miniport driver routines called before *HwVidInitialize*, such as [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332), should not change the state of any video adapter unnecessarily and must not change the state of any video adapter permanently.

While [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) runs, the HAL has control of the video adapter so it can write information to the screen in the early stages of the system boot process. If *HwVidFindAdapter*'s attempt to identify its adapter affects an adapter's state, this routine should restore the original state immediately so that on return from *HwVidFindAdapter* the HAL can continue to display boot-up messages.

For example, [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) should defer determining the DAC type of an adapter to the [*HwVidInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff567345) function, because making this determination does not affect whether the miniport driver will be loaded but does change the state of the adapter permanently.

 

 





