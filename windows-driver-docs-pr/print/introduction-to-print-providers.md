---
title: Introduction to Print Providers
description: Introduction to Print Providers
ms.assetid: a0e5e8c8-7af4-4715-9036-64ae851b307d
keywords:
- print providers WDK , about print providers
- print jobs WDK , print providers
- print providers WDK , flow paths
- OpenPrinter
- jobs WDK print , print providers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Print Providers

> [!WARNING]
> Starting with Windows 10, the APIs which support third-party print providers are deprecated. Microsoft does not recommend any investment into third-party print providers. Additionally, on Windows 8 and newer products where the v4 print driver model is available, third-party print providers may not create or manage queues which use v4 print drivers.

Print providers are responsible for directing print jobs to local or remote print devices. They are also responsible for print queue management operations, such as starting, stopping, and enumerating a server's print queues. Print providers define a high-level, machine-independent, operating system-independent view of a print server.

All print providers implement a common set of [print provider capabilities](print-provider-capabilities.md). These capabilities are defined by a set of API functions, which are called by the spooler's router (Spoolss.dll).

Most functions defined by print providers require a printer handle as input. A spooler client obtains a printer handle by calling **OpenPrinter** (described in the Microsoft Windows SDK documentation) in Winspool.drv, which calls the API server (Spoolsv.exe). The spooler's router (Spoolss.dll) calls each print provider's **OpenPrinter** function until one of them supplies a printer handle and a return value indicating the print provider recognizes the specified printer name. The router then returns its own handle to the API server. The router's handle includes both the printer handle and a provider handle. This handle is returned to the application so that subsequent calls from the application can be directed to the correct provider and printer.

Microsoft provides the following print providers with Windows 2000 and later:

**Localspl.dll**  
[Local print provider](local-print-provider.md). Handles all print jobs directed to printers that are managed from the local server.

**Win32spl.dll**  
Windows network print provider. Handles print jobs directed to remote Win32 (NT-based-operating system or Windows for Workgroups) servers. When the job arrives at the remote server, it is passed to the server's local print provider.

**Nwprovau.dll**  
Novell NetWare print provider. Handles print jobs directed to Novell NetWare print servers.

**Inetpp.dll**  
HTTP print provider. Handles print jobs sent to a URL.

Vendors can create additional network print providers. For more information, see [Writing a Network Print Provider](writing-a-network-print-provider.md).

The following diagram illustrates possible flow paths involving these print providers.

![print provider flow paths ](images/flowpths.png)

When viewing the diagram, you should consider the following points:

-   If the printer is managed by the client system, the print job is handled by the [local print provider](local-print-provider.md) (Localspl.dll). Printers managed by Localspl.dll do not have to be physically local to the client; they can be directly connected to network cards.

-   If the printer is located on a NT-based-operating system server, the network provider (Win32spl.dll) uses RPC to redirect calls from the client's router to the server's Spoolsv.exe process. Because the printer is local to the server, the server's local print provider will handle the print job.

-   If the printer is located on some other type of server, it can be accessed by either the local print provider or by a network print provider that supports that server type, using data formats and network protocols supported by the server.

-   For the local print provider to access a remote printer, it must contain a [port monitor](https://docs.microsoft.com/windows-hardware/drivers/print/port-monitors) that can use network protocols recognized by the remote printer or server.
