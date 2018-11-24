---
title: Static Driver Verifier Input Files
description: Static Driver Verifier Input Files
ms.assetid: 0c31a752-6946-4704-aff6-c9cd1bf9f522
keywords:
- Static Driver Verifier WDK , input files
- StaticDV WDK , input files
- SDV WDK , input files
- input files WDK Static Driver Verifier
- files WDK Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Static Driver Verifier Input Files


The SDV [verification engine](verification-engine.md) takes the following files as input to a verification. Only the driver source files and operating system model files are required for all verifications.

-   Driver project file and source code. Run SDV in the directory where the project file is located.

-   [Operating system model files](operating-system-model.md). SDV selects and assembles the operating system model files based on the rules that you select for the verification.

-   [Processed library files](library-processing-in-static-driver-verifier.md). Library files are required only when the driver depends on non-system libraries. For information and instructions, see Library Processing in Static Driver Verifier.

-   [Rule list file](static-driver-verifier-rule-list-file.md). See [Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md).

-   [Static Driver Verifier Options File](static-driver-verifier-options-file.md). SDV creates a global options file that contains settings that apply to all SDV verifications. To create a local options file for a driver, copy the global options file. You can then edit the copy of the global options file to create a local options file for the driver.

When evaluating the results of a SDV verification, it is very important to examine the input files to confirm the accuracy and completeness of all input files that were used in the verification.

This section includes detailed descriptions of the following files:

[Static Driver Verifier Rule List File](static-driver-verifier-rule-list-file.md)

[Static Driver Verifier Options File](static-driver-verifier-options-file.md)

 

 





