---
title: Mapping the Deinterlace DDI to DirectDraw and DirectX VA
description: Mapping the Deinterlace DDI to DirectDraw and DirectX VA
ms.assetid: a060265f-e1a2-416c-8533-6971cc9e2156
keywords: ["deinterlacing WDK DirectX VA , mapping deinterlacing DDI", "mapping deinterlacing DDI", "container methods WDK DirectX VA", "device methods WDK DirectX VA", "motion compensation WDK DirectX VA", "callbacks WDK DirectX VA"]
---

# Mapping the Deinterlace DDI to DirectDraw and DirectX VA


## <span id="ddk_mapping_the_deinterlace_ddi_to_directdraw_and_directx_va_gg"></span><span id="DDK_MAPPING_THE_DEINTERLACE_DDI_TO_DIRECTDRAW_AND_DIRECTX_VA_GG"></span>


Deinterlacing functionality must be accessed through DirectDraw's [motion compensation callback functions](motion-compensation-callbacks.md) to which the [deinterlace DDI](https://msdn.microsoft.com/library/windows/hardware/ff552701) can be mapped.

The deinterlace DDI is divided into two functional groups: the DirectX VA container methods and the DirectX VA device methods. The container methods determine the capabilities of each DirectX VA device that is contained by the display hardware. The device methods direct the device to perform operations specific to the device. A DirectX VA driver can have only one container, but it can support multiple devices.

It is possible to map the deinterlace DDI to the motion compensation callbacks because they do not use typed parameters (that is, their single parameter is a pointer to a structure). In other words, the information in the single parameter that is passed to a motion compensation callback function can be processed according to its information type. For example, if **DXVA\_DeinterlaceBltFnCode**-type information is passed to the [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) function, *DdMoCompRender* can call the [**DeinterlaceBlt**](https://msdn.microsoft.com/library/windows/hardware/ff563924) function of the deinterlace DDI to perform a bit-block deinterlace of video stream objects. However, if **DXVA\_DeinterlaceQueryModeCapsFnCode**-type information is passed to *DdMoCompRender* instead, *DdMoCompRender* can call the [**DeinterlaceQueryModeCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563946) function of the deinterlace DDI to query for the capabilities of a deinterlacing mode.

The following topics describe how the deinterlace DDI is mapped to the motion compensation callbacks:

[Deinterlace Container Device for Deinterlacing](deinterlace-container-device-for-deinterlacing.md)

[Calling the Deinterlace DDI from a User-Mode Component](calling-the-deinterlace-ddi-from-a-user-mode-component.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Mapping%20the%20Deinterlace%20DDI%20to%20DirectDraw%20and%20DirectX%20VA%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




