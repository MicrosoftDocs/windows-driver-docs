---
title: Performing Gamma Correction on Swap Chains
description: Performing Gamma Correction on Swap Chains
ms.assetid: 4912cd15-bd56-43b6-9419-66917bf3f72c
keywords:
- gamma correction WDK DirectX 9.0 , swap chains
- swap chains WDK DirectX 9.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Performing Gamma Correction on Swap Chains


## <span id="ddk_performing_gamma_correction_on_swap_chains_gg"></span><span id="DDK_PERFORMING_GAMMA_CORRECTION_ON_SWAP_CHAINS_GG"></span>


Applications can maintain back buffers of their swap chains in linear color space in order to perform blending operations correctly. Because the desktop is typically not in linear color space, gamma correction to the contents of back buffers is required before the contents can be presented on the desktop.

An application calls the **IDirect3DSwapChain9::Present** method to present the contents of the next back buffer in the swap chain. In this call, to indicate that the back-buffer contents are in linear color space, the application sets the D3DPRESENT\_LINEAR\_CONTENT flag. The DirectX 9.0 runtime, in turn, calls the display driver's [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) function with the DDBLT\_EXTENDED\_FLAGS and DDBLT\_EXTENDED\_LINEAR\_CONTENT flags set. When the driver receives this *DdBlt* call, the driver determines that the source surface contains content in a linear color space. The driver can then perform gamma 2.2 correction (sRGB) on the linear color space as part of the blt. For more information about extended blit flags, see [Extended Blt Flags](extended-blt-flags.md).

The driver sets the D3DCAPS3\_LINEAR\_TO\_SRGB\_PRESENTATION capability bit in the **Caps3** member of the D3DCAPS9 structure to indicate that its device supports gamma 2.2 correction. The driver returns a D3DCAPS9 structure in response to a **GetDriverInfo2** query similarly to how it returns a D3DCAPS8 structure as described in [Reporting DirectX 8.0 Style Direct3D Capabilities](reporting-directx-8-0-style-direct3d-capabilities.md). Support of this query is described in [Supporting GetDriverInfo2](supporting-getdriverinfo2.md).

For more information about **IDirect3DSwapChain*Xxx*::Present**, see the latest DirectX SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Performing%20Gamma%20Correction%20on%20Swap%20Chains%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




