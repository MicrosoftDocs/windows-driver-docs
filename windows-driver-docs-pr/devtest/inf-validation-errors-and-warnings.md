---
title: INF Validation Errors and Warnings
description: Driver installation errors and warnings can appear as a result of the automatic INF verification that Microsoft Visual Studio performs.
ms.assetid: E021D8F8-BFDA-4F71-B8EA-0997096761FB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF Validation Errors and Warnings


This topic describes driver installation errors and warnings that can appear as a result of the automatic INF verification that Microsoft Visual Studio performs, or when you run the [InfVerif](infverif.md) tool.

Starting in Visual Studio 2015 with WDK 10, when you build your driver, the following INF file errors can appear in the Error List pane. If you are running InfVerif.exe from the command line, the tool displays these errors at the command prompt, or in the HTML version of the results.

## Error Guidance
InfVerif follows a general rule that the lower the error number, the more severe the issue.
Most error codes can be either a warning or an error depending on the arguments supplied to InfVerif.

### Handling Errors
You must fix all errors in order to pass driver tests on the Hardware Dev Center dashboard. Errors are related to the following conditions:
-   The INF parser is unable to successfully interpret your INF
-   The INF parser is able to interpret the INF only by making a default value assumption (ambiguous syntax)
-   The arguments to InfVerif indicate that a rule set should be applied to the INF (such as Universal)

While you don't need to fix warnings before submitting your driver on the Dev Center, we recommend taking the time to understand the issue being reported. If you don't understand a given warning, your INF might not always behave as you expect.

Warnings are typically related to:
-   Syntax that may be incorrect, but has valid scenarios where it is appropriate
-   Syntax that is valid for the given InfVerif parameters but is an error in other modes, such as Universal

Issues related to the Universal setting appear as errors if:
    -   In Visual Studio, you build your driver with target platform set to **Universal** or **Mobile**.
    -   You run InfVerif.exe from the command line and specify the /u flag.

Issues related to the Universal setting appear as warnings if:
    -   In Visual Studio, you build your driver with target platform set to **Desktop**.
    -   You run InfVerif.exe from the command line and do not specify the /u flag.

## Error Codes

Error codes come in the following classifications:

-   [Syntax in the INF file (1100-1299)](#err-11xx)
-   [Universal INF (1300-1319)](#err-130x)
-   [Installation (2000-2999)](#warning-2xxx)

Not all error codes are listed below, as many have self-evident meanings. Errors in the 1000-1099 range are considered self-evident, as they are basic syntax errors.

## Syntax in the INF file (1100-1299)<a name="err-11xx"></a>

While InfVerif failure means driver submission failure, driver installation may still succeed.
This is because when you install a driver, if errors are present in the INF file, Windows also tries the default value for the setting.
Windows does not fail driver installation due to errors in this range, but errors in this range indicate that the behavior may change depending on OS version or SKU.
In cases where the driver installs successfully, these errors indicate that there *are* circumstances where the driver may not install properly.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Error Code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="even">
<td align="left"><p><span id="_1100__DrvStore_CopyFile"></span><span id="_1100__drvstore_copyfile"></span><span id="_1100__DRVSTORE_COPYFILE"></span> <strong>1100: DriverStore Copyfile name mismatch</strong></p></td>
<td align="left">
<p>This error occurs when a file is copied or renamed from its original driver store name and location to a different name and location in the driver store.  For example:</p>
<div class="code">
<pre>
[SourceDisksFiles]
DriverFile.sys=1,x64  

[DestinationDirs]
CopyFileSection=13,SubDirectory  
  
[CopyFileSection]
DriverFile.sys
</pre>
</div>
<p>The driver store maintains the original driver package directory structure.  In the code above, the original location of DriverFile.sys is <i>INF location</i>\x64, but the CopyFiles directive places it in <i>INF location</i>\SubDirectory.  The same error would be shown if the file was renamed as part of the copy.</p>
</td>
</tr>
    
<tr class="odd">
<td align="left"><p><span id="_1203__Section_not_found"></span><span id="_1203__section_not_found"></span><span id="_1203__SECTION_NOT_FOUND"></span> <strong>1203: Section not found</strong></p></td>
<td align="left"><p>For example, the following INF syntax causes error 1203:</p>
<div class="code">
<pre>
[MyInstallSection]
CopyFiles=driverFile.sys
</pre>
</div>
<p>This error is reported because the <strong>CopyFiles</strong> directive expects a section name (that specifies the list of files to copy). However, the <strong>CopyFiles</strong> directive can specify a file name. To differentiate between a section name and a file name, preface a file name with the @ token as shown here:</p>
<div class="code">
<pre>
[MyInstallSection]
CopyFiles=@driverFile.sys
</pre>
</div></td>
</tr>
<tr class="even">
<td align="left"><p><span id="1204__Provider_cannot_be_Microsoft"></span><span id="1204__provider_cannot_be_microsoft"></span><span id="1204__PROVIDER_CANNOT_BE_MICROSOFT"></span><strong>1204: Provider cannot be Microsoft</strong></p></td>
<td align="left"><p>The Provider field in the [Version] section cannot specify Microsoft.</p>
<div class="code">
<pre>
[Version]
Signature="$Windows NT$"
Class=Sample
ClassGuid={78A1C341-4539-11d3-B88D-00C04FAD5171}
Provider="Microsoft"
</pre>
</div></td>
</tr>

<tr class="odd">
<td align="left"><p><span id="1212__invalid_section"></span><span id="1212_INVALID_SECTION"></span><strong>1212: Cannot have both [DefaultInstall] and [Manufacturer]</strong></p></td>
<td align="left"><p>A single INF cannot contain both [DefaultInstall] and [Manufacturer].  INFs authored with both should remove one of the two sections.</p>
</td>
</tr>

<tr class="even">
<td align="left"><p><span id="1220__Cannot_directly_reference_a_section_defined_in_an_included_INF"></span><span id="1220__cannot_directly_reference_a_section_defined_in_an_included_inf"></span><span id="1220__CANNOT_DIRECTLY_REFERENCE_A_SECTION_DEFINED_IN_AN_INCLUDED_INF"></span><strong>1220: Cannot directly reference a section defined in an included INF</strong></p></td>
<td align="left"><p>If your INF file references a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547344" data-raw-source="[DDInstall](https://msdn.microsoft.com/library/windows/hardware/ff547344)">DDInstall</a> section in an included INF, you must use the <strong>Needs</strong> directive. Any other directive that references a section from an included INF causes error 1220.</p>
<p>In this example, the install section of A.INF references an equivalent install section in B.INF.</p>
<p>A.INF contains:</p>
<div class="code">
<pre>
A.INF
[InstallSectionA]
Include = B.INF
Needs = InstallSectionB
AddReg = AddRegB ; WARNING 1220

[InstallSectionA.Services]
Include = B.INF
Needs = InstallSectionB.Services
</pre>
</div>
<p>B.INF contains:</p>
<div class="code">
<pre>
B.INF
[InstallSectionB]
AddReg = AddRegB
[InstallSectionB.Services]
...

[AddRegB]
...
</pre>
</div>
<p>The <strong>Needs</strong> directive must reference an equivalent install section to process in the current install section. For example, a Needs directive in [InstallSectionA.Services] should point to the .Services of another install section. The <strong>Needs</strong> directive may also be used to include the behavior of another DDInstall section of the same INF. Using the <strong>Needs</strong> directive on other types of sections may result in undesired behavior.</p></td>
</tr>

<tr class="odd">
<td align="left"><p><span id="1221__Cannot_modify_services_regkey__must_use_HKR"></span><span id="1221__cannot_modify_services_regkey__must_use_hkr"></span><span id="1221__CANNOT_MODIFY_SERVICES_REGKEY__MUST_USE_HKR"></span><strong>1221: Cannot modify services regkey, must use HKR</strong></p></td>
<td align="left"><p>This error indicates that the INF file references a location in the services registry key, for example <strong>HKLM\SYSTEM\CurrentControlSet\Services&lt;em&gt;Service Name</em></strong>. When accessing the services key, you should instead use the relative root (<strong>HKR</strong>) to associate the registry value with the device or driver instance.</p>
<p>When you use <strong>HKR</strong>, the registry value will not be present until the device is installed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="1230__missing_file_under_sourcedisksfiles_section_"></span><span id="1230__missing_file_under_sourcedisksfiles_section_"></span><span id="1230__MISSING_FILE_UNDER_SOURCEDISKSFILES_SECTION_"></span><strong>1230: Missing file &#39;xxxx&#39; under [SourceDisksFiles] section.</strong></p></td>
<td align="left"><p>This indicates that a file was specified as part of the driver package, but the source location of the file relative to the INF was not specified in a [SourceDisksFiles] section.</p>
<div class="code">
<pre>
[SourceDisksFiles]
filename=disk id
</pre>
</div>
<p>Note that this error frequently occurs if architecture-decorated versions of [SourceDisksFiles] are specified (such as [SourceDisksFiles.amd64], but not all architectures supported by the INF have a [SourceDisksFiles] section.</p></td>
</tr>

<tr class="odd">
<td align="left"><p><span id="1233__Missing_directive_required_for_signature"></span><span id="1233__missing_directive_required_for_signature"></span><span id="1233__MISSING_DIRECTIVE_REQUIRED_FOR_SIGNATURE"></span><strong>1233: Missing directive required for signature</strong></p></td>
<td align="left"><p>In the [Version] section, you must specify a CatalogFile directive (and associated catalog file) to receive a signature on a driver package.</p>
<div class="code">
<pre>
CatalogFile=wudf.cat
</pre>
</div></td>
</tr>

<tr class="even">
<td align="left"><p><span id="1235__String_token_not_defined_in__Strings_"></span><span id="1235__string_token_not_defined_in__strings_"></span><span id="1235__STRING_TOKEN_NOT_DEFINED_IN__STRINGS_"></span><strong>1235: String token not defined in [Strings]</strong></p></td>
<td align="left"><p>A specified string token has no definition in the [Strings] section. For example, the INF file specifies <em>%REG_DWORD%</em> in an <em>add-registry section</em> specified by an <a href="https://msdn.microsoft.com/library/windows/hardware/ff546320" data-raw-source="[&lt;strong&gt;AddReg&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546320)"><strong>AddReg</strong></a> directive, but there is no corresponding REG_DWORD = 0x00010001 in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547485" data-raw-source="[[Strings]](https://msdn.microsoft.com/library/windows/hardware/ff547485)">[Strings]</a> section.</p>
<p>This error frequently occurs if your INF file specifies a registry value that contains an environment variable. For example:</p>
<div class="code">
<pre>
[MyAddReg]
HKR,,DllPath,%SystemRoot%\System32\myDll.sys
</pre>
</div>
<p>This line causes the INF parser to attempt to locate the token &quot;SystemRoot&quot; from the [Strings] section, rather than the intended behavior of storing the literal &quot;%SystemRoot%&quot; in the registry.  To use the literal value %SystemRoot% rather than perform a string replacement, use the escape sequence %%.</p>
<div class="code">
<pre>
[MyAddReg]
HKR,,DllPath,%%SystemRoot%%\System32\myDll.sys
</pre>
</div></td>
</tr>

<tr class="odd">
<td align="left"><p><span id="1285__invalid_classinstall32_"></span><span id="1285__INVALID_CLASSINSTALL32_"></span><strong>1285: Cannot specify [ClassInstall32] section for Microsoft-defined class.</strong></p></td>
<td align="left"><p>As of Windows 10, IHV-supplied INFs are not allowed to use a [ClassInstall32] in an INF of any Microsoft-defined class.</p>
</td>
</tr>

<tr class="even">
<td align="left"><p><strong>1296: Specified service not associated with hardware</strong></p></td>
<td align="left"><p>This warning appears starting in Windows 10, version 1809, and indicates that the hardware does not have an associated service using the specified install section.</p>
</td>
</tr>

</tbody>
</table>

## Universal INF (1300-1319) <a name="err-130x"></a>

>[!IMPORTANT]
>Your driver INF file is universal if you do not get any errors or warnings with error number in the range 13*xx*.

The following errors and warnings are related to INF configurability:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Error/Warning Code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="1300__Found_legacyXxx"></span><span id="1300__found_legacyxxx"></span><span id="1300__FOUND_LEGACYXXX"></span><strong>1300: Found legacy</strong><em>Xxx</em></p></td>
<td align="left"><p>You&#39;ll see this error if you use deprecated sections or directives such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff547448" data-raw-source="[&lt;strong&gt;LogConfig&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547448)"><strong>LogConfig</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff547321" data-raw-source="[&lt;strong&gt;DDInstall.CoInstallers&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547321)"><strong>DDInstall.CoInstallers</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="1301__Found_legacyXxxoperationXxx"></span><span id="1301__found_legacyxxxoperationxxx"></span><span id="1301__FOUND_LEGACYXXXOPERATIONXXX"></span><strong>1301: Found legacy</strong><em>Xxx</em><strong>operation</strong><em>Xxx</em></p></td>
<td align="left"><p>You&#39;ll see this error if you use deprecated sections or directives such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff547448" data-raw-source="[&lt;strong&gt;LogConfig&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547448)"><strong>LogConfig</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff547321" data-raw-source="[&lt;strong&gt;DDInstall.CoInstallers&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547321)"><strong>DDInstall.CoInstallers</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="1302__Found_legacyXxxoperation_forXxx"></span><span id="1302__found_legacyxxxoperation_forxxx"></span><span id="1302__FOUND_LEGACYXXXOPERATION_FORXXX"></span><strong>1302: Found legacy</strong><em>Xxx</em><strong>operation for</strong><em>Xxx</em></p></td>
<td align="left"><p>This error occurs when the operation affects something external to the driver package, like deleting a service or deleting a file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="1303__Found_legacy_operation_defining_co-installers"></span><span id="1303__found_legacy_operation_defining_co-installers"></span><span id="1303__FOUND_LEGACY_OPERATION_DEFINING_CO-INSTALLERS"></span><strong>1303: Found legacy operation defining co-installers</strong></p></td>
<td align="left"><p>Error 1303 indicates that an AddReg operation is specifying a coinstaller. For example:</p>
<div class="code">
<pre>
AddReg = HKR,,CoInstallers32,0x00010000,"MyCoinstaller.dll"
</pre>
</div></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="1304__Found_legacy_operation_using_non-relative_key"></span><span id="1304__found_legacy_operation_using_non-relative_key"></span><span id="1304__FOUND_LEGACY_OPERATION_USING_NON-RELATIVE_KEY"></span><strong>1304: Found legacy operation using non-relative key</strong></p></td>
<td align="left"><p>Error 1304 indicates that a registry operation uses a registry root other than HKR.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="1305__Found_legacy_operation_using_appendable_multi-sz_value"></span><span id="1305__found_legacy_operation_using_appendable_multi-sz_value"></span><span id="1305__FOUND_LEGACY_OPERATION_USING_APPENDABLE_MULTI-SZ_VALUE"></span><strong>1305: Found legacy operation using appendable multi-sz value</strong></p></td>
<td align="left"><p>Error 1305 indicates that the INF deletes a value from a <strong>REG_MULTI_SZ</strong> or appends a value to an existing <strong>REG_MULTI_SZ</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="1306__Found_legacy_operation_with_non-system_target_path_"></span><span id="1306__found_legacy_operation_with_non-system_target_path_"></span><span id="1306__FOUND_LEGACY_OPERATION_WITH_NON-SYSTEM_TARGET_PATH_"></span><strong>1306: Found legacy operation with non-system target path</strong></p></td>
<td align="left"><p>Error 1306 indicates that a file copy specifies a target that is not under %SystemRoot%.</p></td>
</tr>
    
<tr class="even">
<td align="left"><p><span id="1310_needs_extension_"></span><span id="1310_NEEDS_EXTENSION_"></span><strong>1310-1312: Incorrect section extension for a Needs directive</strong></p></td>
<td align="left"><p>Needs directives effectively do a copy/paste of the needed section into the referencing section.  As a baseline validation, InfVerif compares the extension of the section.  This means that a [DDInstall.Services] can only use the Needs directive on other [DDInstall.Services] sections.</p></td>
</tr>

<tr class="odd">
<td align="left"><p><span id="1313_missing_includes_"></span><span id="1313_MISSING_INCLUDES_"></span><strong>1313-1314: Missing includes directive</strong></p></td>
<td align="left"><p>In each section that uses a Needs directive, there must be a corresponding Includes directive to reference the INF that contains the target section.  Previously the Needs directive would be valid if the Include directive was in another INF section.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="133x_functional_errors_"></span><span id="133x_FUNCTIONAL_ERRORS_"></span><strong>133x: Functional errors</strong></p></td>
<td align="left"><p>Multiple registry sections write to a single global key. For example, different sections could have a service set to different service configuations, a global registry key set to different data values, or a destination file pointing to different source files.</p></td>
</tr>
</tbody>
</table>


## Installation (2000-2999) <a name="warning-2xxx"></a>


Issues in the 2000-2999 range appear as warnings. Possible values include the following.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Error Code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="2083__Section_not_referenced_or_used_"></span><span id="2083__section_not_referenced_or_used_"></span><span id="2083__SECTION_NOT_REFERENCED_OR_USED_"></span><strong>2083: Section not referenced or used</strong></p></td>
<td align="left"><p>This warning indicates that the INF file provides a section that is not referenced. When the driver is installed, the contents of the section referenced in the warning are not evaluated.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="2222__Legacy_directive_will_be_ignored."></span><span id="2222__legacy_directive_will_be_ignored."></span><span id="2222__LEGACY_DIRECTIVE_WILL_BE_IGNORED."></span><strong>2222: Legacy directive will be ignored.</strong></p></td>
<td align="left"><p>This warning indicates that the INF specifies a deprecated directive. When the driver is installed, the directive referencing the section is not evaluated. For example, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547448" data-raw-source="[&lt;strong&gt;INF LogConfig Directive&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547448)"><strong>INF LogConfig Directive</strong></a> directive is no longer supported, so the following section results in this warning.</p>
<div class="code">
<pre>
[InstallSection.LogConfigOverride]
LogConfig=LogConfigSection
...
</pre>
</div>
<p>For information about which INF directives are deprecated, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff547388" data-raw-source="[INF Directives](https://msdn.microsoft.com/library/windows/hardware/ff547388)">INF Directives</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="2223__Section_should_have_an_architecture_decoration"></span><span id="2223__section_should_have_an_architecture_decoration"></span><span id="2223__SECTION_SHOULD_HAVE_AN_ARCHITECTURE_DECORATION"></span><strong>2223: Section should have an architecture decoration</strong></p></td>
<td align="left"><p>This warning indicates that the INF file contains an <a href="https://msdn.microsoft.com/library/windows/hardware/ff547454" data-raw-source="[&lt;strong&gt;INF Manufacturer Section&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547454)"><strong>INF Manufacturer Section</strong></a> that specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547456" data-raw-source="[&lt;strong&gt;model section&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547456)"><strong>model section</strong></a> with no architecture decoration. For example, the following INF syntax would result in warning 2223:</p>
<div class="code">
<pre>
[Manufacturer]
%MfgName% = InstallSection

[InstallSection]
...
</pre>
</div>
<p>When you install the driver, the preceding INF syntax defaults to x86.</p>
<p>Instead, declare all supported architectures and provide a corresponding install section for each:</p>
<div class="code">
<pre>
[Manufacturer]
%MfgName% = InstallSection, NTX86, NTAMD64

[InstallSection.NTAMD64]
...

[InstallSection.NTX86]
...
</pre>
</div>
<p>If the INF file specifies a decorated section for x86 and an undecorated section, the undecorated section is ignored when you install your driver.</p></td>
</tr>
</tbody>
</table>






