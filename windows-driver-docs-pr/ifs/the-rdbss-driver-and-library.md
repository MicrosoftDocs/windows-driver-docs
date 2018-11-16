---
title: The RDBSS Driver and Library
description: The RDBSS Driver and Library
ms.assetid: fb2d1939-7af5-474c-8247-e5d48b4bbed6
keywords:
- network redirectors WDK , RDBSS
- redirector drivers WDK , RDBSS
- kernel network redirectors WDK , RDBSS
- RDBSS WDK file systems
- file system drivers WDK , RDBSS
- static libraries WDK file systems
- RDBSS WDK file systems , about RDBSS
- Redirected Drive Buffering Subsystem WDK file systems , about RDBSS
- mini-redirectors WDK , RDBSS
- structures WDK RDBSS
- data structures WDK RDBSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The RDBSS Driver and Library


## <span id="ddk_the_rdbss_driver_and_library_if"></span><span id="DDK_THE_RDBSS_DRIVER_AND_LIBRARY_IF"></span>


The Redirected Drive Buffering Subsystem (RDBSS) is implemented in two forms:

-   A file system driver (*rdbss.sys*) supplied with the operating system.

-   A static library (*rdbsslib.lib*) supplied with the Windows Driver Kit (WDK).

The *rdbss.sys* driver is automatically loaded if any non-monolithic network mini-redirectors are registered on the system. The Microsoft Server Message Block (SMB) redirector (*mrxsmb sys*) is currently the only driver that can be built as a non-monolithic network mini-redirector driver.

All other network mini-redirector drivers, including other Microsoft network mini-redirectors supplied with the operating system, must be implemented as monolithic drivers that link with the *rdbsslib.lib* static library provided with the WDK.

The RDBSS uses a well-defined mechanism for communication with network mini-redirector drivers, I/O Manager, Cache Manager, Memory Manager, and other kernel systems.

RDBSS exports a large number of routines that can be called by a network mini-redirector and other kernel systems to set options and perform various operations. To call the routines exported by RDBSS, a network mini-redirector driver (or other kernel driver) includes the appropriate WDK header files, calls the exported RDBSS routine by name, and links with the appropriate *rdbsslib.lib* file installed with the WDK. Note that different *rdbsslib.lib* files are provided with the WDK for Window Vista, Windows Server 2003, Windows XP, and Windows 2000.

The WDK header files for RDBSS also define a number of macros that are recommended for use by network mini-redirector drivers, rather than calling some of the RDBSS routines directly.

All of the data structures defined and used by RDBSS have a special 4-byte signature at the beginning of the data structure that is used extensively in validation. The values for these RDBSS data structures signatures are defined in the WDK header file, *nodetype.h*. These data structure signatures are used for troubleshooting and debugging RDBSS and network mini-redirector drivers.

The following sections discuss in detail each of the categories of routines exported by RDBSS and the macros defined to call these routines. We begin with a list of all of the routines provided by RDBSS and a similar list of macros defined by RDBSS:

-   [Routines Provided by RDBSS](routines-provided-by-rdbss.md)

-   [Macros Defined by RDBSS](macros-defined-by-rdbss.md)

The routines exported by RDBSS and the RDBSS macros defined to call these routines can be organized into a number of different categories, including the following:

-   [Driver Registration and Start/Stop Control](driver-registration-and-start-stop-control.md)

-   [Pool Allocation and Free Routines](pool-allocation-and-free-routines.md)

-   [Timer and Worker Thread Management](timer-and-worker-thread-management.md)

-   [Work Queue Dispatching Mechanisms](work-queue-dispatching-mechanisms.md)

-   [Diagnostics and Debugging](diagnostics-and-debugging.md)

-   [Logging Routines and Macros](logging-routines-and-macros.md)

-   [Miscellaneous Routines](miscellaneous-routines2.md)

-   [RX\_CONTEXT and IRP Management](rx-context-and-irp-management.md)

-   [Connection and File Structure Management](connection-and-file-structure-management.md)

-   [FCB Resource Synchronization](fcb-resource-synchronization.md)

-   [Buffering State Control](buffering-state-control.md)

-   [Low I/O Routines](low-i-o-routines.md)

-   [Name Cache Management](name-cache-management.md)

-   [Prefix Table Management](prefix-table-management.md)

-   [Purging and Scavenging Control](purging-and-scavenging-control.md)

-   [Multiplex ID Management](multiplex-id-management.md)

-   [Connection Engine Management](connection-engine-management.md)

 

 




