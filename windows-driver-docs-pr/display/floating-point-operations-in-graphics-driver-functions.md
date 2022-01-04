---
title: Floating-Point Operations in Graphics Driver Functions
description: Floating-Point Operations in Graphics Driver Functions
keywords:
- GDI WDK Windows 2000 display , floating-point operations
- graphics drivers WDK Windows 2000 display , floating-point operations
- drawing WDK GDI , floating-point operations
- floating-point operations WDK GDI
- FPU WDK GDI
ms.date: 04/20/2017
---

# Floating-Point Operations in Graphics Driver Functions


## <span id="ddk_floating_point_operations_in_graphics_driver_functions_gg"></span><span id="DDK_FLOATING_POINT_OPERATIONS_IN_GRAPHICS_DRIVER_FUNCTIONS_GG"></span>


If a graphics driver function contains code that uses the floating-point unit (FPU), that code must be preceded by a call to [**EngSaveFloatingPointState**](/windows/win32/api/winddi/nf-winddi-engsavefloatingpointstate) and followed by a call to [**EngRestoreFloatingPointState**](/windows/win32/api/winddi/nf-winddi-engrestorefloatingpointstate). For a list of graphics driver functions, see [Graphics Driver Functions](graphics-driver-functions.md).

If an FPU is available, it will be used by any code that assigns a value to a floating-point variable or performs calculations that involve floating-point numbers. For example, each of the following lines of code uses the FPU.

```cpp
double myDouble = 5;
int myInt = 5 * 4.3;
int myInt = 50 * cos(2);
```

Suppose you are writing a [**DrvAlphaBlend**](/windows/win32/api/winddi/nf-winddi-drvalphablend) function that uses the FPU. The following example demonstrates how you should save and restore the floating-point state.

```cpp
#define DRIVER_TAG // Put your driver tag here, for example 'zyxD'

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

GDI automatically saves the floating-point state for any calls to a driver's [**DrvEscape**](/windows/win32/api/winddi/nf-winddi-drvescape) function when the escape is OPENGL\_CMD, OPENGL\_GETINFO, or MCDFUNCS. In those cases, you can use the FPU in your *DrvEscape* function without calling **EngSaveFloatingPointState** and **EngRestoreFloatingPointState**.

Most DirectDraw and Direct3D callback functions that perform floating-point operations should also save and restore the floating-point state. For more information, see [Performing Floating-point Operations in DirectDraw](performing-floating-point-operations-in-directdraw.md) and [Performing Floating-point Operations in Direct3D](performing-floating-point-operations-in-direct3d.md).

For information about floating-point services provided by GDI, see [GDI Floating-Point Services](gdi-floating-point-services.md).

 

