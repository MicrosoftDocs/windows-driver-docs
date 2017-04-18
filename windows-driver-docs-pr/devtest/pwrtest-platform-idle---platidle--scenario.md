---
title: PwrTest Platform Idle Scenario
description: The PwrTest Platform Idle Scenario (/platidle) polls and attempts to log platform idle transition counts if they are supported by the computer.
ms.assetid: 71A3AB26-AAC5-46DB-99A3-6693D5AF5AC9
---

# PwrTest Platform Idle Scenario


The PwrTest Platform Idle Scenario (**/platidle**) polls and attempts to log platform idle transition counts if they are supported by the computer.

This scenario is useful for tracking platform idle state transitions that occur while the computer is in use. This scenario can also help diagnose if a system is entering deep platform idle states (if manually entered via the power button).

The **/platidle** scenario requires that the computer has support for the *Always on Always connected* (AoAc) power capability.

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


``` syntax
pwrtest /platidle  [/t:n] [/i:n] [/?] 
```

<span id="_t_n"></span><span id="_T_N"></span>**/t:***n*  
Specifies the total time (in minutes) for the scenario to run (the default value for *n* is 30 minutes).

<span id="_i_n"></span><span id="_I_N"></span>**/i:***n*  
Specifies the polling interval (in seconds) for gathering platform idle statistics (the default value for *n* is 5 seconds).

**Examples**

``` syntax
pwrtest /platidle /t:60
```

``` syntax
pwrtest /platidle
```

### <span id="XML_log_file_output"></span><span id="xml_log_file_output"></span><span id="XML_LOG_FILE_OUTPUT"></span>XML log file output

```XML
<PwrTestLog>
  <SystemInformation>
  </SystemInformation>
  <PlatIdle> 
    <PlatformIdleStats StateCount="X" Timestamp="XX/XX/XXXX:XX:XX:XX.XXX">
        <State Index="X" SuccessCount="X" FailureCount="X" CancelCount="X"/>
    </PlatformIdleStats>
  </PlatIdle>
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
<td align="left"><strong>&lt;PlatIdle&gt;</strong></td>
<td align="left"><p>Contains all platform idle statistics. There is only one <strong>&lt;PlatIdle&gt;</strong> element in a PwrTest log file</p></td>
</tr>
<tr class="even">
<td align="left"><strong>&lt;PlatformIdleStats&gt;</strong></td>
<td align="left"><p>Platform idle statistics block.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PwrTest%20Platform%20Idle%20Scenario%20%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





