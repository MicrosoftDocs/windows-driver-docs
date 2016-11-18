---
title: Static Driver Verifier Input Files
description: Static Driver Verifier Input Files
ms.assetid: 0c31a752-6946-4704-aff6-c9cd1bf9f522
keywords: ["Static Driver Verifier WDK , input files", "StaticDV WDK , input files", "SDV WDK , input files", "input files WDK Static Driver Verifier", "files WDK Static Driver Verifier"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Static%20Driver%20Verifier%20Input%20Files%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




