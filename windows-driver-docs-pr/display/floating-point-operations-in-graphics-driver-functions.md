---
title: Floating-Point Operations in Graphics Driver Functions
description: Floating-Point Operations in Graphics Driver Functions
ms.assetid: 5f85dc0b-27c1-4fee-9a0a-cb52d5f2dae7
keywords:
- GDI WDK Windows 2000 display , floating-point operations
- graphics drivers WDK Windows 2000 display , floating-point operations
- drawing WDK GDI , floating-point operations
- floating-point operations WDK GDI
- FPU WDK GDI
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Floating-Point Operations in Graphics Driver Functions


## <span id="ddk_floating_point_operations_in_graphics_driver_functions_gg"></span><span id="DDK_FLOATING_POINT_OPERATIONS_IN_GRAPHICS_DRIVER_FUNCTIONS_GG"></span>


If a graphics driver function contains code that uses the floating-point unit (FPU), that code must be preceded by a call to [**EngSaveFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff565010) and followed by a call to [**EngRestoreFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff565006). For a list of graphics driver functions, see [Graphics Driver Functions](graphics-driver-functions.md).

If an FPU is available, it will be used by any code that assigns a value to a floating-point variable or performs calculations that involve floating-point numbers. For example, each of the following lines of code uses the FPU.

```
double myDouble = 5;
int myInt = 5 * 4.3;
int myInt = 50 * cos(2);
```

Suppose you are writing a [**DrvAlphaBlend**](https://msdn.microsoft.com/library/windows/hardware/ff556176) function that uses the FPU. The following example demonstrates how you should save and restore the floating-point state.

```
#define DRIVER_TAG // Put your driver tag here, for example &#39;zyxD&#39;

BOOL DrvAlphaBlend(...)
{
   ...
   ULONG result;
 double floatVal;
   VOID* pBuf;
   ULONG bufSize;

 // Determine the size of the required buffer.
   bufSize = EngSaveFloatingPointState(NULL, 0);

 if(bufSize > 0)
   {
 // Allocate a zeroed buffer in the nonpaged pool.
      pBuf = EngAllocMem(
         FL_NONPAGED_MEMORY|FL_ZERO_MEMORY, bufSize, DRIVER_TAG);

 if(pBuf != NULL)
      {
 // The buffer was allocated successfully.
 // Save the floating-point state.
         result = EngSaveFloatingPointState(pBuf, bufSize);

 if(TRUE == result)
         {
 // The floating-point state was saved successfully.
 // Use the FPU.
            floatVal = 0.8;
            ...
            EngRestoreFloatingPointState(pBuffer);
         }

         EngFreeMem(pBuf);
      }
   }
   ...
}
```

GDI automatically saves the floating-point state for any calls to a driver's [**DrvEscape**](https://msdn.microsoft.com/library/windows/hardware/ff556217) function when the escape is OPENGL\_CMD, OPENGL\_GETINFO, or MCDFUNCS. In those cases, you can use the FPU in your *DrvEscape* function without calling **EngSaveFloatingPointState** and **EngRestoreFloatingPointState**.

Most DirectDraw and Direct3D callback functions that perform floating-point operations should also save and restore the floating-point state. For more information, see [Performing Floating-point Operations in DirectDraw](performing-floating-point-operations-in-directdraw.md) and [Performing Floating-point Operations in Direct3D](performing-floating-point-operations-in-direct3d.md).

For information about floating-point services provided by GDI, see [GDI Floating-Point Services](gdi-floating-point-services.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Floating-Point%20Operations%20in%20Graphics%20Driver%20Functions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




