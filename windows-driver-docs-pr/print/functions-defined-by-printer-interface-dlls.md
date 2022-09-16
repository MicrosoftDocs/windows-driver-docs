---
title: Functions defined by printer interface DLLs
description: Provides information about functions defined by printer interface DLLs.
keywords:
- printer interface DLL WDK, functions
- functions WDK printer interface DLL
ms.date: 09/12/2022
---

# Functions defined by printer interface DLLs

Printer interface DLLs export the functions listed in the following table.

| Function | Purpose |
|--|--|
| **DllEntryPoint** | Initial DLL entry point, typically called [**DLLMain**](/windows/win32/dlls/dllmain). |
| [**DrvConvertDevMode**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvconvertdevmode) | Converts the specified [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure from one version to another. |
| [**DrvDeviceCapabilities**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdevicecapabilities) | Returns requested information about a printer's capabilities. |
| [**DrvDevicePropertySheets**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdevicepropertysheets) | Calls [CPSUI](common-property-sheet-user-interface.md) to create property sheet pages that describe a printer's properties. |
| [**DrvDocumentEvent**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdocumentevent) | (Optional) Allows the printer interface DLL to specify which events associated with printing a document it will handle. |
| [**DrvDriverEvent**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdriverevent) | (Optional) Allows the printer interface DLL to respond to notifications from the spooler that certain driver-specific events have occurred. |
| [**DrvDocumentPropertySheets**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdocumentpropertysheets)> | Calls CPSUI to create property sheet pages that describe a print document's properties. |
| [**DrvPrinterEvent**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvprinterevent) | Allows the printer interface DLL to respond to notifications from the spooler that certain printer-specific events have occurred. |
| [**DrvQueryColorProfile**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvquerycolorprofile) | (Optional) Allows the printer interface DLL to specify an ICC profile to use for color management. |
| [**DrvQueryJobAttributes**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvqueryjobattributes) | (Optional) Allows the printer interface DLL to specify support for such capabilities as printing multiple document pages on a physical page ("N-up" printing), printing multiple copies of each page, and collating pages. |
| [**DevQueryPrintEx**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-devqueryprintex) | Determines if a print job can be printed using the printer's current configuration. |
| [**DrvSplDeviceCaps**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvspldevicecaps) | Returns requested information about a printer's capabilities. |
| [**DrvUpgradePrinter**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvupgradeprinter) | (Optional) Updates a printer's registry settings when a new version of the driver is added to a system. |
