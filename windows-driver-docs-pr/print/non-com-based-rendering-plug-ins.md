---
title: Non-COM-Based Rendering Plug-Ins
author: windows-driver-content
description: Non-COM-Based Rendering Plug-Ins
MS-HAID:
- 'custdrvr\_6fb879b7-eb9d-426b-9b4d-4f5112f1af12.xml'
- 'print.non\_com\_based\_rendering\_plug\_ins'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 435f9754-50be-4a4b-a5b4-b2bc8d66f034
keywords: ["non-COM-based rendering plug-ins WDK print", "rendering plug-ins WDK print , non-COM-based"]
---

# Non-COM-Based Rendering Plug-Ins


## <a href="" id="ddk-non-com-based-rendering-plug-ins-gg"></a>


A printer minidriver notifies the core driver of its capabilities by implementing the [**OEMEnableDriver**](https://msdn.microsoft.com/library/windows/hardware/ff557708) function, which fills in the members of a [**DRVENABLEDATA**](https://msdn.microsoft.com/library/windows/hardware/ff556206) structure. The **pdrvfn** member of this structure should be set with the array address of [**DRVFN**](https://msdn.microsoft.com/library/windows/hardware/ff556221) structures. Each element of this array should be initialized with a function index, and the address of one of the **OEM***Xxx* functions that the IHV is implementing, respectively. (For detailed descriptions of each of the **OEM***Xxx* functions, see [Non-COM-Based DDI Hook-Out Functions](https://msdn.microsoft.com/library/windows/hardware/ff557586).)

When an application calls Microsoft Win32 GDI to perform a rendering task, Win32 GDI in turn calls into the Unidrv or Pscript5 core driver, which usually handles the task. However, if a printer minidriver has indicated that it is capable of hooking out a specific rendering operation, ,the core driver passes the rendering task to the IHV rendering plug-in.

For example, consider an application that makes a call to the Win32 **LineTo** API (described in the Windows SDK documentation). Generally, this would result in another call to the core driver's [**DrvLineTo**](https://msdn.microsoft.com/library/windows/hardware/ff556245) DDI to draw the line. If the printer minidriver has indicated that it intends to hook out calls to this DDI, however, **DrvLineTo** immediately forwards the call to the IHV's [**OEMLineTo**](https://msdn.microsoft.com/library/windows/hardware/ff557761) function.

An IHV can implement **OEMLineTo**, or any of the other hook-out functions described in [Non-COM-Based DDI Hook-Out Functions](https://msdn.microsoft.com/library/windows/hardware/ff557586), so that it can completely handle the rendering operation, or it can call back to have the core driver handle that operation.

**OEMLineTo** could be implemented as shown in the following pseudocode example:

```
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
// OEM calls Unidrv&#39;s DrvLineTo DDI
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

```
poempdev->pfnUnidrv[UD_DrvLineTo]
```

evaluates to the address of the core driver's **DrvLineTo** DDI. The (**PFN\_DrvLineTo**) expression that precedes it casts the function pointer to the appropriate type. Each of the hook-out functions listed in this section is associated with its own function pointer.

Note that when an **OEM***Xxx* DDI calls back to the Unidrv core driver and the surface involved is a device-managed surface, Unidrv can simply ignore the call by returning **FALSE**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Non-COM-Based%20Rendering%20Plug-Ins%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


