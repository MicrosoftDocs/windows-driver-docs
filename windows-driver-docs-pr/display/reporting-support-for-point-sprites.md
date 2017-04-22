---
title: Reporting Support for Point Sprites
description: Reporting Support for Point Sprites
ms.assetid: 57241e2d-a636-454b-8497-17978b6ec285
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , point sprites
- point sprites WDK DirectX 8.0
- size WDK point sprites
- point size WDK DirectX 8.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reporting Support for Point Sprites


## <span id="ddk_reporting_support_for_point_sprites_gg"></span><span id="DDK_REPORTING_SUPPORT_FOR_POINT_SPRITES_GG"></span>


A driver notifies the runtime of its support for point sprites by setting the **MaxPointSize** field of the D3DCAPS8 structure to a floating-point number greater than one (reporting a value of one is part of the requirement to indicate a DX8 level HAL). This value specifies the maximum point width and height in render target pixels. Devices that do not support point sprites can set this value to 1.0.

The size of a point sprite can be specified either by a new per-vertex element or by a new render state. If the driver and hardware combination supports the interleaving of point size information with other vertex data (rather than simply through the point size render state D3DRS\_POINTSIZE), it should set the D3DFVFCAPS\_PSIZE flag in the **FVFCaps** field of the D3DCAPS8 structure.

The absence of D3DFVFCAPS\_PSIZE indicates that the device does not support a vertex format specified in point size (indicated by the D3DFVF\_PSIZE flag); therefore, the base point size is always specified with the D3DRS\_POINTSIZE render state.

DX8 drivers for which the D3DFVFCAPS\_PSIZE flag is not set are still required to accept D3DFVF\_PSIZE and must ignore any point size data passed through the flexible vertex format (FVF). Note that the D3DUSAGE\_POINTS flag must be set for vertex buffers that are to be used for rendering point sprites. If this flag is set, the driver can avoid allocating these vertex buffers in memory types that are slow for reads into the CPU.

Point sprites present a challenge when user clip planes are being used. It is possible that a particular hardware implementation of point sprites will clip only the actual vertex position of the point sprite against the user clip plane, rather than the expanded quad actually rendered. If the driver and hardware combination can support clipping of point sprites by their actual computed size rather than simple vertex position then the D3DPMISCCAPS\_CLIPPLANESCALEDPOINTS capability bit should be set in the **PrimitiveMiscCaps** field of D3DCAPS8.

DX8 drivers that perform transform and lighting (that is, offer hardware vertex processing) are responsible for a correct point sprite implementation. No emulation is performed by the DirectX 8.0 runtime. This means that even if the hardware is used with software vertex processing, point sprites are the DX8 driver's responsibility. However, in DirectX 8.1 and later, if the hardware is used with software vertex processing, the runtime can provide emulation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Support%20for%20Point%20Sprites%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




