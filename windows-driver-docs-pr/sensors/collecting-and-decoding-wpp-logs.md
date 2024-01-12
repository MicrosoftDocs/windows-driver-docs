---
title: Collecting and Decoding WPP Logs
description: This article provides information about collecting and decoding Windows software trace preprocessor (WPP) logs for the sensor class extension (CX) trace provider.
ms.date: 01/11/2024
---

# Collecting and decoding WPP logs

This article provides information about collecting and decoding Windows software trace preprocessor (WPP) logs for the sensor class extension (CX) trace provider.

WPP provides ways to trace the operation of software components known as trace providers. The following are PDB files included to decode the WPP logs.

- SensorsCx.pdb
- SensorsUtilsV2.pdb

The tracelog tool is used to collect WPP logs. For more information, see [Tracelog](../devtest/tracelog.md). For more information about tracing concepts such as tracing GUIDs, trace flags, trace levels, or PDB files, see [Tracing Tool Concepts](../devtest/tracing-tool-concepts.md).

## Tracing GUID

The following GUID identifies the trace provider for the CX driver in the sensor V2 stack. For more information about using this GUID with tracelog, see [Tracelog](../devtest/tracelog.md).

``` syntax
c88b592b-6090-480f-a839-ca2434de5844
```

## Trace flags

The sensor class extension defines the following WPP_CONTROL_GUIDS trace flags:

``` syntax
EntryExit
DataFlow
Verbose
Information
Warning
Error
Fatal
DriverStatus
```

## Trace levels

The following trace levels are defined for usage with tracelog. For more information about how these are used, see the **level** parameter in the tracelog syntax.

``` syntax
TRACE_LEVEL_FATAL           1
TRACE_LEVEL_ERROR           2
TRACE_LEVEL_WARNING         3
TRACE_LEVEL_INFORMATION     4
TRACE_LEVEL_VERBOSE         5
TRACE_LEVEL_PERF            6
```

## Tracelog macros

The following are WPP macros with their associated trace levels and trace flags. The MSG parameter is a standard format string that is defined for the printf function. Partners can also use the WPP extended format string. For more information about this, see [WPP extended format strings](../devtest/what-are-the-wpp-extended-format-specification-strings-.md). The newline character is also included in the MSG so "\\n" isn't necessary.

| Macro                | Level                   | Flag         | Parameter |
|----------------------|-------------------------|--------------|-----------|
| TraceFatal           | TRACE_LEVEL_FATAL       | Fatal        | MSG       |
| TraceError           | TRACE_LEVEL_ERROR       | Error        | MSG       |
| TraceWarning         | TRACE_LEVEL_WARNING     | Warning      | MSG       |
| TraceInformation     | TRACE_LEVEL_INFORMATION | Information  | MSG       |
| TraceVerbos          | TRACE_LEVEL_VERBOSE     | Verbose      | MSG       |
| TracePerformance     | TRACE_LEVEL_PERF        | &nbsp;       | Flag, MSG |
| TraceData            | TRACE_LEVEL_VERBOSE     | DataFlow     | MSG       |
| TraceDriverStatus    | TRACE_LEVEL_INFORMATION | DriverStatus | MSG       |
| CLX_FunctionEnter    | TRACE_LEVEL_VERBOSE     | EntryExit    | N/A       |
| CLX_FunctionExit     | TRACE_LEVEL_VERBOSE     | EntryExit    | NTSTATUS  |
| SENSOR_FunctionEnter | TRACE_LEVEL_VERBOSE     | EntryExit    | N/A       |
| SENSOR_FunctionExit  | TRACE_LEVEL_VERBOSE     | EntryExit    | NTSTATUS  |

## Decoding ETL logs

The tracefmt tool is used to decode ETL logs. For more information about this tool, see [Tracefmt](../devtest/tracefmt.md).

If you want to do more extensive testing of your sensor driver, see [Test your universal sensor driver](test-your-universal-sensor-driver.md).
