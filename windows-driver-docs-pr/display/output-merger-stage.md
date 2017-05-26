---
title: Output Merger Stage
description: Output Merger Stage
ms.assetid: 9b549614-0f51-4c79-a6c4-ba907a5f9068
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Output%20Merger%20Stage%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




