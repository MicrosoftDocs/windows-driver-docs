---
title: Files in the Source Code Pane
description: Files in the Source Code Pane
ms.assetid: 1bc248be-cdc8-4e6c-9eca-da2943daaf58
keywords: ["Static Driver Verifier Report WDK , Source Code pane", "Source Code pane WDK Static Driver Verifier", "files WDK Static Driver Verifier"]
---

# Files in the Source Code Pane


Files appear in the **Source Code** pane only when the code that they contain is involved in causing or detecting the rule violation. As a result, different files appear in the window for different rule violations by the same driver.

The following types of files appear in the source code pane:

<span id="Driver_source_files"></span><span id="driver_source_files"></span><span id="DRIVER_SOURCE_FILES"></span>**Driver source files**  
Source files for the driver, and for the libraries that it uses, that are involved in the rule violation. This group of files includes C files and header files.

<span id="rule_source_file___________________.slic__"></span><span id="RULE_SOURCE_FILE___________________.SLIC__"></span>**Rule source file (\*** **.slic** **)**  
The source file for the [Static Driver Verifier rules](static-driver-verifier-rule.md) in the verification. This code is written in Specification Language for Interface Checking (SLIC), a simple language that was developed for this purpose.

<span id="sdv-harness.c_"></span><span id="SDV-HARNESS.C_"></span>**sdv-harness.c**   
The source file for the SDV [operating system model](operating-system-model.md) for the rules in the verification.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Files%20in%20the%20Source%20Code%20Pane%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




