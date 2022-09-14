---
title: Functions defined by print providers
description: Provides information about functions defined by print providers.
keywords:
- print providers WDK , functions
- functions WDK print providers
ms.date: 09/07/2022
---

# Functions defined by print providers

> [!WARNING]
> Starting with Windows 10, the APIs which support third-party print providers are deprecated. Microsoft does not recommend any investment into third-party print providers. Additionally, on Windows 8 and newer products where the v4 print driver model is available, third-party print providers may not create or manage queues which use v4 print drivers.

This topic lists all of the functions a print provider can supply. Most of these functions are described in the Microsoft Windows SDK documentation. If the function is described in the Windows Driver Kit (WDK), the function name provides a link to the associated reference page.

All print providers must supply pointers for all listed functions. However, most vendor-supplied print providers are "partial providers" which do not need to support many of the operations defined by the functions. Therefore, many of the function pointers can be **NULL**. For more information about partial print providers, see [Writing a Network Print Provider](writing-a-network-print-provider.md).

In the following function lists, functions that must be supported are labeled "Required".

All print providers must export the initialization function, [**InitializePrintProvidor**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-initializeprintprovidor). Pointers to all the other functions must be supplied in a [**PRINTPROVIDOR**](/windows-hardware/drivers/ddi/winsplp/ns-winsplp-_printprovidor) structure. (Note that these two names are misspelled, but are consistent with the names that appear in the header file, Winsplp.h.)

Functions are divided into groups, and presented in the following sections:

- Initialization function

- Print queue management functions

- Printer driver management functions

- Print job creation functions

- Print job scheduling functions

- Forms management functions

- Print processor management functions

- Print monitor management functions

- Port management functions

- Registry management functions

- Other functions

## Initialization Function

| Function | Description |
|--|--|
| [**InitializePrintProvidor**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-initializeprintprovidor) (Required) | Initializes the print provider and returns pointers to supplied functions. |

## Print queue management functions

| Function | Description |
|--|--|
| **AddPrinter** | Adds a print queue to the list of those managed by the print provider, and associates a print processor with the print queue. |
| **AddPrinterConnection** | Creates a connection to the specified print queue. |
| **ClosePrinter** (Required) | Disables caller access to a specified print queue. |
| **DeletePrinter** | Deletes a print queue from the list of those managed by the print provider. |
| **DeletePrinterConnection** | Removes a connection to the specified print queue. |
| **EnumPrinters** (Required) | Enumerates the list of print queues currently managed by the print provider. |
| **FindClosePrinterChangeNotification** | Disables printer change notifications that were enabled by **FindFirstPrinterChangeNotification**. |
| **FindFirstPrinterChangeNotification** | Returns a handle to a wait object that the caller can use to wait for specified printer events. |
| **GetPrinter** (Required) | Returns current parameter values for a specified print queue. |
| **OpenPrinter** (Required) | Enables caller access to a specified print queue. |
| [**RefreshPrinterChangeNotification**](/previous-versions/ff561930(v=vs.85)) | Called by router if client calls [**FindNextPrinterChangeNotification**](/windows/win32/printdocs/findnextprinterchangenotification) with the PRINTER_NOTIFY_OPTIONS_REFRESH flag set. |
| **ResetPrinter** | Modifies a print queue's data type or [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure. |
| **SetPrinter** (Required) | Sets parameters for a specified print queue. |
| **WaitForPrinterChange** | Obsolete. |

## Printer driver management functions

| Function | Description |
|--|--|
| **AddPrinterDriver** | Adds a specified printer's driver files to a specified server. |
| **AddPrinterDriverEx** | Same as **AddPrinterDriver**, with additional parameters. |
| **DeletePrinterDriver** | Deletes access to a specified printer's driver files, on a specified server. |
| **DeletePrinterDriverEx** | Same as **DeletePrinterDriver**, with additional parameters. |
| **EnumPrinterDrivers** | Returns a list of printer drivers that have been added to a specified server by calling **AddPrinterDriver** or **AddPrinterDriverEx**. |
| **GetPrinterDriver** | Returns information about a printer driver, which the caller can then pass to **AddPrinterDriver**. (The returned information is typically obtained from an INF file.) |
| **GetPrinterDriverEx** | Same as **GetPrinterDriver**, with additional parameters. |
| **GetPrinterDriverDirectory** | Returns the name of the server's printer driver directory. |

## Print job creation functions

| Function | Description |
|--|--|
| **AbortPrinter** (Required) | Attempts to delete the current job from the specified print queue. |
| **AddJob** (Required) | Returns a job identifier and spool file path. The caller uses [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) and **WriteFile** to send data to the spool file. |
| **EndDocPrinter** (Required) | Performs job completion operations. |
| **EndPagePrinter** | Performs page completion operations. |
| **ReadPrinter** | Obtains status information from a bidirectional printer. |
| **ScheduleJob** (Required) | Informs the provider that a specified job can be scheduled. The job is specified by a job identifier previously returned by **AddJob**. |
| **StartDocPrinter** (Required) | Prepares the print provider to begin spooling a print job. |
| **StartPagePrinter** | Prepares the print provider to receive a print job page. |
| **WritePrinter** (Required) | Receives a portion of the print job's data stream. |

> [!NOTE]
> The **AddJob**...**ScheduleJob** sequence is an alternative to the **StartDocPrinter**...**EndDocPrinter** sequence.

## Print job scheduling functions

| Function | Description |
|--|--|
| **EnumJobs** (Required) | Returns a list of scheduled print jobs. |
| **GetJob** (Required) | Returns job parameters. |
| **SetJob** (Required) | Cancels, pauses, resumes, or restarts a print job, or sets job parameters. |

## Forms management functions

| Function | Description |
|--|--|
| **AddForm** | Adds a specified form to the list of those available for a specified printer. |
| **DeleteForm** | Removes a specified form from the list of those available for a specified printer. |
| **EnumForms** | Returns a list of forms available for a specified printer. |
| **GetForm** | Returns characteristics of a specified form. |
| **SetForm** | Modifies characteristics of a specified form. |

## Print processor management functions

| Function | Description |
|--|--|
| **AddPrintProcessor** | Installs a print processor on the specified server and adds it to the list of those that the print provider can call. |
| **DeletePrintProcessor** | Deletes a print processor from the list of those that the print provider can call. |
| **EnumPrintProcessorDataTypes** | Returns a list of the data types supported by the print processors that are callable by the print provider. |
| **EnumPrintProcessors** | Returns the list of print processors that the print provider can call. |
| **GetPrintProcessorDirectory** | Returns the directory path in which print processor files must be stored. |

## Print monitor management functions

| Function | Description |
|--|--|
| **AddMonitor** | Adds a print monitor to the list of those that the print provider can call. |
| **DeleteMonitor** | Deletes a print monitor from the list of those that the print provider can call. |
| **EnumMonitors** | Returns the list of print monitors that the print provider can call. |

## Port management functions

| Function | Description |
|--|--|
| **AddPort** | Adds a printer port to the list of those available, typically by calling the specified port monitor's [**AddPortUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-addportui) function. |
| **AddPortEx** | Same as **AddPort**, with additional parameters. |
| **ConfigurePort** (Required) | Configures a printer port, typically by calling the specified port monitor's [**ConfigurePortUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-configureportui) function. |
| **DeletePort** (Required) | Deletes a printer port from the list of those available, typically by calling the specified port monitor's [**DeletePortUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-deleteportui) function. |
| **EnumPorts** (Required) | Returns a list of available printer ports. |
| **SetPort** | Sets parameters for a specified printer port. |

## Registry management functions

| Function | Description |
|--|--|
| **DeletePrinterData** | Deletes the value currently assigned to a specified value name, under the specified printer's **PrinterDriverData** key. |
| **DeletePrinterDataEx** | Same as **DeletePrinterData**, with additional parameters. |
| **DeletePrinterKey** | Deletes a specified key and its subkeys, if they are currently stored in the registry under the specified printer's **PrinterDriverData** key. |
| **EnumPrinterData** | Returns each of the value names and currently assigned values that are stored in the registry under the specified printer's **PrinterDriverData** key. |
| **EnumPrinterDataEx** | Same as **EnumPrinterData**, with additional parameters. |
| **EnumPrinterKey** | Returns a list of subkeys currently contained in the registry under a specified key name. |
| **GetPrinterData** | Returns the value currently assigned to a specified value name, which is stored in the registry under the specified printer's **PrinterDriverData** key. |
| **GetPrinterDataEx** | Same as **GetPrinterData**, with additional parameters. |
| **SetPrinterData** | Stores a specified value name and value in the registry, under the specified printer's **PrinterDriverData** key. |
| **SetPrinterDataEx** | Same as **SetPrinterData**, with additional parameters. |

## Other functions

| Function | Description |
|--|--|
| [**XcvData**](/previous-versions/ff564255(v=vs.85)) | Provides a communication path between a port monitor UI DLL and a port monitor server DLL. |
