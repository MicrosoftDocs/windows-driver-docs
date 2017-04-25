---
title: Minimum Capability Requirements for DirectX 8.0 Drivers
description: Minimum Capability Requirements for DirectX 8.0 Drivers
ms.assetid: 8c939013-516c-4048-8de5-e95529891ac9
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , reporting capabilities
- D3DCAPS8
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Minimum Capability Requirements for DirectX 8.0 Drivers


## <span id="ddk_minimum_capability_requirements_for_directx_8_0_drivers_gg"></span><span id="DDK_MINIMUM_CAPABILITY_REQUIREMENTS_FOR_DIRECTX_8_0_DRIVERS_GG"></span>


In addition to returning the D3DCAPS8 data structure in response to a **GetDriverInfo2** query, the DirectX 8.0 runtime has other requirements that a driver must meet to be considered a DirectX 8.0 level driver.

A DirectX 8.0 driver must explicitly:

-   Report support for one or more vertex streams in the **MaxStreams** field of D3DCAPS8.

-   Report a maximum point sprite size of at least one in the **MaxPointSize** field of D3DCAPS8.

-   Modify its list of supported texture formats to support new style pixel format specifications.

-   Handle the new [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) (DP2) drawing tokens.

-   Handle [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) for vertex and index buffers even if your driver does not support video memory vertex buffer creation. Handles for system memory vertex and index buffers are passed to the driver.

-   Set the new posttransformed clipping flag D3DPMISCCAPS\_CLIPTLVERT if the hardware supports clipping of posttransformed vertex data.

It should be noted that a driver is not required to support any of the new features of DirectX 8.0 such as pixel or vertex shaders, volume textures, point sprites (beyond the nonzero maximum point size), multisampling or even multiple vertex streams (as the driver can set the maximum number of simultaneous vertex streams to one) in order to be considered a DirectX 8.0 driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Minimum%20Capability%20Requirements%20for%20DirectX%208.0%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




