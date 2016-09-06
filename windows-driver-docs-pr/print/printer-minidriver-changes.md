---
title: Printer Minidriver Changes
author: windows-driver-content
description: Printer Minidriver Changes
MS-HAID:
- 'autocfg\_1e8a23f7-1507-4c20-96aa-30d06063328d.xml'
- 'print.printer\_minidriver\_changes'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8f427642-a758-48bf-96e1-95a27adbaf23
keywords: ["in-box autoconfiguration support WDK printer , minidriver changes", "GPD files WDK print , in-box autoconfiguration support", "GDL files WDK printer", "PPD files WDK autoconfiguration", "plug-ins WDK print , in-box autoconfiguration support"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printer%20Minidriver%20Changes%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


