---
title: Driver Verifier Command Syntax
description: The following syntax is used when running the Verifier utility in a Command Prompt window.You can type several options on the same single line.
keywords:
- Driver Verifier Command Syntax Driver Development Tools
topic_type:
- apiref
api_name:
- Driver Verifier Command Syntax
api_type:
- NA
ms.date: 06/28/2021
ms.localizationpriority: medium
---

# Driver Verifier Command Syntax

The following syntax is used when running the Verifier utility in a Command Prompt window.

You can type several options on the same single line. For example:

```
verifier /flags 7 /driver beep.sys disksdd.sys
```

**Windows 11**

```
  verifier /standard /all
  verifier /standard /driver NAME [NAME ...]
  verifier {/ruleclasses | /rc | dif} <options> [<ruleclass_1> <ruleclass_2> ...] /all
  verifier {/ruleclasses | /rc | dif} <options> [<ruleclass_1> <ruleclass_2> ...] /driver NAME [NAME ...]
  verifier /flags <options> /all
  verifier /flags <options> /driver NAME [NAME ...]
  verifier /rules [OPTION ...]
  verifier /dif [<ruleclass_1> <ruleclass_2> ...] /now /driver NAME [NAME ...]
  verifier /query
  verifier /querysettings
  verifier /bootmode [persistent | disableafterfail | oneboot]
  verifier /bc <number_of_reboots>
  verifier /reset
  verifier /faults [Probability] [PoolTags] [Applications] [DelayMins]
  verifier /faultssystematic [OPTION ...]
  verifier /log LOG_FILE_NAME [/interval SECONDS]
  verifier /volatile /flags <options>
  verifier /volatile /adddriver NAME [NAME ...]
  verifier /volatile /removedriver NAME [NAME ...]
  verifier /volatile /faults [Probability] [PoolTags] [Applications] [DelayMins]
  verifier /domain <types> <options> /driver ... [/logging | /livedump]
  verifier /logging
  verifier /livedump
  verifier /?
  verifier /help
```

Starting in Windows 11, these driver interception framework (DIF) enabled options can be enabled using the /dif option.

The **/dif** command automatically includes rule class 36, DIF mode, but **/ruleclasses** and **/rc** do not. Flags marked with (!) in the help text require DIF mode to be enabled. All Standard rule classes can be enabled without also enabling DIF mode.

Rules marked with (^) in the help text can be enabled without reboot using the **/dif [<ruleclass_1> <ruleclass_2> <ruleclass_k>] /now** command.

**Standard Rule Classes**

 Value | Rule | /now
|------|------|-----|
1 | Special pool | yes
2 | Force IRQL checking | no
4 | Pool tracking | yes
5 | I/O verification | yes
6 | Deadlock detection | no
8 | DMA checking | no
9 | Security checks | yes
12 | Miscellaneous checks | yes
18 | DDI compliance checking | yes
34 | WDF verification | no


**Additional Rule Classes**

 Value | Rule | /now | Needs DIF Mode?
|------|------|------|-------|
3 | Randomized low resources simulation | no | no
10 | Force pending I/O requests | no | no
11 | IRP logging | no | no
14 | Invariant MDL checking for stack | no | no
15 | Invariant MDL checking for driver | no | no
16 | Power framework delay fuzzing | no | no
17 | Port/miniport interface checking | no | no
19 | Systematic low resources simulation | yes | yes
20 | DDI compliance checking (additional) | yes | no
22 | NDIS/WIFI verification | no | no
24 | Kernel synchronization delay fuzzing | no | no
25 | VM switch verification | no | no
26 | Code integrity checks | no | no
33 | Driver isolation checks | no | yes
35 | DDI checking (additional IRQL rules) | yes | yes
36 | DIF mode | yes | n/a

**Windows 10**

You can use the **/volatile** parameter with some Driver Verifier **/flags** options and with **/standard**. You cannot use **/volatile** with the **/flags** options for [DDI compliance checking](ddi-compliance-checking.md), [Power Framework Delay Fuzzing](concurrency-stress-test.md) or [Storport Verification](dv-storport-verification.md). For details, see [Using Volatile Settings](using-volatile-settings.md).

```
  verifier /standard /all
  verifier /standard /driver NAME [NAME ...]
  verifier {/ruleclasses | /rc} <options> [<ruleclass_1> <ruleclass_2> ...] /all
  verifier /flags <options> /all
  verifier /flags <options> /driver NAME [NAME ...]
  verifier /rules [OPTION ...]
  verifier /query
  verifier /querysettings
  verifier /bootmode [persistent | disableafterfail | oneboot]
  verifier /reset
  verifier /faults [Probability] [PoolTags] [Applications] [DelayMins]
  verifier /faultssystematic [OPTION ...]
  verifier /log LOG_FILE_NAME [/interval SECONDS]
  verifier /volatile /flags <options>
  verifier /volatile /adddriver NAME [NAME ...]
  verifier /volatile /removedriver NAME [NAME ...]
  verifier /volatile /faults [Probability] [PoolTags] [Applications] [DelayMins]
  verifier /domain <types> <options> /driver ... [/logging | /livedump]
  verifier /logging
  verifier /livedump
  verifier /?
  verifier /help
```

**Windows 8.1**

You can use the **/volatile** parameter with some Driver Verifier **/flags** options and with **/standard**. You cannot use **/volatile** with the **/flags** options for [DDI compliance checking](ddi-compliance-checking.md), [Power Framework Delay Fuzzing](concurrency-stress-test.md), [Storport Verification](dv-storport-verification.md). For details, see [Using Volatile Settings](using-volatile-settings.md).

```
  verifier /standard /all
  verifier /standard /driver NAME [NAME ...]
  verifier /flags <options> /all
  verifier /flags <options> /driver NAME [NAME ...]
  verifier /rules [OPTION ...]
  verifier /faults [Probability] [PoolTags] [Applications] [DelayMins]
  verifier /faultssystematic [OPTION ...]
  verifier /log LOG_FILE_NAME [/interval SECONDS]
  verifier /query
  verifier /querysettings
  verifier /bootmode [persistent | disableafterfail | oneboot]
  verifier /reset
  verifier /volatile /flags <options>
  verifier /volatile /adddriver NAME [NAME ...]
  verifier /volatile /removedriver NAME [NAME ...]
  verifier /volatile /faults [Probability] [PoolTags] [Applications] [DelayMins]
  verifier /?
```

**Windows 8, Windows 7 Syntax**

You can use the **/volatile** parameter with some Driver Verifier **/flags** options and with **/standard**. You cannot use **/volatile** with the /flags options for [DDI compliance checking](ddi-compliance-checking.md), [Power Framework Delay Fuzzing](concurrency-stress-test.md), [Storport Verification](dv-storport-verification.md), SCSI Verification or with **/disk**. For details, see [Using Volatile Settings](using-volatile-settings.md).

```
verifier [/volatile] [/standard | /flags Options ] [ /all | /driver DriverList ]
verifier /volatile /faults [Probability PoolTags Applications DelayMins] /driver DriverList
verifier /volatile {/adddriver | /removedriver} DriverList
verifier /reset
verifier /querysettings
verifier /query
verifier /log LogFileName [/interval Seconds]
verifier /?
```

## Parameters


### Verifier Command-Line Syntax

**/all**
Directs Driver Verifier to verify all installed drivers after the next boot.

**/bc \<number_of_reboots\>**
Sets the number of reboots for which verification should be active.

This option automatically sets the ResetOnUnusualShutdown boot mode.

**/bootmode** *mode*
Controls whether the settings for Driver Verifier are enabled after a reboot. To set or change this option, you must reboot the computer.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Boot <em>mode</em></th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="persistent"></span><span id="PERSISTENT"></span><strong>persistent</strong></p></td>
<td align="left"><p>Ensures that the Driver Verifier settings persist (stay in effect) over many reboots. This is the default setting.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="disableafterfail"></span><span id="DISABLEAFTERFAIL"></span><strong>disableafterfail</strong></p></td>
<td align="left"><p>If Windows fails to start, this setting disables Driver Verifier for subsequent reboots.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="oneboot"></span><span id="ONEBOOT"></span><strong>oneboot</strong></p></td>
<td align="left"><p>Only enables the Driver Verifier settings for the next time the computer starts. Driver Verifier is disabled for subsequent reboots.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="resetonunusualshutdown"></span><span id="RESETONUNUSUALSHUTDOWN"></span><strong>resetonunusualshutdown</strong></p></td>
<td align="left"><p>(Introduced in Windows 10, build 1709) Driver Verifier will persist until an unusual shutdown occurs. Its abbrevation, <strong>'rous'</strong>, can be used.
</p></td>
</tr>
</tbody>
</table>

**/dif** *DifEnabledRule*
Enable checking using a Dif enabled rule. Checking will take effect the next time the system is rebooted. Added in Windows 11.

**/dif /now** *DifEnabledRule*
Immediately enable checking using a Dif enabled rule. Enables the rule classes immediately without needing reboot. This option
is only valid if no rule classes are already running. See the Windows 11 rule class descriptions for the rule classes capable of immediate activation.

**/driver** *DriverList*
Specifies one or more drivers that will be verified. *DriverList* is a list of drivers by binary name, such as Driver.sys. Use a space to separate each driver name. Wildcard values, such as n\*.sys, are not supported.

**/driver.exclude** *DriverList*
Specifies one or more drivers that will be excluded from verification. This parameter is applicable only if all drivers are selected for verification. *DriverList* is a list of drivers by binary name, such as Driver.sys. Use a space to separate each driver name. Wildcard values, such as n\*.sys, are not supported.

**/faults**
Enables the Low Resources Simulation feature in Driver Verifier. You can use **/faults** in place of **/flags 0x4**. However, you cannot use **/flags 0x4** with the **/faults** subparameters.

You can use the following subparameters of the **/faults** parameter to configure Low Resources Simulation.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Subparameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>Probability</em></p></td>
<td align="left"><p>Specifies the probability that Driver Verifier will fail a given allocation. Type a number (in decimal or hexadecimal) to represent the number of chances in 10,000 that Driver Verifier will fail the allocation. The default value, 600, means 600/10000 or 6%.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Pool Tags</em></p></td>
<td align="left"><p>Limits the allocations that Driver Verifier can fail to allocations with the specified pool tags. You can use a wildcard character (<strong>*</strong>) to represent multiple pool tags. To list multiple pool tags, separate the tags with spaces. By default, all allocations can fail.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Applications</em></p></td>
<td align="left"><p>Limits the allocations that Driver Verifier can fail to allocations for the specified program. Type the name of an executable file. To list programs, separate the program names with spaces. By default, all allocations can fail.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>DelayMins</em></p></td>
<td align="left"><p>Specifies the number of minutes after booting during which Driver Verifier does not intentionally fail any allocations. This delay allows the drivers to load and the system to stabilize before the test begins. Type a number (in decimal or hexadecimal). The default value is 7 (minutes).</p></td>
</tr>
</tbody>
</table>



<span id="_faultssystematic"></span><span id="_FAULTSSYSTEMATIC"></span>**/faultssystematic**
Specifies the options for [Systematic low resources simulation](systematic-low-resource-simulation.md). Use the **0x40000** flag to select Systematic low resources simulation option.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">OPTION</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>enableboottime</p></td>
<td align="left"><p>Enables fault injections across computer reboots.</p></td>
</tr>
<tr class="even">
<td align="left"><p>disableboottime</p></td>
<td align="left"><p>Disables fault injections across computer reboots (this is the default setting).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>recordboottime</p></td>
<td align="left"><p>Enables fault injections in <em>what if</em> mode across computer reboots.</p></td>
</tr>
<tr class="even">
<td align="left"><p>resetboottime</p></td>
<td align="left"><p>Disables fault injections across computer reboots and clears the stack exclusion list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>enableruntime</p></td>
<td align="left"><p>Dynamically enables fault injections.</p></td>
</tr>
<tr class="even">
<td align="left"><p>disableruntime</p></td>
<td align="left"><p>Dynamically disables fault injections.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>recordruntime</p></td>
<td align="left"><p>Dynamically enables fault injections in <em>what if</em> mode.</p></td>
</tr>
<tr class="even">
<td align="left"><p>resetruntime</p></td>
<td align="left"><p>Dynamically disables fault injections and clears the previously faulted stack list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>querystatistics</p></td>
<td align="left"><p>Shows the current fault injection statistics.</p></td>
</tr>
<tr class="even">
<td align="left"><p>incrementcounter</p></td>
<td align="left"><p>Increments the test pass counter used to identify when a fault was injected.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>getstackid <em>COUNTER</em></p></td>
<td align="left"><p>Retrieves the indicated injected stack identifier.</p></td>
</tr>
<tr class="even">
<td align="left"><p>excludestack <em>STACKID</em></p></td>
<td align="left"><p>Excludes the stack from fault injection.</p></td>
</tr>
</tbody>
</table>

**/flags** *Options*
Activates the specified options after the next reboot. This number can be entered in decimal or in hexadecimal (with an **0x** prefix) format. Any combination of the following values is allowed.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Decimal</th>
<th align="left">Hexadecimal</th>
<th align="left">Standard Setting</th>
<th align="left">Option</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>0x1 (bit 0)</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p><a href="special-pool.md" data-raw-source="[Special Pool](special-pool.md)">Special Pool</a></p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>0x2 (bit 1)</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p><a href="force-irql-checking.md" data-raw-source="[Force IRQL Checking](force-irql-checking.md)">Force IRQL Checking</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>4</p></td>
<td align="left"><p>0x4 (bit 2)</p></td>
<td align="left"></td>
<td align="left"><p><a href="low-resources-simulation.md" data-raw-source="[Low Resources Simulation](low-resources-simulation.md)">Low Resources Simulation</a></p></td>
</tr>
<tr class="even">
<td align="left"><p>8</p></td>
<td align="left"><p>0x8 (bit 3)</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p><a href="pool-tracking.md" data-raw-source="[Pool Tracking](pool-tracking.md)">Pool Tracking</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>16</p></td>
<td align="left"><p>0x10 (bit 4)</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p><a href="i-o-verification.md" data-raw-source="[I/O Verification](i-o-verification.md)">I/O Verification</a></p></td>
</tr>
<tr class="even">
<td align="left"><p>32</p></td>
<td align="left"><p>0x20 (bit 5)</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p><a href="deadlock-detection.md" data-raw-source="[Deadlock Detection](deadlock-detection.md)">Deadlock Detection</a> </p></td>
</tr>
<tr class="odd">
<td align="left"><p>64</p></td>
<td align="left"><p>0x40 (bit 6)</p></td>
<td align="left"></td>
<td align="left"><p><a href="enhanced-i-o-verification.md" data-raw-source="[Enhanced I/O Verification](enhanced-i-o-verification.md)">Enhanced I/O Verification</a> This option is automatically activated when you select I/O Verification</p></td>
</tr>
<tr class="even">
<td align="left"><p>128</p></td>
<td align="left"><p>0x80 (bit 7)</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p><a href="dma-verification.md" data-raw-source="[DMA Verification](dma-verification.md)">DMA Verification</a> </p></td>
</tr>
<tr class="odd">
<td align="left"><p>256</p></td>
<td align="left"><p>0x100 (bit 8)</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p><a href="security-checks.md" data-raw-source="[Security Checks](security-checks.md)">Security Checks</a> </p></td>
</tr>
<tr class="even">
<td align="left"><p>512</p></td>
<td align="left"><p>0x200 (bit 9)</p></td>
<td align="left"></td>
<td align="left"><p><a href="force-pending-i-o-requests.md" data-raw-source="[Force Pending I/O Requests](force-pending-i-o-requests.md)">Force Pending I/O Requests</a> </p></td>
</tr>
<tr class="odd">
<td align="left"><p>1024</p></td>
<td align="left"><p>0x400 (bit 10)</p></td>
<td align="left"></td>
<td align="left"><p><a href="irp-logging.md" data-raw-source="[IRP Logging](irp-logging.md)">IRP Logging</a> </p></td>
</tr>
<tr class="even">
<td align="left"><p>2048</p></td>
<td align="left"><p>0x800 (bit 11)</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p><a href="miscellaneous-checks.md" data-raw-source="[Miscellaneous Checks](miscellaneous-checks.md)">Miscellaneous Checks</a> </p></td>
</tr>
<tr class="odd">
<td align="left"><p>8192</p></td>
<td align="left"><p>0x2000 (bit 13)</p></td>
<td align="left"></td>
<td align="left"><p><a href="invariant-mdl-checking-for-stack.md" data-raw-source="[Invariant MDL Checking for Stack](invariant-mdl-checking-for-stack.md)">Invariant MDL Checking for Stack</a> (Starting with Windows 8)</p></td>
</tr>
<tr class="even">
<td align="left"><p>16384</p></td>
<td align="left"><p>0x4000 (bit 14)</p></td>
<td align="left"></td>
<td align="left"><p><a href="invariant-mdl-checking-for-driver.md" data-raw-source="[Invariant MDL Checking for Driver](invariant-mdl-checking-for-driver.md)">Invariant MDL Checking for Driver</a> (Starting with Windows 8)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>32768</p></td>
<td align="left"><p>0x8000 (bit 15)</p></td>
<td align="left"></td>
<td align="left"><p><a href="concurrency-stress-test.md" data-raw-source="[Power Framework Delay Fuzzing](concurrency-stress-test.md)">Power Framework Delay Fuzzing</a> (Starting with Windows 8) <b>(Deprecated in Windows 10 Insider Preview Build 19042 and above)</b></p></td>
</tr>
<tr class="even">
<td align="left"><p>65536</p></td>
<td align="left"><p>0x10000 (bit 16)</p></td>
<td align="left"></td>
<td align="left"><p>Port/miniport interface checking (Starting with Windows 10)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>131072</p></td>
<td align="left"><p>0x20000 (bit 17)</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p><a href="ddi-compliance-checking.md" data-raw-source="[DDI compliance checking](ddi-compliance-checking.md)">DDI compliance checking</a> (Starting with Windows 8)</p></td>
</tr>
<tr class="even">
<td align="left"><p>262144</p></td>
<td align="left"><p>0x40000 (bit 18)</p></td>
<td align="left"></td>
<td align="left"><p><a href="systematic-low-resource-simulation.md" data-raw-source="[Systematic low resources simulation](systematic-low-resource-simulation.md)">Systematic low resources simulation</a> (Starting with Windows 8.1) <b>(Deprecated in Windows 10 Insider Preview Build 19042 and above)</b></p></td>
</tr>
<tr class="odd">
<td align="left"><p>524288</p></td>
<td align="left"><p>0x80000 (bit 19)</p></td>
<td align="left"></td>
<td align="left"><p><a href="ddi-compliance-checking.md#ddi_compliance_checking_additional" data-raw-source="[DDI compliance checking (additional)](ddi-compliance-checking.md#ddi_compliance_checking_additional)">DDI compliance checking (additional)</a> (Starting with Windows 8.1) <b>(Deprecated in Windows 10 Insider Preview Build 19042 and above)</b></p></td>
</tr>
<tr class="even">
<td align="left"><p>2097152</p></td>
<td align="left"><p>0x200000 (bit 21)</p></td>
<td align="left"></td>
<td align="left"><p><a href="ndis-wifi-verification.md" data-raw-source="[NDIS/WIFI verification](ndis-wifi-verification.md)">NDIS/WIFI verification</a> (Starting with Windows 8.1)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>8388608</p></td>
<td align="left"><p>0x800000 (bit 23)</p></td>
<td align="left"></td>
<td align="left"><p><a href="kernel-synchronization-delay-fuzzing.md" data-raw-source="[Kernel synchronization delay fuzzing](kernel-synchronization-delay-fuzzing.md)">Kernel synchronization delay fuzzing</a> (Starting with Windows 8.1) <b>(Deprecated in Windows 10 Insider Preview Build 19042 and above)</b></p></td>
</tr>
<tr class="even">
<td align="left"><p>16777216</p></td>
<td align="left"><p>0x1000000 (bit 24)</p></td>
<td align="left"></td>
<td align="left"><p><a href="vm-switch-verification.md" data-raw-source="[VM switch verification](vm-switch-verification.md)">VM switch verification</a> (Starting with Windows 8.1)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>33554432</p></td>
<td align="left"><p>0x2000000 (bit 25)</p></td>
<td align="left"></td>
<td align="left"><p>Code integrity checks (Starting with Windows 10)</p></td>
</tr>
</tbody>
</table>

You cannot use this method to activate the Storport Verification options. For information, see [Storport Verification](dv-storport-verification.md).


**/flags** *VolatileOptions*
Specifies the Driver Verifier options that are changed immediately without rebooting.

You can use the **/volatile** parameter with all **/flags** values.)

Enter a number in decimal or in hexadecimal format (with an **0x** prefix).

Any combination of the following values is permitted.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Hexadecimal</th>
<th align="left">Option</th>
</tr>
</thead>
<tbody>
</tr>
<tr class="odd">
<td align="left"><p>0x00000004 (bit 2)</p></td>
<td align="left"><p>Randomized Low Resources Simulation</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000020 (bit  5) </p></td>
<td align="left"><p>Deadlock detection</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00000080 (bit  7)</p></td>
<td align="left"><p>DMA checking</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000200 (bit  9)</p></td>
<td align="left"><p>Force pending I/O requests</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00000400 (bit 10)</p></td>
<td align="left"><p>IRP Logging</p></td>
</tr>
</tbody>
</table>

**/ruleclasses** or **/rc** *\<ruleclass_1\> \<ruleclass_2\> ... \<ruleclass_k\>*

The ruleclasses parameter is available starting with Windows Version 1803.

The ruleclasses parameter encompasses a larger set of verification classes than the '/flags' parameter above. While '/flags' is limited to a 32 bit bitmap expression, this option can include more than 32 verification classes. Each positive decimal integer represents a verification class. Multiple classes can be expressed by separating each class id with a space character. The following rule classes IDs are available.

**Standard Rule Classes**

 Value | Rule
|------|------|
1 | Special pool
2 | Force IRQL checking
4 | Pool tracking
5 | I/O verification
6 | Deadlock detection
8 | DMA checking
9 | Security checks
12 | Miscellaneous checks
18 | DDI compliance checking
34 | WDF Verification

**Additional Rule Classes**

These rule classes are intended for specific scenario testing. Rule classes are marked with `(*)` require I/O Verification (5) that will be automatically enabled. Flags marked with `(**)` support disabling of individual rules. Flags marked with `(***)` are in logging mode by default and require /onecheck in order to crash upon violation.

Flags marked with `(!)` require DIF mode (rule class 36) to be enabled.

 Value | Rule
|------|------|
3 | Randomized low resources simulation
10 | Force pending I/O requests (*)
11 | IRP logging (*)
14 | Invariant MDL checking for stack (*)
15 | Invariant MDL checking for driver (*)
16 | Power framework delay fuzzing
17 | Port/miniport interface checking
19 | Systematic low resources simulation
20 | DDI compliance checking (additional)
22 | NDIS/WIFI verification (**)
24 | Kernel synchronization delay fuzzing
25 | VM switch verification
26 | Code integrity checks
33 | Driver isolation checks (***, !)
36 | DIF mode


### Windows 11 Rule Classes

Starting with Windows 11 the following rule classes are available.


**Standard Rule Classes**

 Value | Rule
|------|------|
1 | Special pool (^)
2 | Force IRQL checking (^)
4 | Pool tracking (^)
5 | I/O verification (^)
6 | Deadlock detection
8 | DMA checking
9 | Security checks (^)
12 | Miscellaneous checks (^)
18 | DDI compliance checking (^)
34 | WDF Verification

The '/dif' command automatically includes rule class 36, DIF mode, but
/ruleclasses and /rc do not. Flags marked with (!) require DIF mode to
be enabled. Flags marked with (^) can be enabled without reboot using
the '/dif [<ruleclass_1> <ruleclass_2> <ruleclass_k>] /now' command.

**Additional Rule Classes**

Flags marked with `(!)` require DIF mode (rule class 36) to be enabled.

 Value | Rule
|------|------|
3 | Randomized low resources simulation
10 | Force pending I/O requests (*)
11 | IRP logging (*)
14 | Invariant MDL checking for stack (*)
15 | Invariant MDL checking for driver (*)
16 | Power framework delay fuzzing
17 | Port/miniport interface checking
19 | Systematic low resources simulation (!, ^)
20 | DDI compliance checking - additional (^)
22 | NDIS/WIFI verification (**)
24 | Kernel synchronization delay fuzzing
25 | VM switch verification
26 | Code integrity checks
33 | Driver isolation checks (***, !)
36 | DIF mode


**/log** *LogFileName* \[**/interval**|*Seconds*\]
Creates a log file with name *LogFileName*. Driver Verifier periodically writes statistics to this file. For details, see [Creating Log Files](creating-log-files.md).

If a **verifier /log** command is typed at the command line, the command prompt does not return. To close the log file and return a prompt, use the CTRL+C key. After a reboot, to create a log, you must submit the **verifier /log** command again.

|Option|Description|
|--- |--- |
|/interval Seconds|Specifies the interval between log file updates. The default is 30 seconds.|


**/rules** *Option*
Options for rules that can be disabled (advanced).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>query</strong></p></td>
<td align="left"><p>Shows current status of controllable rules.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>reset</strong></p></td>
<td align="left"><p>resets all rules to their default state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>default</strong> <em>ID</em></p></td>
<td align="left"><p>Sets rule <em>ID</em> to its default state. For the supported rules, the rule <em>ID</em> is the <a href="/windows-hardware/drivers/debugger/bug-check-0xc4--driver-verifier-detected-violation" data-raw-source="[&lt;strong&gt;Bug Check 0xC4&lt;/strong&gt;](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md)"><strong>Bug Check 0xC4</strong></a> (DRIVER_VERIFIER_DETECTED_VIOLATION) parameter 1 value.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>disable</strong> <em>ID</em></p></td>
<td align="left"><p>Disables specified rule <em>ID</em>. For the supported rules, the rule <em>ID</em> is the <a href="/windows-hardware/drivers/debugger/bug-check-0xc4--driver-verifier-detected-violation" data-raw-source="[&lt;strong&gt;Bug Check 0xC4&lt;/strong&gt;](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md)"><strong>Bug Check 0xC4</strong></a> (DRIVER_VERIFIER_DETECTED_VIOLATION) parameter 1 value.</p></td>
</tr>
</tbody>
</table>

**/standard**
 Activates the "standard" or default Driver Verifier options after the next boot. The standard options are [Special Pool](special-pool.md), [Force IRQL Checking](force-irql-checking.md), [Pool Tracking](pool-tracking.md), [I/O Verification](i-o-verification.md), [Deadlock Detection](deadlock-detection.md), [DMA Verification](dma-verification.md). and [WDF Verification](wdf-verification.md)  The standard options also include [Security Checks](security-checks.md), [Miscellaneous Checks](miscellaneous-checks.md) and [DDI compliance checking](ddi-compliance-checking.md).

> [!NOTE]
> Starting in Windows 10 versions after 1803, using **/flags 0x209BB** will no longer automatically enable WDF verification. Use the **/standard** syntax to enable standard options, with WDF verification included.

**/stop**
 Disables rule classes enabled via '/dif /now' to halt verification.

**/volatile /flags**
Changes the settings without rebooting the computer. Volatile settings take effect immediately. You can use the **/volatile** parameter with the **/flags** parameter to enable and disable some options without rebooting. You can also use **/volatile** with the **/adddriver** and **/removedriver** parameters to start or stop the verification of a driver without rebooting, even if Driver Verifier is not already running.

Specifies the Driver Verifier options that are changed immediately without rebooting. Only the following flags can be used with volatile:

0x00000004 (bit  2) - Randomized low resources simulation
0x00000020 (bit  5) - Deadlock detection
0x00000080 (bit  7) - DMA checking
0x00000200 (bit  9) - Force pending I/O requests
0x00000400 (bit 10) - IRP logging

For details, see [Using Volatile Settings](using-volatile-settings.md).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="__adddriver_VolatileDriverList"></span><span id="__adddriver_volatiledriverlist"></span><span id="__ADDDRIVER_VOLATILEDRIVERLIST"></span> <strong>/adddriver</strong> <em>VolatileDriverList</em></p></td>
<td align="left"><p>Adds the specified drivers to the volatile settings. To specify multiple drivers, list their names, separated by spaces. Wildcard values, such as n<em>.sys, are not supported. See <a href="using-volatile-settings.md" data-raw-source="[Using Volatile Settings](using-volatile-settings.md)">Using Volatile Settings</a> for details.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="_removedriver_VolatileDriverList"></span><span id="_removedriver_volatiledriverlist"></span><span id="_REMOVEDRIVER_VOLATILEDRIVERLIST"></span><strong>/removedriver</strong> <em>VolatileDriverList</em></p></td>
<td align="left"><p>Removes the specified drivers from the volatile settings. To specify multiple drivers, list their names, separated by spaces. Wildcard values, such as n</em>.sys, are not supported. See <a href="using-volatile-settings.md" data-raw-source="[Using Volatile Settings](using-volatile-settings.md)">Using Volatile Settings</a> for details.</p></td>
</tr>
</tbody>
</table>

 **/reset**
Clears all Driver Verifier settings. After the next boot, no drivers will be verified.

**/querysettings**
Displays a summary of the options that will be activated and drivers that will be verified after the next boot. The display does not include drivers and options added by using the **/volatile** parameter. For other ways to view these settings, see [Viewing Driver Verifier Settings](viewing-driver-verifier-settings.md).

**/query**
Displays a summary of Driver Verifier's current activity. The **Level** field in the display is the hexadecimal value of options set with the **/volatile** parameter. See [Monitoring Global Counters](monitoring-global-counters.md) and [Monitoring Individual Counters](monitoring-individual-counters.md) for explanations of each statistic.

**/domain** *Types* **** *Options*
Controls the verifier extension settings. The following verifier extension types are supported.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"><em>Types</em></th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="wdm"></span><span id="WDM"></span><strong>wdm</strong></p></td>
<td align="left"><p>Enables verifier extension for WDM drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="ndis"></span><span id="NDIS"></span><strong>ndis</strong></p></td>
<td align="left"><p>Enables verifier extension for networking drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="ks"></span><span id="KS"></span><strong>ks</strong></p></td>
<td align="left"><p>Enables verifier extension for kernel mode streaming drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="audio"></span><span id="AUDIO"></span><strong>audio</strong></p></td>
<td align="left"><p>Enables verifier extension for audio drivers.</p></td>
</tr>
</tbody>
</table>



The following extension options are supported.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"><em>Options</em></th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="rules.default"></span><span id="RULES.DEFAULT"></span><strong>rules.default</strong></p></td>
<td align="left"><p>Enables default validation rules for the selected verifier extension.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="rules.all"></span><span id="RULES.ALL"></span><strong>rules.all</strong></p></td>
<td align="left"><p>Enables all validation rules for the selected verifier extension.</p></td>
</tr>
</tbody>
</table>

<span id="________logging_______"></span><span id="________LOGGING_______"></span> **/logging**
Enables logging for violated rules detected by the selected verifier extensions.

<span id="________livedump_______"></span><span id="________LIVEDUMP_______"></span> **/livedump**
Enables live memory dump collection for violated rules detected by the selected verifier extensions.

<span id="_______________"></span> **/?**
Displays command-line help.

For more information about the use of these commands, see [Controlling Driver Verifier](controlling-driver-verifier.md) and [Monitoring Driver Verifier](monitoring-driver-verifier.md).

<span id="________help______"></span><span id="________HELP______"></span> **/help**
Displays command-line help.

For more information about the use of these commands, see [Controlling Driver Verifier](controlling-driver-verifier.md) and [Monitoring Driver Verifier](monitoring-driver-verifier.md).

## Return Codes

The following values are returned after driver verifier has run.

**0**: EXIT\_CODE\_SUCCESS

**1**: EXIT\_CODE\_ERROR

**2**: EXIT\_CODE\_REBOOT\_NEEDED

