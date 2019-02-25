---
title: PwrTest Execution State Scenario
description: The PwrTest Execution State Scenario (/es) monitors thread execution state changes of the currently running processes and services.
ms.assetid: 5470c99b-5780-486f-b36a-922fb821b7f3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PwrTest Execution State Scenario


The PwrTest Execution State Scenario (**/es**) monitors thread execution state changes of the currently running processes and services.

**Note**  
This PwrTest Execution State Scenario is primarily used for applications that use legacy power request APIs, such as [**SetThreadExecutionState function (Windows)**](https://msdn.microsoft.com/library/windows/desktop/aa373208)). To monitor applications that use newer power request APIs, such as [**PowerSetRequest function (Windows)**](https://msdn.microsoft.com/library/windows/desktop/dd405534) use the [PwrTest Requests Scenario](pwrtest-requests-scenario.md) instead.

 

Applications and services may temporarily override power management settings such as the monitor and sleep idle timeouts by changing their thread execution state. The PwrTest Execution State Scenario monitors thread execution state and system state changes that applications and services have made using the Win32 [**SetThreadExecutionState function (Windows)**](https://msdn.microsoft.com/library/windows/desktop/aa373208).

You can use the **/es** scenario together with [PwrTest Idle Scenario](pwrtest-idle-scenario.md) to help identify the applications and services that are preventing the monitor or system from going idle.

### <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax

```
pwrtest /es  [/t:n] [/stes:{y|n}] [/rss:{y|n}] [/sss:{y|n}] [/all] [/user] [/kernel] [/idle] [/?] 
```

<span id="_t_n"></span><span id="_T_N"></span>**/t:**<em>n</em>  
Specifies the total time (in minutes) for the scenario to run (the default value for *n* is 30 minutes).

<span id="_stes_yn"></span><span id="_STES_YN"></span>**/stes:**{**y**|**n**}  
Specifies whether [**SetThreadExecutionState**](https://msdn.microsoft.com/library/windows/desktop/aa373208) events should be logged (**y** (yes) is the default).

<span id="_rss_yn"></span><span id="_RSS_YN"></span>**/rss:**{**y**|**n**}  
Specifies whether **RegisterSystemState** events should be logged (**y** (yes) is the default).

<span id="_sss_yn"></span><span id="_SSS_YN"></span>**/sss:**{**y**|**n**}  
Specifies whether **SetSystemState** events should be logged (**y** (yes) is the default).

<span id="_all"></span><span id="_ALL"></span>**/all**  
Specifies that all events should be logged ([**SetThreadExecutionState**](https://msdn.microsoft.com/library/windows/desktop/aa373208), **RegisterSystemState**, **SetSystemState**).

<span id="_user"></span><span id="_USER"></span>**/user**  
Specifies that all user events should be logged ([**SetThreadExecutionState**](https://msdn.microsoft.com/library/windows/desktop/aa373208)).

<span id="_kernel"></span><span id="_KERNEL"></span>**/kernel**  
Specifies that only kernel-mode events should be logged (**RegisterSystemState**, **SetSystemState**).

<span id="_idle"></span><span id="_IDLE"></span>**/idle**  
Log idle statistics.

**Examples**

```
pwrtest /es /all
```

```
pwrtest /es /user
```

```
pwrtest /es /kernel
```

```
pwrtest /es /kernel /sss:n
```

```
pwrtest /es /kernel /rss:n
```

```
pwrtest /es /kernel /rss:y /sss:n
```

```
pwrtest /es /sss:n
```

```
pwrtest /es /rss:n /sss:n
```

```
pwrtest /es /stes:n 
```

```
pwrtest /es /all /idle 
```

### <span id="XML_log_file_output"></span><span id="xml_log_file_output"></span><span id="XML_LOG_FILE_OUTPUT"></span>XML log file output

```XML
<PwrTestLog>
  <SystemInformation>
  </SystemInformation>
  <ExecutionState> 
    <EsChange> 
      <Time>XX:XX:XX</Time>
      <Process></Process>
        <RawState></RawState>
        <Continuous></Continuous>
        <System></System>
        <Display></Display>
        <AwayMode></AwayMode>
    </EsChange> 
    <EsChange> 
      <Time>XX:XX:XX</Time>
      <Process></Process>
        <RawState></RawState>
        <Continuous></Continuous>
        <System></System>
        <Display></Display>
        <AwayMode></AwayMode>
    </EsChange> 
  </ExecutionState>
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
<td align="left"><strong>&lt;ExecutionState&gt;</strong></td>
<td align="left"><p>Contains information related to the execution state scenario. There can be only one <strong>&lt;ExecutionState&gt;</strong> element in a PwrTest log file.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;EsChange&gt;</strong></td>
<td align="left"><p>Contains information related a single thread execution state change event. There will be one <strong>&lt;EsChange&gt;</strong> element.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Time&gt;</strong></td>
<td align="left"><p>Indicates the time when the execution state change event occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Process&gt;</strong></td>
<td align="left"><p>Indicates the path to the image file for the process that requested the execution state change.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;RawState&gt;</strong></td>
<td align="left"><p>Indicates the request execution state. This is a 32-bit value of type EXECUTION_STATE (see Windows.h).</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Continuous&gt;</strong></td>
<td align="left"><p>Indicates if the process requested the execution state change to be continuous (ES_CONTINUOUS).</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;System&gt;</strong></td>
<td align="left"><p>Indicates (TRUE) if the process requested the system to be available (ES_SYSTEM_REQUIRED) or not (FALSE).</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Display&gt;</strong></td>
<td align="left"><p>Indicates (TRUE) if the process requested the display to be available (ES_DISPLAY_REQUIRED) or not (FALSE).</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;AwayMode&gt;</strong></td>
<td align="left"><p>Indicates (TRUE) if the process requested away mode to be enabled (ES_AWAYMODE_REQUIRED) or not (FALSE).</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)

 

 






