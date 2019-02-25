---
title: Mapping the Deinterlace DDI to DirectDraw and DirectX VA
description: Mapping the Deinterlace DDI to DirectDraw and DirectX VA
ms.assetid: a060265f-e1a2-416c-8533-6971cc9e2156
keywords:
- deinterlacing WDK DirectX VA , mapping deinterlacing DDI
- mapping deinterlacing DDI
- container methods WDK DirectX VA
- device methods WDK DirectX VA
- motion compensation WDK DirectX VA
- callbacks WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mapping the Deinterlace DDI to DirectDraw and DirectX VA


## <span id="ddk_mapping_the_deinterlace_ddi_to_directdraw_and_directx_va_gg"></span><span id="DDK_MAPPING_THE_DEINTERLACE_DDI_TO_DIRECTDRAW_AND_DIRECTX_VA_GG"></span>


Deinterlacing functionality must be accessed through DirectDraw's [motion compensation callback functions](motion-compensation-callbacks.md) to which the [deinterlace DDI](https://msdn.microsoft.com/library/windows/hardware/ff552701) can be mapped.

The deinterlace DDI is divided into two functional groups: the DirectX VA container methods and the DirectX VA device methods. The container methods determine the capabilities of each DirectX VA device that is contained by the display hardware. The device methods direct the device to perform operations specific to the device. A DirectX VA driver can have only one container, but it can support multiple devices.

It is possible to map the deinterlace DDI to the motion compensation callbacks because they do not use typed parameters (that is, their single parameter is a pointer to a structure). In other words, the information in the single parameter that is passed to a motion compensation callback function can be processed according to its information type. For example, if **DXVA\_DeinterlaceBltFnCode**-type information is passed to the [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) function, *DdMoCompRender* can call the [**DeinterlaceBlt**](https://msdn.microsoft.com/library/windows/hardware/ff563924) function of the deinterlace DDI to perform a bit-block deinterlace of video stream objects. However, if **DXVA\_DeinterlaceQueryModeCapsFnCode**-type information is passed to *DdMoCompRender* instead, *DdMoCompRender* can call the [**DeinterlaceQueryModeCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563946) function of the deinterlace DDI to query for the capabilities of a deinterlacing mode.

The following topics describe how the deinterlace DDI is mapped to the motion compensation callbacks:

[Deinterlace Container Device for Deinterlacing](deinterlace-container-device-for-deinterlacing.md)

[Calling the Deinterlace DDI from a User-Mode Component](calling-the-deinterlace-ddi-from-a-user-mode-component.md)

 

 





