---
title: INF Validation Errors and Warnings
description: Driver installation errors and warnings can appear as a result of the automatic INF verification that Microsoft Visual Studio performs.
ms.assetid: E021D8F8-BFDA-4F71-B8EA-0997096761FB
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---
<!--error used for all things on the page, but some are errors and some are warnings?-->
# INF Validation Errors and Warnings


This topic describes driver installation errors and warnings that can appear as a result of the automatic INF verification that Microsoft Visual Studio performs, or when you run the [InfVerif](infverif.md) tool.

Starting in Visual Studio 2015 with WDK 10, when you build your driver, the following INF file errors can appear in the Error List pane. If you are running InfVerif.exe from the command line, the tool displays these errors at the command prompt, or in the HTML version of the results.

## Error Guidance
InfVerif follows a general rule that the lower the error number, the more severe the issue.  Depending on the context in which InfVerif is invoked, errors codes may vary between a warning and an error.

### Handling Errors
Errors are considered critical and must be addressed.  <!--or what?-->Errors are related to the following conditions:
-   The INF parser was unable to successfully interpret your INF
-   The INF parser was able to interpret the INF if some default-value assumption was made (ambiguous syntax)
-   The arguments to InfVerif indicate some rule set was applied to the INF (such as Universal)

Warnings are not required to be fixed, and typically relate to the following conditions:
-   Syntax that may be incorrect, but has valid scenarios where it is appropriate
-   Syntax that is valid for the given InfVerif parameters, but is an error in other modes, such as Universal

Warnings may be ignored if the developer fully understands the message being reported.  For example, a section that is unreferenced by the INF parser results in warning 2083, however the unreferenced section might exist to be parsed by external code.  In such a case, the 2083 can be ignored. If a given warning is not properly understood, it is likely indicative of some other INF parsing error.

-   Universal errors are reported as errors if:
    -   In Visual Studio, you build your driver with target platform set to **Universal** or **Mobile**.
    -   You run InfVerif.exe from the command line and specify the /u flag.
-   Universal errors are reported as warnings if:
    -   In Visual Studio, you build your driver with target platform set to **Desktop**.
    -   You run InfVerif.exe from the command line and do not specify the /u flag.

## Error Codes

-   [Syntax errors in the INF file (1100-1299)](#err-11xx)
-   [Universal INF errors (1300-1319)](#err-130x)
-   [Installation warnings (2000-2999)](#warning-2xxx)

Not all error codes are listed below, as many have self-evident meanings. Errors in the 1000-1099 range are considered self-evident, as they are basic syntax errors.

## Syntax errors in the INF file (1100-1299)<a name="err-11xx"></a>

When you install a driver, if errors are present in the INF file, Windows reverts to the default value for the setting. <!--so you can have errors and still succeed?-->Windows does not fail driver installation due to errors in this range, but errors in this range indicate that the behavior may change depending on OS version or SKU. In cases where the driver installs successfully, these errors indicate that there *are* circumstances where the driver may not install properly.

|Error Code|Description|
|--- |--- |
|**1100: DriverStore Copyfile name mismatch**|This error occurs when a file is copied or renamed from its original driver store name and location to a different name and location in the driver store. For example:
||`[SourceDisksFiles]`|
||`DriverFile.sys=1,x64`|
||`[DestinationDirs]`|
||`CopyFileSection=13,SubDirectory`|
||`[CopyFileSection]`|
||`DriverFile.sys`|
||The driver store maintains the original driver package directory structure. In the above, the original location of DriverFile.sys is \x64, but CopyFiles places it in \SubDirectory. The same error would be shown if the file was renamed as part of the copy.|
|**1203: Section not found**|For example, the following INF syntax causes error 1203:



[MyInstallSection]
CopyFiles=driverFile.sys




This error is reported because the **CopyFiles** directive expects a section name (that specifies the list of files to copy). However, the **CopyFiles** directive can specify a file name. To differentiate between a section name and a file name, preface a file name with the @ token as shown here:



[MyInstallSection]
CopyFiles=@driverFile.sys|
|**1204: Provider cannot be Microsoft**|The Provider field in the [Version] section cannot specify Microsoft.



[Version]
Signature="$Windows NT$"
Class=Sample
ClassGuid={78A1C341-4539-11d3-B88D-00C04FAD5171}
Provider="Microsoft"|
|**1212: Cannot have both [DefaultInstall] and [Manufacturer]**|A single INF cannot contain both [DefaultInstall] and [Manufacturer]. INFs authored with both should remove one of the two sections.|
|**1220: Cannot directly reference a section defined in an included INF**|If your INF file references a [DDInstall](https://msdn.microsoft.com/library/windows/hardware/ff547344) section in an included INF, you must use the **Needs** directive. Any other directive that references a section from an included INF causes error 1220.

In this example, the install section of A.INF references an equivalent install section in B.INF.

A.INF contains:



A.INF
[InstallSectionA]
Include = B.INF
Needs = InstallSectionB
AddReg = AddRegB ; WARNING 1220

[InstallSectionA.Services]
Include = B.INF
Needs = InstallSectionB.Services




B.INF contains:



B.INF
[InstallSectionB]
AddReg = AddRegB
[InstallSectionB.Services]
...

[AddRegB]
...




The **Needs** directive must reference an equivalent install section to process in the current install section. For example, a Needs directive in [InstallSectionA.Services] should point to the .Services of another install section. The **Needs** directive may also be used to include the behavior of another DDInstall section of the same INF. Using the **Needs** directive on other types of sections may result in undesired behavior.|
|**1221: Cannot modify services regkey, must use HKR**|This error indicates that the INF file references a location in the services registry key, for example **HKLM\SYSTEM\CurrentControlSet\Services\\_Service Name_**. When accessing the services key, you should instead use the relative root (**HKR**) to associate the registry value with the device or driver instance.

When you use **HKR**, the registry value will not be present until the device is installed.|
|**1230: Missing file 'xxxx' under [SourceDisksFiles] section.**|This indicates that a file was specified as part of the driver package, but the source location of the file relative to the INF was not specified in a [SourceDisksFiles] section.



[SourceDisksFiles]
filename=disk id




Note that this error frequently occurs if architecture-decorated versions of [SourceDisksFiles] are specified (such as [SourceDisksFiles.amd64], but not all architectures supported by the INF have a [SourceDisksFiles] section.|
|**1233: Missing directive required for signature**|In the [Version] section, you must specify a CatalogFile directive (and associated catalog file) to receive a signature on a driver package.



CatalogFile=wudf.cat|
|**1235: String token not defined in [Strings]**|A specified string token has no definition in the [Strings] section. For example, the INF file specifies _%REG_DWORD%_ in an _add-registry section_ specified by an [**AddReg**](https://msdn.microsoft.com/library/windows/hardware/ff546320) directive, but there is no corresponding REG_DWORD = 0x00010001 in the [[Strings]](https://msdn.microsoft.com/library/windows/hardware/ff547485) section.

This error frequently occurs if your INF file specifies a registry value that contains an environment variable. For example:



[MyAddReg]
HKR,,DllPath,%SystemRoot%\System32\myDll.sys




This line causes the INF parser to attempt to locate the token "SystemRoot" from the [Strings] section, rather than the intended behavior of storing the literal "%SystemRoot%" in the registry. To use the literal value %SystemRoot% rather than perform a string replacement, use the escape sequence %%.



[MyAddReg]
HKR,,DllPath,%%SystemRoot%%\System32\myDll.sys|
|**1285: Cannot specify [ClassInstall32] section for Microsoft-defined class.**|As of Windows 10, IHV-supplied INFs are not allowed to use a [ClassInstall32] in an INF of any Microsoft-defined class.|




## Universal INF errors (1300-1319) <a name="err-130x"></a>


**Important**
If you do not get any errors or warnings with error number 130*x* and error text ("Found legacy *Xxx* operation..."), your driver INF file is universal.



The following errors and warnings are related to INF configurability:

|Error/Warning Code|Description|
|--- |--- |
|**1301: Found legacy**_Xxx_|You'll see this error if you use deprecated sections or directives such as [**LogConfig**](https://msdn.microsoft.com/library/windows/hardware/ff547448) or [**DDInstall.CoInstallers**](https://msdn.microsoft.com/library/windows/hardware/ff547321).|
|**1302: Found legacy**_Xxx_**operation**_Xxx_|You'll see this error if you use deprecated sections or directives such as [**LogConfig**](https://msdn.microsoft.com/library/windows/hardware/ff547448) or [**DDInstall.CoInstallers**](https://msdn.microsoft.com/library/windows/hardware/ff547321).|
|**1303: Found legacy**_Xxx_**operation for**_Xxx_|This error occurs when the operation affects something external to the driver package, like deleting a service or deleting a file.|
|**1304: Found legacy operation defining co-installers**|Error 1304 indicates that an AddReg operation is specifying a coinstaller. For example:



AddReg = HKR,,CoInstallers32,0x00010000,"MyCoinstaller.dll"|
|**1305: Found legacy operation using non-relative key**|Error 1305 indicates that a registry operation uses a registry root other than HKR.|
|**1306: Found legacy operation using appendable multi-sz value**|Error 1306 indicates that the INF deletes a value from a **REG_MULTI_SZ** or appends a value to an existing **REG_MULTI_SZ**.|
|**1307: Found legacy operation with non-system target path**|Error 1307 indicates that a file copy specifies a target that is not under %SystemRoot%.|
|**1310-1312: Incorrect section extension for a Needs directive**|Needs directives effectively do a copy/paste of the needed section into the referencing section. As a baseline validation, InfVerif compares the extension of the section. This means that a [DDInstall.Services] can only use the Needs directive on other [DDInstall.Services] sections.|
|**1313-1314: Missing includes directive**|In each section that uses a Needs directive, there must be a corresponding Includes directive to reference the INF that contains the target section. Previously the Needs directive would be valid if the Include directive was in another INF section.|


## Installation warnings (2000-2999) <a name="warning-2xxx"></a>


Issues in the 2000-2999 range appears as warnings. Possible values include the following.

|Error Code|Description|
|--- |--- |
|**2083: Section not referenced or used**|This warning indicates that the INF file provides a section that is not referenced. When the driver is installed, the contents of the section referenced in the warning are not evaluated.|
|**2222: Legacy directive will be ignored.**|This warning indicates that the INF specifies a deprecated directive. When the driver is installed, the directive referencing the section is not evaluated. For example, the [**INF LogConfig Directive**](https://msdn.microsoft.com/library/windows/hardware/ff547448) directive is no longer supported, so the following section results in this warning.



[InstallSection.LogConfigOverride]
LogConfig=LogConfigSection
...




For information about which INF directives are deprecated, see [INF Directives](https://msdn.microsoft.com/library/windows/hardware/ff547388).|
|**2223: Section should have an architecture decoration**|This warning indicates that the INF file contains an [**INF Manufacturer Section**](https://msdn.microsoft.com/library/windows/hardware/ff547454) that specifies a [**model section**](https://msdn.microsoft.com/library/windows/hardware/ff547456) with no architecture decoration. For example, the following INF syntax would result in warning 2223:



[Manufacturer]
%MfgName% = InstallSection

[InstallSection]
...




When you install the driver, the preceding INF syntax defaults to x86.

Instead, declare all supported architectures and provide a corresponding install section for each:



[Manufacturer]
%MfgName% = InstallSection, NTX86, NTAMD64

[InstallSection.NTAMD64]
...

[InstallSection.NTX86]
...




If the INF file specifies a decorated section for x86 and an undecorated section, the undecorated section is ignored when you install your driver.|








