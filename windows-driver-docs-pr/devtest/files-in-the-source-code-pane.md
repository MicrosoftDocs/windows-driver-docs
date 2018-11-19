---
title: Files in the Source Code Pane
description: Files in the Source Code Pane
ms.assetid: 1bc248be-cdc8-4e6c-9eca-da2943daaf58
keywords:
- Static Driver Verifier Report WDK , Source Code pane
- Source Code pane WDK Static Driver Verifier
- files WDK Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Files in the Source Code Pane


Files appear in the **Source Code** pane only when the code that they contain is involved in causing or detecting the rule violation. As a result, different files appear in the window for different rule violations by the same driver.

The following types of files appear in the source code pane:

<span id="Driver_source_files"></span><span id="driver_source_files"></span><span id="DRIVER_SOURCE_FILES"></span>**Driver source files**  
Source files for the driver, and for the libraries that it uses, that are involved in the rule violation. This group of files includes C files and header files.

<span id="rule_source_file___________________.slic__"></span><span id="RULE_SOURCE_FILE___________________.SLIC__"></span>**Rule source file (\\*** **.slic** **)**  
The source file for the [Static Driver Verifier rules](static-driver-verifier-rule.md) in the verification. This code is written in Specification Language for Interface Checking (SLIC), a simple language that was developed for this purpose.

<span id="sdv-harness.c_"></span><span id="SDV-HARNESS.C_"></span>**sdv-harness.c**   
The source file for the SDV [operating system model](operating-system-model.md) for the rules in the verification.

 

 





