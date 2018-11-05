---
title: Using WPP Software Tracing in a Trace Provider
description: Using WPP Software Tracing in a Trace Provider
ms.assetid: e215a99b-5082-4e81-84b6-184a2fd4e270
keywords:
- Windows software trace preprocessor WDK , about WPP
- WPP software tracing WDK , about WPP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using WPP Software Tracing in a Trace Provider


## <span id="ddk_using_wpp_software_tracing_in_a_driver_tools"></span><span id="DDK_USING_WPP_SOFTWARE_TRACING_IN_A_DRIVER_TOOLS"></span>


To use the default form of WPP software tracing in a [trace provider](trace-provider.md), such as a kernel-mode driver or a user-mode application, do the following:

-   Define a control GUID that uniquely identifies the [trace provider](trace-provider.md). The provider specifies this GUID in its definition of the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro and in a related control file used by [Tracelog](tracelog.md).

-   Add the required WPP-related C preprocessor directives and WPP macro calls to the provider's source files, as described in [Adding WPP Macros to a Trace Provider](adding-wpp-macros-to-a-trace-provider.md) and in [WPP Software Tracing Reference](https://msdn.microsoft.com/library/windows/hardware/ff556205).

-   Build the driver, as described in [WPP Preprocessor](wpp-preprocessor.md).

-   Use other tools for software tracing, such as [TraceView](traceview.md), [Tracelog](tracelog.md), [Tracefmt](tracefmt.md), and [Tracepdb](tracepdb.md) to configure, start, and stop tracing sessions and to display and filter trace messages. These tools are included in the Windows Driver Kit (WDK) in the \\tools\\tracing directory.

 

 





