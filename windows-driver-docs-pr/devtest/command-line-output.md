---
title: Command-Line Output
description: Command-Line Output
ms.assetid: 21225785-e8b8-4488-b0a0-fe4cea50d1ff
keywords:
- output files WDK Static Driver Verifier
- command-line output WDK Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Command-Line Output


When you submit a command to SDV, it displays information about the command as it executes, status messages that indicate the success or failure of the command, and any error messages or warnings that might have been generated. A summary of the results of the verification appears at the bottom of the output.

For example, the following illustration shows the command-line output from a command to verify the SDV-FailDriver-WDM sample driver with the [SpinLock](wdm-spinlock.md) rule. The SDV-FailDriver-WDM sample driver, a driver with intentional coding errors, is located in the \\tools\\sdv\\samples\\Sdv-FailDriver-WDM folder of the Windows Driver Samples.

In this verification, SDV found that the driver violated the rule.

```
G:\Windows-driver-samples\tools\sdv\samples\SDV-FailDriver-WDM\driver>msbuild /p:Configuration=Release /p:Platform=x64 /t:sdv /p:inputs=/check:spinlock
Microsoft (R) Build Engine version 15.6.82.30579 for .NET Framework
Copyright (C) Microsoft Corporation. All rights reserved.

Build started 3/30/2018 10:56:50 AM.
Project "G:\Windows-driver-samples\tools\sdv\samples\SDV-FailDriver-WDM\driver\fail_driver1.vcxproj" on node 1 (sdv tar
get(s)).
sdv:
  staticdv /check:spinlock
  SDV: H:\Program Files\Windows Kits\10\TOOLS\SDV
  SMV: H:\Program Files\Windows Kits\10\TOOLS\SDV\smv
  SDVAP: H:\Program Files\Windows Kits\10\TOOLS\SDV\smv\analysisplugins\sdv
  Build environment: msbuild
  [INFO] Cleaning ...
  [INFO] Setting interceptor platform to x64
  [INFO] Setting platform to x86_amd64
  [INFO] Validating XML against schema: H:\Program Files\Windows Kits\10\TOOLS\SDV\smv\bin\Config.xsd
  [INFO] Running local scheduler with 8 threads
  [INFO] Driver type found: wdm
  [INFO] Currently reading and validating XML settings from H:\Program Files\Windows Kits\10\TOOLS\SDV\data\wdm\sdv-def
  ault.xml

  [INFO] 1 of 2 jobs remaining. Avg(s): 8.00. Std.Dev(s): 0.00
  [INFO] 1 of 3 jobs remaining. Avg(s): 9.00. Std.Dev(s): 1.00
  Scan ...Done

  [INFO] 0 of 3 jobs remaining. Avg(s): 6.00. Std.Dev(s): 4.32

  Building ...Done
  [INFO] Using plugin SdvPlugin.SmvSdv for analysis.
  [INFO] Running analysis on 11 precondition(s) & 1 rule(s) ...
  [INFO] Checking preconditions...

  [INFO] 10 of 15 jobs remaining. Avg(s): 7.20. Std.Dev(s): 3.66
  [INFO] 10 of 16 jobs remaining. Avg(s): 7.50. Std.Dev(s): 3.40
  [INFO] 11 of 17 jobs remaining. Avg(s): 7.50. Std.Dev(s): 3.40
  [INFO] 10 of 18 jobs remaining. Avg(s): 9.13. Std.Dev(s): 4.08
  [INFO] 11 of 19 jobs remaining. Avg(s): 9.13. Std.Dev(s): 4.08
  [INFO] 10 of 20 jobs remaining. Avg(s): 11.30. Std.Dev(s): 5.68
  [INFO] 11 of 21 jobs remaining. Avg(s): 11.30. Std.Dev(s): 5.68
  [INFO] 11 of 22 jobs remaining. Avg(s): 12.18. Std.Dev(s): 6.09
  [INFO] 10 of 22 jobs remaining. Avg(s): 11.92. Std.Dev(s): 5.89
  [INFO] 10 of 23 jobs remaining. Avg(s): 12.15. Std.Dev(s): 5.72
  [INFO] 10 of 24 jobs remaining. Avg(s): 12.64. Std.Dev(s): 5.79
  [INFO] 7 of 25 jobs remaining. Avg(s): 13.50. Std.Dev(s): 5.80
  [INFO] 7 of 25 jobs remaining. Avg(s): 13.50. Std.Dev(s): 5.80
  [INFO] 7 of 25 jobs remaining. Avg(s): 13.50. Std.Dev(s): 5.80
  [INFO] 7 of 25 jobs remaining. Avg(s): 13.50. Std.Dev(s): 5.80
  [INFO] 6 of 25 jobs remaining. Avg(s): 13.42. Std.Dev(s): 5.65
  [INFO] 5 of 25 jobs remaining. Avg(s): 13.75. Std.Dev(s): 5.69
  [INFO] 4 of 25 jobs remaining. Avg(s): 13.95. Std.Dev(s): 5.63
  [INFO] 3 of 25 jobs remaining. Avg(s): 14.09. Std.Dev(s): 5.53
  [INFO] 2 of 25 jobs remaining. Avg(s): 14.13. Std.Dev(s): 5.42
  [INFO] 1 of 25 jobs remaining. Avg(s): 14.17. Std.Dev(s): 5.30
  [INFO] 0 of 25 jobs remaining. Avg(s): 14.20. Std.Dev(s): 5.20
  [INFO] Precondition check(s) completed.
  [INFO] Verifying rules...

  [INFO] 1 of 27 jobs remaining. Avg(s): 13.65. Std.Dev(s): 5.78
  [INFO] 1 of 28 jobs remaining. Avg(s): 13.37. Std.Dev(s): 5.86
  [INFO] 0 of 28 jobs remaining. Avg(s): 13.21. Std.Dev(s): 5.81

  [INFO] 1 defects found.
  [INFO] Please review using '/view' argument for SDV.

  [INFO] Total time taken 96 seconds
  [INFO] Found 1 bugs!
Done Building Project "G:\Windows-driver-samples\tools\sdv\samples\SDV-FailDriver-WDM\driver\fail_driver1.vcxproj" (sdv
 target(s)).


Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:01:37.93
```

After viewing the results summary to see which rules were violated, you can specify the **/view** option in an MSBuild command to see the Static Driver Verifier Report. For information about the command options, see [Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md). For information about the **Scan**, **Build** and **Check** steps in the output, see [Verification Process](verification-process.md).

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
<p>If this value is greater than 0, verify that the <a href="sdv-map-h.md" data-raw-source="[Sdv-map.h](sdv-map-h.md)">Sdv-map.h</a> file content is correct.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Timeouts</strong></p></td>
<td align="left"><p>The number of rules that SDV stopped verifying because it exceeded its time limit for verifying each rule. The time limit is set in the <a href="static-driver-verifier-options-file.md" data-raw-source="[Static Driver Verifier Options File](static-driver-verifier-options-file.md)">Static Driver Verifier Options File</a>, Sdv-default.xml.</p>
<p>This result is caused by limitations in SDV. It does not indicate an error in the driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Spaceouts</strong></p></td>
<td align="left"><p>The number of rules that SDV stopped verifying because it exceeded the memory limit for verifying the rule. The memory limit is set in the <a href="static-driver-verifier-options-file.md" data-raw-source="[Static Driver Verifier Options File](static-driver-verifier-options-file.md)">Static Driver Verifier Options File</a>, Sdv-default.xml.</p>
<p>This result is caused by limitations in SDV. It does not indicate an error in the driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Other</strong></p></td>
<td align="left"><p>The number of times that SDV encountered an internal error from which it could not recover.</p></td>
</tr>
</tbody>
</table>

 

 

 





