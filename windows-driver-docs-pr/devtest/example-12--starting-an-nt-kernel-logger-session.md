---
title: Example 12 Starting an NT Kernel Logger Session
description: Example 12 Starting an NT Kernel Logger Session
ms.assetid: ce795cd3-4d95-49a1-a8b7-a32c69c776dd
keywords:
- trace sessions WDK , NT Kernel Logger
- NT Kernel Logger trace sessions WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example 12: Starting an NT Kernel Logger Session


## <span id="ddk_starting_an_nt_kernel_logger_session_tools"></span><span id="DDK_STARTING_AN_NT_KERNEL_LOGGER_SESSION_TOOLS"></span>


The following command starts an NT Kernel Logger trace session. Because the NT Kernel Logger trace session is the default, no other parameters are required.

```
tracelog -start
```

By default, process, thread, disk, and TCP/IP events are traced. To override the defaults, you can use the parameters designed for the NT Kernel Logger session.

The following command uses the **-nothread** parameter to turn off tracing of thread events, the **-hf** parameter to trace hard page faults, and the **-cm** parameter to trace registry events. This example also uses the optional **-ft** parameter, which can be used in any trace session, to flush buffers at a fixed time interval in addition to the automatic flush that occurs when a buffer is full.

```
tracelog -start -nothread -hf -cm -ft 2
```

You can also start a real-time trace session with NT Kernel Logger. The following command starts a real-time trace session with the NT Kernel Logger. Again, as in the previous example, you can omit the session name, because "NT Kernel Logger" is the default.

```
tracelog -start -rt
```

You can also use the customized NT Kernel Logger parameters for a real-time trace session, in addition to parameters to customize the buffers and the timer resolution.

To format and display the trace messages from this session, use Tracefmt. The following command displays the trace messages from the NT Kernel Logger session in a Command Prompt window. For more information, see [Tracefmt](tracefmt.md).

```
tracefmt -rt -display
```

 

 





