---
title: W-Buffering DDI
description: W-Buffering DDI
ms.assetid: eb1270c3-0eaa-47a4-8fc6-53aea981b597
keywords:
- Direct3D WDK Windows 2000 display , w-buffering
- w-buffering WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# W-Buffering DDI


## <span id="ddk_w_buffering_ddi_gg"></span><span id="DDK_W_BUFFERING_DDI_GG"></span>


The driver supports w-buffering by enabling the D3DPRASTERCAPS\_WBUFFER cap in the **dwRasterCaps** member of the [**D3DPRIMCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549034) structure. The D3DRENDERSTATE\_ZENABLE render state is passed to the driver to enable or disable w-buffering or z-buffering.

The [**D3DHAL\_DP2VIEWPORTINFO**](https://msdn.microsoft.com/library/windows/hardware/ff545936) structure supports fields that correspond to world-space front and back clip planes (hither and yon respectively). This information can be used to adjust fog tables as well.

 

 





