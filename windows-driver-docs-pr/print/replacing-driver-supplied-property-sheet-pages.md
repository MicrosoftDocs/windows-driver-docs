---
title: Replacing Driver-Supplied Property Sheet Pages
description: Replacing Driver-Supplied Property Sheet Pages
keywords:
- user interface plug-ins WDK print , property sheet pages
- UI plug-ins WDK print , property sheet pages
- property sheet pages WDK print
- replacing property sheet pages
- IPrintCoreUI2
- document-sticky properties WDK print
- printer-sticky properties WDK print
- device-sticky properties WDK print
- sticky properties WDK print
ms.date: 01/30/2023
---

# Replacing Driver-Supplied Property Sheet Pages

[!include[Print Support Apps](../includes/print-support-apps.md)]

The [IPrintCoreUI2 COM Interface](iprintcoreui2-com-interface.md) provides four methods that a Pscript5 UI plug-in running on Windows XP and later versions of Windows operating system must use when it intends to fully replace the core driver's standard UI pages. (The term core driver refers to either the Unidrv or Pscript5 printer driver.) These methods are as follows:

[**IPrintCoreUI2::EnumConstrainedOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-enumconstrainedoptions)

[**IPrintCoreUI2::GetOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-getoptions)

[**IPrintCoreUI2::SetOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-setoptions)

[**IPrintCoreUI2::WhyConstrained**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-whyconstrained)

These methods are supported only during the execution of the UI plug-in's [**IPrintOemUI::DocumentPropertySheets**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-documentpropertysheets) and [**IPrintOemUI::DevicePropertySheets**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-devicepropertysheets) methods and their property sheet callback routines. A UI plug-in supports these methods to display its own user interface. When not supported, these methods return E\_NOTIMPL.

The core driver displays its own property sheet UI in two circumstances--for [**DrvDocumentPropertySheets**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdocumentpropertysheets), and for [**DrvDevicePropertySheets**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdevicepropertysheets). The first method displays properties that apply only to documents (document-sticky properties), while the second method displays properties that apply to a device (device- or printer-sticky properties).

The core driver remembers the type of property sheet it handles (and therefore, the mode -- document-sticky or printer-sticky). The core driver saves that state information in a structure (the [**OEMUIOBJ**](/windows-hardware/drivers/ddi/printoem/ns-printoem-_oemuiobj) structure) it creates for the UI instance. When the core driver calls a plug-in's interface methods, it passes a pointer to an OEMUIOBJ structure, so that when a plug-in calls back to the core driver from [**IPrintCoreUI2::EnumConstrainedOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-enumconstrainedoptions), [**IPrintCoreUI2::GetOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-getoptions), [**IPrintCoreUI2::SetOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-setoptions), or [**IPrintCoreUI2::WhyConstrained**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-whyconstrained), these methods pass the pointer back to the core driver, which is then able to determine the mode.

For **IPrintCoreUI2::EnumConstrainedOptions**, **IPrintCoreUI2::SetOptions**, and **IPrintCoreUI2::WhyConstrained**, only document-sticky features are supported during the execution of **IPrintOemUI::DocumentPropertySheets** or its property sheet callback routine and only printer-sticky features are supported during the execution of **IPrintOemUI::DevicePropertySheets** or its property sheet callback routine. For **IPrintCoreUI2::SetOptions**, any feature whose stickiness does not match the current sticky mode should be ignored. When either **IPrintCoreUI2::EnumConstrainedOptions** or **IPrintCoreUI2::WhyConstrained** is called for a feature whose stickiness does not match the current sticky mode, the method should return E\_INVALIDARG.

For [**IPrintCoreUI2::GetOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-getoptions), both document-sticky and printer-sticky features are supported in document-sticky mode (that is, when [**IPrintOemUI::DocumentPropertySheets**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-documentpropertysheets) or its property sheet callback routine are running), but only printer-sticky features are supported in printer-sticky mode (when [**IPrintOemUI::DevicePropertySheets**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-devicepropertysheets) or its property sheet callback routine are running).
