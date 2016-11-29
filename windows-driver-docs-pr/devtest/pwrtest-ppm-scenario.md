---
title: PwrTest PPM Scenario
description: The PwrTest PPM Scenario logs processor power management (PPM) information and periodic statistics totals.
ms.assetid: 735834dc-7351-44d1-a63f-9cb541184fde
---

# PwrTest PPM Scenario


The PwrTest PPM Scenario logs processor power management (PPM) information and periodic statistics totals.

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


``` syntax
pwrtest /ppm [/n:n] [/i:n] [/c:[y|n]] [/p:{y|n}] [/u:{y|n}] [/live] [/t:n] [/?] 
```

<span id="_n_n"></span><span id="_N_N"></span>**/n:***n*  
Specifies the number of cycles (100 is the default). Press **q** to quit).

<span id="_i_n"></span><span id="_I_N"></span>**/i:***n*  
Specifies the polling interval in milliseconds (ms) for C-state and processor utilization (5000 ms is default).

<span id="_c_yn"></span><span id="_C_YN"></span>**/c:**{**y**|**n**}  
Specifies the whether C-state information should be captured. The options are yes (**y**) or no (**n**). The default is yes (**y**).

<span id="_p_yn"></span><span id="_P_YN"></span>**/p:**{**y**|**n**}  
Specifies whether performance or throttle state information should be captured. The options are yes (**y**) or no (**n**). Yes (**y**) is the default.

<span id="_u_yn"></span><span id="_U_YN"></span>**/u:**{**y**|**n**}  
Specifies whether CPU utilization information should be captured. The options are yes (**y**) or no (**n**). Yes (**y**) is the default.

<span id="_live"></span><span id="_LIVE"></span>**/live**  
Displays processor power management events in real-time (other options are not available).

<span id="_t_n"></span><span id="_T_N"></span>**/t:***n*  
Specifies the indicates the total runtime, in minutes, for the **/live** option (default is 30).

**Examples**

``` syntax
pwrtest /ppm /c:y /p:y /u:y /n:60 /i:1000
```

``` syntax
  pwrtest /ppm /c:n /p:n /u:y /n:3600 /i:1000
```

``` syntax
  pwrtest /ppm /live
```

``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PwrTest%20PPM%20Scenario%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





