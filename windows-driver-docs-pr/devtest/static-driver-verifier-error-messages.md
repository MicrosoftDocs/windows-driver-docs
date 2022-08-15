---
title: Static Driver Verifier Error Messages
description: Static Driver Verifier Error Messages
keywords:
- Static Driver Verifier WDK , errors
- StaticDV WDK , errors
- SDV WDK , errors
- messages WDK Static Driver Verifier
- errors WDK Static Driver Verifier
ms.date: 04/02/2018
---

# Static Driver Verifier Error Messages


This section explains the meaning of some of the more frequently seen SDV error messages and suggests methods for resolving them.

When launching SDV from Visual Studio, you may see the following errors:

* **SDV only operates on non-debug configurations**: As the message says, SDV must be run on a non-debug configuration.  Please ensure your project is set to a Release configuration or create one if not available and re-launch SDV.
* **There was an error loading the available rules**: SDV either cannot find the rules for your driver model or cannot determine the driver model correctly (much more likely if your driver is not a WDM, KMDF, NDIS, or Storport driver).  If your WDK is correctly installed, you may be able to work around this error by running SDV from the command line directly (see [Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md)).
* **SDV was unable to clean the driver directory**: In some cases, permissions errors may prevent SDV from correctly cleaning old results from the driver directory when you click the "Clean" button.  This error will also occur if the sdv files from previous runs are currently in use.  Ensure nothing is using the SDV files in your driver directory, then remove any "sdv" and "sdv.temp" folders and any "staticdv.job" files.

If SDV fails while attempting analysis, it will print the stage it failed in to standard output.  When running SDV from the Visual Studio GUI, you can see this output by switching to the "Alerts" tab.

The stages SDV may fail in are:
* **NormalBuild**: SDV was unable to build the driver using standard MSBuild commands.  This may occur if you have specialized build logic, rely on solution elements in your project file, or have external build components.  If your project relies on the $(SolutionDir) property, you can supply this variable directly by re-running SDV from the command line and appending it to the command line by adding **/p:SolutionDir=\[your solution dir\]** to the end of the MSBuild command.  See [Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md).
* **InterceptedBuild**: SDV was unable to build the driver for analysis.  
* **Scan**: SDV was unable to find the entry points of the driver.  An error here may indicate that no entry points were found and you should update your function roletypes or sdv-map.h.  See [Using Function Role Type Declarations](using-function-role-type-declarations.md) and [Approving the Sdv-map.h File](approving-the-sdv-map-h-file.md) for more information.
* **FinalCompile**: SDV was unable to compile your driver with the rule and OS model.
* **CheckRule**: SDV was unable to correctly verify the rule.

You may be able to learn more details about the error by enabling diagnostics for SDV.  Please see [Static Driver Verifier Diagnostics](static-driver-verifier-diagnostics.md) for details.
