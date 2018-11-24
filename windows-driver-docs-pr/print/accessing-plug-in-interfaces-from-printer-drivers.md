---
title: Accessing Plug-In Interfaces from Printer Drivers
description: Accessing Plug-In Interfaces from Printer Drivers
ms.assetid: 639734c9-1aac-428c-bd5b-803607f1cf66
keywords:
- COM interfaces WDK print , accessing plug-in interfaces
- plug-ins WDK print , accessing interfaces
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing Plug-In Interfaces from Printer Drivers





If a UI plug-in or rendering plug-in is installed, the printer driver (Unidrv or Pscript5) uses the following calling sequence to obtain access to the plug-in's [IPrintOemUI](iprintoemui-com-interface.md), [IPrintOemUI2](iprintoemui2-com-interface.md), [IPrintOemUni](iprintoemuni-com-interface.md), [IPrintOemUni2](iprintoemuni2-com-interface.md), [IPrintOemUni3](iprintoemuni3-com-interface.md), [IPrintOemPS](iprintoemps-com-interface.md), or [IPrintOemPS2](iprintoemps2-com-interface.md) COM interface:

1.  The driver calls LoadLibrary to load the plug-in DLL, which causes a call to the plug-in's `DllMain` function.

2.  The driver calls the plug-in's `DllGetClassObject` function, which returns a pointer to the plug-in's IClassFactory interface.

3.  The driver calls the IClassFactory interface's CreateInstance method, specifying an interface identifier of **IID\_IUnknown**, which causes the method to create an instance of the plug-in's [IPrintOemUI](iprintoemui-com-interface.md), [IPrintOemUI2](iprintoemui2-com-interface.md), [IPrintOemUni](iprintoemuni-com-interface.md), [IPrintOemUni2](iprintoemuni2-com-interface.md), [IPrintOemUni3](iprintoemuni3-com-interface.md), [IPrintOemPS](iprintoemps-com-interface.md), or [IPrintOemPS2](iprintoemps2-com-interface.md) interface and return a pointer to the instance's IUnknown interface.

4.  The driver calls the IUnknown interface's QueryInterface method to determine which version of the [IPrintOemUI](iprintoemui-com-interface.md), [IPrintOemUI2](iprintoemui2-com-interface.md), [IPrintOemUni](iprintoemuni-com-interface.md), [IPrintOemUni2](iprintoemuni2-com-interface.md), [IPrintOemUni3](iprintoemuni3-com-interface.md), [IPrintOemPS](iprintoemps-com-interface.md), or [IPrintOemPS2](iprintoemps2-com-interface.md) interface is supported by the plug-in and to receive a pointer to the supported interface.

5.  The driver calls the plug-in interface's `PublishDriverInterface` method to make the driver's IPrintOemDriverUI, IPrintCoreUI2, IPrintOemDriverUni, IPrintOemDriverPS, or IPrintCorePS2 interface available to the plug-in.

6.  If the plug-in has implemented the [IPrintOemUni](iprintoemuni-com-interface.md) interface, the driver calls [**IPrintOemUni::GetImplementedMethod**](https://msdn.microsoft.com/library/windows/hardware/ff554253) to determine which interface methods have been implemented. Similarly, if the plug-in has implemented the [IPrintOemUni2](iprintoemuni2-com-interface.md) interface, the driver calls **IPrintOemUni2::GetImplementedMethod** for the same purpose.

 

 




