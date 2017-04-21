---
title: Reporting Support for Programmable Pixel Processing Hardware
description: Reporting Support for Programmable Pixel Processing Hardware
ms.assetid: e6456c2a-d40f-4082-9122-fab9299808f7
keywords:
- pixel shaders WDK DirectX 8.0 , programmable hardware
- programmable pixel processing hardware WDK DirectX 8.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reporting Support for Programmable Pixel Processing Hardware


## <span id="ddk_reporting_support_for_programmable_pixel_processing_hardware_gg"></span><span id="DDK_REPORTING_SUPPORT_FOR_PROGRAMMABLE_PIXEL_PROCESSING_HARDWARE_GG"></span>


For a DirectX 8.0 level driver to report support for programmable pixel shader hardware, it must set the **PixelShaderVersion** field of the D3DCAPS8 structure to a valid, nonzero pixel shader version number. The **PixelShaderVersion** is a DWORD where the most significant word must have the value 0xFFFF and the least significant word holds the actual version number. This least significant byte of this word holds the minor version number and the most significant byte holds the major version number. Because the format of this DWORD is complex, the driver must set the value of **PixelShaderVersion** using the macro D3DPS\_VERSION defined in *d3d8types.h*. For example, the following code fragment sets the **PixelShaderVersion** to indicate support for 1.0 level functionality.

```
myD3DCaps8.PixelShaderVersion = D3DPS_VERSION(1, 0);
```

Drivers that do not support programmable pixel processing should set **PixelShaderVersion** to zero.

Unlike reporting the number of constant registers a device has for vertex shaders, a device cannot expose more constant registers than are defined by the pixel shader version it specifies. For example, a device that implements the 1.0 pixel shader specification must expose only eight constant pixel shader registers. However, there is an additional pixel shader related capability that a driver should set, **MaxPixelShaderValue**. This field gives the internal range of values supported for pixel color blending operations.

Implementations must allow data within the range they report to pass through pixel processing unmodified (for example unclamped). This value normally defines the limits of a signed range, that is, an absolute value. Therefore, for example, 1 indicates that the range is \[-1.0 to 1.0\], and 8 indicates that the range is \[-8.0 to 8.0\]. For pixel shader version 1.0 to 1.3, the driver must set the value in **MaxPixelShaderValue** to a minimum of 1. For 1.4, the driver must set the value in **MaxPixelShaderValue** to a minimum of 8.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Support%20for%20Programmable%20Pixel%20Processing%20Hardware%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




