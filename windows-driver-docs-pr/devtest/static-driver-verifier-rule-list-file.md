---
title: Static Driver Verifier Rule List File
description: Static Driver Verifier Rule List File
ms.assetid: 941df64c-b66b-4e7b-b340-9ef6b57d895d
keywords:
- Static Driver Verifier WDK , input files
- StaticDV WDK , input files
- SDV WDK , input files
- input files WDK Static Driver Verifier
- files WDK Static Driver Verifier
- rules WDK Static Driver Verifier
- rule list files WDK Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Static Driver Verifier Rule List File


A SDV rule list file is a text file that lists one or more [Static Driver Verifier rule](https://msdn.microsoft.com/library/windows/hardware/ff551714) or rule name patterns, with one rule or rule name pattern on each line. The rules can appear in any order and they are verified in the order that they appear. The file has an .sdv file name extension, such as Test.sdv.

The rule that is listed on each line can be the name of one rule or it can be a wildcard character (\*), which represents all SDV rules.

SDV includes a set of useful rule list files in the \\tools\\sdv\\samples\\rule\_sets\\wdm subdirectory of the WDK and you can create your own.

To use a rule list file in a command, see the [Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md).

Typically, you would use a rule list file to specify multiple rules for a SDV verification that you cannot specify with a rule name pattern. It is also useful for batch and regression testing.

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

The following sample rule list file lists a set of selected SDV rules.

```
AddDevice
IrqlApcLte
LowerDriverReturn
KeWaitDeadlock
ZwRegistryOpen
```

The following command uses a rule list file, MyRules.sdv, to start a SDV verification.

```
msbuild /t:sdv /p:Inputs="/check:D:\SDV\MyRules.sdv" mydriver.VcxProj /p:Configuration="Windows 7 Release" /p:Platform=Win32
```

### <span id="comment"></span><span id="COMMENT"></span>Comment

The rule list files that you create to list the rules for a verification have the .sdv file name extension. The SDV source code files for rules have a .slic file name extension.

 

 





