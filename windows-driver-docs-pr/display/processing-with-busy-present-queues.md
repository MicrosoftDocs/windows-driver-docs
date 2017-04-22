---
title: Processing with Busy Present Queues
description: Processing with Busy Present Queues
ms.assetid: 5fce137b-001c-49f6-85ad-94c9eead9aa0
keywords:
- busy present queues WDK DirectX 9.0
- present queues WDK DirectX 9.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Processing with Busy Present Queues


## <span id="ddk_processing_with_busy_present_queues_gg"></span><span id="DDK_PROCESSING_WITH_BUSY_PRESENT_QUEUES_GG"></span>


A DirectX 9.0 version driver must return the DDERR\_WASSTILLDRAWING value from a call to its [*DdFlip*](https://msdn.microsoft.com/library/windows/hardware/ff549306) function if the runtime passed the DDFLIP\_DONOTWAIT flag in the **dwFlags** member of the [**DD\_FLIPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551520) structure and the driver is unable to schedule a presentation, for example, if the present queue is full or if the driver is waiting for a vsync interval. The runtime calls the driver's *DdFlip* function with DDFLIP\_DONOTWAIT set if an application called the **IDirect3DSwapChain9::Present** method with the D3DPRESENT\_DONOTWAIT flag set. If the driver cannot schedule a presentation, its *DdFlip* function returns DDERR\_WASSTILLDRAWING in the **ddRVal** member of DD\_FLIPDATA. The application's **Present** method in turn returns DDERR\_WASSTILLDRAWING, which lets the application perform other processing.

The D3DPRESENT\_DONOTWAIT flag is new for DirectX 9.0. The DDFLIP\_DONOTWAIT flag has been available since DirectX 7.0. If a DirectX 7.0 application were to set DDFLIP\_DONOTWAIT in a call to the **IDirectDrawSurface7::Flip** method, a DirectX 7.0 or later driver's *DdFlip* function would receive the DDFLIP\_DONOTWAIT flag.

If D3DPRESENT\_DONOTWAIT is not set, **Present** behaves as in DirectX 8.1 and earlier. That is, **Present** spins until the hardware is free, without returning an error.

For more information about **IDirect3DSwapChain*Xxx*::Present**, see the latest DirectX SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Processing%20with%20Busy%20Present%20Queues%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




