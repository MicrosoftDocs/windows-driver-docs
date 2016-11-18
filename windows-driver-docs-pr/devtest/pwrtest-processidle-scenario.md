---
title: PwrTest ProcessIdle Scenario
description: The PwrTest ProcessIdle Scenario forces background maintenance tasks to run (now rather than at their scheduled time) and monitors their progress.
ms.assetid: 14932191-C956-4623-AF62-5A6650D72164
---

# PwrTest ProcessIdle Scenario


The PwrTest ProcessIdle Scenario forces background maintenance tasks to run (now rather than at their scheduled time) and monitors their progress.

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


``` syntax
pwrtest /processidle [/t:n] [/?] 
```

<span id="_t_n"></span><span id="_T_N"></span>**/t:***n*  
Specifies the maximum time (in minutes) for the scenario to run, after which the wait is aborted, even if idle tasks are continuing to run (default is to run until all tasks are completed).

**Examples**

``` syntax
pwrtest /processidle  
```

``` syntax
pwrtest /processidle  /t:30
```

### <span id="XML_log_file_output"></span><span id="xml_log_file_output"></span><span id="XML_LOG_FILE_OUTPUT"></span>XML log file output

```XML
<PwrTestLog>
  <SystemInformation>
  </SystemInformation>
  <ProcessIdle> 
    <JobStart>
      <Timestamp></Timestamp>
      <TaskName></TaskName>
    </JobStart>
    <JobEndSuccess>
      <Timestamp></Timestamp>
      <TaskName></TaskName>
    </JobEndSuccess>
    <JobEndFailure>
      <Timestamp></Timestamp>
      <TaskName></TaskName>
    </JobEndFailure>
    <JobEndTermination>
      <Timestamp></Timestamp>
      <TaskName></TaskName>
    </JobEndTermination>
    <JobCompletionPending>
      <Timestamp></Timestamp>
      <TaskName></TaskName>
    </JobCompletionPending>
    <IdleTaskRegister>
      <Timestamp></Timestamp>
      <TaskName></TaskName>
      <ProcessId></ProcessId>
    </IdleTaskRegister>
    <IdleTaskUnregister>
      <Timestamp></Timestamp>
      <TaskName></TaskName>
      <ProcessId></ProcessId>
    </IdleTaskUnregister>
    <IdleTaskStart>
      <Timestamp></Timestamp>
      <TaskName></TaskName>
      <ProcessId></ProcessId>
    </IdleTaskStart>
    <IdleTaskStop>
      <Timestamp></Timestamp>
      <TaskName></TaskName>
      <ProcessId></ProcessId>
    </IdleTaskStop>
    <IdleTaskNotifyStart>
      <Timestamp></Timestamp>
      <TaskName></TaskName>
      <ProcessId></ProcessId>
    </IdleTaskNotifyStart>
    <IdleTaskNotifyComplete>
      <Timestamp></Timestamp>
      <TaskName></TaskName>
      <ProcessId></ProcessId>
    </IdleTaskNotifyComplete>
    <OtherProcessIdleTasksCallsInProgress>
      <Timestamp></Timestamp>
    </OtherProcessIdleTasksCallsInProgress>
  </ProcessIdle>
</PwrTestLog> 
```

The following table describes the XML elements that appear in the log file.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Element</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>&lt;ProcessIdle&gt;</strong></td>
<td align="left"><p>Contains all the different process idle events. Only one <strong>&lt;ProcessIdle&gt;</strong> element in a PwrTest log file.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Timestamp&gt;</strong></td>
<td align="left"><p>Time stamp of any given event.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;TaskName&gt;</strong></td>
<td align="left"><p>Name of idle task.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ProcessID&gt;</strong></td>
<td align="left"><p>Process ID of idle task.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;JobStart&gt;</strong></td>
<td align="left"><p>Event indicates a job started.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;JobEndSuccess&gt;</strong></td>
<td align="left"><p>Event indicates a job finished successfully.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;JobEndFailure&gt;</strong></td>
<td align="left"><p>Event indicates a job failed.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;JobEndTermination&gt;</strong></td>
<td align="left"><p>Event indicates a job was terminated early.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;JobCompletionPending&gt;</strong></td>
<td align="left"><p>Event indicates a job completion is still pending.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;IdleTaskRegister&gt;</strong></td>
<td align="left"><p>Event indicates an idle task was registered.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;IdleTaskUnregister&gt;</strong></td>
<td align="left"><p>Event indicates an idle task was unregistered.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;IdleTaskStart&gt;</strong></td>
<td align="left"><p>Event indicates an idle task started.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;IdleTaskStop&gt;</strong></td>
<td align="left"><p>Event indicates an idle task has stopped.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;IdleTaskNotifyStart&gt;</strong></td>
<td align="left"><p>Event indicates a process has invoked idle tasks.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;IdleTaskNotifyComplete&gt;</strong></td>
<td align="left"><p>Event indicates a process is finished invoking idle tasks.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;OtherProcessIdleTasksCallsInProgress&gt;</strong></td>
<td align="left"><p>Event indicates another process called the <strong>ProcessIdleTasks</strong> function in the background. Note that Pwrtest calls the <strong>ProcessIdleTasks</strong> function that is exported by advapi32.dll.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PwrTest%20ProcessIdle%20Scenario%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





