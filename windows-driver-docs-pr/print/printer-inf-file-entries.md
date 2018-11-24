---
title: Printer INF File Entries
description: Printer INF File Entries
ms.assetid: 897072bb-e481-4c8d-a2bf-57b19c69ac0e
keywords:
- INF files WDK print , entries
- dependent files WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Printer INF File Entries





For an installation application to install a printer on a print server, it must call the spooler's **AddPrinterDriverEx** function to load driver files and then call the spooler's **AddPrinter** function to make the printer available on the server.

The **AddPrinterDriverEx** function requires a DRIVER\_INFO\_3 structure as input, and the **AddPrinter** function requires a PRINTER\_INFO\_2 structure as input. The default Windows 2000 or later printer class installer, Ntprint.dll, reads printer INF files to obtain string values that must be placed in these structures before the functions are called.


The **AddPrinterDriverEx** and **AddPrinter** functions, along with the DRIVER\_INFO\_3 and PRINTER\_INFO\_2 structures, are described in the Microsoft Windows SDK documentation.

A set of INF file entries for printer drivers that Ntprint.dll recognizes has been defined. These entries have the following format:

*EntryName* = *Value*

where *EntryName* is a string identifying the entry and *Value* is a string value assigned to the entry.

The following table lists INF file entries that should be included in printer INF files. For each entry, the table includes the following:

-   The value that should be assigned to the entry.

-   The default value that Ntprint.dll uses if the entry is not defined.

-   The structure member into which Ntprint.dll places a pointer to the entry value.

| INF File Entry       |Value|Default Value (if entry not specified)|Structure Member |
|----------------------|-----|-------------|-----------------------------------------|
| ConfigFile           | The name of the driver's [printer interface DLL](printer-interface-dll.md). | Value specified for DriverFile. | **pConfigFile** member of the DRIVER\_INFO\_3 structure (described in the Windows SDK documentation) |
| DataFile             | The name of a driver's associated data file, such as a PPD file. | Driver's section name within the INF file. | **pDataFile** member of the DRIVER\_INFO\_3 structure |
| DefaultDataType      | Not used with NT-based-operating systems. |||
| DriverCategory       | See **Note 1**, following this table. | If the INF file doesn’t specify a driver category (like most v3 drivers), then the assumption is that the driver’s category is **PrintFax.Printer**. | None |
| DriverFile           | The name of the driver's [printer graphics DLL](printer-graphics-dll.md). | Driver's section name within the INF file. | **pDriverPath** member of the DRIVER\_INFO\_3 structure |
| ExcludeFromSelect    | See **Note 2**, following this table. | None | None |
| HelpFile             | The name of the interface DLL's help file. | None. A help file is not specified. | **pHelpFile** member of the DRIVER\_INFO\_3 structure |
| LanguageMonitor      | The name of a language monitor to be associated with the printer driver. See the **LanguageMonitor Value Format** section. | None. A language monitor is not specified. | **pMonitorName** member of the DRIVER\_INFO\_3 structure |
| PrintProcessor       | The name of a print processor to be associated with the printer queue. See the **PrintProcessor Value Format** section. | The default print processor (WinPrint) is used. | **pPrintProcessor** member of the DRIVER\_INFO\_2 structure (described in the Windows SDK documentation) |
| VendorSetup          | The name of a function within a vendor-supplied DLL, that handles [customized printer setup operations](customized-printer-setup-operations.md). | None. See **Note 3**, following this table. | None |
| InboxVersionRequired | The minimum acceptable version for all core drivers that the INF references. For more information about InboxVersionRequired, see [INF InboxVersionRequired Directive](inf-inboxversionrequired-directive.md). | None | None |

 

 **Note**  **1 (DriverCategory)**: If the INF file specifies a category, these are the allowed values (0 to 5 respectively) for specifying categories:
 
 
| Driver Category          | Value | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PrintFax.Printer         | 0     | A print queue that represents either a printer connected to the computer (through a local or network protocol), or a proxy to a physical printer on another computer. When the user prints to a physical printer, the result is paper with the document printed on it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PrintFax.Fax             | 1     | A print queue that represents a physical or virtual fax machine. When the user prints to a fax printer, the result (possibly after further user interaction) is that a fax is sent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PrintFax.Printer.File    | 2     | A print queue that generates soft-copy documents. When the user prints to a file printer, the user must first enter a file name, and the spooler then sends the printed output to that file. File printers always require a file name but take no other user input. When there is no option for the user to provide a filename, the app generates a filename that is made available to the spooler. Common examples of File Printers are Microsoft XPS Document Writer (MXDW) and PDF writers.                                                                                                                                                                                                                                                 |
| PrintFax.Printer.Virtual | 3     | A print queue that has a driver that performs some operation on printed data that is opaque to the print spooler. When the user prints to a virtual printer, some possible results include the printed document being saved somewhere on the computer, being sent to another application, or being sent by e-mail. A common example of printing to a virtual printer, is the scenario where the printed document is sent to the Microsoft Office OneNote Printer. When the user selects to print to a virtual printer, there can be a need for further user interaction, initiated by the driver or some other driver component. For more information, see [Virtual Printers in Printer INF Files](virtual-printers-in-printer-inf-files.md). |
| PrintFax.Printer.Service | 4     | A print queue that represents a printing service. When the user selects to print to a service, then the result (possibly after further user interaction) is that a third-party printing service receives the printed content. The user can then go to the physical business location to pick up the printed output.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PrintFax.Printer.3D      | 5     | A print queue that represents the data stream for a 3D printer. If this category is unintentionally specified for a 2D printer (a regular printer), the 2D printer will simply output the 2D content of the data stream. If this category is correctly specified for a 3D printer, but a 2D data stream is sent to the 3D printer, the 3D printer will not generate any output.                                                                                                                                                                                                                                                                                                                                                                |

 

Also note that v4 print drivers use a Manifest file. For more information, see [V4 Driver Manifest](v4-driver-manifest.md).

 

**Note**  **2 (ExcludeFromSelect)**: The [*device ID*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-id) of a device that should not be shown in the **Select Device** dialog or in the Add Printer Wizard. For printers, this includes all PnP entries of devices that have duplicate device descriptions in the INF file; for example, devices that have multiple entries for infrared and parallel enumeration or for another bus. The ExcludeFromSelect entry, unlike all others in this table, must appear in the Control Flags section of the INF file. See [**INF ControlFlags Section**](https://msdn.microsoft.com/library/windows/hardware/ff546342) for more information.

 

**Note**  **3 (VendorSetup)**: If no VendorSetup entry is specified, customized setup operations are not performed. In particular, no user interface is permitted during print processor, print monitor, or printer driver installation, except through the use of the VendorSetup INF entry. For more information about this entry, see [Customized Printer Setup Operations](customized-printer-setup-operations.md).

 

**Important**  : VendorSetup is now deprecated and should not be used by any *new* v3 or v4 drivers that you develop. This information about VendorSetup is provided for reference only, or for the maintenance of existing v3 drivers that already use this INF directive.

 

Printer INF file entries are typically specified within [printer INF file data sections](printer-inf-file-data-sections.md). For examples, see the [sample printer INF files](sample-printer-inf-files.md).

### <a href="" id="ddk-languagemonitor-value-format-gg"></a>LanguageMonitor Value Format

When a LanguageMonitor entry is included in a printer INF file, the value format is as follows:

LanguageMonitor=" *MonitorName* , *MonitorDLLName* "

where *MonitorName* is a text string representing the monitor's displayed name, and *MonitorDLLName* is the file name of the monitor DLL.

### <a href="" id="ddk-printprocessor-value-format-gg"></a>PrintProcessor Value Format

When a PrintProcessor entry is included in a printer INF file, the value format is as follows:

PrintProcessor=" *PrintProcessorName* , *PrintProcessorDLLName* "

where *PrintProcessorName* is a text string representing the print processor's displayed name, and *PrintProcessorDLLName* is the file name of the DLL.

### <a href="" id="ddk-dependent-files-gg"></a>Dependent Files

For Windows 2000 and later, a dependent file is a printer driver file that is included in a [printer INF file Install section](printer-inf-file-install-sections.md) with a [dirid](printer-dirids.md) of 66000, but not assigned to the DriverFile, DataFile, ConfigFile, or HelpFile entries.

The following example shows excerpts from an INF file that installs three dependent files by copying them to the printer-driver directory (that is, to the directory specified by dirid 66000):

```cpp
[Contoso]
%PRINTER_MODEL_123%=Contoso_Install_Section,LPTENUM\Contoso_1284.4_P29C5
...
[Contoso_Install_Section]
CopyFiles=@Contoso.ini,@Contoso.xml,@Contoso.dll
...
[DestinationDirs]
DefaultDestDir=66000
...
[Strings]
PRINTER_MODEL_123 = "Contoso Printer Model 123"
```

In this example, Contoso.ini is a printer INI file, Contoso.xml is a bidi extension file, and Contoso.dll is a customized component. For more information about printer INI files, bidi extension files, and customized components, see [Installing Customized Driver Components](installing-customized-driver-components.md) and [Bidirectional Communication Schema](bidirectional-communication-schema.md).

[Point-and-print](introduction-to-point-and-print.md) operations install both the driver and driver-dependent files on the client.

A maximum of 64 dependent files can be specified for each printer model.

## Related topics
[Bidirectional Communication Schema](bidirectional-communication-schema.md)  
[**INF ControlFlags Section**](https://msdn.microsoft.com/library/windows/hardware/ff546342)  
[Installing Customized Driver Components](installing-customized-driver-components.md)  
[Point-and-print](introduction-to-point-and-print.md)  
[Printer INF file Install section](printer-inf-file-install-sections.md)  
[V4 Driver Manifest](v4-driver-manifest.md)  



