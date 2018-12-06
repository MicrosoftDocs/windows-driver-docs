---
title: Processing with Busy Present Queues
description: Processing with Busy Present Queues
ms.assetid: 5fce137b-001c-49f6-85ad-94c9eead9aa0
keywords:
- busy present queues WDK DirectX 9.0
- present queues WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing with Busy Present Queues


## <span id="ddk_processing_with_busy_present_queues_gg"></span><span id="DDK_PROCESSING_WITH_BUSY_PRESENT_QUEUES_GG"></span>


A DirectX 9.0 version driver must return the DDERR\_WASSTILLDRAWING value from a call to its [*DdFlip*](https://msdn.microsoft.com/library/windows/hardware/ff549306) function if the runtime passed the DDFLIP\_DONOTWAIT flag in the **dwFlags** member of the [**DD\_FLIPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551520) structure and the driver is unable to schedule a presentation, for example, if the present queue is full or if the driver is waiting for a vsync interval. The runtime calls the driver's *DdFlip* function with DDFLIP\_DONOTWAIT set if an application called the **IDirect3DSwapChain9::Present** method with the D3DPRESENT\_DONOTWAIT flag set. If the driver cannot schedule a presentation, its *DdFlip* function returns DDERR\_WASSTILLDRAWING in the **ddRVal** member of DD\_FLIPDATA. The application's **Present** method in turn returns DDERR\_WASSTILLDRAWING, which lets the application perform other processing.

The D3DPRESENT\_DONOTWAIT flag is new for DirectX 9.0. The DDFLIP\_DONOTWAIT flag has been available since DirectX 7.0. If a DirectX 7.0 application were to set DDFLIP\_DONOTWAIT in a call to the **IDirectDrawSurface7::Flip** method, a DirectX 7.0 or later driver's *DdFlip* function would receive the DDFLIP\_DONOTWAIT flag.

If D3DPRESENT\_DONOTWAIT is not set, **Present** behaves as in DirectX 8.1 and earlier. That is, **Present** spins until the hardware is free, without returning an error.

For more information about **IDirect3DSwapChain*Xxx*::Present**, see the latest DirectX SDK documentation.

 

 





