---
title: Replacing Driver-Supplied Property Sheet Pages
description: Replacing Driver-Supplied Property Sheet Pages
ms.assetid: b7f79841-f82c-4a60-9c2f-58772a65a5eb
keywords: ["user interface plug-ins WDK print , property sheet pages", "UI plug-ins WDK print , property sheet pages", "property sheet pages WDK print", "replacing property sheet pages", "IPrintCoreUI2", "document-sticky properties WDK print", "printer-sticky properties WDK print", "device-sticky properties WDK print", "sticky properties WDK print"]
---

# Replacing Driver-Supplied Property Sheet Pages


## <a href="" id="ddk-replacing-driver-supplied-property-sheet-pages-gg"></a>


The [IPrintCoreUI2 COM Interface](iprintcoreui2-com-interface.md) provides four methods that a Pscript5 UI plug-in running on Windows XP and later versions of Windows operating system must use when it intends to fully replace the core driver's standard UI pages. (The term core driver refers to either the Unidrv or Pscript5 printer driver.) These methods are as follows:

[**IPrintCoreUI2::EnumConstrainedOptions**](https://msdn.microsoft.com/library/windows/hardware/ff553045)

[**IPrintCoreUI2::GetOptions**](https://msdn.microsoft.com/library/windows/hardware/ff553069)

[**IPrintCoreUI2::SetOptions**](https://msdn.microsoft.com/library/windows/hardware/ff553081)

[**IPrintCoreUI2::WhyConstrained**](https://msdn.microsoft.com/library/windows/hardware/ff553087)

These methods are supported only during the execution of the UI plug-in's [**IPrintOemUI::DocumentPropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff554173) and [**IPrintOemUI::DevicePropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff554165) methods and their property sheet callback routines. A UI plug-in supports these methods to display its own user interface. When not supported, these methods return E\_NOTIMPL.

The core driver displays its own property sheet UI in two circumstances--for [**DrvDocumentPropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff548548), and for [**DrvDevicePropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff548542). The first method displays properties that apply only to documents (document-sticky properties), while the second method displays properties that apply to a device (device- or printer-sticky properties).

The core driver remembers the type of property sheet it handles (and therefore, the mode -- document-sticky or printer-sticky). The core driver saves that state information in a structure (the [**OEMUIOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff559571) structure) it creates for the UI instance. When the core driver calls a plug-in's interface methods, it passes a pointer to an OEMUIOBJ structure, so that when a plug-in calls back to the core driver from [**IPrintCoreUI2::EnumConstrainedOptions**](https://msdn.microsoft.com/library/windows/hardware/ff553045), [**IPrintCoreUI2::GetOptions**](https://msdn.microsoft.com/library/windows/hardware/ff553069), [**IPrintCoreUI2::SetOptions**](https://msdn.microsoft.com/library/windows/hardware/ff553081), or [**IPrintCoreUI2::WhyConstrained**](https://msdn.microsoft.com/library/windows/hardware/ff553087), these methods pass the pointer back to the core driver, which is then able to determine the mode.

For **IPrintCoreUI2::EnumConstrainedOptions**, **IPrintCoreUI2::SetOptions**, and **IPrintCoreUI2::WhyConstrained**, only document-sticky features are supported during the execution of **IPrintOemUI::DocumentPropertySheets** or its property sheet callback routine and only printer-sticky features are supported during the execution of **IPrintOemUI::DevicePropertySheets** or its property sheet callback routine. For **IPrintCoreUI2::SetOptions**, any feature whose stickiness does not match the current sticky mode should be ignored. When either **IPrintCoreUI2::EnumConstrainedOptions** or **IPrintCoreUI2::WhyConstrained** is called for a feature whose stickiness does not match the current sticky mode, the method should return E\_INVALIDARG.

For [**IPrintCoreUI2::GetOptions**](https://msdn.microsoft.com/library/windows/hardware/ff553069), both document-sticky and printer-sticky features are supported in document-sticky mode (that is, when [**IPrintOemUI::DocumentPropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff554173) or its property sheet callback routine are running), but only printer-sticky features are supported in printer-sticky mode (when [**IPrintOemUI::DevicePropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff554165) or its property sheet callback routine are running).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Replacing%20Driver-Supplied%20Property%20Sheet%20Pages%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




