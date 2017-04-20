---
title: Accessing Plug-In Interfaces from Printer Drivers
author: windows-driver-content
description: Accessing Plug-In Interfaces from Printer Drivers
ms.assetid: 639734c9-1aac-428c-bd5b-803607f1cf66
keywords:
- COM interfaces WDK print , accessing plug-in interfaces
- plug-ins WDK print , accessing interfaces
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Accessing Plug-In Interfaces from Printer Drivers


## <a href="" id="ddk-accessing-plug-in-interfaces-from-printer-drivers-gg"></a>


If a UI plug-in or rendering plug-in is installed, the printer driver (Unidrv or Pscript5) uses the following calling sequence to obtain access to the plug-in's [IPrintOemUI](iprintoemui-com-interface.md), [IPrintOemUI2](iprintoemui2-com-interface.md), [IPrintOemUni](iprintoemuni-com-interface.md), [IPrintOemUni2](iprintoemuni2-com-interface.md), [IPrintOemUni3](iprintoemuni3-com-interface.md), [IPrintOemPS](iprintoemps-com-interface.md), or [IPrintOemPS2](iprintoemps2-com-interface.md) COM interface:

1.  The driver calls LoadLibrary to load the plug-in DLL, which causes a call to the plug-in's `DllMain` function.

2.  The driver calls the plug-in's `DllGetClassObject` function, which returns a pointer to the plug-in's IClassFactory interface.

3.  The driver calls the IClassFactory interface's CreateInstance method, specifying an interface identifier of **IID\_IUnknown**, which causes the method to create an instance of the plug-in's [IPrintOemUI](iprintoemui-com-interface.md), [IPrintOemUI2](iprintoemui2-com-interface.md), [IPrintOemUni](iprintoemuni-com-interface.md), [IPrintOemUni2](iprintoemuni2-com-interface.md), [IPrintOemUni3](iprintoemuni3-com-interface.md), [IPrintOemPS](iprintoemps-com-interface.md), or [IPrintOemPS2](iprintoemps2-com-interface.md) interface and return a pointer to the instance's IUnknown interface.

4.  The driver calls the IUnknown interface's QueryInterface method to determine which version of the [IPrintOemUI](iprintoemui-com-interface.md), [IPrintOemUI2](iprintoemui2-com-interface.md), [IPrintOemUni](iprintoemuni-com-interface.md), [IPrintOemUni2](iprintoemuni2-com-interface.md), [IPrintOemUni3](iprintoemuni3-com-interface.md), [IPrintOemPS](iprintoemps-com-interface.md), or [IPrintOemPS2](iprintoemps2-com-interface.md) interface is supported by the plug-in and to receive a pointer to the supported interface.

5.  The driver calls the plug-in interface's `PublishDriverInterface` method to make the driver's IPrintOemDriverUI, IPrintCoreUI2, IPrintOemDriverUni, IPrintOemDriverPS, or IPrintCorePS2 interface available to the plug-in.

6.  If the plug-in has implemented the [IPrintOemUni](iprintoemuni-com-interface.md) interface, the driver calls [**IPrintOemUni::GetImplementedMethod**](https://msdn.microsoft.com/library/windows/hardware/ff554253) to determine which interface methods have been implemented. Similarly, if the plug-in has implemented the [IPrintOemUni2](iprintoemuni2-com-interface.md) interface, the driver calls **IPrintOemUni2::GetImplementedMethod** for the same purpose.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Accessing%20Plug-In%20Interfaces%20from%20Printer%20Drivers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


