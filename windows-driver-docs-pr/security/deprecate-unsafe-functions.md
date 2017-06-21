---
title: Deprecate unsafe functions
description: Create a process to look for and remove code vulnerabilities from your driver code.
ms.assetid: E61A5557-EBEF-43F3-850C-0DE35F6462AA
ms.author: windowsdriverdev
ms.date: 06/06/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Deprecate unsafe functions


Create a process to look for and remove code vulnerabilities from your driver code. Because driver code is highly specialized, and threats continue to evolve, a single checklist cannot apply uniformly to all drivers. The following are general points to consider when creating drivers.

## <span id="Operating_system_and_compiler_features"></span><span id="operating_system_and_compiler_features"></span><span id="OPERATING_SYSTEM_AND_COMPILER_FEATURES"></span>Operating system and compiler features


Be aware of changes in the operating system and compilers. New releases often contain new features that can help you to prevent or mitigate security threats.

For example, going back to the release of the Windows XP, Microsoft added safe string functions, which replaced the standard C/C++ string manipulation functions (strcat, strcpy and so on). The standard C/C++ functions do not enforce buffer sizes, thus allowing applications to write beyond the end of a buffer. The safe string functions prevent this error.

**Important**  All drivers should use the safe string functions. For more information, see [Using Safe String Functions](https://msdn.microsoft.com/library/windows/hardware/ff565508) and the header file Ntstrsafe.h.

 

## <span id="Driver_testing"></span><span id="driver_testing"></span><span id="DRIVER_TESTING"></span>Driver testing


Use driver development and testing tools available in the Windows Development Kit (WDK). The WDK includes tools such as Static and dynamic Driver Verifier and driver specific code analysis. These tools can find some types of bugs in driver code and can also find unsafe and insecure coding practices that lead to security issues.

For more information about these tools, see [Tools for Verifying Drivers](https://msdn.microsoft.com/windows/hardware/drivers/devtest/tools-for-verifying-drivers).

## <span id="Driver_specific_code_analysis"></span><span id="driver_specific_code_analysis"></span><span id="DRIVER_SPECIFIC_CODE_ANALYSIS"></span>Driver specific code analysis


Driver specific code analysis uses a set of rules that are installed with the WDK to examine code in Visual Studio. For more information see [Code Analysis for drivers overview](https://msdn.microsoft.com/windows/hardware/drivers/devtest/code-analysis-for-drivers-overview).

## <span id="HLK_tests"></span><span id="hlk_tests"></span><span id="HLK_TESTS"></span>HLK tests


The Windows Hardware Lab Kit (Windows HLK) is a test framework used to test hardware devices. For more information, see [Windows Hardware Lab Kit](https://msdn.microsoft.com/library/windows/hardware/dn930814) in [Test for performance and compatibility](https://msdn.microsoft.com/windows/hardware/commercialize/test/index).

## <span id="Kernel-mode_drivers"></span><span id="kernel-mode_drivers"></span><span id="KERNEL-MODE_DRIVERS"></span>Kernel-mode drivers


Kernel-mode drivers run in the trusted system address space and are, in effect, extensions of the operating system. Kernel-mode drivers must validate all data and addresses that originate with user-mode processes.

Numerous security and reliability issues apply to kernel-mode drivers. The following are a few examples of the areas in which kernel-mode drivers can be vulnerable to security threats:

-   Handling unexpected IOCTLs
-   Validating buffer lengths
-   Handling IOCTLs that permit FILE\_ANY\_ACCESS
-   Securing device objects
-   Securing Registry keys
-   Handling user-mode buffers
-   Using handles that are passed from user mode to kernel mode

For information about specific points at which kernel-mode drivers might be vulnerable, see the resources listed at the end of this topic and the white paper titled *Common Driver Reliability Issues* available for download at <http://www.microsoft.com/whdc/driver/security/drvqa.mspx>. All writers of kernel-mode drivers should become familiar with this material.

## <span id="Resources"></span><span id="resources"></span><span id="RESOURCES"></span>Resources


-   *24 Deadly Sins of Software Security : Programming Flaws and How to Fix Them*, by Michael Howard, David LeBlanc and John Viega
-   *Writing Secure Software*The art of software security assessment : identifying and preventing software vulnerabilities by Mark Dowd, John McDonald and Justin Schuh
-   *Writing Secure Software* Second Edition, by Michael Howard and David LeBlanc

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[hw_design\hw_design]:%20Deprecate%20unsafe%20functions%20%20RELEASE:%20%286/16/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




