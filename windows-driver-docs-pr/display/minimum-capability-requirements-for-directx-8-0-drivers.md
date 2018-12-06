---
title: Minimum Capability Requirements for DirectX 8.0 Drivers
description: Minimum Capability Requirements for DirectX 8.0 Drivers
ms.assetid: 8c939013-516c-4048-8de5-e95529891ac9
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , reporting capabilities
- D3DCAPS8
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





