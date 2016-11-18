---
title: Command-Line Output
description: Command-Line Output
ms.assetid: 21225785-e8b8-4488-b0a0-fe4cea50d1ff
keywords: ["output files WDK Static Driver Verifier", "command-line output WDK Static Driver Verifier"]
---

# Command-Line Output


When you submit a command to SDV, it displays a header with version information, status messages that indicate the success or failure of the command, and any error messages or warnings that might have been generated. A summary of the results of the verification appears at the bottom of the output.

For example, the following illustration shows the command-line output from a command to verify the Fail\_Driver1 sample driver with the rules in the Config.sdv[rule list file](static-driver-verifier-rule-list-file.md). The Fail\_Driver1 sample driver, a driver with intentional coding errors, and the Config.sdv file are installed in the \\tools\\sdv\\sample\\fail\_drivers\\wdm\\fail\_driver1 subdirectory of the WDK.

In this verification, SDV found four defects, one for each rule that it verified.

``` syntax
C:\Program Files (x86)\Windows Kits\8.0\Tools\sdv\samples\fail_drivers\wdm\fail_driver1>msbuild fail_driver1.vcxproj /t:sdv /p:inputs="/check=config.sdv" /p:configuration="Win8 beta release" /p:platform=win32
Microsoft (R) Build Engine version 4.0.30319.17369
[Microsoft .NET Framework, version 4.0.30319.17369]
Copyright (C) Microsoft Corporation. All rights reserved.

Build started 1/25/2012 12:24:58 PM.
Project "c:\Program Files (x86)\Windows Kits\8.0\Tools\sdv\samples\fail_drivers\wdm\fail_driver1\fail_driver1.vcxproj"on node 1 (sdv target(s)).
Sdv:
  staticdv.exe /check=config.sdv
  ---------------------------------------------------------------------
  Microsoft (R) Windows (R) Static Driver Verifier Version 2.1.468.0
  Copyright (C) Microsoft Corporation.  All rights reserved.
  ---------------------------------------------------------------------
  SDV is building for <Win8 beta release|win32>
  Build     'fail_driver1'  ...Done
  Scan      'fail_driver1'  ...Done
  No reuse data to copy from previous SDV run.
  Compile   'fail_driver1' for [sdv_flat_dispatch_harness] ...Done
  Compile   'fail_driver1' for [sdv_flat_dispatch_startio_harness] ...Done
  Compile   'fail_driver1' for [sdv_flat_simple_harness] ...Done
  Compile   'fail_driver1' for [sdv_flat_simple_harness] ...Done
  Compile   'fail_driver1' for [sdv_flat_simple_harness] ...Done
  Compile   'fail_driver1' for [sdv_flat_simple_harness] ...Done
  Compile   'fail_driver1' for [sdv_flat_simple_harness] ...Done
  Compile   'fail_driver1' for [sdv_flat_simple_harness] ...Done
  Compile   'fail_driver1' for [sdv_flat_harness] ...Done
  Compile   'fail_driver1' for [sdv_flat_harness] ...Done
  Compile   'fail_driver1' for [sdv_flat_harness] ...Done
  PreCheck  'fail_driver1' for 'checkirpmjpnp' ...Running
  PreCheck  'fail_driver1' for 'checkdriverunload' ...Running
  PreCheck  'fail_driver1' for 'workerthread' ...Running
  PreCheck  'fail_driver1' for 'checkadddevice' ...Running
  PreCheck  'fail_driver1' for 'checkirpmjpnp'  ...Done
  PreCheck  'fail_driver1' for 'checkadddevice'  ...Done
  PreCheck  'fail_driver1' for 'checkdriverunload'  ...Done
  PreCheck  'fail_driver1' for 'workerthread'  ...Done
  PreCheck  'fail_driver1' for 'iocompletion' ...Running
  PreCheck  'fail_driver1' for 'isrroutine' ...Running
  PreCheck  'fail_driver1' for 'kedpcroutine' ...Running
  PreCheck  'fail_driver1' for 'iodpcroutine' ...Running
  PreCheck  'fail_driver1' for 'iodpcroutine'  ...Done
  PreCheck  'fail_driver1' for 'iocompletion'  ...Done
  PreCheck  'fail_driver1' for 'isrroutine'  ...Done
  PreCheck  'fail_driver1' for 'kedpcroutine'  ...Done
  PreCheck  'fail_driver1' for 'startioroutine' ...Running
  PreCheck  'fail_driver1' for 'dispatchroutine' ...Running
  PreCheck  'fail_driver1' for 'cancelroutine' ...Running
  PreCheck  'fail_driver1' for 'dispatchroutine'  ...Done
  PreCheck  'fail_driver1' for 'startioroutine'  ...Done
  PreCheck  'fail_driver1' for 'cancelroutine'  ...Done
  Compile   'fail_driver1' for [sdv_xflat_harness_cancel] ...Done
  Compile   'fail_driver1' for [sdv_flat_simple_harness] ...Done
  Compile   'fail_driver1' for [sdv_flat_simple_harness] ...Done
  Compile   'fail_driver1' for [sdv_simple_harness_with_completion_no_cancel] ...Done
  Compile   'fail_driver1' for [sdv_flat_harness] ...Done
  Check     'fail_driver1' for 'spinlock' ...Running
  Check     'fail_driver1' for 'irqlkesetevent' ...Running
  Check     'fail_driver1' for 'lowerdriverreturn' ...Running
  Check     'fail_driver1' for 'irqlioapclte' ...Running
  Check     'fail_driver1' for 'irqlioapclte'  ...Done
  Check     'fail_driver1' for 'spinlock'  ...Done
  Check     'fail_driver1' for 'irqlkesetevent'  ...Done
 Check     'fail_driver1' for 'cancelspinlock' ...Running
  Check     'fail_driver1' for 'cancelspinlock'  ...Done
  Check     'fail_driver1' for 'lowerdriverreturn'  ...Done
  SDV checked 11 properties(s).
  SDV performed 5 check(s) with:
        5  Defect(s)
  Run this command to view the results:msbuild <driver project file> /p:configuration="<release configuration>" /p:platform=<Win32|x64> /t:Sdv /p:inputs="/view"

  Merging results
  Nothing to merge for c:\Program Files (x86)\Windows Kits\8.0\Tools\sdv\samples\fail_drivers\wdm\fail_driver1
  SDV exit code: 0
Done Building Project "c:\Program Files (x86)\Windows Kits\8.0\Tools\sdv\samples\fail_drivers\wdm\fail_driver1\fail_driver1.vcxproj" (sdv target(s)).


Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:02:12.14
```

After viewing the results summary to see which rules were violated, you can specify the **/view** option in an MSBuild command to see the Static Driver Verifier Report. For information about the command options, see [Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md). For information about the **Build** and **Check** steps in the output, see [Verification Process](verification-process.md).

The following table describes the results that can appear in the results summary.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Result Types</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Rule Passes</strong></p></td>
<td align="left"><p>The number of rules that SDV verified, but for which it could not prove any violation of the rule.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Defects</strong></p></td>
<td align="left"><p>The number of rule violations that SDV detected.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Not Applicable</strong></p></td>
<td align="left"><p>The number of rules that SDV could not verify, either because the driver did not support the entry point that is required for the analysis, or because the driver did not call the function that the rule monitors.</p>
<p>If this value is greater than 0, verify that the [Sdv-map.h](sdv-map-h.md) file content is correct.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Timeouts</strong></p></td>
<td align="left"><p>The number of rules that SDV stopped verifying because it exceeded its time limit for verifying each rule. The time limit is set in the [Static Driver Verifier Options File](static-driver-verifier-options-file.md), Sdv-default.xml.</p>
<p>This result is caused by limitations in SDV. It does not indicate an error in the driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Spaceouts</strong></p></td>
<td align="left"><p>The number of rules that SDV stopped verifying because it exceeded the memory limit for verifying the rule. The memory limit is set in the [Static Driver Verifier Options File](static-driver-verifier-options-file.md), Sdv-default.xml.</p>
<p>This result is caused by limitations in SDV. It does not indicate an error in the driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Other</strong></p></td>
<td align="left"><p>The number of times that SDV encountered an internal error from which it could not recover.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Command-Line%20Output%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




