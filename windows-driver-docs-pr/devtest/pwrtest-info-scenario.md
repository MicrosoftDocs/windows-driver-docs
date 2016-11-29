---
title: PwrTest Info Scenario
description: The PwrTest Info Scenario captures and logs the current system power information from various categories.
ms.assetid: 1d13d1dd-eb8d-434a-b994-e747a86f3457
---

# PwrTest Info Scenario


The PwrTest Info Scenario captures and logs the current system power information from various categories.

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


``` syntax
pwrtest /info:option [/p:{n|a|*}] [/w:n]  [/?] 
```

<span id="_info_option"></span><span id="_INFO_OPTION"></span>**/info:***option*  

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"><em>option</em></th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="all"></span><span id="ALL"></span><strong>all</strong></p></td>
<td align="left"><p>Displays all system information.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="powercap"></span><span id="POWERCAP"></span><strong>powercap</strong></p></td>
<td align="left"><p>Displays SYSTEM_POWER_CAPABILITIES.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="powerinfo"></span><span id="POWERINFO"></span><strong>powerinfo</strong></p></td>
<td align="left"><p>Displays SYSTEM_POWER_CAPABILITIES.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="battery"></span><span id="BATTERY"></span><strong>battery</strong></p></td>
<td align="left"><p>Displays SYSTEM_BATTERY_STATE.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="ppm"></span><span id="PPM"></span><strong>ppm</strong></p></td>
<td align="left"><p>Displays all processor information.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="ppmidle"></span><span id="PPMIDLE"></span><strong>ppmidle</strong></p></td>
<td align="left"><p>Displays processor idle state information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="ppmperf"></span><span id="PPMPERF"></span><strong>ppmperf</strong></p></td>
<td align="left"><p>Displays processor performance state information.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="ppmperfverbose"></span><span id="PPMPERFVERBOSE"></span><strong>ppmperfverbose</strong></p></td>
<td align="left"><p>Displays processor performance state information in the verbose format .</p></td>
</tr>
</tbody>
</table>

 

<span id="_p_na_"></span><span id="_P_NA_"></span>**/p:**{*n*|**a**|**\***}  

Specifies the logical processor number for **/info:ppm/info:ppmidle**, or **/info:ppmperf** options.

<span id="a_or__"></span><span id="A_OR__"></span>**a** or **\***  
Specifies all the logical processor(s) (default).

<span id="_w_yn"></span><span id="_W_YN"></span>**/w:**{**y**|**n**}  
Specifies the time in seconds to wait for PPM rundown event (default is 10 seconds).

**Examples**

``` syntax
pwrtest /info:all
```

``` syntax
  pwrtest /info:battery
```

``` syntax
  pwrtest /info:ppm
```

``` syntax
  pwrtest /info:ppm /p:1
```

``` syntax
 pwrtest /info:ppmidle
```

``` syntax
  pwrtest /info:ppmperf /p:2
```

### <span id="XML_log_file_output"></span><span id="xml_log_file_output"></span><span id="XML_LOG_FILE_OUTPUT"></span>XML log file output

```XML
<PwrTestLog>
  <SystemInformation>
  </SystemInformation>
  <InfoScenario>
    <SYSTEM_POWER_CAPABILITIES> 
      <SystemS1StateSupported></SystemS1StateSupported>
      <SystemS2StateSupported></SystemS2StateSupported>
      <SystemS3StateSupported></SystemS3StateSupported>
      <SystemS4StateSupported></SystemS4StateSupported>
      <SystemS5StateSupported></SystemS5StateSupported>
      <RtcWakeSupported></RtcWakeSupported>
      <FastSystemS4></FastSystemS4>
    </SYSTEM_POWER_CAPABILITIES> 
    <SYSTEM_POWER_INFORMATION> 
      <MaxIdlenessAllowed></MaxIdlenessAllowed>
      <Idleness></Idleness>
      <TimeRemaining></TimeRemaining>
      <CoolingMode></CoolingMode>
    </SYSTEM_POWER_INFORMATION> 
    <SYSTEM_BATTERY_STATE> 
      <AcOnLine></AcOnLine>
      <BatteryPresent></BatteryPresent>
      <Charging></Charging>
      <Discharging></Discharging>
      <MaxCapacity></MaxCapacity>
      <RemainingCapacity></RemainingCapacity>
      <RateOfDrain></RateOfDrain>
      <EstimatedTime></EstimatedTime>
      <DefaultAlert1></DefaultAlert1>
      <DefaultAlert2></DefaultAlert2>
    </SYSTEM_BATTERY_STATE> 
    <PROCESSOR_POWER_INFORMATION> 
      <CPUNumber></CPUNumber>
      <MaxMhz></MaxMhz>
      <CurrentMhz></CurrentMhz>
      <MhzLimit></MhzLimit>
      <MaxIdleState></MaxIdleState>
      <CurrentIdleState></CurrentIdleState>
    </PROCESSOR_POWER_INFORMATION> 
    </InfoScenario>
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
<td align="left"><strong>&lt;InfoScenario&gt;</strong></td>
<td align="left"><p>Contains information related to the info scenario. There is only one <strong>&lt;InfoScenario&gt;</strong> element in a PwrTest log file.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;SYSTEM_POWER_CAPABILITIES&gt;</strong></td>
<td align="left"><p>Contains information related to system power capabilities. This information is retrieved from the SYSTEM_POWER_CAPABILITIES structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;SystemSxStateSupported&gt;</strong></td>
<td align="left"><p>Indicates if a given system ACPI sleep state is supported on the system.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;RtcWakeSupported&gt;</strong></td>
<td align="left"><p>Indicates the lowest sleep state where RTC wake (wake on timer) is supported. The value is of the SYSTEM_POWER_STATE enumeration.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;FastSystemS4&gt;</strong></td>
<td align="left"><p>Indicates if hybrid sleep is available on the system.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;SYSTEM_POWER_INFORMATION&gt;</strong></td>
<td align="left"><p>Contains information related to the idleness of the system.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;MaxIdlenessAllowed&gt;</strong></td>
<td align="left"><p>Indicates the idleness (in percentage) when the system is considered idle and the idle timeout begins counting.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Idleness&gt;</strong></td>
<td align="left"><p>Current idle level, expressed in percentage.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;TimeRemaining&gt;</strong></td>
<td align="left"><p>Indicates the time remaining in the system standby idle timer, in seconds.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;CoolingMode&gt;</strong></td>
<td align="left"><p>Indicates the current system cooling mode: (0) Active, (1), Passive, (2) Invalid.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;SYSTEM_BATTERY_STATE&gt;</strong></td>
<td align="left"><p>Contains information related to the current state of the system battery.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;AcOnLine&gt;</strong></td>
<td align="left"><p>Indicates whether the system is currently operating on AC power.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;BatteryPresent&gt;</strong></td>
<td align="left"><p>Indicates if at least one battery is present in the system.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;Charging&gt;</strong></td>
<td align="left"><p>Indicates whether at least one battery is currently charging.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;Discharging&gt;</strong></td>
<td align="left"><p>Indicates whether at least one battery is currently discharging.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;MaxCapacity&gt;</strong></td>
<td align="left"><p>Maximum capacity of the battery when new, in milliwatt hours (mW-h).</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;RemainingCapacity&gt;</strong></td>
<td align="left"><p>Estimated remaining capacity of the battery, in milliwatt hours (mW-h).</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;RateOfDrain&gt;</strong></td>
<td align="left"><p>Indicates the current rate of discharge of the battery in milliwatts (mW).</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;EstimatedTime&gt;</strong></td>
<td align="left"><p>Estimated time remaining on the battery, in seconds.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;DefaultAlert1&gt;</strong></td>
<td align="left"><p>Indicates the battery manufacturer's suggested capacity when a low battery alert should occur.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;DefaultAlert2&gt;</strong></td>
<td align="left"><p>Indicates the battery manufacturer's suggested capacity when a warning battery alert should occur.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;PROCESSOR_POWER_INFORMATION&gt;</strong></td>
<td align="left"><p>Contains information related to the system processors and their power management capabilities.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;CPUNumber&gt;</strong></td>
<td align="left"><p>Indicates which processor the current &lt;PROCESSOR_POWER_INFORMATION&gt; element is describing.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;MaxMhz&gt;</strong></td>
<td align="left"><p>Indicates the maximum frequency of the processor.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;CurrentMhz&gt;</strong></td>
<td align="left"><p>Indicates the current frequency of the processor.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;MhzLimit&gt;</strong></td>
<td align="left"><p>Indicates the current limit on the processor clock frequency.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>&lt;MaxIdleState&gt;</strong></td>
<td align="left"><p>Indicates the maximum idle state of the processor.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;CurrentIdleState&gt;</strong></td>
<td align="left"><p>Indicates the current idle state of the processor.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PwrTest%20Info%20Scenario%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





