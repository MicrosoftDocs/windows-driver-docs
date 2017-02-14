---
title: Enabling Alpha Channels On Full-Screen Back Buffers
description: Enabling Alpha Channels On Full-Screen Back Buffers
ms.assetid: 9d922464-fb1b-459b-9363-61afff7c51e3
keywords: ["DirectX 8.0 release notes WDK Windows 2000 display , alpha channels on full-screen back buffers", "flipping chain WDK DirectX 8.0", "primary flipping chain WDK DirectX 8.0", "full-screen flipping chain WDK DirectX 8.0", "alpha channels WDK DirectX 8.0"]
---

# Enabling Alpha Channels On Full-Screen Back Buffers


## <span id="ddk_enabling_alpha_channels_on_full_screen_back_buffers_gg"></span><span id="DDK_ENABLING_ALPHA_CHANNELS_ON_FULL_SCREEN_BACK_BUFFERS_GG"></span>


In the DirectDraw DDI, the creation of a primary flipping chain has no intrinsic pixel format. Consequently, surfaces in this chain take on the pixel format of the display mode. For example, a primary flipping chain created in a 32bpp mode takes on a D3DFMT\_X8R8G8B8 format.

Such a chain is created for many full-screen applications. Because the back buffer of the chain has no alpha channel, the D3DRS\_ALPHABLENDENABLE render state and the associated blend-render states for destination surfaces are poorly defined. DirectX 8.1 introduces a new feature that the Direct3D runtime uses to inform a driver of an application's request to create a full-screen flipping chain of surfaces with an alpha channel in the pixel formats of those surfaces.

To indicate support of this feature, the driver must set the D3DCAPS3\_ALPHA\_FULLSCREEN\_FLIP\_OR\_DISCARD bit (defined in the *d3d8caps.h* file) in the **Caps3** member of the D3DCAPS8 structure. The driver returns a D3DCAPS8 structure in response to a **GetDriverInfo2** query as described in [Reporting DirectX 8.0 Style Direct3D Capabilities](reporting-directx-8-0-style-direct3d-capabilities.md). Support of this query is described in [Supporting GetDriverInfo2](supporting-getdriverinfo2.md).

After support of this feature is determined, the driver can receive [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) calls with the DDSCAPS2\_ENABLEALPHACHANNEL (defined in the *ddraw.h* file) bit set in the **dwCaps2** member of the [**DDSCAPS2**](https://msdn.microsoft.com/library/windows/hardware/ff550292) structure. This bit is only set to create surfaces that are part of a primary flipping chain or that are on stand-alone back buffers.

If the driver detects this bit, the driver determines that the surfaces take on not the display mode's format, but the display mode's format plus alpha. For example, in a 32bpp mode, such surfaces should be given the D3DFMT\_A8R8G8B8 format.

This feature is available on Windows XP and later versions and on Windows 2000 operating system versions that have the DirectX 8.1 runtime installed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Enabling%20Alpha%20Channels%20On%20Full-Screen%20Back%20Buffers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




