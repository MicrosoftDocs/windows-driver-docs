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

[**CalcPrivateBlendStateSize**](https://msdn.microsoft.com/library/windows/hardware/ff538274)

[**CalcPrivateDepthStencilStateSize**](https://msdn.microsoft.com/library/windows/hardware/ff538282)

[**CalcPrivateDepthStencilViewSize**](https://msdn.microsoft.com/library/windows/hardware/ff538284)

[**ClearDepthStencilView**](https://msdn.microsoft.com/library/windows/hardware/ff539408)

[**ClearRenderTargetView**](https://msdn.microsoft.com/library/windows/hardware/ff539409)

[**CreateBlendState**](https://msdn.microsoft.com/library/windows/hardware/ff540594)

[**CreateDepthStencilState**](https://msdn.microsoft.com/library/windows/hardware/ff540627)

[**CreateDepthStencilView**](https://msdn.microsoft.com/library/windows/hardware/ff540629)

[**DestroyBlendState**](https://msdn.microsoft.com/library/windows/hardware/ff552745)

[**DestroyDepthStencilState**](https://msdn.microsoft.com/library/windows/hardware/ff552759)

[**DestroyDepthStencilView**](https://msdn.microsoft.com/library/windows/hardware/ff552762)

[**SetBlendState**](https://msdn.microsoft.com/library/windows/hardware/ff569527)

[**SetDepthStencilState**](https://msdn.microsoft.com/library/windows/hardware/ff569532)

[**SetPredication**](https://msdn.microsoft.com/library/windows/hardware/ff569547)

[**SetRenderTargets**](https://msdn.microsoft.com/library/windows/hardware/ff569553)

[**SetTextFilterSize**](https://msdn.microsoft.com/library/windows/hardware/ff569663)

 

 





