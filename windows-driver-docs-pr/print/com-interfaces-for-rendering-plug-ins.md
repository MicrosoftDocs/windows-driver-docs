---
title: COM Interfaces for Rendering Plug-Ins
author: windows-driver-content
description: COM Interfaces for Rendering Plug-Ins
ms.assetid: 3a1a67ed-7c29-42fa-9bd2-ee38468f6d4b
keywords: ["rendering plug-ins WDK print , COM interfaces", "COM interfaces WDK print , rendering plug-ins"]
---

# COM Interfaces for Rendering Plug-Ins


## <a href="" id="ddk-com-interfaces-for-rendering-plug-ins-gg"></a>


The following COM interfaces are defined for communication between Microsoft's printer drivers and rendering plug-ins:

[IPrintOemUni COM Interface](iprintoemuni-com-interface.md), which allows the [printer graphics DLL](printer-graphics-dll.md) for Unidrv to call rendering plug-ins.

[IPrintOemUni2 COM Interface](iprintoemuni2-com-interface.md), which extends the capabilities of the IPrintOemUni COM interface.

[IPrintOemUni3 COM Interface](iprintoemuni3-com-interface.md), which extends the capabilities of the IPrintOemUni and IPrintOemUni2 COM interfaces.

[IPrintOemDriverUni COM Interface](iprintoemdriveruni-com-interface.md), which supplies utility operations to rendering plug-ins for Unidrv.

[IPrintOemPS COM Interface](iprintoemps-com-interface.md), which allows the [printer graphics DLL](printer-graphics-dll.md) for Pscript5 to call rendering plug-ins.

[IPrintOemPS2 COM Interface](iprintoemps2-com-interface.md), which extends the capabilities of the IPrintOemPS COM interface.

[IPrintOemDriverPS COM Interface](iprintoemdriverps-com-interface.md), which supplies utility operations to rendering plug-ins for Pscript5.

[IPrintCorePS2 COM Interface](iprintcoreps2-com-interface.md), which provides helper methods for Pscript5 minidriver render plug-ins.

The following figure shows the inheritance tree for the COM interfaces used in render plug-ins.

![diagram illustrating the inheritance tree for the com interfaces used in render plug-ins](images/rendintf.png)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20COM%20Interfaces%20for%20Rendering%20Plug-Ins%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


