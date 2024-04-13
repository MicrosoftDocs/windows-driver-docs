---
title: Input Buffer Order
description: Input Buffer Order
keywords:
- input buffers WDK DirectX VA
- deinterlacing WDK DirectX VA , input buffer order
- buffers WDK DirectX VA
ms.date: 04/20/2017
---

# Input Buffer Order


## <span id="ddk_input_buffer_order_gg"></span><span id="DDK_INPUT_BUFFER_ORDER_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

For each combination deinterlacing and substream compositing operation, the VMR initiates a call to the driver-supplied [*DdMoCompRender*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mocompcb_render) callback function. In the *DdMoCompRender* call, the **lpBufferInfo** member of the [**DD\_RENDERMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_rendermocompdata) structure points to an array of buffers that describes the destination surface and the surface for each input video source sample. The *DdMoCompRender* function in turn calls the driver's [**DeinterlaceBltEx**](./dxva-deinterlacebobdeviceclass-deinterlacebltex.md) function. For more information, see [Calling the Deinterlace DDI from a User-Mode Component](calling-the-deinterlace-ddi-from-a-user-mode-component.md).

The order of the elements in the array of [**DXVA\_VideoSample2**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_videosample2) structures in the **Source** member of the [**DXVA\_DeinterlaceBltEx**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_deinterlacebltex) structure matches the **lpBufferInfo** array with the exception that the destination surface is not present.

The following topics describe the rules for arranging surfaces in the **lpBufferInfo** array and provide examples that explain the sequence order of surfaces:

[Input Buffer Order Rules](input-buffer-order-rules.md)

[Input Buffer Order Example 1](input-buffer-order-example-1.md)

[Input Buffer Order Example 2](input-buffer-order-example-2.md)

[Input Buffer Order Example 3](input-buffer-order-example-3.md)

[Input Buffer Order Example 4](input-buffer-order-example-4.md)

[Input Buffer Order Example 5](input-buffer-order-example-5.md)

[Input Buffer Order Example 6](input-buffer-order-example-6.md)

 

