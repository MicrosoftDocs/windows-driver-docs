---
title: PwrTest PPM Scenario
description: The PwrTest PPM Scenario logs processor power management (PPM) information and periodic statistics totals.
ms.assetid: 735834dc-7351-44d1-a63f-9cb541184fde
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PwrTest PPM Scenario


The PwrTest PPM Scenario logs processor power management (PPM) information and periodic statistics totals.

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


```
pwrtest /ppm [/n:n] [/i:n] [/c:[y|n]] [/p:{y|n}] [/u:{y|n}] [/live] [/t:n] [/?] 
```

<span id="_n_n"></span><span id="_N_N"></span>**/n:**<em>n</em>  
Specifies the number of cycles (100 is the default). Press **q** to quit).

<span id="_i_n"></span><span id="_I_N"></span>**/i:**<em>n</em>  
Specifies the polling interval in milliseconds (ms) for C-state and processor utilization (5000 ms is default).

<span id="_c_yn"></span><span id="_C_YN"></span>**/c:**{**y**|**n**}  
Specifies the whether C-state information should be captured. The options are yes (**y**) or no (**n**). The default is yes (**y**).

<span id="_p_yn"></span><span id="_P_YN"></span>**/p:**{**y**|**n**}  
Specifies whether performance or throttle state information should be captured. The options are yes (**y**) or no (**n**). Yes (**y**) is the default.

<span id="_u_yn"></span><span id="_U_YN"></span>**/u:**{**y**|**n**}  
Specifies whether CPU utilization information should be captured. The options are yes (**y**) or no (**n**). Yes (**y**) is the default.

<span id="_live"></span><span id="_LIVE"></span>**/live**  
Displays processor power management events in real-time (other options are not available).

<span id="_t_n"></span><span id="_T_N"></span>**/t:**<em>n</em>  
Specifies the indicates the total runtime, in minutes, for the **/live** option (default is 30).

**Examples**

```
pwrtest /ppm /c:y /p:y /u:y /n:60 /i:1000
```

```
  pwrtest /ppm /c:n /p:n /u:y /n:3600 /i:1000
```

```
  pwrtest /ppm /live
```

```
  pwrtest /ppm /live /t:60
```

### <span id="XML_log_file_output"></span><span id="xml_log_file_output"></span><span id="XML_LOG_FILE_OUTPUT"></span>XML log file output

```XML
<PwrTestLog>
  <SystemInformation>
  </SystemInformation>
  <PPMScenario> 
    <ProcessorInformation> 
      <PerformanceStates> 
        <PerformanceState  
            number="0" 
            frequency="" 
            percentofmaxfrequency="" 
            type="" /> 
      </PerformanceStates> 
      <ProcessorName> </ProcessorName> 
      <InterfaceType> </InterfaceType> 
      <TransitionLatency units=""></TransitionLatency> 
    </ProcessorInformation> 
    <ProcessorTraces interval=""> 
      <Trace> 
        <CpuId></CpuId> 
        <ElapsedT></ElapsedT> 
        <CPUIdle></CPUIdle> 
        <PState></PState> 
        <Frequency></Frequency> 
        <PercentOfMax></PercentOfMax> 
        <PStateType></PStateType> 
        <COne></COne> 
        <CTwo></COne> 
        <CThree></CThree> 
      </Trace> 
    </ProcessorTraces> 
  </PPMScenario> 
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
<td align="left"><strong>&lt;PPMScenario&gt;</strong></td>
<td align="left"><p>Contains information related to the PPM scenario. There is only one <strong>&lt;SleepScenario&gt;</strong> element in a PwrTest log file.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ProcessorInformation&gt;</strong></td>
<td align="left"><p>Contains information related to the static attributes of the processor, such as performance and throttle state capabilities.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;PerformanceStates&gt;</strong></td>
<td align="left"><p>Contains a list of <strong>&lt;PerformanceState&gt;</strong> elements.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ProcessorName&gt;</strong></td>
<td align="left"><p>Indicates the friendly name of the processor.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;InterfaceType&gt;</strong></td>
<td align="left"><p>Indicates the mechanism used to interface between Windows and platform processor power management features.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;TransitionLatency&gt;</strong></td>
<td align="left"><p>Indicates the latency when switching performance states. Includes an units attribute, typically microseconds (µs)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;ProcessorTraces&gt;</strong></td>
<td align="left"><p>Contains a list of <strong>&lt;Trace&gt;</strong> elements. Includes an interval attribute indicating the interval of each <strong>&lt;Trace&gt;</strong> element.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Trace&gt;</strong></td>
<td align="left"><p>Contains trace information, which will vary depending on the command options you use with PwrTest.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;CpuId&gt;</strong></td>
<td align="left"><p>Identifies the processor.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ElapsedT&gt;</strong></td>
<td align="left"><p>Indicates the elapsed time since the start of PwrTest in milliseconds.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;CPUIdle&gt;</strong></td>
<td align="left"><p>Indicates the percentage of processor idle time.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;PState&gt;</strong></td>
<td align="left"><p>Indicates the current processor performance state.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Frequency&gt;</strong></td>
<td align="left"><p>Indicates the actual frequency of the current processor performance state in Megahertz.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;PercentOfMax&gt;</strong></td>
<td align="left"><p>Indicates the percentage of maximum frequency for the current performance state.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;PStateType&gt;</strong></td>
<td align="left"><p>Indicates whether the performance state is a performance state (1) or a throttle state (0).</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;COne&gt;</strong></td>
<td align="left"><p>Indicates the percentage of CPU idle time spent in the C1 CPU idle state.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;CTwo&gt;</strong></td>
<td align="left"><p>Indicates the percentage of CPU idle time spent in the C2 CPU idle state.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;CThree&gt;</strong></td>
<td align="left"><p>Indicates the percentage of CPU idle time spent in the C3 CPU idle state.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)

 

 






