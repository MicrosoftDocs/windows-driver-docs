---
title: Enabling and Viewing WDTF Traces
description: Enabling and Viewing WDTF Traces
ms.assetid: 9bed6042-3691-4a5e-a143-51acf746b1ae
keywords:
- Windows Device Testing Framework WDK , tracing events
- WDTF WDK , tracing events
- tracing WDK WDTF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling and Viewing WDTF Traces


WDTF *Tracing* refers to reporting events that occur internally within WDTF objects. Because WDTF is heavily instrumented, all WDTF objects provide tracing information as they run. WDTF handles tracing by using [WPP Software Tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204). This type of tracing is a standardized format that you can read by using WDK tools, including [TraceView](https://msdn.microsoft.com/library/windows/hardware/ff556063). This topic covers how to use [Logman](http://go.microsoft.com/fwlink/p/?linkid=136332) and [Tracefmt](https://msdn.microsoft.com/library/windows/hardware/ff552974) to view WDTF run-time traces. This topic also discusses how you can programmatically configure WDTF trace levels.

-   [How to collect and save WDTF traces](#how-to-collect)
-   [How to view WDTF traces](#how-to-view)
-   [Programmatically configuring WDTF trace levels](#wdtf-enable-level)

### <a href="" id="how-to-collect"></a>How to collect and save WDTF Traces

**To start collecting WDTF traces**

1.  On the test computer, open a Command Prompt window with elevated privileges (**Run as administrator**) and enter the following commands:

    ``` syntax
    logman.exe create trace "autosession\WDTF" -p {6210f559-c7f7-4d2f-b674-4bc9315cecc7} 0xffffffff 0xff -o c:\WDTF_Traces\TraceFile.etl
    reg add HKLM\SYSTEM\CurrentControlSet\Control\WMI\Autologger\WDTF /v LogFileMode /t REG_DWORD /d 1 /f
    reg add HKLM\SYSTEM\CurrentControlSet\Control\WMI\Autologger\WDTF /v FileMax /t REG_DWORD /d 16 /f
    reg add HKLM\SYSTEM\CurrentControlSet\Control\WMI\Autologger\WDTF /v MaxFileSize /t REG_DWORD /d 0 /f
    ```

2.  Reboot the computer.

See [Logman](http://go.microsoft.com/fwlink/p/?linkid=136332) (Logman.exe) for information about other options. For information about creating a trace season, see [Configuring and Starting an AutoLogger Session](https://msdn.microsoft.com/library/windows/desktop/aa363687).

**To stop collecting WDTF traces and save log files**

1.  You can stop collecting WDTF traces and delete the data collector with the following commands:

    ``` syntax
    logman.exe -stop -ets WDTF
    logman.exe delete "autosession\WDTF"
    ```

2.  Reboot the computer.
3.  Copy the log files from the test computer to another computer for later analysis.

    The ETL log files collected can be very large in size. For best results, copy the log files from the test computer (for example, c:\\WDTF\_Traces\\TraceFile.etl) to another computer. Then you can delete the log files from the test computer.

### <a href="" id="how-to-view"></a>How to view WDTF traces

Viewing WDTF traces requires formatting the ETL files. The following steps show how to use [Tracefmt.exe](https://msdn.microsoft.com/library/windows/hardware/ff552974) to convert the ETL files to text or CSV files.

**To view WDTF Traces**

1.  For example, the following command converts the ETL file that has been saved as c:\\WDTF\_Traces\\TraceFile.etl to text.

    ``` syntax
    Tracefmt.exe –r http://msdl.microsoft.com/download/symbols c:\WDTF_Traces\TraceFile.etl -o OutputTxtFile.txt
    ```

2.  The following command converts the ETL file that has been saved as c:\\WDTF\_Traces\\TraceFile.etl to comma separated file (CSV).

    ``` syntax
    Tracefmt.exe –r http://msdl.microsoft.com/download/symbols c:\WDTF_Traces\TraceFile.etl -csv –o OutputCsvFile.csv
    ```

3.  Open the CSV files in Microsoft Excel so you can use filtering features of Excel to filter the collected traces. You can filter the traces for certain time periods. You can filter the traces to examine traces logged by certain WDTF components.

## Programmatically configuring WDTF trace levels


All WDTF objects provide tracing information as they run.

WDTF provides a set of configurable [**TTraceLevel**](https://msdn.microsoft.com/library/windows/hardware/ff539616) levels. For information on how to set the **TTraceLevel** of a specific object instance at run-time, see the [**ITracing::SetTraceLevel**](https://msdn.microsoft.com/library/windows/hardware/ff539522) method.

For information on how to set the default [**TTraceLevel**](https://msdn.microsoft.com/library/windows/hardware/ff539616) for an interface, see the [Windows Device Testing Framework Reference](https://msdn.microsoft.com/library/windows/hardware/ff539647).

For a detailed description of the types of traces included in each [**TTraceLevel**](https://msdn.microsoft.com/library/windows/hardware/ff539616), see the [**ITracer**](https://msdn.microsoft.com/library/windows/hardware/ff539512) interface. You can globally configure these levels yourself using the **ITracer**'s registry TraceLevel Path.

The following table describes the trace levels that you can set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Level</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>Off. No tracing is provided.</p></td>
</tr>
<tr class="even">
<td><p>1</p></td>
<td><p>Low</p></td>
</tr>
<tr class="odd">
<td><p>2</p></td>
<td><p>Medium. This level is the default level of tracing.</p></td>
</tr>
<tr class="even">
<td><p>3</p></td>
<td><p>High</p></td>
</tr>
<tr class="odd">
<td><p>4</p></td>
<td><p>Full. All tracing information is reported.</p></td>
</tr>
<tr class="even">
<td><p>5-8</p></td>
<td><p>Custom levels.</p></td>
</tr>
<tr class="odd">
<td><p>9</p></td>
<td><p>Sets the object back to its initial trace level.</p></td>
</tr>
</tbody>
</table>

 

When you are debugging by using trace content, consider setting the trace levels to 1 for all objects and then setting trace levels much higher for the objects that you are examining.

For more information about trace levels, see the [**ITracer**](https://msdn.microsoft.com/library/windows/hardware/ff539512) interface.

## Related topics
[Configuring and Starting an AutoLogger Session](https://msdn.microsoft.com/library/windows/desktop/aa363687)  
[Logman](http://go.microsoft.com/fwlink/p/?linkid=136332)  
[Tracefmt](https://msdn.microsoft.com/library/windows/hardware/ff552974)  
[TraceView](https://msdn.microsoft.com/library/windows/hardware/ff556063)  
[WPP Software Tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204)  



