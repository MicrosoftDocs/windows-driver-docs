---
title: PwrTest ProcessIdle Scenario
description: The PwrTest ProcessIdle Scenario forces background maintenance tasks to run (now rather than at their scheduled time) and monitors their progress.
ms.assetid: 14932191-C956-4623-AF62-5A6650D72164
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PwrTest ProcessIdle Scenario


The PwrTest ProcessIdle Scenario forces background maintenance tasks to run (now rather than at their scheduled time) and monitors their progress.

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


```
pwrtest /processidle [/t:n] [/?] 
```

<span id="_t_n"></span><span id="_T_N"></span>**/t:**<em>n</em>  
Specifies the maximum time (in minutes) for the scenario to run, after which the wait is aborted, even if idle tasks are continuing to run (default is to run until all tasks are completed).

**Examples**

```
pwrtest /processidle  
```

```
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

 

 






