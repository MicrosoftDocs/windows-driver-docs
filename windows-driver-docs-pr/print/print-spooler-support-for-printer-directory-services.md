---
title: Print Spooler Support for Printer Directory Services
description: Print Spooler Support for Printer Directory Services
keywords:
- Directory Services WDK printer
- print spooler Directory Services support WDK
- publishing WDK printer
ms.date: 06/09/2020
ms.localizationpriority: medium
---

# Print Spooler Support for Printer Directory Services

Print spooler support for Directory Services consists of:

- Publishing print queues

- Maintaining three registry keys

- Allowing access to spooler-maintained registry keys

- Returning a print queue's publication state

## Publishing Print Queues

The **SetPrinter** function allows callers to publish, unpublish, or update a print queue object. For these purposes, the **SetPrinter** function must be called with an input structure of PRINTER\_INFO\_7.

A print queue object can be published only if it is associated with the computer object describing the print server to which the user is connected. A user's ability to publish a print queue is determined by their access rights, as contained in the user's client security context. You can publish a print queue if you have Manage Printers permission on the print queue.

## Maintaining Three Registry Keys

Three registry keys contain copies of all information published in the print queue object. The three keys are referenced using the following identifiers, defined in winspool.h:

| Key | Definition |
| --- | --- |
| SPLDS_DRIVER_KEY | For storing driver-specific information, which can be supplied by the spooler or the driver. |
| SPLDS_SPOOLER_KEY | For storing spooler-supplied, spooler-specific information. |
| SPLDS_USER_KEY | For storing application-supplied, user-specific information. |

The spooler uses SPLDS\_DRIVER\_KEY to store driver capabilities that can be obtained by calling the Microsoft Windows SDK **DeviceCapabilities** function. The driver is responsible for storing driver capabilities that the spooler cannot obtain, as described in [Printer Driver Support for Printer Directory Services](printer-driver-support-for-printer-directory-services.md). Values stored under these keys must be identified by **SPLDS\_**-prefixed constants, defined in winspool.h.

The spooler keeps track of which values under these keys have been modified since the last time the print queue object was updated. Each time the spooler publishes or updates the print queue object, it copies all modified values into the object.

## Allowing Access to Spooler-Maintained Registry Keys

The spooler allows printer drivers to access the three spooler-maintained registry keys by calling the **SetPrinterDataEx**, **GetPrinterDataEx** and **EnumPrinterDataEx** functions, all of which are described in the Microsoft Windows SDK documentation. The **SetPrinterDataEx** function sets values under the keys, while **GetPrinterDataEx** and **EnumPrinterDataEx** return current values. (Drivers should not set values under the SPLDS\_SPOOLER\_KEY key.) Callers of these functions do not specify a complete registry path; the functions automatically determine the path to the specified print queue's registry entries.

## Returning a Print Queue's Publication State

The **GetPrinter** function allows callers to determine if a print queue is currently published. For this purpose, the **GetPrinter** function must be called with an input structure of PRINTER\_INFO\_7. The function returns the print queue's publication state (published or unpublished) and object identifier.

All the previously mentioned functions are described in the Windows SDK documentation. The functions are not used exclusively for DS-related operations.
