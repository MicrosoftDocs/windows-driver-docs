---
title: Accessing Printer Driver Interfaces from Plug-Ins
description: Accessing Printer Driver Interfaces from Plug-Ins
keywords:
- COM interfaces WDK print , accessing printer driver interfaces
- plug-ins WDK print , accessing interfaces
ms.date: 01/26/2023
---

# Accessing Printer Driver Interfaces from Plug-Ins

[!include[Print Support Apps](../includes/print-support-apps.md)]

If a plug-in calls methods that belong to the driver-supplied [IPrintOemDriverUI](iprintoemdriverui-com-interface.md), [IPrintCoreHelperPS](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperps), [IPrintCoreHelperUni](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperuni), [IPrintCoreUI2](iprintcoreui2-com-interface.md), [IPrintOemDriverUni](iprintoemdriveruni-com-interface.md), [IPrintOemDriverPS](iprintoemdriverps-com-interface.md), or [IPrintCorePS2](iprintcoreps2-com-interface.md) COM interfaces, it must obtain an interface pointer from the driver as follows:

1. The plug-in must implement the IPrintOemUI, IPrintOemUI2, IPrintOemUni, IPrintOemUni2, IPrintOemPS, or IPrintOemPS2 interface's PublishDriverInterface method.

1. When the driver (Unidrv or Pscript5) calls the plug-in's PublishDriverInterface method, it supplies a pointer to the IPrintOemDriverUI, [IPrintCoreUI2](iprintcoreui2-com-interface.md), [IPrintOemDriverUni](iprintoemdriveruni-com-interface.md), [IPrintOemDriverPS](iprintoemdriverps-com-interface.md), or [IPrintCorePS2](iprintcoreps2-com-interface.md) instance's IUnknown interface.

1. The plug-in must use the IUnknown interface pointer to call IUnknown::QueryInterface, specifying the interface identifier that represents the desired version of the [IPrintOemDriverUI](iprintoemdriverui-com-interface.md), [IPrintCoreUI2](iprintcoreui2-com-interface.md), [IPrintOemDriverUni](iprintoemdriveruni-com-interface.md), [IPrintOemDriverPS](iprintoemdriverps-com-interface.md), or [IPrintCorePS2](iprintcoreps2-com-interface.md) interface. (For more information, see [Interface Identifiers for Printer Drivers](interface-identifiers-for-printer-drivers.md).)

1. If the plug-in specifies an interface identifier representing an interface version supported by the driver, QueryInterface returns a pointer to the [IPrintOemDriverUI](iprintoemdriverui-com-interface.md), [IPrintCoreUI2](iprintcoreui2-com-interface.md), [IPrintOemDriverUni](iprintoemdriveruni-com-interface.md), [IPrintOemDriverPS](iprintoemdriverps-com-interface.md), or [IPrintCorePS2](iprintcoreps2-com-interface.md) interface. Note that the driver calls the interface's AddRef method (described in the Windows SDK documentation) before it returns the interface pointer to the plug-in. The plug-in should save this pointer to use it later to call interface methods.

1. When the [IPrintOemDriverUI](iprintoemdriverui-com-interface.md), [IPrintCoreUI2](iprintcoreui2-com-interface.md), [IPrintOemDriverUni](iprintoemdriveruni-com-interface.md), [IPrintOemDriverPS](iprintoemdriverps-com-interface.md), or [IPrintCorePS2](iprintcoreps2-com-interface.md) interface pointer is no longer needed, the plug-in must call the interface's Release method (described in the Windows SDK documentation).

For plug-ins to use the new Windows Vista [IPrintCoreHelperPS](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperps) or [IPrintCoreHelperUni](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperuni) interface, the plug-in needs to add support for **OEMGI\_GETREQUESTEDHELPERINTERFACES** in its [**IPrintOemUI::GetInfo**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-getinfo), [**IPrintOemPS::GetInfo**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-getinfo), or [**IPrintOemUni::GetInfo**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-getinfo) method.
