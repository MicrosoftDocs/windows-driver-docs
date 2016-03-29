---
title: COM-Based Rendering Plug-Ins
description: COM-Based Rendering Plug-Ins
ms.assetid: c80d6c2b-ba4d-4bd1-bd3a-8c1b0bf29884
keywords: ["COM-based rendering plug-ins WDK print", "rendering plug-ins WDK print , COM-based"]
---

# COM-Based Rendering Plug-Ins


## <a href="" id="ddk-com-based-rendering-plug-ins-gg"></a>


To provide customized hooking functions, your COM-based rendering plug-in must implement the [**IPrintOemUni::EnableDriver**](https://msdn.microsoft.com/library/windows/hardware/ff554248) or [**IPrintOemPS::EnableDriver**](https://msdn.microsoft.com/library/windows/hardware/ff553212) method, which fills in a [**DRVENABLEDATA**](https://msdn.microsoft.com/library/windows/hardware/ff556206) structure with the address of each hooking function.

A COM-based rendering plug-in can hook out a graphics DDI function only if the Unidrv or Pscript5 driver defines the function. For a list of such functions, see [**IPrintOemUni::EnableDriver**](https://msdn.microsoft.com/library/windows/hardware/ff554248) or [**IPrintOemPS::EnableDriver**](https://msdn.microsoft.com/library/windows/hardware/ff553212).

If you provide a particular customized hooking function, that function preempts the driver's equivalent graphics DDI function. When you design a customized hooking function, you have the following options:

-   The hooking function can completely handle the graphics DDI operation internally.

-   The hooking function can call back to the printer driver's equivalent graphics DDI function.

By calling back to the driver's graphics DDI function, the hooking function can perform preprocessing or postprocessing of function arguments, but still allow the driver to actually perform the graphics DDI operation. One of the input arguments to a rendering plug-in's [**IPrintOemUni::EnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff554249) or [**IPrintOemPS::EnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff553215) method is a [**DRVENABLEDATA**](https://msdn.microsoft.com/library/windows/hardware/ff556206) structure that contains pointers to the driver's graphics DDI functions. If you want to call back to these functions, you should save the contents of this structure.

It might be necessary for you to provide a [customized PDEV structure](customized-pdev-structures.md). You can reference this structure from within a graphics DDI hooking function, through the [**SURFOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff569901) structure pointer that each hooking function receives as input. Specifically, the SURFOBJ structure's **dhpdev** member points to a [**DEVOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff547573) structure, and the DEVOBJ structure's **pdevOEM** member points to your customized PDEV structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20COM-Based%20Rendering%20Plug-Ins%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




