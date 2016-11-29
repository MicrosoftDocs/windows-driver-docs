---
title: PwrTest Device Scenario
description: The PwrTest Device Scenario monitors device idle statistics.
ms.assetid: 75C53B6E-3D1F-4E9D-A99E-3060A9CC37BC
---

# PwrTest Device Scenario


The PwrTest Device Scenario monitors device idle statistics.

This scenario is primarily used for Windows 7 device power activity, subsequent versions of Windows use a different mechanism for tracking device idle that is not currently supported by Pwrtest. For versions of Windows newer than Windows 7, use the [Windows Performance Toolkit (WPT)](http://go.microsoft.com/fwlink/p/?linkid=294280). The WPT includes the Windows Performance Recorder (WPR) that you can use to trace the kernel-mode power provider and the Windows Performance Analyzer (WPA) that can show the power framework (PoFx) device statistics and can graph the transitions afterward.

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


``` syntax
pwrtest /device  [/t:n] [/?] 
```

<span id="_t_n"></span><span id="_T_N"></span>**/t:***n*  
Specifies the total time (in minutes) for the scenario to run (the default value for *n* is 30 minutes).

**Examples**

``` syntax
pwrtest /device /t:60
```

``` syntax
pwrtest /device
```

### <span id="XML_log_file_output"></span><span id="xml_log_file_output"></span><span id="XML_LOG_FILE_OUTPUT"></span>XML log file output

```XML
<PwrTestLog>
  <SystemInformation>
  </SystemInformation>
  <DeviceIdleEvents> 
    <DeviceIdleChangeEvent>
        <Timestamp></TimeStamp>
        <InstancePath></InstancePath>
        <Description></Description>
    </DeviceIdleChangeEvent>
    <DeviceIdleEvent>
        <Timestamp></TimeStamp>
        <InstancePath></InstancePath>
        <Device></Device>
        <Pdo></Pdo>
        <ConservationTimeout></ConservationTimeout>
        <PerformanceTimeout></PerformanceTimeout>
        <AccruedIdleTime></AccruedIdleTime>
        <BusyCount></BusyCount>
        <AccruedBusyCount></AccruedBusyCount>
        <IdlePowerState></IdlePowerState>
        <CurrentPowerState></CurrentPowerState>
        <Analysis></Analysis>
    </DeviceIdleEvent>
  </DeviceIdleEvents>
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
<td align="left"><strong>&lt;DeviceIdleEvents&gt;</strong></td>
<td align="left"><p>Contains all the different device idle events. Only one <strong>&lt;DeviceIdleEvents</strong> element per PwrTest log file.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Timestamp&gt;</strong></td>
<td align="left"><p>Time stamp of any given event.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;InstancePath&gt;</strong></td>
<td align="left"><p>Device instance path.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;DeviceIdleChangeEvent&gt;</strong></td>
<td align="left"><p>Device add or remove event.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Description&gt;</strong></td>
<td align="left"><p>DeviceRemoved or DeviceDetected.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;DeviceIdleEvent&gt;</strong></td>
<td align="left"><p>Device idle statistics event.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Device&gt;</strong></td>
<td align="left"><p>Functional device object.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Pdo&gt;</strong></td>
<td align="left"><p>Physical device object</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;ConservationTimeout&gt;</strong></td>
<td align="left"><p>Conservative timeout (usually used on DC power).</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;PerformanceTimeout&gt;</strong></td>
<td align="left"><p>Performance timeout (usually used on AC power).</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;AccruedIdleTime&gt;</strong></td>
<td align="left"><p>The idle time accrued during the period.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;BusyCount&gt;</strong></td>
<td align="left"><p>The number of times the device driver called [<strong>PoSetDeviceBusy</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559755) during the period.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;AccruedBusyCount&gt;</strong></td>
<td align="left"><p>The total number of times the device driver called [<strong>PoSetDeviceBusy</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559755).</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;IdlePowerState&gt;</strong></td>
<td align="left"><p>Shows which numeric state is the idle state.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;CurrentPowerState&gt;</strong></td>
<td align="left"><p>The current numeric power state.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Analysis&gt;</strong></td>
<td align="left"><p>String that describes what happened during the period.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PwrTest%20Device%20Scenario%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





