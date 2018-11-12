---
title: Performing Gamma Correction on Swap Chains
description: Performing Gamma Correction on Swap Chains
ms.assetid: 4912cd15-bd56-43b6-9419-66917bf3f72c
keywords:
- gamma correction WDK DirectX 9.0 , swap chains
- swap chains WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Performing Gamma Correction on Swap Chains


## <span id="ddk_performing_gamma_correction_on_swap_chains_gg"></span><span id="DDK_PERFORMING_GAMMA_CORRECTION_ON_SWAP_CHAINS_GG"></span>


Applications can maintain back buffers of their swap chains in linear color space in order to perform blending operations correctly. Because the desktop is typically not in linear color space, gamma correction to the contents of back buffers is required before the contents can be presented on the desktop.

An application calls the **IDirect3DSwapChain9::Present** method to present the contents of the next back buffer in the swap chain. In this call, to indicate that the back-buffer contents are in linear color space, the application sets the D3DPRESENT\_LINEAR\_CONTENT flag. The DirectX 9.0 runtime, in turn, calls the display driver's [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) function with the DDBLT\_EXTENDED\_FLAGS and DDBLT\_EXTENDED\_LINEAR\_CONTENT flags set. When the driver receives this *DdBlt* call, the driver determines that the source surface contains content in a linear color space. The driver can then perform gamma 2.2 correction (sRGB) on the linear color space as part of the blt. For more information about extended blit flags, see [Extended Blt Flags](extended-blt-flags.md).

The driver sets the D3DCAPS3\_LINEAR\_TO\_SRGB\_PRESENTATION capability bit in the **Caps3** member of the D3DCAPS9 structure to indicate that its device supports gamma 2.2 correction. The driver returns a D3DCAPS9 structure in response to a **GetDriverInfo2** query similarly to how it returns a D3DCAPS8 structure as described in [Reporting DirectX 8.0 Style Direct3D Capabilities](reporting-directx-8-0-style-direct3d-capabilities.md). Support of this query is described in [Supporting GetDriverInfo2](supporting-getdriverinfo2.md).

For more information about **IDirect3DSwapChain*Xxx*::Present**, see the latest DirectX SDK documentation.

 

 





