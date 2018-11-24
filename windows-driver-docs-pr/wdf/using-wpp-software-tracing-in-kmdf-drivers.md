---
title: Using WPP Software Tracing in KMDF Drivers
description: Using WPP Software Tracing in KMDF Drivers
ms.assetid: dad7aa8d-4ced-47b3-80d2-ec9cfb355783
keywords:
- software tracing WDK , framework-based drivers
- debugging drivers WDK KMDF , software tracing
- tracing WDK , framework-based drivers
- WPP software tracing WDK , framework-based drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using WPP Software Tracing in KMDF Drivers


[WPP software tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204) enables you to add tracing messages that help you debug your driver. Additionally, the framework's [event logger](using-the-framework-s-event-logger.md) provides hundreds of tracing messages that you can view.

You can view tracing messages by using [TraceView](https://msdn.microsoft.com/library/windows/hardware/ff553872) or [Tracelog](https://msdn.microsoft.com/library/windows/hardware/ff552994). You can also [send trace messages to a kernel debugger](https://msdn.microsoft.com/library/windows/hardware/ff546837).

### Adding Tracing Messages to Your Driver

To add tracing messages to your framework-based driver, you must:

- Add an **\#include** directive to each of your driver's source files that contains any of the WPP macros. This directive must identify a [trace message header (TMH) file](https://msdn.microsoft.com/library/windows/hardware/ff553926). The file name must have a format of &lt;*driver-source-file-name*&gt;**.tmh**.

  For example, if your driver consists of two source files, called *MyDriver1.c* and *MyDriver2.c*, then *MyDriver1.c* must contain:

  **\#include "MyDriver1.tmh"**

  and *MyDriver2.c* must contain:

  **\#include "MyDriver2.tmh"**

  When you build your driver in Microsoft Visual Studio, the WPP preprocessor generates the .*tmh* files.

- Define a [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro in a header file. This macro defines a GUID and [trace flags](https://msdn.microsoft.com/library/windows/hardware/ff553904) for your driver's tracing messages.

- Include a [WPP\_INIT\_TRACING](https://msdn.microsoft.com/library/windows/hardware/ff556191) macro in your driver's [**DriverEntry routine**](https://msdn.microsoft.com/library/windows/hardware/ff540807). This macro activates software tracing in your driver.

- Include a [WPP\_CLEANUP](https://msdn.microsoft.com/library/windows/hardware/ff556179) macro in your driver's [*EvtDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff541694) callback function. This macro deactivates software tracing in your driver.

- Use the [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918) macro, or a [customized version](https://msdn.microsoft.com/library/windows/hardware/ff542492) of the macro, in your driver to create trace messages.

- Open the Property Pages for your driver project. Right-click the driver project in Solution Explorer and select **Properties**. In the Property Pages for the driver, click **Configuration Properties**, and then **Wpp**. Under the **General** menu, set **Run WPP Tracing** to Yes. Under the **File Options** menu, you should also specify the framework's WPP template file, for example:

  ```cpp
  {km-WdfDefault.tpl}*.tmh
  ```
    
- To specify additional WPP trace settings for your driver project in Visual Studio, right-click on the driver project in Solutions Explorer. Then follow the link to Properties->Configuration Properties->WPP Tracing. 

- To specify a trace configuration file use the 'Scan Configuration Data' setting. For more than one trace configuration file add it under the 'Command Line'-> 'Additional Options' as follows
  ```cpp
  -scan:"$(KMDF_INC_PATH)\$(KMDF_VER_PATH)\wdftraceenums.h"
  ```
  For more information about adding tracing messages to your driver, see [Adding WPP Macros to a Driver](https://msdn.microsoft.com/library/windows/hardware/ff541243).

### Sample Drivers That Use WPP Software Tracing

The AMCC5933, NONPNP, KMDF\_FX2, PCIDRV, PLX9x5x, and Serial [sample drivers](sample-kmdf-drivers.md) use WPP software tracing.

 

 





