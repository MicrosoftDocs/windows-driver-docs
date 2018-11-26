---
title: Print Provider Capabilities
description: Print Provider Capabilities
ms.assetid: 1b01aac5-673a-4593-a52e-6017d9683c42
keywords:
- print providers WDK , capabilities
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Print Provider Capabilities





**Warning**  
Starting with Windows 10, the APIs which support third-party print providers are deprecated. Microsoft does not recommend any investment into third-party print providers. Additionally, on Windows 8 and newer products where the v4 print driver model is available, third-party print providers may not create or manage queues which use v4 print drivers.

 

By supporting predefined sets of API functions, Microsoft Windows 2000 and later print providers can supply the following capabilities:

-   Print Queue Management

    Adding, deleting, opening, closing, enumerating, and setting parameters for print queues. Also, providing notification of changes to a print queue's state.

-   Printer Driver Management

    Adding, deleting, enumerating, and specifying a directory for printer drivers.

-   Print Job Creation

    Starting and ending a document, starting and ending a document page, writing the job's data stream to a port, reading printer status information.

-   Print Job Scheduling

    Scheduling, enumerating, and setting parameters for a print job.

-   Forms Management

    Adding, deleting, enumerating, and setting parameters for print forms.

-   Print Processor Management

    Adding, deleting, enumerating, specifying a directory for and the data types supported by print processors.

-   Print Monitor Management

    Adding, deleting, and enumerating print monitors.

-   Port Management

    Adding, deleting, configuring, enumerating, and setting parameters for printer ports.

-   Registry Management

    Creating, deleting, and enumerating registry keys and values associated with a print provider.

-   Other Capabilities

    Displaying a message box, shutting down the print provider, reading a memory mapped spool file, providing a communication path between port monitor UI DLLs and port monitor server DLLs.

These capabilities are implemented as a set of [functions defined by print providers](functions-defined-by-print-providers.md).

 

 




