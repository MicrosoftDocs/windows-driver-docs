---
title: Static Driver Verifier Rule List File
description: Static Driver Verifier Rule List File
ms.assetid: 941df64c-b66b-4e7b-b340-9ef6b57d895d
keywords: ["Static Driver Verifier WDK , input files", "StaticDV WDK , input files", "SDV WDK , input files", "input files WDK Static Driver Verifier", "files WDK Static Driver Verifier", "rules WDK Static Driver Verifier", "rule list files WDK Static Driver Verifier"]
---

# Static Driver Verifier Rule List File


A SDV rule list file is a text file that lists one or more [Static Driver Verifier rule](https://msdn.microsoft.com/library/windows/hardware/ff551714) or rule name patterns, with one rule or rule name pattern on each line. The rules can appear in any order and they are verified in the order that they appear. The file has an .sdv file name extension, such as Test.sdv.

The rule that is listed on each line can be the name of one rule or it can be a wildcard character (\*), which represents all SDV rules. You can also use the wildcard character (\*) in a rule name to mean any character or characters.

SDV includes a set of useful rule list files in the \\tools\\sdv\\samples\\rule\_sets\\wdm subdirectory of the WDK and you can create your own.

To use a rule list file in a command, see the [Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md).

Typically, you would use a rule list file to specify multiple rules for a SDV verification that you cannot specify with a rule name pattern. It is also useful for batch and regression testing.

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

The following sample rule list file directs SDV to run rules that begin with "Irql" or include "Cancel".

```
Irql*
*Cancel*
```

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Static%20Driver%20Verifier%20Rule%20List%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




