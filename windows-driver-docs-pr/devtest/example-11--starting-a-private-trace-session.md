---
title: Example 11 Starting a Private Trace Session
description: Example 11 Starting a Private Trace Session
ms.assetid: e1826811-cb1c-400f-a3e1-aaa6ae83ef42
keywords:
- trace sessions WDK , private
- private trace sessions WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example 11: Starting a Private Trace Session


## <span id="ddk_starting_a_private_trace_session_tools"></span><span id="DDK_STARTING_A_PRIVATE_TRACE_SESSION_TOOLS"></span>


The following command starts a private trace session of a user-mode application that is instrumented for tracing.

```
tracelog -start MyTrace -guid MyProvider.guid -um
```

You can use the same parameters to customize a private trace session that you would use for a standard trace session, except that you cannot perform real-time tracing of private trace sessions.

**Heap memory process logger.** The following command starts a private session that traces the heap memory events in a process. It works on any user-mode process, even one that is not instrumented for tracing.

Because this feature uses a provider that is built into Windows, this command specifies the process (using a process ID) that is being traced, not the provider (using a GUID) that is generating the trace messages..

This command uses the **-um** parameter to specify a private (user-mode) trace session and the **-heap** parameter to specify a heap memory trace. It uses the **-pids** parameter to specify the process ID of the process to be traced. In this case, the command includes one process with ID **7008**.

The command also uses the optional **-f** parameter to specify the trace log file. The **-f** parameter is included to remind you that you can use most of the other Tracelog parameters to customize the trace session.

```
tracelog -start MyTrace -um -heap -pids 1 7008 -f testtrace.etl
```

**Critical section process logger.** The following command starts a critical section logger, a private session that traces the critical section events in a process. This command uses a provider (identified by the GUID, CritsecGUID) that is included in Windows, so it can be used on any user-mode process, even one that is not instrumented for tracing.

The command syntax is identical to that for the heap memory process logger, except that it uses the **-critsec** parameter instead of the **-heap** parameter.

In this example, the command starts the critical section process logger on two related processes. Therefore, the value of the *\#PIDs* variable is **2**, and both process IDs **4806** and **5164** are listed.

```
tracelog -start MyTrace -um -critsec -pids 2 4806 5164 -f testtrace.etl
```

 

 





