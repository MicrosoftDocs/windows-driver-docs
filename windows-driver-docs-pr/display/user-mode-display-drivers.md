---
title: User-Mode Display Drivers
description: User-Mode Display Drivers
keywords:
- display driver model WDK Windows Vista , user-mode display drivers
- Windows Vista display driver model WDK , user-mode display drivers
- user-mode display drivers WDK Windows Vista , about user-mode display drivers
- user-mode display drivers WDK Windows Vista
- Direct3D WDK display
ms.date: 12/18/2024
ms.topic: concept-article
---

# User-mode display drivers

Along with a kernel-mode display driver, graphics hardware vendors must also write a user-mode display driver (UMD) for their display adapters. The UMD is a dynamic-link library (DLL) that the Direct3D runtime loads.

The UMD can consist of one DLL that supports multiple Direct3D versions, or it can consist of separate DLLs. The following articles discuss various aspects of the UMD:

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

[Supporting Direct3D Version 11](supporting-direct3d-version-11.md)

[Processing High-Definition Video](processing-high-definition-video.md)

[Protecting Video Content](protecting-video-content.md)

[Verifying Overlay Support](verifying-overlay-support.md)

[Supporting OpenGL Enhancements](supporting-opengl-enhancements.md)

[Managing Resources for Multiple GPU Scenarios](managing-resources-for-multiple-gpu-scenarios.md)
