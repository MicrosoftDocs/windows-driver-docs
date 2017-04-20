---
title: Changing State on the Adapter
description: Changing State on the Adapter
ms.assetid: bf503a42-ac32-4d68-9ad9-afec69c5fe2a
keywords:
- video adapter state changes WDK video miniport
- states WDK video miniport
- adapter states WDK video miniport
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Changing State on the Adapter


## <span id="ddk_changing_state_on_the_adapter_gg"></span><span id="DDK_CHANGING_STATE_ON_THE_ADAPTER_GG"></span>


The miniport driver must not permanently change the state of the adapter until its [*HwVidInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff567345) routine is called. Miniport driver routines called before *HwVidInitialize*, such as [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332), should not change the state of any video adapter unnecessarily and must not change the state of any video adapter permanently.

While [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) runs, the HAL has control of the video adapter so it can write information to the screen in the early stages of the system boot process. If *HwVidFindAdapter*'s attempt to identify its adapter affects an adapter's state, this routine should restore the original state immediately so that on return from *HwVidFindAdapter* the HAL can continue to display boot-up messages.

For example, [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) should defer determining the DAC type of an adapter to the [*HwVidInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff567345) function, because making this determination does not affect whether the miniport driver will be loaded but does change the state of the adapter permanently.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Changing%20State%20on%20the%20Adapter%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




