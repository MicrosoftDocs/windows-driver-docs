---
title: PwrTest Battery Scenario
description: The PwrTest Battery Scenario is designed to facilitate automated inspection of battery and power source information.
ms.assetid: e0bad871-a826-4951-9a84-93c9b1aa0653
---

# PwrTest Battery Scenario


The PwrTest Battery Scenario is designed to facilitate automated inspection of battery and power source information.

PwrTest is capable of logging battery capacity, voltage, rate of drain, and general state for as many batteries as are in the system. Battery data is logged at a specified interval for a specified number of cycles.

### <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax

``` syntax
pwrtest /battery [/c:n] [/i:n] [/?] 
```

<span id="_c_n"></span><span id="_C_N"></span>**/c:***n*  
Specifies the number of cycles (100 is the default) to run.

<span id="_i_n"></span><span id="_I_N"></span>**/i:***n*  
Specifies the polling interval in milliseconds (the default is 5000).

**Examples**

``` syntax
pwrtest /battery 
```

``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PwrTest%20Battery%20Scenario%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





