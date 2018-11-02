---
title: How do I redefine an fprintf function as a tracing call
description: How do I redefine an fprintf function as a tracing call
ms.assetid: def82d48-454b-421b-a63d-695dae733fd0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I redefine an fprintf function as a tracing call?


An **fprintf** function call, which is eventually converted to an **sprintf** function call, is a very resource-intensive call that can degrade performance perceptibly, especially when it is used repeatedly.

Redefining an **fprintf** function as a tracing call is much more efficient, because the trace messages are stored in binary format and formatting is postponed until you display the trace log.

To redefine a printing function such as **fprintf** as a tracing call, the resulting call must do two things:

-   Assign a default level for the tracing function, such as error, warning, or noise.

-   Ignore the handle.

The following example shows a function description that does both:

```
-func:fprintf{LEVEL=Noise}(NULL,MSG,...)
```

You can define this function description in a local configuration file, such as localwpp.ini, or use the **-func** parameter of RUN\_WPP (the macro that invokes the WPP preprocessor) to define the function description.

For a complete list of the optional parameters for RUN\_WPP, see [WPP Preprocessor](wpp-preprocessor.md).

 

 





