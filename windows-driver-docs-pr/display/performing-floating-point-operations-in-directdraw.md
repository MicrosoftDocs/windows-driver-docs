---
title: Performing Floating-point Operations in DirectDraw
description: Performing Floating-point Operations in DirectDraw
ms.assetid: 2ce638e8-2d32-4692-8093-adb413bfbe52
keywords:
- floating-point operations WDK DirectDraw
- drawing WDK DirectDraw , floating-point operations
- DirectDraw WDK Windows 2000 display , floating-point operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Performing Floating-point Operations in DirectDraw


## <span id="ddk_performing_floating_point_operations_in_directdraw_gg"></span><span id="DDK_PERFORMING_FLOATING_POINT_OPERATIONS_IN_DIRECTDRAW_GG"></span>


DirectDraw driver callback functions must perform all floating-point operations between calls to the GDI-supplied [**EngSaveFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff565010) and [**EngRestoreFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff565006) functions. That is, the driver's callback functions must save the floating-point state prior to performing a floating-point operation and must restore the floating-point state when the floating-point operation completes. For more information about floating-point operations, see [Floating-Point Operations in Graphics Driver Functions](floating-point-operations-in-graphics-driver-functions.md).

 

 





