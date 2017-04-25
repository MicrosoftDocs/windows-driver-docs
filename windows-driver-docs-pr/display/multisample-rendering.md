---
title: Multisample Rendering
description: Multisample Rendering
ms.assetid: 7c21b0e0-bdd3-4de3-a5c5-5adc2d2e2b33
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , multisample rendering
- multisample rendering WDK DirectX 8.0
- rendering multisamples WDK DirectX 8.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Multisample Rendering


## <span id="ddk_multisample_rendering_gg"></span><span id="DDK_MULTISAMPLE_RENDERING_GG"></span>


DirectX 8.0 introduces support for multisample rendering with the number of samples per pixel under application control. The **IDirect3DDevice8** interface supports multisampling in both fullscreen and windowed modes of operation. Furthermore, there is sufficient flexibility to support hardware that performs the processing of samples into pixels at the back end (directly out of the frame buffer) or at the front end (via a special flip or blt call).For more information about **IDirect3DDevice8**, see the DirectX 8.0 documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Multisample%20Rendering%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




