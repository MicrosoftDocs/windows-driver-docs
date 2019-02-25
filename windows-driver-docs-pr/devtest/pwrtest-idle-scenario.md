---
title: PwrTest Idle Scenario
description: The PwrTest Idle Scenario monitors user and CPU idle statistics displays idle statistics gathered by kernel every 15 seconds.
ms.assetid: 7E40DD91-D236-41B3-BC3A-DEB6DDD76139
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PwrTest Idle Scenario


The PwrTest Idle Scenario monitors user and CPU idle statistics displays idle statistics gathered by kernel every 15 seconds.

You can combine this scenario with the [PwrTest Execution State Scenario](pwrtest-execution-state-scenario.md) (**/es**) to simultaneously monitor legacy execution state changes, which can help you diagnose why a system is not idling out to sleep.

**Note**  This is a legacy scenario and its recommended replacement is the [PwrTest PPM Scenario](pwrtest-ppm-scenario.md) (**/ppm**) for monitoring CPU idle statistics, and the [PwrTest Monitor Scenario](pwrtest-monitor-scenario.md) (**/monitor**) for monitoring user idle.

 

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


```
pwrtest /idle  [/t:n] [/?] [/es [es_options]
```

<span id="_t_n"></span><span id="_T_N"></span>**/t:**<em>n</em>  
Specifies the total time (in minutes) for the scenario to run (the default value for *n* is 30 minutes).

<span id="_es___es_options_"></span><span id="_ES___ES_OPTIONS_"></span>**/es \[**<em>es\_options</em>**\]**  
Runs the [PwrTest Execution State (ES) Scenario](pwrtest-execution-state-scenario.md).

**Examples**

```
pwrtest /idle /t:60
```

```
pwrtest /idle /es /user
```

```
pwrtest /idle /es /kernel
```

### <span id="XML_log_file_output"></span><span id="xml_log_file_output"></span><span id="XML_LOG_FILE_OUTPUT"></span>XML log file output

```XML
<PwrTestLog>
  <SystemInformation>
  </SystemInformation>
  <PowerIdleStatistics> 
    <IdleStats> 
      <Time></Time>
      <Threshold></Threshold>
      <LowestIdleness></LowestIdleness>
      <AverageIdleness></AverageIdleness>
      <AccruedIdleTime></AccruedIdleTime>
      <NonIdleIgnored></NonIdleIgnored>
      <IdleToSleep></IdleToSleep>
      <NonIdleReferences></NonIdleReferences>
    </IdleStats>
    <EsChange> 
      <Time>XX:XX:XX</Time>
      <Process></Process>
        <RawState></RawState>
        <Continuous></Continuous>
        <System></System>
        <Display></Display>
        <AwayMode></AwayMode>
    </EsChange> 
  </PowerIdleStatistics>
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
<td align="left"><strong>&lt;PowerIdleStatistics&gt;</strong></td>
<td align="left"><p>Contains information related to the idle scenario scenario. Only one <strong>&lt;PowerIdleStatistics&gt;</strong> element can appear in the PwrTest log file.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;IdleStats&gt;</strong></td>
<td align="left"><p>Contains idle statistics of the last idle period.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Time&gt;</strong></td>
<td align="left"><p>Time of most recent idle statistics event.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Threshold&gt;</strong></td>
<td align="left"><p>Idle ignore threshold.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;LowestIdleness&gt;</strong></td>
<td align="left"><p>Lowest idleness percent in the period.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;AverageIdleness&gt;</strong></td>
<td align="left"><p>Average idleness percent in the period.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;AccruedIdleTime&gt;</strong></td>
<td align="left"><p>Accrued idle time during the period.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;NonIdleIgnored&gt;</strong></td>
<td align="left"><p>Non-idle time that was ignored during the period.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;IdleToSleep&gt;</strong></td>
<td align="left"><p>Did the system idle to sleep during the period?</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;NonIdleReferences&gt;</strong></td>
<td align="left"><p>Amount of non-idle ignore references during the period.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;EsChange&gt;</strong></td>
<td align="left"><p>Contains information related a single thread execution state change event. There will be one <strong>&lt;EsChange&gt;</strong> element for each thread execution state change event recorded in the PwrTest log file.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Time&gt;</strong></td>
<td align="left"><p>Indicates the time when the execution state change event occurred.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Process&gt;</strong></td>
<td align="left"><p>Indicates the path to the image file for the process that requested the execution state change.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;RawState&gt;</strong></td>
<td align="left"><p>Indicates the request execution state. This is a 32-bit value of type EXECUTION_STATE (see Windows.h).</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Continuous&gt;</strong></td>
<td align="left"><p>Indicates (TRUE) if the process requested the execution state change to be continuous (ES_CONTINUOUS) or not (FALSE).</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;System&gt;</strong></td>
<td align="left"><p>Indicates (TRUE) if the process requested the system to be available (ES_SYSTEM_REQUIRED) or not (FALSE).</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Display&gt;</strong></td>
<td align="left"><p>Indicates (TRUE) if the process requested the display to be available (ES_DISPLAY_REQUIRED) or not (FALSE).</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;AwayMode&gt;</strong></td>
<td align="left"><p>Indicates (TRUE) if the process requested away mode to be enabled (ES_AWAYMODE_REQUIRED) or not (FALSE).</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)

 

 






