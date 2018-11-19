---
title: PwrTest Monitor Scenario
description: The PwrTest Monitor Scenario logs user idle statistics related to monitor or display auto-dimming and blanking.
ms.assetid: 8B45C85A-01E8-4256-82F3-097871CB9021
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PwrTest Monitor Scenario


The PwrTest Monitor Scenario logs user idle statistics related to monitor or display auto-dimming and blanking.

When you run the PwrTest Monitor Scenario, you might want to also run the [PwrTest Requests Scenario](pwrtest-requests-scenario.md) (**/requests**) scenario in another window. The PwrTest Requests Scenario might help to understand why the monitor might still be on or the system still awake, even though the user has been idle long enough for the idle timers to expire.

If you run both scenarios, be sure to use the **/ln:**<em>name</em> parameter so that you can change the log file and ETW trace session names. The names need to be different to avoid a conflict between the two instances of the tool.

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


```
pwrtest /monitor  [/t:n] [/?] 
```

<span id="_t_n"></span><span id="_T_N"></span>**/t:**<em>n</em>  
Specifies the total time (in minutes) for the scenario to run (the default value for *n* is 30 minutes).

**Examples**

```
pwrtest /device 
```

```
pwrtest /device /t:60
```

### <span id="XML_log_file_output"></span><span id="xml_log_file_output"></span><span id="XML_LOG_FILE_OUTPUT"></span>XML log file output

```XML
<PwrTestLog>
  <SystemInformation>
  </SystemInformation>
  <MonitorPower> 
    <PhysicalMonitorBrightnessEvent>
        <Timestamp></TimeStamp>
        <PhysicalMonitorBrightnessPercent></PhysicalMonitorBrightnessPercent>
    </PhysicalMonitorBrightnessEvent>
    <MonitorIdleStatusEvent>
        <Timestamp></TimeStamp>
        <SessionId></SessionId>
        <AccruedIdleTimeMs></AccruedIdleTimeMs>
    </MonitorIdleStatusEvent>
    <MonitorTimeoutsChangeEvent>
        <Timestamp></TimeStamp>
        <SessionId></SessionId>
        <DisplayTimeoutValueMs></DisplayTimeoutValueMs>
        <ScreenSaverTimeoutValueMs></ScreenSaverTimeoutValueMs>
        <DimTimeoutValueMs></DimTimeoutValueMs>
        <DimBrightnessValue></DimBrightnessValue>
        <NormalBrightnessValue></NormalBrightnessValue>
    </MonitorTimeoutsChangeEvent>
    <MonitorIdleActionExpireEvent>
        <Timestamp></TimeStamp>
        <SessionId></SessionId>
        <IsConsoleSession></IsConsoleSession>
        <IdleAction></IdleAction>
        <IdleStartTime></IdleStartTime>
        <TimeoutValueMs></TimeoutValueMs>
    </MonitorIdleActionExpireEvent>
    <MonitorPowerEvent>
        <Timestamp></TimeStamp>
        <SessionId></SessionId>
        <IsConsoleSession></IsConsoleSession>
        <NewState></NewState>
        <PreviousState></PreviousState>
        <PreviousStateTime></PreviousStateTime>
    </MonitorPowerEvent>
    <MonitorAdaptiveDimTimeoutEvent>
        <Timestamp></TimeStamp>
        <Timeout></Timeout>
    </MonitorAdaptiveDimTimeoutEvent>
  </MonitorPower>
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
<td align="left"><strong>&lt;MonitorPower&gt;</strong></td>
<td align="left"><p>Contains all the different monitor power events. There can be only one <strong>&lt;MonitorPower&gt;</strong> element in a PwrTest log file.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Timestamp&gt;</strong></td>
<td align="left"><p>Time stamp of any given event.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;SessionId&gt;</strong></td>
<td align="left"><p>The name of the user session the event is for.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;IsConsoleSession&gt;</strong></td>
<td align="left"><p>Shows whether the physical console session is attached to the physical monitor .</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;PhysicalMonitorBrightnessEvent&gt;</strong></td>
<td align="left"><p>Event indicates the current monitor brightness.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;MonitorIdleStatusEvent&gt;</strong></td>
<td align="left"><p>Event indicates the user is idle.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;AccruedIdleTimeMs&gt;</strong></td>
<td align="left"><p>Accrued user idle time in milliseconds.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;MonitorTimeoutsChangeEvent&gt;</strong></td>
<td align="left"><p>Event indicates the current idle timeouts.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;DisplayTimeoutValueMs&gt;</strong></td>
<td align="left"><p>Displays blank timeout value in milliseconds.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ScreenSaverTimeoutValueMs&gt;</strong></td>
<td align="left"><p>Screen saver timeout value in milliseconds.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;DimTimeoutValueMs&gt;</strong></td>
<td align="left"><p>Displays the dim timeout value in milliseconds</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;DimBrightnessValue&gt;</strong></td>
<td align="left"><p>Brightness to use when in the dim state.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;NormalBrightnessValue&gt;</strong></td>
<td align="left"><p>Brightness to use when in on state.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;MonitorIdleActionExpireEvent&gt;</strong></td>
<td align="left"><p>Event indicates an idle timeout was hit and an action was taken.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;IdleAction&gt;</strong></td>
<td align="left"><p>Describes the action that was taken (screen saver start, console locked, monitor dim, monitor blank).</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;IdleStartTime&gt;</strong></td>
<td align="left"><p>Start time of this idle state.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;TimeoutValueMs&gt;</strong></td>
<td align="left"><p>Timeout value of this idle state in milliseconds.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;MonitorPowerEvent&gt;</strong></td>
<td align="left"><p>Event indicates a display idle timeout was hit and an action was taken.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;NewState&gt;</strong></td>
<td align="left"><p>New state of the monitor (on/dim/off).</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;PreviousState&gt;</strong></td>
<td align="left"><p>Previous state of the monitor (on/dim/off).</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;PreviousStateTime&gt;</strong></td>
<td align="left"><p>Time that was spent in the previous state.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;MonitorAdaptiveDimTimeoutEvent&gt;</strong></td>
<td align="left"><p>Event indicates the adaptive dim timeout has changed.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Timeout&gt;</strong></td>
<td align="left"><p>New timeout value in seconds.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)

 

 






