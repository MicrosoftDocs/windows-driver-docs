---
title: Event tracing
author: windows-driver-content
description: You can use Event Tracing for Windows (ETW) or the Windows software trace preprocessor (WPP) to trace the operations in your HID over I²C.
ms.assetid: F23E5516-36B9-478E-90D3-54D1C52CB467
---

# Event tracing


You can use Event Tracing for Windows (ETW) or the Windows software trace preprocessor (WPP) to trace the operations in your HID over I²C device driver. For more information about ETW, see the [Event Tracing](http://go.microsoft.com/fwlink/p/?linkid=256040) topic in the Windows Development Reference. For more information about WPP, see [WPP Software Tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204) and [Inflight Trace Recorder (IFR) for logging traces](https://msdn.microsoft.com/library/windows/hardware/dn914610).

## Using the Inflight Trace Recorder (IFR)


The Inflight Trace Recorder (IFR), that is enabled by default for all drivers, lets you view trace output from the HIDI²C driver to a kernel debugger. The following command displays WPP trace messages for HIDI²C.

``` syntax
!rcdrkd.rcdrlogdump hidi2c
```

The Inflight Trace Recorder (IFR) stores these trace messages in a fixed-size circular buffer. As a result, the output may not contain the entire trace log.

## Using logman.exe


For more verbose and controllable traces, you can use [logman.exe]( http://go.microsoft.com/fwlink/p/?linkid=256232) to capture traces. The following commands capture WPP traces for HIDI²C:

``` syntax
Logman create trace -n HIDI2C_WPP -o HIDI2C_WPP.etl -nb 128 640 -bs 128 
Logman update trace -n HIDI2C_WPP -p {E742C27D-29B1-4E4B-94EE-074D3AD72836} 0x7FFFFFFF 255
Logman start –n HIDI2C_WPP
 
<RUN your SCENARIO here>

Logman stop -n HIDI2C_WPP
Logman delete -n HIDI2C_WPP
```

You can parse the resulting trace log file into text using either the PDB or TMF files for HIDI²C.

## Enabling ETW tracing


The HIDI²C driver logs ETW events for specific events. These events are logged in the Event Viewer logs.

You can also view these events using the following logman.exe commands:

``` syntax
Logman create trace -n HIDI2C_ETW -o HIDI2C_ETW.etl -nb 128 640 -bs 128 
Logman update trace -n HIDI2C_ETW -p Microsoft-Windows-SPB-HIDI2C 
Logman start –n HIDI2C_ETW
 
<RUN your SCENARIO here>

Logman stop -n HIDI2C_ETW
Logman delete -n HIDI2C_ETW
```

The resulting trace log can parsed with tools like **Xperf** or **Windows Performance Analyzer** (WPA).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Event%20tracing%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


