---
title: Retroactively Requiring Free-Threaded CalcPrivate DDIs
description: Retroactively Requiring Free-Threaded CalcPrivate DDIs
ms.assetid: a25fbe8e-737a-4b47-8293-7cf13ebc8ac2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retroactively Requiring Free-Threaded CalcPrivate DDIs


Direct3D version 11 retroactively requires user-mode display driver functions that begin with *pfnCalcPrivate* on Direct3D version 10 DDI functions that are free-threaded. This retroactive requirement matches the behavior of the Direct3D version 11 DDI to always require *pfnCalcPrivate\** and [**pfnCalcDeferredContextHandleSize**](https://msdn.microsoft.com/library/windows/hardware/ff538272) functions that are free-threaded even if the driver indicates it does not support DDI threading. For more information about how the driver indicates threading support, see [Supporting Threading, Command Lists, and 3-D Pipeline](supporting-threading--command-lists--and-3-d-pipeline.md). The reason for this retroactive requirement is that such functions are typically very simple as they return an immediate value for size. The functions that are more complex decide which immediate value to return based on the parameters that are passed to the function. The requirement for functions that begin with *pfnCalcPrivate* to actually write any data to places other than the stack does not exist. The requirement for these functions to read any data other than parameters is a rarity. Any requirement to read data does not produce contention issues. This fact allows the Direct3D version 11 API to take a much needed optimization and prevent from performing expensive synchronization twice per create (for example, any call to create an object like a call to [**CreateResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540691) or [**CreateGeometryShader**](https://msdn.microsoft.com/library/windows/hardware/ff540648)), instead of just once.

A notable exception to this retroactive free-threaded requirement is the [**CalcPrivateDeviceSize**](https://msdn.microsoft.com/library/windows/hardware/ff538288) function that is used to satisfy display device creation. *CalcPrivateDeviceSize* is located on the adapter function table ([**D3D10\_2DDI\_ADAPTERFUNCS**](https://msdn.microsoft.com/library/windows/hardware/ff541900) or [**D3D10DDI\_ADAPTERFUNCS**](https://msdn.microsoft.com/library/windows/hardware/ff541811)). *CalcPrivateDeviceSize* does not fall underneath the group of functions that experienced the relaxation in threading model. It is not required to free-thread the *CalcPrivateDeviceSize* function.

 

 





