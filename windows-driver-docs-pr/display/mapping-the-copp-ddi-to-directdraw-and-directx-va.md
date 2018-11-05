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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





