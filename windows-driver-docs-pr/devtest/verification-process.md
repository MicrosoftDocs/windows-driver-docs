---
title: Verification Process
description: Verification Process
ms.assetid: 3803771b-94ef-4e02-9d08-8703283b3f99
keywords:
- Static Driver Verifier WDK , verification process
- StaticDV WDK , verification process
- SDV WDK , verification process
- verification process WDK Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Verification Process


SDV conducts a *verification*, that is, a test to determine whether the driver's actual behavior complies with rules that define proper behavior.

When you submit a command to verify a driver, SDV performs a three-step process, during which it determines which files it needs, prepares the files, and verifies the driver.

This topic describes what happens in each of the steps of the verification process.

### <span id="build"></span><span id="BUILD"></span>Build

During the **Build** step, SDV compiles, links, and builds the driver using MSBuild.

### <span id="scan"></span><span id="SCAN"></span>Scan

During the **Scan** step, SDV scans your driver's code for function role type declarations, assembles a list of driver entry points, and creates the [Sdv-map.h](sdv-map-h.md) file in the directory that stores the *sources* file for the driver (known as the **driver's sources directory**).

### <span id="check"></span><span id="CHECK"></span>Check

During the **Check** step, SDV prepares for and verifies the driver by using the rules that you selected for the verification. For more information about the rules that you can select, see [Static Driver Verifier Rules](https://msdn.microsoft.com/library/windows/hardware/ff551714).

SDV begins by determining if the selected rules require additional components of the operating system model. If they do, SDV copies the additional operating system model files into the driver's sources directory.

Next, the driver files, library files, rule code (*RuleName*.slic) files, and operating system model files are linked into a single executable file for the verification.

The SDV verification engine then verifies one rule at a time, until it verifies all selected rules.

During this step, SDV creates a subdirectory for each rule that it verified in the *DriverPath*\\sdv\\check directory.

### <span id="comment"></span><span id="COMMENT"></span>Comment

While SDV performs the steps in the verification process, it writes status messages to the command line, along with error messages that report errors that arise in each step. For information about the status messages, see [Command-Line Output](command-line-output.md). For information about the error messages, see [Static Driver Verifier Error Messages](static-driver-verifier-error-messages.md). For information about enabling diagnostics to help you and Microsoft troubleshoot problems with SDV, see [Static Driver Verifier Diagnostics](static-driver-verifier-diagnostics.md).

 

 





