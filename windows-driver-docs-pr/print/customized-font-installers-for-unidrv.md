---
title: Customized Font Installers for Unidrv
description: Customized Font Installers for Unidrv
ms.assetid: d753368d-b1c8-454e-a02b-131dc778e723
keywords:
- printer driver customizing WDK , installing components
- customizing printer drivers WDK , installing components
- installing custom printer driver components WDK
- font installers WDK Unidrv
- .uff files
- UFF files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Customized Font Installers for Unidrv





Vendor-supplied font installation software is required for cartridge fonts that are not described by [font cartridge](font-cartridges.md) entries in a printer's [*GPD*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-generic-printer-description--gpd-) file. These fonts must be described using [Unidrv font format files](customized-font-management.md#ddk-unidrv-font-format-files-gg) (.uff files). Creating .uff files is the responsibility of vendor-supplied font installers.

Vendor-supplied font installers should also provide support for downloadable [*PCL*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pcl) soft fonts.

The two techniques to create a customized font installer are as follows:

-   Supply a user interface plug-in

    This plug-in must implement the following COM interface methods:

    [**IPrintOemUI::FontInstallerDlgProc**](https://msdn.microsoft.com/library/windows/hardware/ff554176)

    [**IPrintOemUI::UpdateExternalFonts**](https://msdn.microsoft.com/library/windows/hardware/ff554188)

-   Supply a separate executable file

    During font installation, the executable file must store its name in the registry by calling SetPrinterData (described in the Windows SDK documentation) and specifying a value for the "FontInstaller" key.

Unidrv uses the following algorithm for locating a font installer:

1.  If the name of a font installer executable file is stored in the registry, Unidrv does not allow the system administrator to select font installation operations from the printer's property sheet. Instead, the administrator must run the supplied executable file.

2.  If an installer executable file is not available, Unidrv enables selection of font installation operations from the printer's property sheet. Unidrv determines if a user interface plug-in has been installed. If so, its font installation methods are called. If a user interface plug-in has not been installed, or if its font installation methods return E\_NOTIMPL, the driver uses its own fault installer.

 

 




