---
title: Event Tracing
description: You can use Event Tracing for Windows (ETW) or the Windows software trace preprocessor (WPP) to trace the operations in your HID over I<sup>2</sup>C.
ms.date: 01/11/2024
---

# Event tracing

You can use Event Tracing for Windows (ETW) or the Windows software trace preprocessor (WPP) to trace the operations in your HID over I<sup>2</sup>C device driver. For more information about ETW, see the [Event Tracing](/windows/win32/etw/event-tracing-portal) topic in the Windows Development Reference. For more information about WPP, see [WPP Software Tracing](../devtest/wpp-software-tracing.md) and [Inflight Trace Recorder (IFR) for logging traces](../devtest/using-wpp-recorder.md).

## Using the Inflight Trace Recorder (IFR)

The Inflight Trace Recorder (IFR), that is enabled by default for all drivers, lets you view trace output from the HIDI<sup>2</sup>C driver to a kernel debugger. The following command displays WPP trace messages for HIDI<sup>2</sup>C.

``` syntax
!rcdrkd.rcdrlogdump hidi2c
```

The Inflight Trace Recorder (IFR) stores these trace messages in a fixed-size circular buffer. As a result, the output may not contain the entire trace log.

## Using logman.exe

For more verbose and controllable traces, you can use [logman.exe]( https://go.microsoft.com/fwlink/p/?linkid=256232) to capture traces. The following commands capture WPP traces for HIDI<sup>2</sup>C:

``` syntax
Logman create trace -n HIDI2C_WPP -o HIDI2C_WPP.etl -nb 128 640 -bs 128 
Logman update trace -n HIDI2C_WPP -p {E742C27D-29B1-4E4B-94EE-074D3AD72836} 0x7FFFFFFF 255
Logman start –n HIDI2C_WPP
 
<RUN your SCENARIO here>

Logman stop -n HIDI2C_WPP
Logman delete -n HIDI2C_WPP
```

You can parse the resulting trace log file into text using either the PDB or TMF files for HIDI<sup>2</sup>C.

## Enabling ETW tracing

The HIDI<sup>2</sup>C driver logs ETW events for specific events. These events are logged in the Event Viewer logs.

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
