---
title: Customizing Other Printer Interface Operations
author: windows-driver-content
description: Customizing Other Printer Interface Operations
MS-HAID:
- 'custdrvr\_64ea88ab-b165-4878-a8a6-8a8f335b2377.xml'
- 'print.customizing\_other\_printer\_interface\_operations'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ae59d2e7-9049-432d-b519-9e7c88af8d48
keywords: ["user interface plug-ins WDK print , customization methods", "UI plug-ins WDK print , customization methods", "IPrintOemUI"]
---

# Customizing Other Printer Interface Operations


## <a href="" id="ddk-customizing-other-printer-interface-operations-gg"></a>


A UI plug-in can optionally implement any of the following IPrintOemUI methods:

[**IPrintOemUI::DeviceCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff554162)

[**IPrintOemUI::DevQueryPrintEx**](https://msdn.microsoft.com/library/windows/hardware/ff554172)

[**IPrintOemUI::PrinterEvent**](https://msdn.microsoft.com/library/windows/hardware/ff554182)

[**IPrintOemUI::UpgradePrinter**](https://msdn.microsoft.com/library/windows/hardware/ff554189)

The methods are equivalent to similarly named functions exported by the user-mode [printer interface DLL](printer-interface-dll.md) that is used by Unidrv and Pscript5. These customization methods do not replace the equivalent functions in the driver's printer interface DLL. In each case, the printer interface DLL function is called first, and then the driver calls the plug-in's customization method.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Customizing%20Other%20Printer%20Interface%20Operations%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


