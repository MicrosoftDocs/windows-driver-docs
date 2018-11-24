---
title: PwrTest Battery Scenario
description: The PwrTest Battery Scenario is designed to facilitate automated inspection of battery and power source information.
ms.assetid: e0bad871-a826-4951-9a84-93c9b1aa0653
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PwrTest Battery Scenario


The PwrTest Battery Scenario is designed to facilitate automated inspection of battery and power source information.

PwrTest is capable of logging battery capacity, voltage, rate of drain, and general state for as many batteries as are in the system. Battery data is logged at a specified interval for a specified number of cycles.

### <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax

```
pwrtest /battery [/c:n] [/i:n] [/?] 
```

<span id="_c_n"></span><span id="_C_N"></span>**/c:**<em>n</em>  
Specifies the number of cycles (100 is the default) to run.

<span id="_i_n"></span><span id="_I_N"></span>**/i:**<em>n</em>  
Specifies the polling interval in milliseconds (the default is 5000).

**Examples**

```
pwrtest /battery 
```

```
pwrtest /battery /c:4 /i:1000
```

### <span id="XML_log_file_output"></span><span id="xml_log_file_output"></span><span id="XML_LOG_FILE_OUTPUT"></span>XML log file output

```XML
<PwrTestLog>
  <SystemInformation>
  </SystemInformation>
  <BatteryScenario>
    <Batteries>
      <Battery id="" shortterm="" rechargable="" >
        <Name></Name>
        <UniqueID></UniqueID>
        <Chemistry></Chemistry>
        <Manufacturer></Manufacturer>
        <DesignedCapacity></DesignedCapacity>
        <FullChargeCapacity></FullChargeCapacity>
        <CriticalBias></CriticalBias>
        <CycleCount></CycleCount>
        <ManufactureDate></ManufactureDate>
        <FullLifeTime Units=""></FullLifeTime>
      </Battery> 
    </Batteries>
    <BatteryTraces interval="">
      <Trace>
        <ElapsedT></ElapsedT>
        <ACStatus></ACStatus>
        <Capacity id=""></Capacity>
        <TimeRemaining></TimeRemaining>
        <Capacity id=""></Capacity>
        <RateOfDrain id=””></RateOfDrain>
        <Voltage id=””></Voltage>
        <Capacity id=""></Capacity>
        <RateOfDrain id=””></RateOfDrain>
        <Voltage id=””> </Voltage>
      </Trace>
    </BatteryTraces> 
  </BatteryScenario>
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
<td align="left"><strong>&lt;UniqueID&gt;</strong></td>
<td align="left"><p>Indicates the unique ID of the battery.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Chemistry&gt;</strong></td>
<td align="left"><p>Indicates battery chemistry.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Manufacturer&gt;</strong></td>
<td align="left"><p>Indicates the battery manufacturer.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;DesignedCapacity&gt;</strong></td>
<td align="left"><p>Indicates the designed capacity of the battery in milliwatt hours (mW-h).</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;FullChargeCapacity&gt;</strong></td>
<td align="left"><p>Indicates the fully charged capacity of the battery in milliwatt hours (mW-h).</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;CriticalBias&gt;</strong></td>
<td align="left"><p>Indicates a bias from zero, in mW-h, which is applied to the battery reporting.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;CycleCount&gt;</strong></td>
<td align="left"><p>Indicates the number of charge/discharge cycles the battery has experienced.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ManufactureDate&gt;</strong></td>
<td align="left"><p>Indicates the manufacture date of the battery.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;FullLifeTime&gt;</strong></td>
<td align="left"><p>Indicates the battery full life time in seconds.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;BatteryTraces&gt;</strong></td>
<td align="left"><p>Contains a list of <strong>&lt;Trace&gt;</strong> elements. Has an attribute indicating the battery information polling interval.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Trace&gt;</strong></td>
<td align="left"><p>Contains information about battery status such as voltage, capacity and rate of drain for a given interval.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;ElapsedT&gt;</strong></td>
<td align="left"><p>Indicates the elapsed time since PwrTest was started</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;ACStatus&gt;</strong></td>
<td align="left"><p>Indicates if the system is running on AC (1) or battery (0) power.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;TimeRemaining&gt;</strong></td>
<td align="left"><p>Indicates the battery life time remaining from all system batteries, in seconds.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Capacity&gt;</strong></td>
<td align="left"><p>Indicates the capacity of the battery in milliwatt hours (mW-h). Has an id attribute to indicate which battery the capacity is being reported for.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;RateOfDrain&gt;</strong></td>
<td align="left"><p>Indicates the rate of drain of the battery in milliwatts (mW). Has an ID attribute to indicate which battery the rate of drain is being reported for.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Voltage&gt;</strong></td>
<td align="left"><p>Indicates the battery voltage in millivolts (mV). Has an ID attribute to indicate which battery the voltage is being reported for.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)

 

 






