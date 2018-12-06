---
title: PwrTest Thermal Scenario
description: The PwrTest Thermal Scenario monitors ACPI thermal zone information and statistics.
ms.assetid: C6941A50-EA0F-4C46-A290-8CAAD292E156
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PwrTest Thermal Scenario


The PwrTest Thermal Scenario monitors ACPI thermal zone information and statistics. This scenario is only supported on systems that report thermal zones and temperature changes.

**Note**  This scenario only works on systems that report thermal data to the operating system.

 

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


```
pwrtest /thermal [/t:n] [/?] 
```

<span id="_t_n"></span><span id="_T_N"></span>**/t:**<em>n</em>  
Specifies the total time (in minutes) for the scenario to run (the default value for *n* is 30 minutes).

<span id="_temp_kcf"></span><span id="_TEMP_KCF"></span>**/temp:**{**k**|**c**|**f**}  
Specifies the temperature scale Kelvin (**k**), Celsius (**c**), Fahrenheit (**f**) to use for all output and logging (default is Kelvin).

**Examples**

```
pwrtest /thermal  
```

```
pwrtest /thermal  /t:30
```

```
pwrtest /thermal  /t:30 /temp:f
```

### <span id="XML_log_file_output"></span><span id="xml_log_file_output"></span><span id="XML_LOG_FILE_OUTPUT"></span>XML log file output

```XML
<PwrTestLog>
  <SystemInformation>
  </SystemInformation>
  <ThermalEvents> 
    <PassiveCooling>
        <Timestamp></TimeStamp>
        <TemperatureScale></TemperatureScale>
        <ThermalZoneDeviceInstance></ThermalZoneDeviceInstance>
        <_TMP></_TMP>
        <_PSV></_PSV>
        <_TC1></_TC1>
        <_TC2></_TC2>
        <_TSP></_TSP>
    </PassiveCooling>
    <ActiveCooling>
        <Timestamp></TimeStamp>
        <TemperatureScale></TemperatureScale>
        <ThermalZoneDeviceInstance></ThermalZoneDeviceInstance>
        <_TMP></_TMP>
        <_AC0></_AC0>
        <_AC1></_AC1>
        <_AC2></_AC2>
        <_AC3></_AC3>
        <_AC4></_AC4>
        <_AC5></_AC5>
        <_AC6></_AC6>
        <_AC7></_AC7>
        <_AC8></_AC8>
        <_AC9></_AC9>
    </ActiveCooling>
    <Hot>
        <Timestamp></TimeStamp>
        <TemperatureScale></TemperatureScale>
        <ThermalZoneDeviceInstance></ThermalZoneDeviceInstance>
        <_HOT></_HOT>
    </Hot>
    <Critical>
        <Timestamp></TimeStamp>
        <TemperatureScale></TemperatureScale>
        <ThermalZoneDeviceInstance></ThermalZoneDeviceInstance>
        <_CRT></_CRT>
    </Critical>
    <ActiveCoolingDevicePower>
        <Timestamp></TimeStamp>
        <TemperatureScale></TemperatureScale>
        <ThermalZoneDeviceInstance></ThermalZoneDeviceInstance>
        <FanDeviceInstance></FanDeviceInstance>
        <PowerState></PowerState>
        <ActiveCoolingLevel></ActiveCoolingLevel>
        <ActiveCoolingDeviceIndex></ActiveCoolingDeviceIndex>
    </ActiveCoolingDevicePower>
  </ThermalEvents>
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
<td align="left"><strong>&lt;ThermalEvents&gt;</strong></td>
<td align="left"><p>Contains all the different thermal events. There can be only one <strong>&lt;ThermalEvents&gt;</strong> element in the PwrTest log file.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;EnteringCS&gt;</strong></td>
<td align="left"><p>Connected Standby (CS) entry started, the system is in CS as soon as the display goes off and input is disabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;ExitingCS&gt;</strong></td>
<td align="left"><p>CS exit started.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ExitedCS&gt;</strong></td>
<td align="left"><p>CS exit completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;AbortingCS&gt;</strong></td>
<td align="left"><p>CS entry aborting and exiting before entering deepest phase.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;AbortedCS&gt;</strong></td>
<td align="left"><p>CS exit completed after aborted entry.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;InputDisabled&gt;</strong></td>
<td align="left"><p>User input was disabled on the local console.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;InputEnabled&gt;</strong></td>
<td align="left"><p>User input was enabled on the local console.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;PhaseEnter&gt;</strong></td>
<td align="left"><p>CS phase entered, name attribute is the name of the CS phase.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;PhaseExit&gt;</strong></td>
<td align="left"><p>CS phase exited, name attribute is the name of the CS phase.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;ExecutionRequiredSet&gt;</strong></td>
<td align="left"><p>A process made an execution required request which will block DAM phase completion.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ExecutionRequiredCleared&gt;</strong></td>
<td align="left"><p>A process cleared an execution required request which will unblock DAM phase completion.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;PlatformIdleStats&gt;</strong></td>
<td align="left"><p>Platform idle statistics block.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;State&gt;</strong></td>
<td align="left"><p>Transition counts for a platform idle state since the previous platform idle statistics block.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)

[PowerCfg](http://go.microsoft.com/fwlink/p/?linkid=294568)

 

 






