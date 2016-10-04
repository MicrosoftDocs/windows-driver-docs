---
title: Customized Graphics DDI Functions
author: windows-driver-content
description: Customized Graphics DDI Functions
MS-HAID:
- 'custdrvr\_485af06e-fe7c-45b0-953b-7d87c4071382.xml'
- 'print.customized\_graphics\_ddi\_functions'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 33d7d567-5371-4873-a4ef-cd2b06f65d73
keywords: ["rendering plug-ins WDK print , graphics DDI functions", "graphics DDI functions WDK print", "hooking graphics DDI functions WDK print"]
---

# Customized Graphics DDI Functions


## <a href="" id="ddk-customized-graphics-ddi-functions-gg"></a>


Printer minidriver developers can extend the capabilities of the core printer driver graphics DDIs by implementing plug-in methods. A rendering plug-in can hook out some graphics DDI functions to provide customized implementations of the core printer driver functions. Developers of new printer rendering plug-ins should implement COM-based methods for their plug-ins. See [COM Interfaces for Rendering Plug-Ins](com-interfaces-for-rendering-plug-ins.md) for a list of the defined COM interfaces.

Prior to the publication of the COM interfaces, IHVs could extend the capabilities of the graphics DDIs by implementing one or more OEM*Xxx* functions for their rendering plug-ins. Although the use of these functions is still supported for compatibility reasons, writers of new rendering plug-ins should use the methods in the COM interfaces.

The rest of this section contains the following topics:

[COM-Based Rendering Plug-Ins](com-based-rendering-plug-ins.md)

[Non-COM-Based Rendering Plug-Ins](non-com-based-rendering-plug-ins.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Customized%20Graphics%20DDI%20Functions%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


