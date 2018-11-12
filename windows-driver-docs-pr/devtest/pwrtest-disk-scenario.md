---
title: PwrTest Disk Scenario
description: The PwrTest Disk Scenario monitors disk idle statistics and spin-down events.
ms.assetid: E54AA721-27C6-4E42-B42A-77AC70711A26
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PwrTest Disk Scenario


The PwrTest Disk Scenario monitors disk idle statistics and spin-down events.

This scenario is primarily used for Windows 7 hard disk power activity, subsequent versions of Windows use a different mechanism for tracking disk idle that is not currently supported by Pwrtest. For versions of Windows newer than Windows 7, use the [Windows Performance Toolkit (WPT)](http://go.microsoft.com/fwlink/p/?linkid=294280). The WPT includes the Windows Performance Recorder (WPR) that you can use to trace the kernel-mode power provider and the Windows Performance Analyzer (WPA) that can show the power framework (PoFx) device statistics and can graph the transitions afterward.

**Note**  
This scenario does not work for all types of disks or controllers because not all storage drivers register for idle detection. See [Handling PnP Start in a Storage Class Driver](https://msdn.microsoft.com/library/windows/hardware/ff554995) for more information.

 

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


```
pwrtest /disk  [/t:n] [/?] 
```

<span id="_t_n"></span><span id="_T_N"></span>**/t:**<em>n</em>  
Specifies the total time (in minutes) for the scenario to run (the default value for *n* is 30 minutes).

**Examples**

```
pwrtest /disk /t:60
```

```
pwrtest /disk
```

### <span id="XML_log_file_output"></span><span id="xml_log_file_output"></span><span id="XML_LOG_FILE_OUTPUT"></span>XML log file output

```XML
<PwrTestLog>
  <SystemInformation>
  </SystemInformation>
  <DiskIdleEvents> 
    <DiskIdleChangeEvent>
        <Timestamp></TimeStamp>
        <DiskNumber></DiskNumber>
        <InstancePath></InstancePath>
        <Description></Description>
    </DiskIdleChangeEvent>
    <DiskIdlePolicyChange>
        <Timestamp></TimeStamp>
        <Timeout></Timeout>
        <IgnoreThreshold></IgnoreThreshold>
    </DiskIdlePolicyChange>
    <DiskIdleEvent>
        <Timestamp></TimeStamp>
        <DiskNumber></DiskNumber>
        <InstancePath></InstancePath>
        <Device></Device>
        <Pdo></Pdo>
        <BusyCount></BusyCount>
        <AccruedBusyCount></AccruedBusyCount>
        <IdlePowerState></IdlePowerState>
        <CurrentPowerState></CurrentPowerState>
        <Timeout></Timeout>
        <IgnoreThreshold></IgnoreThreshold>
        <AccruedIdleTime></AccruedIdleTime>
        <AccruedNonIdleTime></AccruedNonIdleTime>
        <Analysis></Analysis>
    </DiskIdleEvent>
  </DiskIdleEvents>
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
<td align="left"><strong>&lt;DiskIdleEvents&gt;</strong></td>
<td align="left"><p>Contains all the different disk idle events. Only one &lt;DeviceIdleEvents&gt; element per PwrTest log file.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Timestamp&gt;</strong></td>
<td align="left"><p>Time stamp of any given event.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;DiskNumber&gt;</strong></td>
<td align="left"><p>Identifies which physical disk is this event for.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;InstancePath&gt;</strong></td>
<td align="left"><p>Device instance path.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;DeviceIdleChangeEvent&gt;</strong></td>
<td align="left"><p>Device add or remove event.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Description&gt;</strong></td>
<td align="left"><p>DeviceRemoved or DeviceDetected.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;DiskIdlePolicyChange&gt;</strong></td>
<td align="left"><p>Disk timeouts change event.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Timeout&gt;</strong></td>
<td align="left"><p>New disk spin-down timeout.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;IgnoreThreshold&gt;</strong></td>
<td align="left"><p>New disk idle ignore threshold.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Device&gt;</strong></td>
<td align="left"><p>Functional device object.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Pdo&gt;</strong></td>
<td align="left"><p>Physical device object</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;BusyCount&gt;</strong></td>
<td align="left"><p>The number of times the device driver called <a href="https://msdn.microsoft.com/library/windows/hardware/ff559755" data-raw-source="[&lt;strong&gt;PoSetDeviceBusy&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559755)"><strong>PoSetDeviceBusy</strong></a> during the period.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;AccruedBusyCount&gt;</strong></td>
<td align="left"><p>The number of times the device driver call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559755" data-raw-source="[&lt;strong&gt;PoSetDeviceBusy&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559755)"><strong>PoSetDeviceBusy</strong></a> total.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;IdlePowerState&gt;</strong></td>
<td align="left"><p>What numeric state is the idle state.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;CurrentPowerState&gt;</strong></td>
<td align="left"><p>The current numeric power state.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Timeout&gt;</strong></td>
<td align="left"><p>Timeout (in seconds).</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;IgnoreThreshold&gt;</strong></td>
<td align="left"><p>The number of seconds of non-idle time to ignore</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;AccruedIdleTime&gt;</strong></td>
<td align="left"><p>The accrued idle time during the period.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;AccruedNonIdleTime&gt;</strong></td>
<td align="left"><p>The total idle time that has accrued.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Analysis&gt;</strong></td>
<td align="left"><p>String that describes what happened during the period.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)

 

 






