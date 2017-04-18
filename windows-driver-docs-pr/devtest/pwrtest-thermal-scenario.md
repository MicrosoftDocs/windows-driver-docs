---
title: PwrTest Thermal Scenario
description: The PwrTest Thermal Scenario monitors ACPI thermal zone information and statistics. This scenario is only supported on systems that report thermal zones and temperature changes.
ms.assetid: C6941A50-EA0F-4C46-A290-8CAAD292E156
---

# PwrTest Thermal Scenario


The PwrTest Thermal Scenario monitors ACPI thermal zone information and statistics. This scenario is only supported on systems that report thermal zones and temperature changes.

**Note**  This scenario only works on systems that report thermal data to the operating system.

 

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


``` syntax
pwrtest /thermal [/t:n] [/?] 
```

<span id="_t_n"></span><span id="_T_N"></span>**/t:***n*  
Specifies the total time (in minutes) for the scenario to run (the default value for *n* is 30 minutes).

<span id="_temp_kcf"></span><span id="_TEMP_KCF"></span>**/temp:**{**k**|**c**|**f**}  
Specifies the temperature scale Kelvin (**k**), Celsius (**c**), Fahrenheit (**f**) to use for all output and logging (default is Kelvin).

**Examples**

``` syntax
pwrtest /thermal  
```

``` syntax
pwrtest /thermal  /t:30
```

``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PwrTest%20Thermal%20Scenario%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





