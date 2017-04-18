---
title: Example 11 Starting a Private Trace Session
description: Example 11 Starting a Private Trace Session
ms.assetid: e1826811-cb1c-400f-a3e1-aaa6ae83ef42
keywords: ["trace sessions WDK , private", "private trace sessions WDK"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%2011:%20Starting%20a%20Private%20Trace%20Session%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




