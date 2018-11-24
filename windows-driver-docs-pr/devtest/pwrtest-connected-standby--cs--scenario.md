---
title: PwrTest Connected Standby Scenario
description: The PwrTest Connected Standby Scenario (/cs) facilitates automated testing of connected standby transitions.
ms.assetid: 2601603D-F9AF-4DEB-9A1B-F5A091A51B2B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PwrTest Connected Standby Scenario


The PwrTest Connected Standby Scenario (**/cs**) facilitates automated testing of connected standby transitions.

PwrTest logs the progress through the PDC phases and attempts to log platform idle transition counts if they are supported by the system. This is useful for diagnosing if a system is entering deep platform idle states, and if any software components are blocking the transition.

This scenario requires the test system to support the *Always on Always connected* (AoAc) power capability (most SoC and ARM systems support this). This scenario also requires the power button driver that is part of Windows Driver Testing Framework (WDTF). WDTF (and the included power button driver) is automatically installed when you provision a system for testing using Visual Studio and the WDK. For more information, see[Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/library/windows/hardware/dn745909), or [Provision a computer for driver deployment and testing (WDK 8)](https://msdn.microsoft.com/library/windows/hardware/hh698272). For information about WDTF, see [**Windows Device Testing Framework (WDTF) (Windows Drivers)**](https://msdn.microsoft.com/library/windows/hardware/ff539547).

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


```
pwrtest /cs [/c:n] [/d:n] [/p:n][/?] 
```

<span id="_c_n"></span><span id="_C_N"></span>**/c:**<em>n</em>  
Specifies the number of cycles (1 is default) to run.

<span id="_d_n"></span><span id="_D_N"></span>**/d:**<em>n</em>  
Specifies the delay time (in seconds) between connected standby transitions (60 seconds is the default).

<span id="_p_n"></span><span id="_P_N"></span>**/p:**<em>n</em>  
Specifies the connected standby exit time (in seconds; 60 seconds is the default).

**Examples**

```
pwrtest /cs /c:4 
```

```
pwrtest /cs /c:4 /p:120 /d:150
```

### <span id="XML_log_file_output"></span><span id="xml_log_file_output"></span><span id="XML_LOG_FILE_OUTPUT"></span>XML log file output

```XML
<PwrTestLog>
  <SystemInformation>
  </SystemInformation>
  <CSTransitions>
    <EnteringCS Timestamp="XX/XX/XXXX:XX:XX:XX.XXX"/>
    <InputDisabled Timestamp="XX/XX/XXXX:XX:XX:XX.XXX"/>
    <PhaseEnter name="name" Timestamp="XX/XX/XXXX:XX:XX:XX.XXX"/>
    <PhaseExit name="name" Timestamp="XX/XX/XXXX:XX:XX:XX.XXX"/>
    <ExitingCS Timestamp="XX/XX/XXXX:XX:XX:XX.XXX"/> || 
        <AbortingCS Timestamp="XX/XX/XXXX:XX:XX:XX.XXX"/>
    <InputEnabled Timestamp="XX/XX/XXXX:XX:XX:XX.XXX"/>
    <ExitedCS Timestamp="XX/XX/XXXX:XX:XX:XX.XXX"/> || 
        <AbortedCS Timestamp="XX/XX/XXXX:XX:XX:XX.XXX"/>
    <ExecutionRequiredSet Caller="c:\folder\process.exe" 
        Timestamp="XX/XX/XXXX:XX:XX:XX.XXX"/> ||
        <ExecutionRequiredCleared Caller="c:\folder\process.exe" 
            Timestamp="XX/XX/XXXX:XX:XX:XX.XXX"/>
    <PlatformIdleStats StateCount="X" Timestamp="XX/XX/XXXX:XX:XX:XX.XXX">
        <State Index="X" SuccessCount="X" FailureCount="X" CancelCount="X"/>
    </PlatformIdleStats>
  </CSTransitions>
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
<td align="left"><strong>&lt;CSTransitions&gt;</strong></td>
<td align="left"><p>Contains all the different connected standby events. There can be only one <strong>&lt;CSTransitions&gt;</strong> element in the PwrTest log file.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Timestamp&gt;</strong></td>
<td align="left"><p>Time stamp of any given event.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;TemperatureScale&gt;</strong></td>
<td align="left"><p>Temperature scale (Kelvin/Celcius/Fahrenheit&gt; of any given event.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ThermalZoneDeviceInstance&gt;</strong></td>
<td align="left"><p>Device instance name of thermal zone of any given event.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;_TMP&gt;</strong></td>
<td align="left"><p>Current temperature of the system in any given event.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;_PSV&gt;, &lt;_TCx&gt;, &lt;_TSP&gt;, &lt;_ACx&gt;, &lt;_HOT&gt;, &lt;_CRT&gt;, etc.</strong></td>
<td align="left"><p>System temperature thresholds sent with a given event.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;PassiveCooling&gt;</strong></td>
<td align="left"><p>Event indicates system is now in a passive cooling zone.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ActiveCooling&gt;</strong></td>
<td align="left"><p>Event indicates system is now in an active cooling zone.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Hot&gt;</strong></td>
<td align="left"><p>Event indicates system has hit a hot trip point.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Critical&gt;</strong></td>
<td align="left"><p>Event indicates system has hit a critical trip point.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;ActiveCoolingDevicePower&gt;</strong></td>
<td align="left"><p>Event indicates an active cooling device has turned on.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;FanDeviceInstance&gt;</strong></td>
<td align="left"><p>Device instance name of the fan.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;PowerState&gt;</strong></td>
<td align="left"><p>The On (1) or Off (0) power state.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ActiveCoolingLevel&gt;</strong></td>
<td align="left"><p>Numeric level of active cooling.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;ActiveCoolingDeviceIndex&gt;</strong></td>
<td align="left"><p>Numeric index of cooling device.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)

 

 






