---
title: Example 8 Configuring Trace Buffers
description: Example 8 Configuring Trace Buffers
ms.assetid: 7bcc076c-6feb-4660-88d7-dc4206b53dce
keywords: ["trace buffers WDK", "buffers WDK software tracing"]
---

# Example 8: Configuring Trace Buffers


## <span id="ddk_configuring_trace_buffers_tools"></span><span id="DDK_CONFIGURING_TRACE_BUFFERS_TOOLS"></span>


The following command starts a trace log session and customizes the buffers for the session:

```
tracelog -start MyTrace -guid MyProvider.guid -f testtrace.etl -flag 2 -level ffff -b 128 -min 10 -max 30
```

The command starts a session named "MyTrace". It uses the **-guid** parameter to specify the provider file and the **-f** parameter to specify the name and location of the trace log.

It uses the **-flag** parameter to set the flag value to 2 and the **-level** parameter to set the level value to FFFF, which generates all available trace messages. These settings are specific to the provider.

To accommodate the high message rate, this command uses the **-b** parameter to increase the size of each buffer to 128 KB, the **-min** parameter to increase the minimum number of buffers to 10, and the **-max** parameter to increase the maximum number of buffers to 30.

In response, Tracelog starts a trace session and displays a few of the session properties. The properties that were set by the command are shown in bold type for easy identification.

```
Logger Started...
Enabling trace to logger 2
Operation Status:       0L      The operation completed successfully.

Logger Name:            MyTrace
Logger Id:              2
Logger Thread Id:       00000D7C
Buffer Size:            128 Kb
Maximum Buffers:        30
Minimum Buffers:        10
Number of Buffers:      10
Free Buffers:           9
Buffers Written:        1
Events Lost:            0
Log Buffers Lost:       0
Real Time Buffers Lost: 0
AgeLimit:               15
Log File Mode:          Sequential
Enabled tracing:        0x00000002
Log Filename:           d:\traces\testtrace.etl 
```

It is always important to watch the **Events Lost** counter in the trace session properties list. If you are losing events, rerun the trace session with increased buffer capacity (size, number, or both). To view the properties of a trace session, use **tracelog -l** or **tracelog -q***SessionName*.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%208:%20Configuring%20Trace%20Buffers%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




