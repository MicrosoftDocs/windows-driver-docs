---
title: PwrTest Sleep Scenario
description: The PwrTest Sleep Scenario facilitates automated testing of sleep and resume transitions.
ms.assetid: 2003ff3e-bc29-4741-a0a6-371948982679
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PwrTest Sleep Scenario


The PwrTest Sleep Scenario facilitates automated testing of sleep and resume transitions.

PwrTest is capable of directing the platform into one or more sleep states in an automated fashion and logging sleep state performance information such as the BIOS initialization and total resume times.

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


```
pwrtest /sleep [/c:n] [/d:n] [/p:n] [/h:{y|n}] [/s:{1|3|4|all|rnd|hibernate|standby}] [/unattend] [/e:n] [/?] 
```

<span id="_c_n"></span><span id="_C_N"></span>**/c:**<em>n</em>  
Specifies the number of cycles (1 is the default) to run.

<span id="_d_n"></span><span id="_D_N"></span>**/d:**<em>n</em>  
Specifies the delay time in seconds (90 is the default).

<span id="_p_n"></span><span id="_P_N"></span>**/p:**<em>n</em>  
Specifies the sleep time in seconds (60 is default). If wake timer isn't supported for hibernate, the system will restart and immediately resume after writing the hibernation file) .

<span id="_h_yn"></span><span id="_H_YN"></span>**/h:**{**y**|**n**}  
Specifies whether hybrid sleep should be enabled (y) or disabled (n). The default is system policy.

<span id="_s_134allrndhibernatestandby"></span><span id="_S_134ALLRNDHIBERNATESTANDBY"></span>**/s:**{**1**|**3**|**4**|**all**|**rnd**|**hibernate**|**standby**}  

<span id="1"></span>**1**  
Specifies that the target state is always S1.

<span id="3"></span>**3**  
Specifies that the target state is always S3.

<span id="4"></span>**4**  
Specifies that the target state is always S4.

<span id="all"></span><span id="ALL"></span>**all**  
Specifies cycling through all supported power states in order.

<span id="rnd"></span><span id="RND"></span>**rnd**  
Specifies cycling through all supported power states randomly.

<span id="hibernate"></span><span id="HIBERNATE"></span>**hibernate**  
Specifies target state is always hibernate (S4).

<span id="standby"></span><span id="STANDBY"></span>**standby**  
Specifies target state is any available Standby state (S1 or S3).

<span id="_unattend____"></span><span id="_UNATTEND____"></span>**/unattend**   
Specifies not to change system execution state after wakeup.

<span id="_e_n"></span><span id="_E_N"></span>**/e:**<em>n</em>  
Specifies the timeout in seconds to wait for the transition end event (120 seconds is the default) .

**Examples**

```
pwrtest pwrtest /sleep /c:4 /s:all 
```

```
  pwrtest /sleep /c:4 /p:120 /d:150 /s:all
```

### <span id="XML_log_file_output"></span><span id="xml_log_file_output"></span><span id="XML_LOG_FILE_OUTPUT"></span>XML log file output

```XML
<PwrTestLog>
  <SystemInformation>
  </SystemInformation>
  <SleepScenario> 
    <SleepTransitions 
            critical="" 
            hybrid="" 
            delay="" 
            sleeptime=""> 
            <SleepTransition 
                  number="" 
                  status=""> 
                  <StartT></StartT> 
                  <EndT></EndT> 
                  <Duration></Duration> 
                  <TargetState></TargetState> 
                  <EffectiveState></EffectiveState> 
                  <BIOSInit></BIOSInit> 
                  <DriverInit></DriverInit> 
                  <Suspend></Suspend> 
                  <Resume></Resume> 
                  <HiberRead></HiberRead> 
                  <HiberWrite></HiberWrite> 
            </SleepTransition> 
            <SleepTransition 
                  number="" 
                  status=""> 
                  <StartT></StartT> 
                  <EndT></EndT> 
                  <Duration></Duration> 
                  <TargetState></TargetState> 
                  <EffectiveState></EffectiveState> 
                  <BIOSInit></BIOSInit> 
                  <DriverInit></DriverInit> 
                  <Suspend></Suspend> 
                  <Resume></Resume> 
                  <HiberRead></HiberRead> 
                  <HiberWrite></HiberWrite> 
            </SleepTransition> 
    </SleepTransitions> 
  </SleepScenario> 
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
<td align="left"><strong>&lt;SleepScenario&gt;</strong></td>
<td align="left"><p>Contains information related to the sleep scenario. There is only one <strong>&lt;SleepScenario&gt;</strong> element in a PwrTest log file.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;SleepTransitions&gt;</strong></td>
<td align="left"><p>Provides overall data about the sleep transition cycles such as the state of critical and hybrid sleep features.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;SleepTransition&gt;</strong></td>
<td align="left"><p>Provides per-sleep cycle information such as the start and end times, as well as details about the resume time, such as the BIOS initialization time. A <strong>&lt;SleepTransition&gt;</strong> element is generated for each sleep transition cycle.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;StartT&gt;</strong></td>
<td align="left"><p>Indicates the start time of the sleep cycle. (<em>hh</em>:<em>mm</em>:<em>ss</em>)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;EndT&gt;</strong></td>
<td align="left"><p>Indicates the end time of the sleep cycle. (<em>hh</em>:<em>mm</em>:<em>ss</em>)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Duration&gt;</strong></td>
<td align="left"><p>Indicates the duration of the sleep cycle. (<em>hh</em>:<em>mm</em>:<em>ss</em>)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;TargetState&gt;</strong></td>
<td align="left"><p>Indicates the target sleep state.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;EffectiveState&gt;</strong></td>
<td align="left"><p>Indicates the effective sleep state.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;BIOSInit&gt;</strong></td>
<td align="left"><p>Indicates the amount of time required to initialize the BIOS (TargetState must be 3) on resume in milliseconds.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;DriverInit&gt;</strong></td>
<td align="left"><p>Indicates the amount of time required to initialize drivers on resume in milliseconds.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Suspend&gt;</strong></td>
<td align="left"><p>Indicates the amount of time required to suspend the system in milliseconds.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Resume&gt;</strong></td>
<td align="left"><p>Indicates the total amount of time required to resume the system in milliseconds.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;HiberRead&gt;</strong></td>
<td align="left"><p>Indicates the time required to read the hibernation file in milliseconds. (TargetState must be 4)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;HiberWrite&gt;</strong></td>
<td align="left"><p>Indicates the time required to write the hibernation file in milliseconds. (EffectiveState must be 4)</p></td>
</tr>
</tbody>
</table>



## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)










