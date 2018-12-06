---
title: Example 15 Measuring DPC/ISR Time
description: Example 15 Measuring DPC/ISR Time
ms.assetid: 47936b8b-fd04-44dc-9cd9-77e9d89b4499
keywords:
- deferred procedure calls WDK software tracing
- DPCs WDK software tracing
- interrupt service routines WDK software tracing
- ISRs WDK software tracing
- time WDK software tracing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example 15: Measuring DPC/ISR Time


## <span id="ddk_measuring_dpc_isr_time_tools"></span><span id="DDK_MEASURING_DPC_ISR_TIME_TOOLS"></span>


You can measure the amount of time that a driver spends in deferred procedure calls (DPCs) and interrupt service routines (ISRs) by tracing these events in the Windows kernel. This information will help you to minimize the time the driver spends at higher IRQLs, making the driver and the system more efficient.

Microsoft recommends that DPCs should not run longer than 100 microseconds and ISRs should not run longer than 25 microseconds. For the most recent requirements, see the [Hardware Certification Program]( http://go.microsoft.com/fwlink/p/?linkid=227016).

The procedure that is described in this section includes the following steps:

1.  Start kernel tracing of DPC/ISR events.

2.  Monitor the trace session for events lost and, if necessary, increase the size of the trace buffers.

3.  Exercise the test driver.

4.  Stop the trace session.

5.  Use Tracerpt to generate a report that summarizes DPC/ISR activity.

6.  Analyze the reports

### <span id="step_1__start_a_trace_session_"></span><span id="STEP_1__START_A_TRACE_SESSION_"></span>Step 1: Start a trace session.

The following command starts an NT Kernel Logger trace session:

```
tracelog -start -f test01.etl -dpcisr -UsePerfCounter -b 64
```

The **tracelog -start** command starts the trace session. Because "NT Kernel Logger" is the default session name, you do not need to specify it, and you cannot use the **-guid** parameter to specify a provider file. The command uses the **-f** parameter to indicate a log session and to direct the trace messages to the *test01.etl* event trace log file.

The command includes the **-dpcisr** parameter to enable tracing of DPCs, ISRs, context switches, and image loading.

When tracing DPCs and ISRs, always add the **-UsePerfCounter** parameter to the command. The system timer resolution is too low to measure the time spent in these activities. Also, Tracerpt, the tool that formats DPC/ISR events, requires the performance counter clock values for its reports. (Tracerpt is included in Windows XP and later versions of Windows.)

Finally, the command uses the **-b** parameter to increase the size of the trace buffers to 64 KB. Because DPC/ISR tracing generates a high volume of trace messages at a rapid rate, it is important to increase the size of the trace buffers so that you do not lose events.

In response to this command, Tracelog starts the NT Kernel Logger session and displays its properties.

```
Logger Started...
Operation Status:       0L      The operation completed successfully.

Logger Name:            NT Kernel Logger
Logger Id:              ffff
Logger Thread Id:       00000C18
Buffer Size:            64 Kb
Maximum Buffers:        25
Minimum Buffers:        3
Number of Buffers:      5
Free Buffers:           4
Buffers Written:        14
Events Lost:            0
Log Buffers Lost:       0
Real Time Buffers Lost: 0
AgeLimit:               15
Log File Mode:          Sequential
Enabled tracing:        Process Thread Disk File ImageLoad
Log Filename:           c:\Tracelog\test01.etl
```

Note that DPC, ISR, and context switch events do not appear in the **Enabled tracing** field of the display. Because these events are monitored by internal instrumentation, they do not appear in this list even when they are enabled. However, image load events, which are also enabled by the **-dpcisr** parameter, do appear.

### <span id="step_2__check_for_lost_events_"></span><span id="STEP_2__CHECK_FOR_LOST_EVENTS_"></span>Step 2: Check for lost events.

Use a **tracelog -q** (query) command periodically to check for lost events. If you find them, use a **tracelog -update** command to add more buffers to the trace session.

```
tracelog -q
```

The **tracelog -q** command takes a session name, but it isn't necessary to supply one in this case because "NT Kernel Logger" is the default.

In response to this command, Tracelog displays the properties of the session.

```
Operation Status:       0L      The operation completed successfully.

Logger Name:            NT Kernel Logger
Logger Id:              ffff
Logger Thread Id:       00000BC4
Buffer Size:            64 Kb
Maximum Buffers:        25
Minimum Buffers:        3
Number of Buffers:      25
Free Buffers:           23
Buffers Written:        571
Events Lost:            544
Log Buffers Lost:       0
Real Time Buffers Lost: 0
AgeLimit:               15
Log File Mode:          Sequential
Enabled tracing:        Process Thread Disk File ImageLoad
Log Filename:           c:\Tracelog\test.etl
```

In this case, 544 events that were generated were not saved in a buffer. To prevent this from recurring, use a **tracelog -update** command to increase the size of each buffer (**-b**) or to increase the maximum number of buffers (**-max**), for example:

```
tracelog -update -b 128 -max 40
```

### <span id="step_3__exercise_the_driver_"></span><span id="STEP_3__EXERCISE_THE_DRIVER_"></span>Step 3: Exercise the driver.

Use your test routines to make the driver perform its functions. Consider running two tests, one for basic functions and one for more advanced functions.

### <span id="step_4__stop_the_trace_session_"></span><span id="STEP_4__STOP_THE_TRACE_SESSION_"></span>Step 4: Stop the trace session.

Use the following command to stop the trace session:

```
tracelog -stop
```

A **tracelog -stop** command usually requires a session name, but because "NT Kernel Logger" is the default, the session name is not required.

### <span id="step_5__create_a_dpc_isr_report_"></span><span id="STEP_5__CREATE_A_DPC_ISR_REPORT_"></span>Step 5: Create a DPC/ISR report.

To summarize the DPC/ISR messages in the event trace log, use the version of Tracerpt included in Windows XP with SP2 and later versions of Windows.

The following Tracerpt command formats the messages in the *Test01.etl* file and creates an text-formatted report of the activity in Windows XP with SP2.

```
tracerpt test01.etl -report dpcisr.txt -df
```

In this command, the **-report** parameter specifies the method of analysis and the name of the output file. The **-df** parameter is required to format the messages correctly only in Windows XP with SP2.

When creating this report in Windows Server 2003 with SP1 and later versions of Windows, you can create an HTML-formatted report by using the following command.

```
tracerpt test01.etl -report dpcisr.html -f HTML
```

In this command, the **-report** parameter specifies the name of the output file and the **-f** parameter specifies the report format.

### <span id="step_6__analyze_the_report_"></span><span id="STEP_6__ANALYZE_THE_REPORT_"></span>Step 6: Analyze the report.

The "Windows Event Trace Session Report" has the following sections:

-   **Image Statistics.** Displays data about the processes running on the computer during the trace.

-   **Disk Totals.** Displays data about disk I/O for each process running during the trace.

-   **DPC processor utilization for the whole trace:** Displays the percentage of processor time spent servicing DPC routines for each driver.

-   **Distribution of all DPC execution times for the whole trace**. A table of time ranges in microsecond units. The table displays the percentage of DPC routines that fall into each time range.

-   **Distribution of DriverName ( DPCRoutineAddress ) DPC execution times for the whole trace.** A table of time ranges in microsecond units. The table displays the percentage of instances of this DPC routine that fall into each time range. A section like this one appears for every DPC routine in the trace.

-   **ISR processor utilization for the whole trace.** Displays the percentage of processor time spent servicing interrupt service routines for each driver in the trace.

-   **Distribution of all ISR execution times for the whole trace.** A table of time ranges in microsecond units. The table displays the percentage of ISR routines that fall into each time range.

-   **Distribution of DriverName ( ISRAddress ) ISR execution times for the whole trace.** A table of time ranges in microsecond units. The table displays the percentage of instances of the ISR that fall into each time range. A section like this one appears for every ISR in the trace.

-   **Distribution of DPC and ISR processor utilization for TracingPeriodInMs two microsecond time windows.** Displays the combined processor utilization by DPCs and ISRs during the trace.

-   **Distribution of DriverName ( ISRAddress ) ISR to DriverName ( DPCRoutineAddress ) DPC latencies for the whole trace.** Displays the distribution of delay intervals between the end of an ISR and the beginning of the associated DPC.

The following excerpt from a sample report shows the distribution of DPC execution times for Ipsec.sys. In general, DPC routines lasting more than 100 microseconds are discouraged. The report shows that more than half of the DPC routines for this driver exceed the threshold.

```
+------------------------------------------------------------------------------+
| Distribution of ipsec.sys (F7AA7449) DPC execution times for the whole trace |
+------------------------------------------------------------------------------+
| Lower Bound         Upper Bound            Count             Percent         |
+------------------------------------------------------------------------------+
|           0                   1                0                0.00%        |
|           1                   2                0                0.00%        |
|           2                   3                8               42.11%        |
|           3                   4                1                5.26%        |
|           4                   5                0                0.00%        |
|           5                  10                0                0.00%        |
|          10                  25                0                0.00%        |
|          25                  50                0                0.00%        |
|          50                 100                0                0.00%        |
|         100                 250               10               52.63%        |
+------------------------------------------------------------------------------+
|                                               19              100.00%        |
+------------------------------------------------------------------------------+
```

 

 





