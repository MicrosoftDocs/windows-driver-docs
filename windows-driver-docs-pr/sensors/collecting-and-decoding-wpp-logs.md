---
title: Collecting and decoding WPP logs
description: This topic provides information about collecting and decoding Windows software trace preprocessor (WPP) logs for the sensor class extension (CX) trace provider.
ms.assetid: 174CDE37-D0D1-44BF-AD50-5A90C989FDE2
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Collecting and decoding WPP logs


This topic provides information about collecting and decoding Windows software trace preprocessor (WPP) logs for the sensor class extension (CX) trace provider.

WPP provides ways to trace the operation of software components known as trace providers. The following are PDB files included to decode the WPP logs.

-   SensorsCx.pdb

-   SensorsUtilsV2.pdb

The tracelog tool is used to collect WPP logs. For more information, see [Tracelog](https://msdn.microsoft.com/library/windows/hardware/ff552994.aspx). For more information about tracing concepts such as tracing GUIDs, trace flags, trace levels, or PDB files, see [Tracing Tool Concepts](https://msdn.microsoft.com/library/windows/hardware/ff553975.aspx).

## Tracing GUID


The following GUID identifies the trace provider for the CX driver in the sensor V2 stack. For more information about using this GUID with tracelog, see [Tracelog](https://msdn.microsoft.com/library/windows/hardware/ff552994.aspx).

``` syntax
c88b592b-6090-480f-a839-ca2434de5844
```

## Trace flags


The sensor class extension defines the following WPP\_CONTROL\_GUIDS trace flags:

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


The following are WPP macros with their associated trace levels and trace flags. The MSG parameter is a standard format string that is defined for the printf function. Partners can also use the WPP extended format string. For more information about this see the [WPP extended format strings](http://go.microsoft.com/fwlink/p/?linkid=324276) topic on MSD. The newline character is also included in the MSG so “\\n” is not necessary.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Macro</th>
<th>Level</th>
<th>Flag</th>
<th>Parameter</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>TraceFatal</p></td>
<td><p>TRACE_LEVEL_FATAL</p></td>
<td><p>Fatal</p></td>
<td><p>MSG</p></td>
</tr>
<tr class="even">
<td><p>TraceError</p></td>
<td><p>TRACE_LEVEL_ERROR</p></td>
<td><p>Error</p></td>
<td><p>MSG</p></td>
</tr>
<tr class="odd">
<td><p>TraceWarning</p></td>
<td><p>TRACE_LEVEL_WARNING</p></td>
<td><p>Warning</p></td>
<td><p>MSG</p></td>
</tr>
<tr class="even">
<td><p>TraceInformation</p></td>
<td><p>TRACE_LEVEL_INFORMATION</p></td>
<td><p>Information</p></td>
<td><p>MSG</p></td>
</tr>
<tr class="odd">
<td><p>TraceVerbos</p></td>
<td><p>TRACE_LEVEL_VERBOSE</p></td>
<td><p>Verbose</p></td>
<td><p>MSG</p></td>
</tr>
<tr class="even">
<td><p>TracePerformance</p></td>
<td><p>TRACE_LEVEL_PERF</p></td>
<td><p></p></td>
<td><p>Flag, MSG</p></td>
</tr>
<tr class="odd">
<td><p>TraceData</p></td>
<td><p>TRACE_LEVEL_VERBOSE</p></td>
<td><p>DataFlow</p></td>
<td><p>MSG</p></td>
</tr>
<tr class="even">
<td><p>TraceDriverStatus</p></td>
<td><p>TRACE_LEVEL_INFORMATION</p></td>
<td><p>DriverStatus</p></td>
<td><p>MSG</p></td>
</tr>
<tr class="odd">
<td><p>CLX_FunctionEnter</p></td>
<td><p>TRACE_LEVEL_VERBOSE</p></td>
<td><p>EntryExit</p></td>
<td><p>N/A</p></td>
</tr>
<tr class="even">
<td><p>CLX_FunctionExit</p></td>
<td><p>TRACE_LEVEL_VERBOSE</p></td>
<td><p>EntryExit</p></td>
<td><p>NTSTATUS</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_FunctionEnter</p></td>
<td><p>TRACE_LEVEL_VERBOSE</p></td>
<td><p>EntryExit</p></td>
<td><p>N/A</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_FunctionExit</p></td>
<td><p>TRACE_LEVEL_VERBOSE</p></td>
<td><p>EntryExit</p></td>
<td><p>NTSTATUS</p></td>
</tr>
</tbody>
</table>

 

## Decoding ETL logs


The tracefmt tool is used to decode ETL logs. For more information about this tool, see [Tracefmt](http://go.microsoft.com/fwlink/p/?linkid=324212).

If you want to do more extensive testing of your sensor driver, see [Test your universal sensor driver](test-your-universal-sensor-driver.md.

 

 




