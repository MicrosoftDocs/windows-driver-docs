---
title: Example 6 Tracing Special Sessions
description: Example 6 Tracing Special Sessions
ms.assetid: 5e528086-812c-478b-a2d1-69d54781cbb2
keywords:
- Tracefmt WDK , special sessions
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





