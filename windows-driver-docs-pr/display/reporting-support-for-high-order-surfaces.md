---
title: Reporting Support for High Order Surfaces
description: Reporting Support for High Order Surfaces
ms.assetid: cf214ed7-2c06-4dc6-8c73-c2a3f51332ab
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , high order surfaces, reporting support
- high order surfaces WDK DirectX 8.0 , reporting support
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reporting Support for High Order Surfaces


## <span id="ddk_reporting_support_for_high_order_surfaces_gg"></span><span id="DDK_REPORTING_SUPPORT_FOR_HIGH_ORDER_SURFACES_GG"></span>


A driver reports its support for high order surfaces using four new capability bits in the **DevCaps** field of the D3DCAPS8 structure. These flags are as follows:

### <span id="d3ddevcaps_quinticrtpatches"></span><span id="D3DDEVCAPS_QUINTICRTPATCHES"></span>D3DDEVCAPS\_QUINTICRTPATCHES

Device supports quintic béziers and B-splines.

### <span id="d3ddevcaps_rtpatches"></span><span id="D3DDEVCAPS_RTPATCHES"></span>D3DDEVCAPS\_RTPATCHES

Device supports rectangular and triangular patches.

### <span id="d3ddevcaps_rtpatchhandlezero"></span><span id="D3DDEVCAPS_RTPATCHHANDLEZERO"></span>D3DDEVCAPS\_RTPATCHHANDLEZERO

When this device capability is set, the hardware architecture does not require caching of any information and that uncached patches (handle zero) are drawn as efficiently as cached ones. Note that D3DDEVCAPS\_RPATCHHANDLERZERO does not mean that a patch with handle zero can be drawn. A handle zero patch can always be drawn whether this cap is set or not.

### <span id="d3ddevcaps_npatches"></span><span id="D3DDEVCAPS_NPATCHES"></span>D3DDEVCAPS\_NPATCHES

Device supports n-patches.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Support%20for%20High%20Order%20Surfaces%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




