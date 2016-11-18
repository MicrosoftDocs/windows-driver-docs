---
title: Verification Process
description: Verification Process
ms.assetid: 3803771b-94ef-4e02-9d08-8703283b3f99
keywords: ["Static Driver Verifier WDK , verification process", "StaticDV WDK , verification process", "SDV WDK , verification process", "verification process WDK Static Driver Verifier"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Verification%20Process%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




