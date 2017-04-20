---
title: Direct3D Context Management
description: Direct3D Context Management
ms.assetid: 143f5150-9ac4-43f7-985f-0baa32871af2
keywords:
- context WDK Direct3D
- Direct3D WDK Windows 2000 display , context management
- context WDK Direct3D , about context management
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Direct3D Context Management


## <span id="ddk_direct3d_context_management_gg"></span><span id="DDK_DIRECT3D_CONTEXT_MANAGEMENT_GG"></span>


A context encapsulates the state information for an application-created Microsoft Direct3D hardware abstraction layer (HAL) device; that is, a context describes how the driver should draw. State includes information such as the surface being rendered to, the depth surface, shading information, and texture information.

A Direct3D driver is responsible for creating and managing its own rendering contexts.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Direct3D%20Context%20Management%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




