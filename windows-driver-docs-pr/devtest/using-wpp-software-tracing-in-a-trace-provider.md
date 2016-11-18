---
title: Using WPP Software Tracing in a Trace Provider
description: Using WPP Software Tracing in a Trace Provider
ms.assetid: e215a99b-5082-4e81-84b6-184a2fd4e270
keywords: ["Windows software trace preprocessor WDK , about WPP", "WPP software tracing WDK , about WPP"]
---

# Using WPP Software Tracing in a Trace Provider


## <span id="ddk_using_wpp_software_tracing_in_a_driver_tools"></span><span id="DDK_USING_WPP_SOFTWARE_TRACING_IN_A_DRIVER_TOOLS"></span>


To use the default form of WPP software tracing in a [trace provider](trace-provider.md), such as a kernel-mode driver or a user-mode application, do the following:

-   Define a control GUID that uniquely identifies the [trace provider](trace-provider.md). The provider specifies this GUID in its definition of the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro and in a related control file used by [Tracelog](tracelog.md).

-   Add the required WPP-related C preprocessor directives and WPP macro calls to the provider's source files, as described in [Adding WPP Macros to a Trace Provider](adding-wpp-macros-to-a-trace-provider.md) and in [WPP Software Tracing Reference](https://msdn.microsoft.com/library/windows/hardware/ff556205).

-   Build the driver, as described in [WPP Preprocessor](wpp-preprocessor.md).

-   Use other tools for software tracing, such as [TraceView](traceview.md), [Tracelog](tracelog.md), [Tracefmt](tracefmt.md), and [Tracepdb](tracepdb.md) to configure, start, and stop tracing sessions and to display and filter trace messages. These tools are included in the Windows Driver Kit (WDK) in the \\tools\\tracing directory.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Using%20WPP%20Software%20Tracing%20in%20a%20Trace%20Provider%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




