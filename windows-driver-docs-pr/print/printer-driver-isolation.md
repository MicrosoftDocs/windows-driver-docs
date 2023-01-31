---
title: Printer Driver Isolation
description: Printer driver isolation improves the reliability of the Windows print service, by enabling printer drivers to run in processes that are separate from the process in which the print spooler runs.
ms.date: 01/30/2023
ms.custom: contperf-fy22q2
---

# Printer Driver Isolation

[!include[Print Support Apps](../includes/print-support-apps.md)]

Printer driver isolation improves the reliability of the Windows print service, by enabling printer drivers to run in processes that are separate from the process in which the print spooler runs.

Support for printer driver isolation is implemented in Windows 7, Windows Server 2008 R2 and later operating systems.

Starting with Windows 7 and Windows Server 2008 R2, an inbox printer driver must support printer driver isolation and be able to run in an isolated process.

In previous versions of Windows, printer drivers always ran in the same process as the spooler. Printer driver components that ran in the spooler process included the following:

- Print driver configuration modules

- Print processors

- Rendering modules

The failure of a single print driver component could cause the print subsystem to fail, halting print operations for all users and for all print components.

Starting with Windows 7 and Windows Server 2008 R2, an administrator can, as an option, configure a printer driver to run in an isolated process--a process that is separate from the spooler process. By isolating the driver, the administrator can prevent a fault in a driver component from halting the print service.

For more information about the spooler functions, see [Spooler Component Functions and Structures](/windows-hardware/drivers/ddi/_print/index).

## Driver isolation support in INF files

By default, if the INF file that installs a printer driver does not indicate that the driver supports driver isolation, the printer class installer configures the driver to run in the spooler process. However, if the INF file indicates that the driver supports driver isolation, the installer configures the driver to run in an isolated process. An administrator can override these configuration settings and specify, for each driver, whether to run the driver in the spooler process or in an isolated process.

To support driver isolation, the INF file that installs a printer driver can use the **DriverIsolation** keyword to indicate whether the driver supports printer driver isolation. Setting **DriverIsolation**=2 indicates that the driver supports driver isolation. Setting **DriverIsolation**=0 indicates that the driver does not support driver isolation. Omitting the **DriverIsolation** keyword from the INF file has the same effect as setting **DriverIsolation**=0.

## Spooler functions for driver isolation settings

The following table shows the spooler functions that an administrator can use to configure the driver-isolation settings.

| Function name | Operation |
|--|--|
| [GetPrinterDataEx](/windows/win32/printdocs/getprinterdataex) | Get the driver-isolation settings for a printer. |
| [SetPrinterDataEx](/windows/win32/printdocs/setprinterdataex) | Set the driver-isolation settings for a printer. |
| [EnumPrinterDataEx](/windows/win32/printdocs/enumprinterdataex) | Enumerate driver-isolation settings for a printer. |
| [FindFirstPrinterChangeNotification](/windows/win32/printdocs/findfirstprinterchangenotification), [FindNextPrinterChangeNotification](/windows/win32/printdocs/findnextprinterchangenotification) | Request notifications of changes to the driver-isolation settings for a printer. |

The format for the data is as follows:

- Driver in each group is separated by '\\'

- Each driver group is separated by '\\\\'

The first group loads the driver into the spooler processes. Each subsequent group loads the drivers in isolated processes per group. The second group is considered the 'shared' group in which other isolation-capable drivers are loaded by default.

## Configuring driver isolation mode through administration

A computer administrator can use the Windows Print Management console or call the Windows spooler functions to configure the driver-isolation settings for each printer driver installed on a computer. The administrator configures the driver to use one of the settings listed in the following table.

| Driver-isolation mode | Meaning |
|--|--|
| Shared | Run the driver in a process that is shared with other printer drivers but is separate from the spooler process. |
| Isolated | Run the driver in a process that is separate from the spooler process and is not shared with other printer drivers. |
| None | Run the driver in the spooler process. |

Ideally, a printer driver is able to run in shared mode. That is, it runs in an isolated process shared with other printer drivers but separate from the spooler process. A driver might need to run in isolated mode if it can run in a process separate from the spooler process, but has difficulty sharing the process with other drivers. For example, a poorly designed driver might have file names that conflict with those of related drivers or of different versions of the same driver, or the driver might fault frequently or have a memory leak that interferes with the operation of other drivers that run in the same process.

To support troubleshooting, the domain administrator can disable the driver-isolation feature on a computer in the domain, or the administrator can force all of the printer drivers on the computer to run in isolated mode. In isolated mode, each driver must run in a process separate from the spooler and from the other printer drivers.

If driver isolation is disabled by group policy, the isolation is off for all printer drivers. If isolation is enabled, then the individual drivers are mode-checked. If a driver has isolation mode set, it runs in shared, isolated, or none mode, based on the registry entry. However, if the driver does not have isolation mode set and it is compatible with isolation, it runs in shared mode. If the driver is not compatible with the mode, the group policy override determines whether the driver runs in shared mode or none mode.

The following chart shows a decision map for choosing the driver isolation mode:

![flowchart for choosing the driver isolation mode.](images/isolation.png)

## Spooler functions allowed under driver isolation

Only specific functions are allowed under driver isolation.

## Spoolss.dll functions

The following functions are exported by spoolss.dll and are available to spooler plugins by linking to spoolss.lib.

- [**AddMonitorW**](/windows/win32/printdocs/addmonitor)

- [**AppendPrinterNotifyInfoData**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-appendprinternotifyinfodata)

- [**ClosePrinter**](/windows/win32/printdocs/closeprinter)

- [**DeletePortW**](/windows/win32/printdocs/deleteport)

- [**DeletePrintProcessorW**](/windows/win32/printdocs/deleteprintprocessor)

- [**EndDocPrinter**](/windows/win32/printdocs/enddocprinter)

- [**EndPagePrinter**](/windows/win32/printdocs/enddocprinter)

- [**EnumFormsW**](/windows/win32/printdocs/enumforms)

- [**EnumJobsW**](/windows/win32/printdocs/enumjobs)

- [**FlushPrinter**](/windows/win32/printdocs/flushprinter)

- [**GetJobAttributes**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-getjobattributes)

- [**GetJobAttributesEx**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-getjobattributesex)

- [**GetJobW**](/windows/win32/printdocs/getjob)

- [**GetPrinterDataExW**](/windows/win32/printdocs/getprinterdataex)

- [**GetPrinterDataW**](/windows/win32/printdocs/getprinterdata)

- [**GetPrinterDriverDirectoryW**](/windows/win32/printdocs/getprinterdriverdirectory)

- [**GetPrinterDriverW**](/windows/win32/printdocs/getprinterdriver)

- [**GetPrinterW**](/windows/win32/printdocs/getprinter)

- [**ImpersonatePrinterClient**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-impersonateprinterclient)

- [**OpenPrinterW**](/windows/win32/printdocs/openprinter)

- [**ReadPrinter**](/windows/win32/printdocs/readprinter)

- [**RouterCreatePrintAsyncNotificationChannel**](/windows-hardware/drivers/ddi/prnasntp/nf-prnasntp-routercreateprintasyncnotificationchannel)

- [**RouterGetPrintClassObject**](/windows-hardware/drivers/ddi/prnasntp/nf-prnasntp-routergetprintclassobject)

- [**SetJobW**](/windows/win32/printdocs/setjob)

- [**SetPrinterDataExW**](/windows/win32/printdocs/setprinterdataex)

- [**SetPrinterDataW**](/windows/win32/printdocs/setprinterdata)

- [**StartDocPrinterW**](/windows/win32/printdocs/startdocprinter)

- [**StartPagePrinter**](/windows/win32/printdocs/startpageprinter)

- [**WritePrinter**](/windows/win32/printdocs/writeprinter)

## WinSpool.drv Functions

The following functions are exported by winspool.drv and are available to spooler plugins by linking to Winspool.h.

- [**AppendPrinterNotifyInfoData**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-appendprinternotifyinfodata)

- [**ExtDeviceMode**](/windows-hardware/drivers/ddi/winspool/nf-winspool-extdevicemode)

- [**ImpersonatePrinterClient**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-impersonateprinterclient)

- [**IsValidDevmode**](/windows/win32/printdocs/isvaliddevmode)

- [**PartialReplyPrinterChangeNotification**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-partialreplyprinterchangenotification)

- [**ReplyPrinterChangeNotification**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-replyprinterchangenotification)

- [**RevertToPrinterSelf**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-reverttoprinterself)

- [**RouterAllocBidiMem**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-routerallocbidimem)

- [**RouterAllocBidiResponseContainer**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-routerallocbidiresponsecontainer)

- [**RouterAllocPrinterNotifyInfo**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-routerallocprinternotifyinfo)

- [**RouterCreatePrintAsyncNotificationChannel**](/windows-hardware/drivers/ddi/prnasntp/nf-prnasntp-routercreateprintasyncnotificationchannel)

- [**RouterFreeBidiMem**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-routerfreebidimem)

- [**RouterFreeBidiResponseContainer**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-routerfreebidiresponsecontainer)

- [**RouterFreePrinterNotifyInfo**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-routerfreeprinternotifyinfo)

- [**RouterGetPrintClassObject**](/windows-hardware/drivers/ddi/prnasntp/nf-prnasntp-routergetprintclassobject)

- [**RouterRegisterForPrintAsyncNotifications**](/windows-hardware/drivers/ddi/prnasntp/nf-prnasntp-routerregisterforprintasyncnotifications)

- [**RouterUnregisterForPrintAsyncNotifications**](/windows-hardware/drivers/ddi/prnasntp/nf-prnasntp-routerunregisterforprintasyncnotifications)

## See also

[Spooler Component Functions and Structures](/windows-hardware/drivers/ddi/_print/index)
