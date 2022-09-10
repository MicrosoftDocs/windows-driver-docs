---
title: What's new for Windows 8 display drivers (WDDM 1.2)
description: Features new in Windows 8 for display drivers.
keywords:
- new for Windows 8 WDK display
- WDDM 1.2, new for Windows 8 WDK display
ms.date: 07/18/2022
---

# What was new for Windows 8 display drivers (WDDM 1.2)

Windows 8 introduced version 1.2 of the Windows Display Driver Model (WDDM). WDDM 1.2 also supports Microsoft Direct3D Version 11.1. See these topics for info on features, guidance to independent hardware vendors (IHVs), and hardware requirements:

* [WDDM 1.2 and Windows 8](wddm-in-windows-8.md) contains an overview of WDDM 1.2

* [WDDM 1.2 features](wddm-v1-2-features.md) describes the features added in WDDM 1.2

Kernel-mode driver interfaces are declared in these headers:

* D3d9types.h
* D3dkmddi.h
* D3dkmdt.h
* Dispmprt.h
* Dxgiddi.h

User-mode driver interfaces are declared in these headers:

* D3d10umddi.h
* D3dkmthk.h (OpenGL functions)
* D3dukmdt.h (includes kernel-mode definitions)
* D3dumddi.h

ETW events for user-mode drivers are declared in this header:

* Umdprovider.h

The following sections list requirements that have also been added to the documentation.

## Summary of Direct3D support requirements

These topics list the hardware capabilities and formats that user-mode drivers must support for different Direct3D feature levels:

* [Hardware support for Direct3D feature levels](hardware-support-for-direct3d-feature-levels.md)
* [Required Direct3D 9 capabilities](required-direct3d-9-capabilities.md)
* [Required DXGI formats](required-dxgi-formats.md)

## Corrections to XR_BIAS conversions

XR and XR_BIAS format requirements have been corrected in these topics:

* [XR Layout](xr-layout.md)
* [XR_BIAS Color Channel Conversion Rules](xr-bias-color-channel-conversion-rules.md)
* [XR_BIAS to Float Conversion Rules](xr-bias-to-float-conversion-rules.md)
* [Float to XR_BIAS Conversion Rules](float-to-xr-bias-conversion-rules.md)
* [Conversion from BGR8888 to XR_BIAS](conversion-from-bgr8888-to-xr-bias.md)
