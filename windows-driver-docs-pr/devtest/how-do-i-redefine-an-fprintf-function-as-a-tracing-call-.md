---
title: How do I redefine an fprintf function as a tracing call
description: How do I redefine an fprintf function as a tracing call
ms.assetid: def82d48-454b-421b-a63d-695dae733fd0
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20do%20I%20redefine%20an%20fprintf%20function%20as%20a%20tracing%20call?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




