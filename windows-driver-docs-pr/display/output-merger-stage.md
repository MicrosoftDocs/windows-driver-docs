---
title: Output Merger Stage
description: Output Merger Stage
ms.assetid: 9b549614-0f51-4c79-a6c4-ba907a5f9068
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Output Merger Stage


The final step in the logical pipeline is visibility determination, through stencil or depth, and writing or blending of outputs to render targets, which can be one of many resource types. These operations, as well as the binding of output resources (render targets), are defined at the output merger stage.

The Direct3D runtime calls the following driver functions to create, set up, clear, and destroy the output:

[**CalcPrivateBlendStateSize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_calcprivateblendstatesize)

[**CalcPrivateDepthStencilStateSize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_calcprivatedepthstencilstatesize)

[**CalcPrivateDepthStencilViewSize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_calcprivatedepthstencilviewsize)

[**ClearDepthStencilView**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_cleardepthstencilview)

[**ClearRenderTargetView**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_clearrendertargetview)

[**CreateBlendState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createblendstate)

[**CreateDepthStencilState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdepthstencilstate)

[**CreateDepthStencilView**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdepthstencilview)

[**DestroyBlendState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_destroyblendstate)

[**DestroyDepthStencilState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_destroydepthstencilstate)

[**DestroyDepthStencilView**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_destroydepthstencilview)

[**SetBlendState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_setblendstate)

[**SetDepthStencilState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_setdepthstencilstate)

[**SetPredication**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_setpredication)

[**SetRenderTargets**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_setrendertargets)

[**SetTextFilterSize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_settextfiltersize)

 

 





