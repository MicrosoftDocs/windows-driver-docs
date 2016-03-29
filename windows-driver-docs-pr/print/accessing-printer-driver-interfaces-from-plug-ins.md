---
title: Accessing Printer Driver Interfaces from Plug-Ins
description: Accessing Printer Driver Interfaces from Plug-Ins
ms.assetid: 021ba789-99bd-4ab5-98fb-0d24ffd0ce25
keywords: ["COM interfaces WDK print , accessing printer driver interfaces", "plug-ins WDK print , accessing interfaces"]
---

# Accessing Printer Driver Interfaces from Plug-Ins


## <a href="" id="ddk-accessing-printer-driver-interfaces-from-plug-ins-gg"></a>


If a plug-in calls methods that belong to the driver-supplied [IPrintOemDriverUI](iprintoemdriverui-com-interface.md), [IPrintCoreHelperPS](https://msdn.microsoft.com/library/windows/hardware/ff552906), [IPrintCoreHelperUni](https://msdn.microsoft.com/library/windows/hardware/ff552940), [IPrintCoreUI2](iprintcoreui2-com-interface.md), [IPrintOemDriverUni](iprintoemdriveruni-com-interface.md), [IPrintOemDriverPS](iprintoemdriverps-com-interface.md), or [IPrintCorePS2](iprintcoreps2-com-interface.md) COM interfaces, it must obtain an interface pointer from the driver as follows:

1.  The plug-in must implement the IPrintOemUI, IPrintOemUI2, IPrintOemUni, IPrintOemUni2, IPrintOemPS, or IPrintOemPS2 interface's PublishDriverInterface method.

2.  When the driver (Unidrv or Pscript5) calls the plug-in's PublishDriverInterface method, it supplies a pointer to the IPrintOemDriverUI, [IPrintCoreUI2](iprintcoreui2-com-interface.md), [IPrintOemDriverUni](iprintoemdriveruni-com-interface.md), [IPrintOemDriverPS](iprintoemdriverps-com-interface.md), or [IPrintCorePS2](iprintcoreps2-com-interface.md) instance's IUnknown interface.

3.  The plug-in must use the IUnknown interface pointer to call IUnknown::QueryInterface, specifying the interface identifier that represents the desired version of the [IPrintOemDriverUI](iprintoemdriverui-com-interface.md), [IPrintCoreUI2](iprintcoreui2-com-interface.md), [IPrintOemDriverUni](iprintoemdriveruni-com-interface.md), [IPrintOemDriverPS](iprintoemdriverps-com-interface.md), or [IPrintCorePS2](iprintcoreps2-com-interface.md) interface. (For more information, see [Interface Identifiers for Printer Drivers](interface-identifiers-for-printer-drivers.md).)

4.  If the plug-in specifies an interface identifier representing an interface version supported by the driver, QueryInterface returns a pointer to the [IPrintOemDriverUI](iprintoemdriverui-com-interface.md), [IPrintCoreUI2](iprintcoreui2-com-interface.md), [IPrintOemDriverUni](iprintoemdriveruni-com-interface.md), [IPrintOemDriverPS](iprintoemdriverps-com-interface.md), or [IPrintCorePS2](iprintcoreps2-com-interface.md) interface. Note that the driver calls the interface's AddRef method (described in the Windows SDK documentation) before it returns the interface pointer to the plug-in. The plug-in should save this pointer to use it later to call interface methods.

5.  When the [IPrintOemDriverUI](iprintoemdriverui-com-interface.md), [IPrintCoreUI2](iprintcoreui2-com-interface.md), [IPrintOemDriverUni](iprintoemdriveruni-com-interface.md), [IPrintOemDriverPS](iprintoemdriverps-com-interface.md), or [IPrintCorePS2](iprintcoreps2-com-interface.md) interface pointer is no longer needed, the plug-in must call the interface's Release method (described in the Windows SDK documentation).

For plug-ins to use the new Windows Vista [IPrintCoreHelperPS](https://msdn.microsoft.com/library/windows/hardware/ff552906) or [IPrintCoreHelperUni](https://msdn.microsoft.com/library/windows/hardware/ff552940) interface, the plug-in needs to add support for **OEMGI\_GETREQUESTEDHELPERINTERFACES** in its [**IPrintOemUI::GetInfo**](https://msdn.microsoft.com/library/windows/hardware/ff554178), [**IPrintOemPS::GetInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553221), or [**IPrintOemUni::GetInfo**](https://msdn.microsoft.com/library/windows/hardware/ff554256) method.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Accessing%20Printer%20Driver%20Interfaces%20from%20Plug-Ins%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




