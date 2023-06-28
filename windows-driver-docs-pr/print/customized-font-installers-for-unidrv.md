---
title: Customized font installers for Unidrv
description: Customized font installers for Unidrv
keywords:
- printer driver customizing WDK , installing components
- customizing printer drivers WDK , installing components
- installing custom printer driver components WDK
- font installers WDK Unidrv
- .uff files
- UFF files
ms.date: 06/16/2023
---

# Customized font installers for Unidrv

[!include[Print Support Apps](../includes/print-support-apps.md)]

Vendor-supplied font installation software is required for cartridge fonts that aren't described by [font cartridge](font-cartridges.md) entries in a printer's *GPD* file. These fonts must be described using [Unidrv font format files](customized-font-management.md#unidrv-font-format-files) (.uff files). Creating .uff files is the responsibility of vendor-supplied font installers.

Vendor-supplied font installers should also provide support for downloadable *PCL* soft fonts.

The two techniques to create a customized font installer are as follows:

- Supply a user interface plug-in

    This plug-in must implement the following COM interface methods:

    [**IPrintOemUI::FontInstallerDlgProc**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-fontinstallerdlgproc)

    [**IPrintOemUI::UpdateExternalFonts**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-updateexternalfonts)

- Supply a separate executable file

    During font installation, the executable file must store its name in the registry by calling SetPrinterData (described in the Windows SDK documentation) and specifying a value for the "FontInstaller" key.

Unidrv uses the following algorithm for locating a font installer:

1. If the name of a font installer executable file is stored in the registry, Unidrv doesn't allow the system administrator to select font installation operations from the printer's property sheet. Instead, the administrator must run the supplied executable file.

1. If an installer executable file isn't available, Unidrv enables selection of font installation operations from the printer's property sheet. Unidrv determines if a user interface plug-in has been installed. If so, its font installation methods are called. If a user interface plug-in hasn't been installed, or if its font installation methods return E\_NOTIMPL, the driver uses its own fault installer.
