---
title: Extended Format Aware Requirements
description: Extended Format Aware Requirements
ms.assetid: eab9c254-fca7-449d-a6cf-1b20d2e7173c
keywords:
- Direct3D version 10.1 WDK Windows 7 display , extended format aware requirements
- extended format aware requirements WDK Windows 7 display
- XR_BIAS WDK Windows 7 display
- XR_BIAS WDK Windows 7 display , PresentDXGI
- XR_BIAS WDK Windows 7 display , BltDXGI
- PresentDXGI and XR_BIAS WDK Windows 7 display
- BltDXGI and XR_BIAS WDK Windows 7 display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Extended Format Aware Requirements


This section applies only to Windows 7 and later operating systems.

User-mode display drivers that are extended format aware guarantee to return accurate values from their [**CheckFormatSupport**](https://msdn.microsoft.com/library/windows/hardware/ff539390) entry-point function for every format in the table in the [Details of the Extended Format](details-of-the-extended-format.md) section. However, drivers do not necessarily support every format.

Extended format aware drivers implicitly guarantee that casting of fully-typed back buffers is supported.

Extended format aware drivers implicitly support all of the BGRX and BGRA formats with capabilities as defined in the table in the [Details of the Extended Format](details-of-the-extended-format.md) section.

Extended format aware drivers implicitly support BGRA and BGRA\_SRGB scan out as described in the [BGRA Scan-Out Support](bgra-scan-out-support.md) section.

If an extended format aware driver returns any support bits for any of the new formats, it must return all of the bits that are required in the table in the [Details of the Extended Format](details-of-the-extended-format.md) section. The driver cannot return any bits that are not required in the table.

### <span id="claiming_support_under_direct3d_version_10_1"></span><span id="CLAIMING_SUPPORT_UNDER_DIRECT3D_VERSION_10_1"></span>Claiming Support under Direct3D Version 10.1

The Direct3D 10.1 and later DDIs are updated to allow the user-mode display driver to claim support for two new versions. One version corresponds to drivers that want to support feature level 10.0, and the other version corresponds to drivers that want to support feature level 10.1. The following are the new version definitions:

```
// D3D10.0 or D3D10.1 with extended format support (but not Windows 7 scheduling)
#define D3D10_0_x_DDI_BUILD_VERSION 10
#define D3D10_0_x_DDI_SUPPORTED ((((UINT64)D3D10_0_DDI_INTERFACE_VERSION) << 32) | (((UINT64)D3D10_0_x_DDI_BUILD_VERSION) << 16))
#define D3D10_1_x_DDI_BUILD_VERSION 10
#define D3D10_1_x_DDI_SUPPORTED ((((UINT64)D3D10_1_DDI_INTERFACE_VERSION) << 32) | (((UINT64)D3D10_1_x_DDI_BUILD_VERSION) << 16))
```

### <span id="xr_bias_and_presentdxgi"></span><span id="XR_BIAS_AND_PRESENTDXGI"></span>XR\_BIAS and PresentDXGI

Drivers are not required to support windowed present of XR\_BIAS resources through calls to their [**PresentDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff569179) functions. These cases are restricted at the runtime level. As with all other formats, drivers perform full-screen present of XR\_BIAS through either a flip operation or a bit-block transfer (bitblt) operation with an identical source and destination resource. No stretch or conversion is necessary.

### <span id="xr_bias_and_bltdxgi"></span><span id="XR_BIAS_AND_BLTDXGI"></span>XR\_BIAS and BltDXGI

The Direct3D runtime calls a driver's [**BltDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff538252) function to perform only the following operations on XR\_BIAS source resources:

-   A copy to a destination that is also XR\_BIAS

-   A copy of unmodified source data

-   A stretch in which point sample is acceptable

-   A rotation

Because XR\_BIAS does not support Multiple Sample Anti Aliasing (MSAA), drivers are not required to resolve XR\_BIAS resources.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Extended%20Format%20Aware%20Requirements%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




