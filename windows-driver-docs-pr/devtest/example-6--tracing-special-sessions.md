---
title: Example 6 Tracing Special Sessions
description: Example 6 Tracing Special Sessions
ms.assetid: 5e528086-812c-478b-a2d1-69d54781cbb2
keywords: ["Tracefmt WDK , special sessions"]
---

# Example 6: Tracing Special Sessions


You can use Tracefmt to format trace messages from the NT Kernel Logger, WMI Event Logger, and Global Logger reserved trace sessions.

The following command formats and displays trace messages from an NT Kernel Logger real-time trace session. (For information about starting an NT Kernel Logger trace session, see [TraceView](traceview.md) or [Tracelog](tracelog.md).)

```
tracefmt -rt -tmf system.tmf -display
```

This command does not include the name of the trace session, even though it uses the **-rt** parameter. It is not required in this case, because "NT Kernel Logger" is the default value.

However, the **-tmf** parameter is required in order to direct Tracefmt to the system.tmf file. By default, Tracefmt uses default.tmf, which does not include formatting instructions for NT Kernel Logger trace messages. The **-p** parameter finds the TMF file only when the TMF file name is a message guid, such as 37753236-c81f-505e-d40a-128d3bb2b5ff.tmf.

This command also uses the **-display** parameter, which displays the trace messages in the Command Prompt window in addition to writing them to a log file. In this case, because the **-o** parameter is omitted, the messages are written to the default log file, FmtFile.txt, in the local directory.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%206:%20Tracing%20Special%20Sessions%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




