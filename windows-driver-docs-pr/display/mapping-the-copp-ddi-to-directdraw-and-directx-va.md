---
title: Mapping the COPP DDI to DirectDraw and DirectX VA
description: Mapping the COPP DDI to DirectDraw and DirectX VA
ms.assetid: 737dabab-39f0-44fd-9d34-56d812ffde88
keywords:
- copy protection WDK COPP , mapping COPP DDI
- video copy protection WDK COPP , mapping COPP DDI
- COPP WDK DirectX VA , mapping COPP DDI
- protected video WDK COPP , mapping COPP DDI
- mapping COPP DDI WDK DirectX VA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Mapping the COPP DDI to DirectDraw and DirectX VA


## <span id="ddk_mapping_the_copp_ddi_to_directdraw_and_directx_va_gg"></span><span id="DDK_MAPPING_THE_COPP_DDI_TO_DIRECTDRAW_AND_DIRECTX_VA_GG"></span>


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

COPP functionality must be accessed through the [motion compensation callback functions](motion-compensation-callbacks.md) of DirectDraw, to which the [COPP DDI](https://msdn.microsoft.com/library/windows/hardware/ff540449) can be mapped. Because the COPP DDI is implemented in the video miniport driver, the display driver must [communicate with the video miniport driver by using COPP IOCTLs](communicating-ioctls-to-the-video-miniport-driver.md).

The COPP DDI can be mapped to the motion compensation callback functions because they do not use typed parameters (that is, their single parameter is a pointer to a structure). In other words, the information in the single parameter that is passed to a motion compensation callback function can be processed according to its information type.

For example, if **DXVA\_COPPGetCertificateLengthFnCode**-type information is passed to the [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) function, then *DdMoCompRender* can initiate a call to the [*COPPGetCertificateLength*](https://msdn.microsoft.com/library/windows/hardware/ff539644) function of the COPP DDI to query for the length in bytes of the certificate used by the graphics hardware. However, if **DXVA\_COPPSequenceStartFnCode**-type information is passed to *DdMoCompRender* instead, then *DdMoCompRender* can initiate a call to the [*COPPSequenceStart*](https://msdn.microsoft.com/library/windows/hardware/ff540421) function of the COPP DDI to indicate the start of a protected command and status sequence on the current video session.

The following topics describe how the COPP DDI is mapped to the motion compensation callback functions:

[DirectX VA COPP Device](directx-va-copp-device.md)

[Calling the COPP DDI from a User-Mode Component](calling-the-copp-ddi-from-a-user-mode-component.md)

[Calling the COPP DDI from the Display Driver](calling-the-copp-ddi-from-the-display-driver.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Mapping%20the%20COPP%20DDI%20to%20DirectDraw%20and%20DirectX%20VA%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




