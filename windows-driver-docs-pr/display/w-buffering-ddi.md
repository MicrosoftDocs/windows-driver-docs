---
title: W-Buffering DDI
description: W-Buffering DDI
keywords:
- Direct3D WDK Windows 2000 display , w-buffering
- w-buffering WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# W-Buffering DDI


## <span id="ddk_w_buffering_ddi_gg"></span><span id="DDK_W_BUFFERING_DDI_GG"></span>


The driver supports w-buffering by enabling the D3DPRASTERCAPS\_WBUFFER cap in the **dwRasterCaps** member of the [**D3DPRIMCAPS**](/windows-hardware/drivers/ddi/d3dcaps/ns-d3dcaps-_d3dprimcaps) structure. The D3DRENDERSTATE\_ZENABLE render state is passed to the driver to enable or disable w-buffering or z-buffering.

The [**D3DHAL\_DP2VIEWPORTINFO**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2viewportinfo) structure supports fields that correspond to world-space front and back clip planes (hither and yon respectively). This information can be used to adjust fog tables as well.

 

