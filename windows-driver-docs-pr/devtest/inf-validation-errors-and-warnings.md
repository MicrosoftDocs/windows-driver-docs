---
title: INF Validation Errors and Warnings
description: This topic describes driver installation errors and warnings that can appear as a result of the automatic INF verification that Microsoft Visual Studio performs, or when you run the InfVerif tool.
ms.assetid: E021D8F8-BFDA-4F71-B8EA-0997096761FB
---

# INF Validation Errors and Warnings


This topic describes driver installation errors and warnings that can appear as a result of the automatic INF verification that Microsoft Visual Studio performs, or when you run the [InfVerif](infverif.md) tool.

Starting in Visual Studio 2015 with WDK 10, when you build your driver, the following INF file errors can appear in the Error List pane. If you are running InfVerif.exe from the command line, the tool displays these errors at the command prompt, or in the HTML version of the results.

-   [Ignored lines in the INF file (1200-1299)](#err-12xx)
-   [Universal INF errors (1300-1309)](#err-130x)
-   [Installation warnings (2000-2999)](#warning-2xxx)

## <span id="err_12xx"></span><span id="ERR_12XX"></span>Syntax errors in the INF file (1200-1299)


When you install a driver, Windows skips lines in the INF file that contain errors, but does not fail driver installation due to errors in this range. If the driver installs successfully, you might not notice that some lines were skipped.

Errors in the 1200-1299 range correspond to lines in the INF file that would be ignored at driver installation. As such, they do not prevent the installation of your driver. But because they are skipped, your INF file may not be doing all the things that you expected.

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
<td align="left"><p><span id="1220__Cannot_directly_reference_a_section_defined_in_an_included_INF"></span><span id="1220__cannot_directly_reference_a_section_defined_in_an_included_inf"></span><span id="1220__CANNOT_DIRECTLY_REFERENCE_A_SECTION_DEFINED_IN_AN_INCLUDED_INF"></span><strong>1220: Cannot directly reference a section defined in an included INF</strong></p></td>
<td align="left"><p>If your INF file references a [DDInstall](https://msdn.microsoft.com/library/windows/hardware/ff547344) section in an included INF, you must use the <strong>Needs</strong> directive. Any other directive that references a section from an included INF causes error 1220.</p>
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
<tr class="even">
<td align="left"><p><span id="1221__Cannot_modify_services_regkey__must_use_HKR"></span><span id="1221__cannot_modify_services_regkey__must_use_hkr"></span><span id="1221__CANNOT_MODIFY_SERVICES_REGKEY__MUST_USE_HKR"></span><strong>1221: Cannot modify services regkey, must use HKR</strong></p></td>
<td align="left"><p>This error indicates that the INF file references a location in the services registry key, for example <strong>HKLM\SYSTEM\CurrentControlSet\Services\\<em>Service Name</em></strong>. When accessing the services key, you should instead use the relative root (<strong>HKR</strong>) to associate the registry value with the device or driver instance.</p>
<p>When you use <strong>HKR</strong>, the registry value will not be present until the device is installed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="1230__missing_file_under_sourcedisksfiles_section_"></span><span id="1230__missing_file_under_sourcedisksfiles_section_"></span><span id="1230__MISSING_FILE_UNDER_SOURCEDISKSFILES_SECTION_"></span><strong>1230: Missing file 'xxxx' under [SourceDisksFiles] section.</strong></p></td>
<td align="left"><p>This indicates that a file was specified as part of the driver package, but the source location of the file relative to the INF was not specified in a [SourceDisksFiles] section.</p>
<div class="code">
<pre>
[SourceDisksFiles]
filename=disk id
</pre>
</div>
<p>Note that this error frequently occurs if architecture-decorated versions of [SourceDisksFiles] are specified (such as [SourceDisksFiles.amd64], but not all architectures supported by the INF have a [SourceDisksFiles] section.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="1233__Missing_directive_required_for_signature"></span><span id="1233__missing_directive_required_for_signature"></span><span id="1233__MISSING_DIRECTIVE_REQUIRED_FOR_SIGNATURE"></span><strong>1233: Missing directive required for signature</strong></p></td>
<td align="left"><p>In the [Version] section, you must specify a CatalogFile directive (and associated catalog file) to receive a signature on a driver package.</p>
<div class="code">
<pre>
CatalogFile=wudf.cat
</pre>
</div></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="1235__String_token_not_defined_in__Strings_"></span><span id="1235__string_token_not_defined_in__strings_"></span><span id="1235__STRING_TOKEN_NOT_DEFINED_IN__STRINGS_"></span><strong>1235: String token not defined in [Strings]</strong></p></td>
<td align="left"><p>A specified string token has no definition in the [Strings] section. For example, the INF file specifies <em>%REG_DWORD%</em> in an <em>add-registry section</em> specified by an [<strong>AddReg</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546320) directive, but there is no corresponding REG_DWORD = 0x00010001 in the [[Strings]](https://msdn.microsoft.com/library/windows/hardware/ff547485) section.</p>
<p>This error frequently occurs if your INF file specifies a registry value that contains an environment variable. For example:</p>
<div class="code">
<pre>
[MyAddReg]
HKR,,DllPath,”%SystemRoot%\System32\myDll.sys”
</pre>
</div>
<p>This line causes the INF parser to attempt to locate the token "SystemRoot" from the [Strings] section, rather than the intended behavior of storing the literal "%SystemRoot%" in the registry.  To use the literal value “%SystemRoot%” rather than perform a string replacement, use the escape sequence ‘%%’.</p>
<div class="code">
<pre>
[MyAddReg]
HKR,,DllPath,”%%SystemRoot%%\System32\myDll.sys”
</pre>
</div></td>
</tr>
</tbody>
</table>

 

## <span id="err_130x"></span><span id="ERR_130X"></span>Universal INF errors (1300-1309)


**Important**  
If you do not get any errors or warnings with error number 130*x* and error text ("Found legacy *Xxx* operation..."), your driver INF file is universal.

 

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
<td align="left"><p><span id="1301__Found_legacyXxx"></span><span id="1301__found_legacyxxx"></span><span id="1301__FOUND_LEGACYXXX"></span><strong>1301: Found legacy</strong> <em>Xxx</em></p></td>
<td align="left"><p>You'll see this error if you use deprecated sections or directives such as [<strong>LogConfig</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547448) or [<strong>DDInstall.CoInstallers</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547321).</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="1302__Found_legacyXxxoperationXxx"></span><span id="1302__found_legacyxxxoperationxxx"></span><span id="1302__FOUND_LEGACYXXXOPERATIONXXX"></span><strong>1302: Found legacy</strong> <em>Xxx</em> <strong>operation</strong> <em>Xxx</em></p></td>
<td align="left"><p>You'll see this error if you use deprecated sections or directives such as [<strong>LogConfig</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547448) or [<strong>DDInstall.CoInstallers</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547321).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="1303__Found_legacyXxxoperation_forXxx"></span><span id="1303__found_legacyxxxoperation_forxxx"></span><span id="1303__FOUND_LEGACYXXXOPERATION_FORXXX"></span><strong>1303: Found legacy</strong> <em>Xxx</em> <strong>operation for</strong> <em>Xxx</em></p></td>
<td align="left"><p>This error occurs when the operation affects something external to the driver package, like deleting a service or deleting a file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="1304__Found_legacy_operation_defining_co-installers"></span><span id="1304__found_legacy_operation_defining_co-installers"></span><span id="1304__FOUND_LEGACY_OPERATION_DEFINING_CO-INSTALLERS"></span><strong>1304: Found legacy operation defining co-installers</strong></p></td>
<td align="left"><p>Error 1304 indicates that an AddReg operation is specifying a coinstaller. For example:</p>
<div class="code">
<pre>
AddReg = HKR,,CoInstallers32,0x00010000,"MyCoinstaller.dll"
</pre>
</div></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="1305__Found_legacy_operation_using_non-relative_key"></span><span id="1305__found_legacy_operation_using_non-relative_key"></span><span id="1305__FOUND_LEGACY_OPERATION_USING_NON-RELATIVE_KEY"></span><strong>1305: Found legacy operation using non-relative key</strong></p></td>
<td align="left"><p>Error 1305 indicates that a registry operation uses a registry root other than HKR.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="1306__Found_legacy_operation_using_appendable_multi-sz_value"></span><span id="1306__found_legacy_operation_using_appendable_multi-sz_value"></span><span id="1306__FOUND_LEGACY_OPERATION_USING_APPENDABLE_MULTI-SZ_VALUE"></span><strong>1306: Found legacy operation using appendable multi-sz value</strong></p></td>
<td align="left"><p>Error 1306 indicates that the INF deletes a value from a <strong>REG_MULTI_SZ</strong> or appends a value to an existing <strong>REG_MULTI_SZ</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="1307__Found_legacy_operation_with_non-system_target_path_"></span><span id="1307__found_legacy_operation_with_non-system_target_path_"></span><span id="1307__FOUND_LEGACY_OPERATION_WITH_NON-SYSTEM_TARGET_PATH_"></span><strong>1307: Found legacy operation with non-system target path</strong></p></td>
<td align="left"><p>Error 1307 indicates that a file copy specifies a target that is not under %SystemRoot%.</p></td>
</tr>
</tbody>
</table>

 

Whether these issues appear as errors or warnings depends on the following:

-   Issues with configurability are reported as errors if:
    -   In Visual Studio, you build your driver with target platform set to **Universal** or **Mobile**.
    -   You run InfVerif.exe from the command line and specify the /c flag.
-   Issues with configurability are reported as warnings if:
    -   In Visual Studio, you build your driver with target platform set to **Desktop**.
    -   You run InfVerif.exe from the command line and do not specify the /c flag.

## <span id="warning_2xxx"></span><span id="WARNING_2XXX"></span>Installation warnings (2000-2999)


Issues in the 2000-2999 range appears as warnings. Possible values include the following.

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
<td align="left"><p>This warning indicates that the INF specifies a deprecated directive. When the driver is installed, the directive referencing the section is not evaluated. For example, the [<strong>INF LogConfig Directive</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547448) directive is no longer supported, so the following section results in this warning.</p>
<div class="code">
<pre>
[InstallSection.LogConfigOverride]
LogConfig=LogConfigSection
...
</pre>
</div>
<p>For information about which INF directives are deprecated, see [INF Directives](https://msdn.microsoft.com/library/windows/hardware/ff547388).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="2223__Section_should_have_an_architecture_decoration"></span><span id="2223__section_should_have_an_architecture_decoration"></span><span id="2223__SECTION_SHOULD_HAVE_AN_ARCHITECTURE_DECORATION"></span><strong>2223: Section should have an architecture decoration</strong></p></td>
<td align="left"><p>This warning indicates that the INF file contains an [<strong>INF Manufacturer Section</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547454) that specifies a [<strong>model section</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547456) with no architecture decoration. For example, the following INF syntax would result in warning 2223:</p>
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20INF%20Validation%20Errors%20and%20Warnings%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




