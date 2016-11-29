---
title: Example 12 Starting an NT Kernel Logger Session
description: Example 12 Starting an NT Kernel Logger Session
ms.assetid: ce795cd3-4d95-49a1-a8b7-a32c69c776dd
keywords: ["trace sessions WDK , NT Kernel Logger", "NT Kernel Logger trace sessions WDK"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%2012:%20Starting%20an%20NT%20Kernel%20Logger%20Session%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




