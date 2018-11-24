---
title: PwrTest Requests Scenario
description: The PwrTest Requests Scenario logs power requests from processes and services running in the system as they happen.
ms.assetid: 4B082680-5C43-45F6-9A0E-0C23E9B1F282
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PwrTest Requests Scenario


The PwrTest Requests Scenario logs power requests from processes and services running in the system as they happen.

You can use the PwrTest Requests Scenario to diagnose why a computer doesn't go to sleep or why the monitor stays on.

You could also use the administrator tool [PowerCfg](http://go.microsoft.com/fwlink/p/?linkid=294568) (powercfg.exe) for this purpose (**powercfg.exe /requests**). PowerCfg is included with Windows (Windows\\System32 directory). However, Powercfg.exe only captures the power requests that are active at the time you run the tool. In contrast, the PwrTest Requests Scenario runs for a specified time and logs power requests as they are created and closed, so the requests don’t need to be active when the tool is run.

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


```
pwrtest /requests [/t:n] [/?] 
```

<span id="_t_n"></span><span id="_T_N"></span>**/t:**<em>n</em>  
Specifies the total time (in minutes) for the scenario to run (the default value for *n* is 30 minutes).

**Examples**

```
pwrtest /requests  
```

```
pwrtest /requests  /t:60
```

### <span id="XML_log_file_output"></span><span id="xml_log_file_output"></span><span id="XML_LOG_FILE_OUTPUT"></span>XML log file output

```XML
<PwrTestLog>
  <SystemInformation>
  </SystemInformation>
  <PowerRequests> 
    <CreatePowerRequestEvent>
        <Timestamp></TimeStamp>
        <Caller></Caller>
        <Context></Context>
        <RequestObject></RequestObject>
        <Type></Type>
        <ProcessID></ProcessID>
        <SessionID></SessionID>
        <Legacy></Legacy>
        <SystemAllowed></SystemAllowed>
        <DisplayAllowed></DisplayAllowed>
        <AwayModeAllowed></AwayModeAllowed>
        <PerfBoostAllowed></PerfBoostAllowed>
        <ExecutionRequiredAllowed></ExecutionRequiredAllowed>    
        <SystemCount></SystemCount>
        <DisplayCount></DisplayCount>
        <AwayModeCount></AwayModeCount>
        <PerfBoostCount></PerfBoostCount>
        <ExecutionRequiredCount></ExecutionRequiredCount>
    </CreatePowerRequestEvent>
    <ChangePowerRequestEvent>
        <Timestamp></TimeStamp>
        <Caller></Caller>
        <RequestObject></RequestObject>
        <SystemCount></SystemCount>
        <DisplayCount></DisplayCount>
        <AwayModeCount></AwayModeCount>
        <PerfBoostCount></PerfBoostCount>
        <ExecutionRequiredCount></ExecutionRequiredCount>
    </ChangePowerRequestEvent>
    <ClosePowerRequestEvent>
        <Timestamp></TimeStamp>
        <Caller></Caller>
        <RequestObject></RequestObject>
    </ClosePowerRequestEvent>
  </PowerRequests>
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
<td align="left"><strong>&lt;PowerRequests&gt;</strong></td>
<td align="left"><p>Contains all the different power request events. There can be only one <strong>&lt;PowerRequests&gt;</strong> element in a PwrTest log file.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Timestamp&gt;</strong></td>
<td align="left"><p>Time stamp of any given event.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Caller&gt;</strong></td>
<td align="left"><p>Name of the requester.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Context&gt;</strong></td>
<td align="left"><p>Device instance path if applicable</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;RequestObject&gt;</strong></td>
<td align="left"><p>Request object for the event.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Type&gt;</strong></td>
<td align="left"><p>Numeric type of caller.</p>
<p>0 = driver</p>
<p>1 = process</p>
<p>2 = shared service</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;ProcessID&gt;</strong></td>
<td align="left"><p>Process ID of caller.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;SessionID&gt;</strong></td>
<td align="left"><p>Session ID of caller if process.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Legacy&gt;</strong></td>
<td align="left"><p>Reports True or False if the caller used legacy <a href="https://msdn.microsoft.com/library/windows/desktop/aa373208" data-raw-source="[&lt;strong&gt;SetThreadExecutionState function (Windows)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa373208)"><strong>SetThreadExecutionState function (Windows)</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff559768" data-raw-source="[&lt;strong&gt;PoSetSystemState&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559768)"><strong>PoSetSystemState</strong></a> APIs or the newer <a href="https://msdn.microsoft.com/library/windows/desktop/dd405534" data-raw-source="[&lt;strong&gt;PowerSetRequest function (Windows)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/dd405534)"><strong>PowerSetRequest function (Windows)</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff559762" data-raw-source="[&lt;strong&gt;PoSetPowerRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559762)"><strong>PoSetPowerRequest</strong></a> APIs.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;SystemAllowed&gt;</strong></td>
<td align="left"><p>Reports whether system requests are allowed for this caller.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;DisplayAllowed&gt;</strong></td>
<td align="left"><p>Reports whether display requests are allowed for this caller.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;AwayModeAllowed&gt;</strong></td>
<td align="left"><p>Reports whether away mode requests are allowed for this caller.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;PerfBoostAllowed&gt;</strong></td>
<td align="left"><p>Reports whether performance boost requests are allowed for this caller.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ExecutionRequiredAllowed&gt;</strong></td>
<td align="left"><p>Reports whether execution required requests are allowed for this caller.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;SystemCount&gt;</strong></td>
<td align="left"><p>Number of system requests for this caller.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;DisplayCount&gt;</strong></td>
<td align="left"><p>Number of display requests for this caller.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;AwayModeCount&gt;</strong></td>
<td align="left"><p>Number of away mode requests for this caller.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;PerfBoostCount&gt;</strong></td>
<td align="left"><p>Number of performance boost requests for this caller.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;ExecutionRequiredCount&gt;</strong></td>
<td align="left"><p>Number of execution required requests for this caller.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;CreatePowerRequestEvent&gt;</strong></td>
<td align="left"><p>Caller has created a new request.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;ChangePowerRequestEvent&gt;</strong></td>
<td align="left"><p>Caller has changed the request count.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ClosePowerRequestEvent&gt;</strong></td>
<td align="left"><p>Caller has closed the request.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)

[PowerCfg](http://go.microsoft.com/fwlink/p/?linkid=294568)

 

 






