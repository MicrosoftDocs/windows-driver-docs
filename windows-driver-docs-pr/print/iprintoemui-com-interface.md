---
title: IPrintOemUI COM Interface
description: IPrintOemUI COM Interface
keywords:
- IPrintOemUI
ms.date: 07/18/2023
---

# IPrintOemUI COM Interface

[!include[Print Support Apps](../includes/print-support-apps.md)]

The `IPrintOemUI` COM interface is the means by which the [printer interface DLL](printer-interface-dll.md) for Unidrv or Pscript5 communicates with a UI plug-in. The `IPrintOemUI` interface is implemented by each UI plug-in.

The following table lists and describes all the methods that the `IPrintOemUI` interface supplies. UI plug-ins must define all listed methods. If a method is not needed, it can simply return E_NOTIMPL.

| Method | Description |
|--|--|
| [**IPrintOemUI::CommonUIProp**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-commonuiprop) | Enables a UI plug-in to modify an existing printer property sheet page or document property sheet page. |
| [**IPrintOemUI::DeviceCapabilities**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-devicecapabilities) | Enables a UI plug-in to specify customized device capabilities. |
| [**IPrintOemUI::DevicePropertySheets**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-devicepropertysheets) | Enables a UI plug-in to add a new page to a printer device's printer property sheet. |
| [**IPrintOemUI::DevMode**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-devmode) | Performs operations on a UI plug-in's private [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) members. |
| [**IPrintOemUI::DevQueryPrintEx**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-devqueryprintex) | Enables a UI plug-in to help determine if a print job is printable. |
| [**IPrintOemUI::DocumentPropertySheets**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-documentpropertysheets) | Enables a UI plug-in to add a new page to a printer device's document property sheet. |
| [**IPrintOemUI::DriverEvent**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-driverevent) | Called by the print spooler when processing driver-specific events that might require action by the printer driver. |
| [**IPrintOemUI::FontInstallerDlgProc**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-fontinstallerdlgproc) | Replaces the Unidrv font installer's user interface. |
| [**IPrintOemUI::GetInfo**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-getinfo) | (Implementation required.) Returns a UI plug-in's identification information. |
| [**IPrintOemUI::PrinterEvent**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-printerevent) | Enables a UI plug-in to process printer events. |
| [**IPrintOemUI::PublishDriverInterface**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-publishdriverinterface) | (Implementation required.) Supplies a pointer to the Unidrv or Pscript5 driver's [IPrintOemDriverUI COM interface](iprintoemdriverui-com-interface.md), [IPrintCoreUI2 COM interface](iprintcoreui2-com-interface.md), [IPrintCoreHelperPS interface](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperps), or [IPrintCoreHelperUni interface](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperuni). |
| [**IPrintOemUI::QueryColorProfile**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-querycolorprofile) | Enables a printer interface DLL to specify an ICC profile for color management. |
| [**IPrintOemUI::UpdateExternalFonts**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-updateexternalfonts) | Enables a printer interface DLL to update a printer's [Unidrv font format files](customized-font-management.md#unidrv-font-format-files). |
| [**IPrintOemUI::UpgradePrinter**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-upgradeprinter) | Enables a UI plug-in to upgrade device option values that are stored in the registry. |

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).
