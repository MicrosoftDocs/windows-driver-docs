---
title: Retroactively Requiring Free-Threaded CalcPrivate DDIs
description: Retroactively Requiring Free-Threaded CalcPrivate DDIs
ms.assetid: a25fbe8e-737a-4b47-8293-7cf13ebc8ac2
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Retroactively Requiring Free-Threaded CalcPrivate DDIs


Direct3D version 11 retroactively requires user-mode display driver functions that begin with *pfnCalcPrivate* on Direct3D version 10 DDI functions that are free-threaded. This retroactive requirement matches the behavior of the Direct3D version 11 DDI to always require *pfnCalcPrivate\** and [**pfnCalcDeferredContextHandleSize**](https://msdn.microsoft.com/library/windows/hardware/ff538272) functions that are free-threaded even if the driver indicates it does not support DDI threading. For more information about how the driver indicates threading support, see [Supporting Threading, Command Lists, and 3-D Pipeline](supporting-threading--command-lists--and-3-d-pipeline.md). The reason for this retroactive requirement is that such functions are typically very simple as they return an immediate value for size. The functions that are more complex decide which immediate value to return based on the parameters that are passed to the function. The requirement for functions that begin with *pfnCalcPrivate* to actually write any data to places other than the stack does not exist. The requirement for these functions to read any data other than parameters is a rarity. Any requirement to read data does not produce contention issues. This fact allows the Direct3D version 11 API to take a much needed optimization and prevent from performing expensive synchronization twice per create (for example, any call to create an object like a call to [**CreateResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540691) or [**CreateGeometryShader**](https://msdn.microsoft.com/library/windows/hardware/ff540648)), instead of just once.

A notable exception to this retroactive free-threaded requirement is the [**CalcPrivateDeviceSize**](https://msdn.microsoft.com/library/windows/hardware/ff538288) function that is used to satisfy display device creation. *CalcPrivateDeviceSize* is located on the adapter function table ([**D3D10\_2DDI\_ADAPTERFUNCS**](https://msdn.microsoft.com/library/windows/hardware/ff541900) or [**D3D10DDI\_ADAPTERFUNCS**](https://msdn.microsoft.com/library/windows/hardware/ff541811)). *CalcPrivateDeviceSize* does not fall underneath the group of functions that experienced the relaxation in threading model. It is not required to free-thread the *CalcPrivateDeviceSize* function.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Retroactively%20Requiring%20Free-Threaded%20CalcPrivate%20DDIs%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




