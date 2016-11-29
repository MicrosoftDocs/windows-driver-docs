---
title: Nmake2MsBuild
description: The Nmake2MsBuild utility generates a Visual Studio project for a driver that was built using a previous version of the WDK from your driver's source code files, and from the sources, dirs, and makefile.inc files.
ms.assetid: D6E1C124-9A5F-486B-865E-45A0BC58A5A3
---

# Nmake2MsBuild


**Note**  The Nmake2MsBuild tool was removed from the WDK starting in Windows 10, version 1511.

 

The Nmake2MsBuild utility generates a Visual Studio project for a driver that was built using a previous version of the WDK from your driver's source code files, and from the *sources*, *dirs*, and *makefile.inc* files. The utility creates the Visual Studio project file in the same directory as your existing *sources* files. The utility does not alter your source code or your earlier build files.

For information about using the utility, see [Converting a WDK sources file to a Visual Studio project](converting-a-wdk-sources-file-to-a-visual-studio-project.md).

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


The Nmake2MsBuild.exe utility has the following syntax:

``` syntax
NMake2MSBuild.exe  < sources [<sources>...] | dirs >
                          [-Name:<Name of output project>]
                          [-Package:<Path to package project file to generate>]
                          [-Solution:<Path to Solution file to generate>]
                          [-Log:[<LogFile>]:[<Verbosity>]]
                          [-ConsoleLog:<Verbosity>]
                          [-NoPackageProject]
                          [-NoSolution]
                          [-SafeMode]
             
```

The conversion tool is located in the %PROGRAMFILES%\\Windows Kits\\8.0\\tools\\x86\\ directory.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><em>sources</em></td>
<td align="left"><p>Specifies the path to the <em>sources</em> file for a driver built with the previous version of the WDK. If you specify a <em>sources</em> file, the utility parses that <em>sources</em> file and the corresponding <em>makefile.inc</em> and generates a Visual Studio project file. The Visual Studio project file is placed in the same directory as the <em>sources</em> file.</p>
<p>You can specify more than one <em>sources</em> files at a time. All resulting projects will share the same Solution and Package Project.</p></td>
</tr>
<tr class="even">
<td align="left"><em>dirs</em></td>
<td align="left"><p>Specifies the path to the <em>dirs</em> file for a driver built with the previous version of the WDK. If you specify a <em>dirs</em> file, the utility looks in the directory tree for all <em>sources</em> files and the corresponding makefile.inc files and generates a Visual Studio project files for each one.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>-Package:</strong><em>&lt;Path to Package file to generate&gt;</em></td>
<td align="left">Specifies a custom name for the driver package project file.</td>
</tr>
<tr class="even">
<td align="left"><strong>-Solution:</strong><em>&lt;Path to Solution file to generate&gt;</em></td>
<td align="left">Specifies a custom name for the driver solution file (.sln).</td>
</tr>
<tr class="odd">
<td align="left">-<strong>Log:[</strong><em>&lt;LogFile&gt;</em><strong>]:[</strong><em>&lt;Verbosity&gt;</em><strong>]</strong></td>
<td align="left">Specifies a name for the Log file, and specifies the level of logging (see <em>Verbosity</em>).</td>
</tr>
<tr class="even">
<td align="left"><strong>-ConsoleLog:</strong><em>&lt;Verbosity&gt;</em></td>
<td align="left">Specifies a name for the Console log file, and specifies the level of logging (see <em>Verbosity</em>).</td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-Name:</strong><em>&lt;Name of output project&gt;</em></p></td>
<td align="left"><p>Specifies a custom name for the VcxProj file that will be generated. Alternatively, if a <em>dirs</em> file is being converted, this parameter is used to specify the name of the generated solution.</p></td>
</tr>
<tr class="even">
<td align="left"><em>Verbosity</em></td>
<td align="left">The default logging levels for Log file and Console logging are <strong>Verbose</strong> and <strong>Information</strong> respectively. <em>Verbosity</em> is one of <strong>System.Diagnostics.SourceLevels</strong>.</td>
</tr>
<tr class="odd">
<td align="left"><strong>-SafeMode</strong></td>
<td align="left">SafeMode does not provide IDE/UI support for NMAKE targets, but could provide a more accurate conversion for NMAKE targets. Only specify -SafeMode if you experience issues during build steps that were previously performed in your project's NMAKE targets.</td>
</tr>
</tbody>
</table>

 

## <span id="Comments"></span><span id="comments"></span><span id="COMMENTS"></span>Comments


The conversion tool is located in the %PROGRAMFILES%\\Windows Kits\\8.0\\tools\\x86\\ directory.

Response (.Rsp) files are supported for specifying command line parameters. Each parameters should be specified on a separate line.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


To build a driver project that was built with a previous version of the WDK (using Build.exe and a sources and dirs file), you must first convert it to a .VcxProj project using Nmake2MsBuild.exe conversion utility.

For example, to convert a driver that was previously built with the Windows 7 WDK, called MyDriver, you first open a **Visual Studio Command Prompt** window. Browse to the directory or supply the path to the directory that contains the *sources* or *dirs* build configuration file. For example, the following command generates the MyDriver.Vcxproj file in the same folder as the *sources* file.

``` syntax
nmake2msbuild.exe  .\myDriver\sources
```

## <span id="related_topics"></span>Related topics


[Converting a WDK sources file to a Visual Studio project](converting-a-wdk-sources-file-to-a-visual-studio-project.md)

[Creating a Driver From Existing Source Files](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_from_existing_source_files)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Nmake2MsBuild%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





