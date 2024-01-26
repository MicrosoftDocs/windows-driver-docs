---
title: Static Driver Verifier Commands (MSBuild)
description: Commands used with Static Driver Verifier
ms.date: 04/20/2017
---

# Static Driver Verifier commands (MSBuild)

You can run Static Driver Verifier (SDV) in a **Visual Studio Command Prompt** window, either through installing the Windows Driver Kit (WDK) or by running the Enterprise Windows Driver Kit (EWDK). Navigate to the directory where the driver's project file or the library's project file is stored. The parameters can appear in any order on the command line.

>[!NOTE]
>SDV is integrated into Visual Studio upon installation of the WDK and can also be run from the IDE via the "Driver" menu.

```command
msbuild /t:sdv /p:Inputs="Parameters" ProjectFile /p:Configuration=configuration /p:Platform=platform
```

You must select a Release configuration (for example, **/p:Configuration="Windows 7 Release"**). For the list of supported Release Configurations, see [Building a Driver](../develop/building-a-driver.md). The Platform can be **Win32** (for x86) or **x64** (for example, **/p:Platform=Win32**).

>[!NOTE]
>Be sure to check your computer's power management plan to ensure the computer will not go into a sleep state during the analysis.

## Parameters

### /**scan**

Scans the driver's source code for function role type declarations. For information about how to declare the driver supplied callback functions and dispatch routines, see [Using Function Role Type Declarations](using-function-role-type-declarations.md). During this scan, SDV tries to detect the driver entry points that it needs to verify the driver. It records the results of the scan in [Sdv-map.h](sdv-map-h.md), a file that it creates in the driver's project directory.

For more information, see [Preparing your source code](using-static-driver-verifier-to-find-defects-in-drivers.md#preparing-your-source-code).

### **/check:**<em>Rule</em> | *Rule*,...  

Starts a verification with the specified rule(s). You can specify more than one rule by separating each rule with a comma. Run the **/check:** command and specify the driver's Visual Studio project file (\*.vcxproj).

*Rule* is the name of one [rule](static-driver-verifier-rule.md) or a rule name pattern that includes wildcard characters (\*) to represent one or more characters. When used alone, the wildcard character (\*) represents all rules.

### **/check:*RuleList*.sdv**

Starts a verification with the rules in the specified rule list file. You can list only one file with this parameter. In the rule list file, each line can be the name of one rule or it can be a wildcard character (\*), which represents all SDV rules.  Run **/check:*RuleList*.sdv** command and specify the driver's Visual Studio project file (\*.vcxproj).

<em>RuleList</em>**.sdv** is the fully qualified path and file name of a [rule list file](static-driver-verifier-rule-list-file.md). The file must have the **.sdv** file name extension. Unless the file is in the local directory, the path is required. If the path or file name includes spaces, you must enclose <em>RuleList.</em>**sdv** in quotation marks.

If you specify the **/check:** option without specifying a rule, SDV runs with the default rule set for the driver model.

### **/lib**

Processes the library in the current directory. SDV calls MSBuild.exe to compile and build the library for external use, and it generates the files that it needs to include the library in the driver verification.

Use this parameter before verifying drivers that require the library. Run the **msbuild /t:sdv /p:Inputs="/lib"** command and specify the Visual Studio project file (\*.vcxproj) for the library.

For more information about the use and effect of the **/lib** parameter, see [Library Processing in Static Driver Verifier](library-processing-in-static-driver-verifier.md).

### **/view**

Opens Static Driver Verifier. Run **/view** commands and specify the driver's Visual Studio project file (\*.vcxproj).

The results are available as soon as a verification is complete, and remain available until you use a **/clean** command to delete the SDV files from the driver's project directory.

### **/clean**

Deletes SDV files from the directory. Because these files are used to generate the Static Driver Verifier Report display, the **/clean** command also deletes the report of the verification.

Run a **/clean** command and specify the Visual Studio project file (\*.vcxproj) for the driver or library. The command deletes SDV files only for the project specified.

Run a **/clean** command for a driver project before each verification.

Run a **/clean** command for a library when the library files are outdated, such as when the library code changes.

A **/clean** command does not remove the Sdv-map.h file, if the approved flag is set to true in the Sdv-map.h file (Approved=true). SDV can then use this file for future verifications.

### **/?**

Displays usage for SDV commands. Commands that use this parameter do not have to be run in a build environment window.

## Comments

Running **msbuild /t:/sdv p:/Inputs= /?** without parameters displays usage for the SDV commands.

A **/clean** command deletes the files that SDV uses to create the Static Driver Verifier Report display for a verification. After running this command, the Static Driver Verifier Report display for the verification is no longer available.

## Examples

To run SDV using all rules on the driver files in the local directory for the mydriver project:

```command
msbuild /t:sdv /p:Inputs="/check:*" mydriver.VcxProj /p:Configuration="Windows 7 Release"/p:Platform=Win32
```

To run SDV using the [CancelSpinLock](./wdm-cancelspinlock.md) rule on the driver files in the local directory:

```command
msbuild /t:sdv /p:Inputs="/check:CancelSpinLock" mydriver.VcxProj /p:Configuration="Windows 7 Release" /p:Platform=Win32
```

To run SDV using the rule that is specified in the Rules1.sdv rule list file in the D:\\SDV directory:

```command
msbuild /t:sdv /p:Inputs="/check:D:\SDV\Rules1.sdv" mydriver.VcxProj /p:Configuration="Windows 7 Release" /p:Platform=Win32
```

To run SDV again, this time using the /clean option:

```command
msbuild /t:sdv /p:Inputs="/clean" mydriver.VcxProj /p:Configuration="Windows 7 Release"/p:Platform=Win32
```

To display Static Driver Verifier so that you can view the results for the most recent verification of the driver in the local directory:

```command
msbuild /t:sdv /p:Inputs="/view" mydriver.VcxProj /p:Configuration="Windows 7 Release" /p:Platform=Win32
```

## Related topics

[Using Static Driver Verifier to Find Defects in Windows Drivers](using-static-driver-verifier-to-find-defects-in-drivers.md)
