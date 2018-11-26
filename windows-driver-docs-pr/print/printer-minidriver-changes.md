---
title: Printer Minidriver Changes
description: Printer Minidriver Changes
ms.assetid: 8f427642-a758-48bf-96e1-95a27adbaf23
keywords:
- in-box autoconfiguration support WDK printer , minidriver changes
- GPD files WDK print , in-box autoconfiguration support
- GDL files WDK printer
- PPD files WDK autoconfiguration
- plug-ins WDK print , in-box autoconfiguration support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Printer Minidriver Changes


The printer minidriver consists of a printer description file ([*GPD*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-generic-printer-description--gpd-), [*PPD*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-postscript-printer-description--ppd-), or GDL file), together with optional user interface (UI) plug-ins, rendering plug-ins, and rendering filters. For in-box inclusion, only one UI plug-in is permitted, and only one Unidrv or Pscript rendering plug-in is permitted. An IHV port monitor is not permitted to be included as an in-box with a printer minidriver.

For the GPD, PPD, or GDL file, there are two cases to consider:

-   Additions to a GDL file: GDL files are printer data files that supersede GPD and PPD files.

-   Modifications to existing GPD or PPD files used for a printer whose driver already ships with Windows and has a GPD file or PPD file associated with it.

The following topics describe the changes that must be made in the driver UI and in the printer data files:

[UI Plug-in Changes](ui-plug-in-changes.md)

[Adding GDL Extensions to an Existing GPD File](adding-gdl-extensions-to-an-existing-gpd-file.md)

[Adding GDL Extensions to an Existing PPD File](adding-gdl-extensions-to-an-existing-ppd-file.md)

[BidiFiles Entry in a Minidriver's INI File](bidifiles-entry-in-a-minidriver-s-ini-file.md)

[Naming Conventions in Pscript and Unidrv Minidrivers](naming-conventions-in-pscript-and-unidrv-minidrivers.md)

 

 




