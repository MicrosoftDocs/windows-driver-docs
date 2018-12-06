---
title: Non-COM-Based Rendering Plug-Ins
description: Non-COM-Based Rendering Plug-Ins
ms.assetid: 435f9754-50be-4a4b-a5b4-b2bc8d66f034
keywords:
- non-COM-based rendering plug-ins WDK print
- rendering plug-ins WDK print , non-COM-based
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Non-COM-Based Rendering Plug-Ins





A printer minidriver notifies the core driver of its capabilities by implementing the [**OEMEnableDriver**](https://msdn.microsoft.com/library/windows/hardware/ff557708) function, which fills in the members of a [**DRVENABLEDATA**](https://msdn.microsoft.com/library/windows/hardware/ff556206) structure. The **pdrvfn** member of this structure should be set with the array address of [**DRVFN**](https://msdn.microsoft.com/library/windows/hardware/ff556221) structures. Each element of this array should be initialized with a function index, and the address of one of the **OEM***Xxx* functions that the IHV is implementing, respectively. (For detailed descriptions of each of the **OEM***Xxx* functions, see [Non-COM-Based DDI Hook-Out Functions](https://msdn.microsoft.com/library/windows/hardware/ff557586).)

When an application calls Microsoft Win32 GDI to perform a rendering task, Win32 GDI in turn calls into the Unidrv or Pscript5 core driver, which usually handles the task. However, if a printer minidriver has indicated that it is capable of hooking out a specific rendering operation, ,the core driver passes the rendering task to the IHV rendering plug-in.

For example, consider an application that makes a call to the Win32 **LineTo** API (described in the Windows SDK documentation). Generally, this would result in another call to the core driver's [**DrvLineTo**](https://msdn.microsoft.com/library/windows/hardware/ff556245) DDI to draw the line. If the printer minidriver has indicated that it intends to hook out calls to this DDI, however, **DrvLineTo** immediately forwards the call to the IHV's [**OEMLineTo**](https://msdn.microsoft.com/library/windows/hardware/ff557761) function.

An IHV can implement **OEMLineTo**, or any of the other hook-out functions described in [Non-COM-Based DDI Hook-Out Functions](https://msdn.microsoft.com/library/windows/hardware/ff557586), so that it can completely handle the rendering operation, or it can call back to have the core driver handle that operation.

**OEMLineTo** could be implemented as shown in the following pseudocode example:

```cpp
BOOL APIENTRY
  OEMLineTo(
    SURFOBJ  *pso,
    CLIPOBJ  *pco,
    BRUSHOBJ  *pbo,
    LONG  x1,
    LONG  y1,
    LONG  x2,
    LONG  y2,
    RECTL  *prclBounds,
    MIX  mix
)
{
if ( OEM intends to handle the call ) {
 code to handle the call
}
else
// OEM calls Unidrv's DrvLineTo DDI
  bRetVal = (((PFN_DrvLineTo)(poempdev->pfnUnidrv[UD_DrvLineTo])) (
 pso,
            pco,
            pbo,
            x1,
            x2,
 y1,
            y2,
            prclBounds,
            mix,));
}
```

In the preceding example, the expression

```cpp
poempdev->pfnUnidrv[UD_DrvLineTo]
```

evaluates to the address of the core driver's **DrvLineTo** DDI. The (**PFN\_DrvLineTo**) expression that precedes it casts the function pointer to the appropriate type. Each of the hook-out functions listed in this section is associated with its own function pointer.

Note that when an **OEM***Xxx* DDI calls back to the Unidrv core driver and the surface involved is a device-managed surface, Unidrv can simply ignore the call by returning **FALSE**.

 

 




