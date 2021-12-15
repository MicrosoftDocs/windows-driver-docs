---
title: Static Driver Verifier Diagnostics
description: Static Driver Verifier Diagnostics
ms.date: 04/20/2017
---

# Static Driver Verifier Diagnostics


SDV has a diagnostics mode that can help you and Microsoft troubleshoot problems that SDV might encounter. When diagnostics mode is enabled, SDV logs messages to a series of files in your driver project, one per stage of verification and per rule.

### <span id="enabling_diagnostics"></span><span id="ENABLING_DIAGNOSTICS"></span>Enabling Diagnostics

Diagnostics mode for SDV (also known as debug mode) can currently only be enabled when running from the command line.  For more details on running from the command line, see [Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md).

To activate diagnostics, add the **/debug** flag after a **/check** command.  For example:

```
msbuild /t:sdv /p:Inputs="/check:* /debug" mydriver.VcxProj /p:Configuration="Release" /p:Platform=x64
```

Enabling diagnostics will result in significantly more output to the command window, as well as the creation of specific log files.

### <span id="enabling_diagnostics"></span><span id="ENABLING_DIAGNOSTICS"></span>Understanding Diagonistics

SDV will create several files at each stage of execution which will provide details on that step.  When SDV fails partway through execution, it will not create any diagonistic files for later stages.

The files created are, in order:
* **smvexecute-NormalBuild.log**: This is located in your driver's source directory and shows the output of SDV's initial attempt to build the driver without additional instrumentation and analysis.
* **smvexecute-InterceptedBuild.log**: This is located in your driver's source directory and shows the output of SDV building the driver with analysis hooks added.  
* **smvcl.log**: This is located in the "sdv" directory created in your driver project by SDV.  It shows the compiler output of the InterceptedBuild step.  If you see a failure in **smvexecute-InterceptedBuild.log**, you may be able to find additional details in **smvcl.log.**

* **smvexecute-Scan.log**: This is located in the "sdv" directory created in your driver project by SDV.  It shows the output of SDV's attempt to scan the driver to find entry points.  An error here may indicate that no entry points were found and you should update your function roletypes or sdv-map.h.  See [Using Function Role Type Declarations](using-function-role-type-declarations.md) and [Approving the Sdv-map.h File](approving-the-sdv-map-h-file.md) for more information.
* **smvexecute-FinalCompile.log**: One of these files is created for each rule verified by sdv, and can be found in the "sdv\check\[rule name]" subfolder SDV creates in your driver project.  This file shows the output of SDV's attempt to build the driver with the OS model and specific rule.  
* **smvexecute-CheckRule.log**: One of these files is created for each rule verified by sdv, and can be found in the "sdv\check\[rule name]" subfolder SDV creates in your driver project.  This file shows the output of SDV's attempt to verify the specified rule against your driver.

You should look for the file corresponding to the stage listing as failed in the command output.  If the failure occurred in the **FinalCompile** or **CheckRule** steps, be sure to check the folder for the specific rule listed as failing.
