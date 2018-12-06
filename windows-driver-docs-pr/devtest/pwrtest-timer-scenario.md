---
title: PwrTest Timer Scenario
description: The PwrTest Timer Scenario logs system timer resolution changes as they happen.
ms.assetid: 842A827F-8046-4A31-938B-B1EA2119421A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PwrTest Timer Scenario


The PwrTest Timer Scenario logs system timer resolution changes as they happen.

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


```
pwrtest /timer /?  [/t:n]  [/?] 
```

<span id="_t_n"></span><span id="_T_N"></span>**/t:**<em>n</em>  
Specifies the total time (in minutes) for the scenario to run (the default value for *n* is 30 minutes).

**Examples**

```
  pwrtest /timer
```

```
pwrtest /timer /t:5
```

### <span id="XML_log_file_output"></span><span id="xml_log_file_output"></span><span id="XML_LOG_FILE_OUTPUT"></span>XML log file output

```XML
<PwrTestLog>
  <SystemInformation>
  </SystemInformation>
  <TimerEvents> 
    <TimerResolutionRundown>
      <Timestamp></Timestamp>
      <CurrentResolution></CurrentResolution>
      <MinimumResolution></MinimumResolution>
      <MaximumResolution></MaximumResolution>
      <KernelCount></KernelCount>
      <KernelResolution></KernelResolution>
    </TimerResolutionRundown>
    <TimerResolutionRequestRundown>
        <Timestamp></Timestamp>
        <AppName></AppName>
        <Resolution></Resolution>
        <ProcessID></ProcessID>
    </TimerResolutionRequestRundown>
    <NtSetTimerResolution>
      <Timestamp></Timestamp>
      <AppName></AppName>
      <ServiceName></ServiceName>
      <Resolution></Resolution>
      <ProcessID></ProcessID>
    </NtSetTimerResolution>
    <UpdateTimerResolution>
      <Timestamp></Timestamp>
      <Resolution></Resolution>
    </UpdateTimerResolution>
    <ExSetTimerResolution>
      <Timestamp></Timestamp>
      <Resolution></Resolution>
    </ExSetTimerResolution>  
  </TimerEvents>
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
<td align="left"><strong>&lt;TimerEvents&gt;</strong></td>
<td align="left"><p>Contains all the different timer events. Only one <strong>&lt;TimerEvents&gt;</strong> element can appear in a PwrTest log file.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Timestamp&gt;</strong></td>
<td align="left"><p>Time stamp of any given event.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;TimerResolutionRundown&gt;</strong></td>
<td align="left"><p>Event to show current timer resolution statistics. Only one of these events will be logged.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;CurrentResolution&gt;</strong></td>
<td align="left"><p>Current resolution in milliseconds.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;MinimumResolution&gt;</strong></td>
<td align="left"><p>Minimum resolution.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;MaximumResolution&gt;</strong></td>
<td align="left"><p>Maximum resolution.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;KernelCount&gt;</strong></td>
<td align="left"><p>Number of resolution requests from kernel mode.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;KernelResolution&gt;</strong></td>
<td align="left"><p>Current kernel timer resolution.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;TimerResolutionRequestRundown&gt;</strong></td>
<td align="left"><p>Events to show current resolution requests. Multiple events may be logged.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;AppName&gt;</strong></td>
<td align="left"><p>Process name of requester.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Resolution&gt;</strong></td>
<td align="left"><p>Resolution of request in milliseconds.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ProcessID&gt;</strong></td>
<td align="left"><p>Process ID of requester.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;NtSetTimerResolution&gt;</strong></td>
<td align="left"><p>Event indicates a process made a timer resolution request.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ServiceName&gt;</strong></td>
<td align="left"><p>Service name of requester if applicable.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;UpdateTimerResolution&gt;</strong></td>
<td align="left"><p>Event indicates the system updated the timer resolution.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ExSetTimerResolution&gt;</strong></td>
<td align="left"><p>Event indicates a kernel component made a timer resolution request.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)

 

 






