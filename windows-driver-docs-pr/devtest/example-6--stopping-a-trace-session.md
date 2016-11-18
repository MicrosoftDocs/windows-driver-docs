---
title: Example 6 Stopping a Trace Session
description: Example 6 Stopping a Trace Session
ms.assetid: a8520531-bebb-4334-9dc3-d50f4a851e7e
keywords: ["trace sessions WDK , stopping", "stopping trace sessions"]
---

# Example 6: Stopping a Trace Session


## <span id="ddk_stopping_a_trace_session_tools"></span><span id="DDK_STOPPING_A_TRACE_SESSION_TOOLS"></span>


The following command stops the MyTrace trace session:

```
tracelog -stop MyTrace
```

In response, Tracelog displays the properties of the trace session.

```
Operation Status:       0L      The operation completed successfully.

Logger Name:            MyTrace
Logger Id:              2
Logger Thread Id:       000008C8
Buffer Size:            8 Kb
Maximum Buffers:        26
Minimum Buffers:        4
Number of Buffers:      6
Free Buffers:           6
Buffers Written:        1
Events Lost:            0
Log Buffers Lost:       0
Real Time Buffers Lost: 0
AgeLimit:               15
Log File Mode:          Sequential
Log Filename:           C:\Tracing\MyTrace.etl
```

To verify that the trace session is stopped, use a list (**tracelog -l**) or query (**tracelog -q**) command.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%206:%20Stopping%20a%20Trace%20Session%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




