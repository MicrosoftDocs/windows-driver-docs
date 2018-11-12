---
title: Reporting Support for High Order Surfaces
description: Reporting Support for High Order Surfaces
ms.assetid: cf214ed7-2c06-4dc6-8c73-c2a3f51332ab
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , high order surfaces, reporting support
- high order surfaces WDK DirectX 8.0 , reporting support
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





