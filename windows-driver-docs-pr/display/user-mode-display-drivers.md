---
title: User-Mode Display Drivers
description: User-Mode Display Drivers
ms.assetid: cb4e8fb9-a2f0-43b2-ae9e-ccffa850ccd7
keywords: ["display driver model WDK Windows Vista , user-mode display drivers", "Windows Vista display driver model WDK , user-mode display drivers", "user-mode display drivers WDK Windows Vista , about user-mode display drivers", "user-mode display drivers WDK Windows Vista", "Direct3D WDK display"]
---

# User-Mode Display Drivers


## <span id="ddk_user_mode_display_drivers_gg"></span><span id="DDK_USER_MODE_DISPLAY_DRIVERS_GG"></span>


Graphics hardware vendors must write user-mode display drivers for their display adapters. The user-mode display driver is a dynamic-link library (DLL) that is loaded by the Microsoft Direct3D runtime. A user-mode display driver must at least support the [Direct3D version 9 DDI](https://msdn.microsoft.com/library/windows/hardware/ff552927). User-mode display drivers can also support the [Direct3D version 10 DDI](https://msdn.microsoft.com/library/windows/hardware/ff552909). The user-mode display driver can consist of one DLL that supports both Direct3D version 9 DDI and Direct3D version 10 DDI or it can consist of two separate DLLs, one for version 9 and the other for version 10 of Direct3D DDI. The following topics discuss various aspects of the user-mode display driver:

[Returning Error Codes Received from Runtime Functions](returning-error-codes-received-from-runtime-functions.md)

[Handling the E\_INVALIDARG Return Value](handling-the-e-invalidarg-return-value.md)

[Processing Shader Codes](processing-shader-codes.md)

[Converting the Direct3D Fixed-Function State](converting-the-direct3d-fixed-function-state.md)

[Copying Depth-Stencil Values](copying-depth-stencil-values.md)

[Validating Index Values](validating-index-values.md)

[Supporting Multiple Processors](supporting-multiple-processors.md)

[Handling Multiple Locks](handling-multiple-locks.md)

[DirectX Video Acceleration 2.0](directx-video-acceleration-2-0.md)

[Supporting Direct3D Version 10](supporting-direct3d-version-10.md)

[Supporting Direct3D Version 10.1](supporting-direct3d-version-10-1.md)

[Supporting Direct3D Version 11](supporting-direct3d-version-11.md)

[Processing High-Definition Video](processing-high-definition-video.md)

[Protecting Video Content](protecting-video-content.md)

[Verifying Overlay Support](verifying-overlay-support.md)

[Supporting OpenGL Enhancements](supporting-opengl-enhancements.md)

[Managing Resources for Multiple GPU Scenarios](managing-resources-for-multiple-gpu-scenarios.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20User-Mode%20Display%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




