---
title: ProjectUpgradeTool
description: The ProjectUpgradeTool takes Microsoft Visual Studio 2012 projects (*.vcxproj) and solution files (*.sln) that were created with the Windows Driver Kit (WDK) for Windows 8 and upgrades them to work with the WDK for Windows 8.1 and Microsoft Visual Studio 2013.
ms.assetid: DEB7799C-D505-40E6-B2B0-CF774A99B1BE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ProjectUpgradeTool


The ProjectUpgradeTool takes Microsoft Visual Studio 2012 project (\*.vcxproj) and solution files (\*.sln) that were created with the Windows Driver Kit (WDK) for Windows 8 and upgrades them to work with the WDK for Windows 8.1 and Microsoft Visual Studio 2013.

**Important**  The ProjectUpgradeTool does not change your source files. The tool only converts the project and solutions files. By default, the tool saves a backup copy of the original files.



**To upgrade a WDK 8 project or solution to WDK 8.1**

1.  Open a Visual Studio Command Prompt window.
2.  Type the command **ProjectUpgradeTool** and specify the root (or parent) directory that contains the Windows Driver Kit (WDK) 8 project or solution files that you want to upgrade to the Windows Driver Kit (WDK) 8.1 for Windows 8.1. For example, the following command upgrades all the files in C:\\myDriver directory and subdirectories.

    ```
    ProjectUpgradeTool.exe  C:\myDriver
    ```

3.  Open the WDK 8.1 project or solution files using Visual Studio 2013. The tool keeps the original names of the files. The previous versions are saved with the .backup file name extension.
    **Note**  If you want to be able to build targets for Windows Vista, using Visual Studio 2013 and WDK 8.1, see [What to do if you are unable to build a Windows Vista target after migrating a WDK 8 project to WDK 8.1](#build-vista-with-wdk-8-1).



## <span id="ProjectUpgradeTool_Syntax"></span><span id="projectupgradetool_syntax"></span><span id="PROJECTUPGRADETOOL_SYNTAX"></span>ProjectUpgradeTool Syntax


The project upgrade tool is located in the %WindowsSdkDir%\\bin\\x86\\ directory. For example, C:\\Program Files (x86)\\Windows Kits\\8.1\\bin\\x86.

The ProjectUpgradeTool.exe has the following syntax:

```
ProjectUpgradeTool.exe  < rootDir >
                          [-Log:[<LogFile>]:[<Verbosity>]]
                          [-ConsoleLog:<Verbosity>]
                          [-NoBackup]
                          [-NoToolsetUpgrade]
                          [-InPlaceUpgrade]
                          [-ForceUpgrade]
                          [-KeepObsoleteConfigs]   
```

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>-Log:</strong><em>&lt;LogFile&gt;</em><strong>:[</strong><em>&lt;Verbosity&gt;</em><strong>]</strong></p></td>
<td align="left"><p>Specifies a name for the Log file, and specifies the level of logging (see <em>Verbosity</em>).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-ConsoleLog:</strong><em>&lt;Verbosity&gt;</em></p></td>
<td align="left"><p>Specifies a name for the Console log file, and specifies the level of logging (see <em>Verbosity</em>).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Verbosity</em></p></td>
<td align="left"><p>The default logging levels for Log file and Console logging are <strong>Verbose</strong> and <strong>Information</strong> respectively. <em>Verbosity</em> is one of <strong>System.Diagnostics.SourceLevels</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-NoBackup</strong></p></td>
<td align="left"><p>Tells the ProjectUpgradeTool not to make backup copy of the original project (.vcxproj) or solutions (.sln). When you select this option, the original project and solution files are overwritten and will only work with the WDK for Windows 8.1 and Visual Studio 2013.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-NoToolsetUpgrade</strong></p></td>
<td align="left"><p>Specify the <strong>-NoToolsetUpgrade</strong> option if you do not want to use the WDK 8.1 platform toolset when you specify build configurations for Windows versions prior to Windows 8.1. When you select this option, only the <strong>WinPreRel</strong> configurations will be built using the most recent WDK.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-InPlaceUpgrade</strong></p></td>
<td align="left"><p>Replaces every existing build configuration with the new <strong>WinPreRel</strong> configuration. This prevents you from building for previous versions of Windows.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-ForceUpgrade</strong></p></td>
<td align="left"><p>Forces every project file (.vcxproj) to be upgraded, even if the project does not meet the requirements of a driver project.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-KeepObsoleteConfigs</strong></p></td>
<td align="left"><p>Retains target configurations for operating systems that are no longer supported by the WDK (for example, Windows Vista). However, to build for these obsolete targets, you need to have Visual Studio 2012 and the WDK 8 installed on the computer, in addition to WDK 8.1 and Visual Studio 2013. For example, suppose you want to upgrade the driver project to use the WDK 8.1 for all supported target versions (Windows 7, Windows 8, and Windows 8.1). And you still want to use the same driver project to continue building for Windows Vista. To do that, you upgrade the project file using the <strong>-KeepObsoleteConfigs</strong> option to keep the Windows Vista target configuration in the project. The Windows Vista configuration will continue to use the <strong>WindowsKernelModeDriver8.0</strong> tool set (available in WDK 8), even if you build the project in Visual Studio 2013.</p></td>
</tr>
</tbody>
</table>



## <span id="Comments"></span><span id="comments"></span><span id="COMMENTS"></span>Comments


-   [What to do if you see Error MSB8020 (Platform Toolset = 'WindowsKernelModeDriver8.0') cannot be found](#what-to-do-if-you-see-error-msb8020)
-   [What to do if you are unable to build a Windows Vista target after migrating a WDK 8 project to WDK 8.1](#build-vista-with-wdk-8-1)

### <span id="What_to_do_if_you_see_Error_MSB8020__Platform_Toolset____WindowsKernelModeDriver8.0___cannot_be_found_"></span><span id="what_to_do_if_you_see_error_msb8020__platform_toolset____windowskernelmodedriver8.0___cannot_be_found_"></span><span id="WHAT_TO_DO_IF_YOU_SEE_ERROR_MSB8020__PLATFORM_TOOLSET____WINDOWSKERNELMODEDRIVER8.0___CANNOT_BE_FOUND_"></span><a name="what-to-do-if-you-see-error-msb8020"></a>What to do if you see Error MSB8020 (Platform Toolset = 'WindowsKernelModeDriver8.0') cannot be found

If you attempt to open a project or solution that was created with WDK 8, you might see the following error message when you attempt to build the project using WDK 8.1.

```
1>C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.Cpp.Platform.targets(54,5): error MSB8020: The builds tools for WindowsKernelModeDriver8.0 (Platform Toolset = 'WindowsKernelModeDriver8.0') cannot be found. To build using the WindowsKernelModeDriver8.0 build tools, please install WindowsKernelModeDriver8.0 build tools. Alternatively, you may update to the current Visual Studio tools by selecting the Project menu or right-click the solution, and then selecting "Update VC++ Projects...".
```

The platform toolset in the WDK 8 was **WindowsKernelModeDriver8.0**. To fix this error, run the ProjectUpgradeTool as described here and upgrade your WDK 8 solution to use the toolset available in WDK 8.1

### <span id="build_vista_with_WDK_8.1"></span><span id="build_vista_with_wdk_8.1"></span><span id="BUILD_VISTA_WITH_WDK_8.1"></span><a name="build-vista-with-wdk-8-1"></a>What to do if you are unable to build a Windows Vista target after migrating a WDK 8 project to WDK 8.1

**Issue:** Unable to build a Windows Vista target after migrating a WDK 8 project to WDK 8.1.

**Scenario:** You have created a project using the WDK 8 and Visual Studio 2012. You’ve upgraded the project/solution using WDK 8.1 and Visual Studio 2013, using the ProjectUpgradeTool tool. You do this using the following command to preserve the Windows Vista configuration: **ProjectUpgradeTool.exe** *PathToProjectFolder* **-KeepObsoleteConfigs.**

You open the project in WDK 8.1. When you build a Win32 Windows Vista target, you might see the following error message:

```
error MSB6004: The specified task executable location "C:\Program Files (x86)\Windows Kits\8.0\bin\x86\x86\CL.exe" is invalid.   C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V110\Microsoft.CppCommon.targets  347 5   KMDF Driver1
```

When you build an x64 Windows Vista target, you might see the following error messages:

```
error TRK0002: Failed to execute command: ""C:\Program Files (x86)\Windows Kits\8.0\bin\x64\stampinf.exe" -d * -a amd64 -v * -k 1.11 -u 1.11.0 -f x64\VistaRelease\KMDFDriver1.inf". The operation identifier is not valid.  C:\Users\Administrator\Desktop\KMDF Driver1 - Copy\KMDF Driver1\TRACKER KMDF Driver1
```

```
error : Verification Error: Driver package has no driver version.    C:\Program Files (x86)\Windows Kits\8.0\build\WindowsDriver8.0.common.targets   1338    5   KMDF Driver1 Package
```

**Workaround:** You need to make two changes.

1.  **Correct the WindowsDriver8.0.x64.props and WindowsDriver8.0.Win32.props files.**

    You need to make corrections in conditional expressions in these two \*.props files. The files are located in C:\\Program Files (x86)\\Windows Kits\\8.0\\build directory.

    In each \*.props file, locate the expression where `('$(VisualStudioVersion)' != '11.0')`. For example, the first instance will look like the following:

    ```XML
            <When  Condition="&#39;$(VisualStudioVersion)&#39; != &#39;11.0&#39;">
          <PropertyGroup>
            <CLToolPath Condition="&#39;$(CLToolPath)&#39; == &#39;&#39;">$(WDKContentRoot)bin\x86\x64</CLToolPath>
            <CLToolArchitecture>Native32Bit</CLToolArchitecture>
            <LinkToolPath Condition="&#39;$(LinkToolPath)&#39; == &#39;&#39;">$(WDKContentRoot)bin\x86\x64</LinkToolPath>
            <LinkToolArchitecture>Native32Bit</LinkToolArchitecture>
            <MIDLToolPath Condition="&#39;$(MIDLToolPath)&#39; == &#39;&#39;">$(WDKContentRoot)bin\x86</MIDLToolPath>
            <MIDLToolArchitecture>Native32Bit</MIDLToolArchitecture>
            <LibToolPath Condition="&#39;$(LibToolPath)&#39; == &#39;&#39;">$(WDKContentRoot)bin\x86</LibToolPath>
            <LibToolArchitecture>Native32Bit</LibToolArchitecture>
            <ExecutablePath>$(WDKContentRoot)bin\x86\x64;$(WDKContentRoot)bin\x86;$(WDKContentRoot)tools\pfd\bin\bin\AMD64;$(WDKContentRoot)tools\tracing\x64;$(ExecutablePath)</ExecutablePath>      
        </PropertyGroup>
        </When>
    ```

    Change the not equals (!=) to less than ("&lt;").

    ```XML
        <When  Condition="&#39;$(VisualStudioVersion)&#39; &lt;&#39;11.0&#39;">
    ```

    Locate the next instance of the expression where `('$(VisualStudioVersion)' != '11.0')`

    ```XML
        <When Condition="(&#39;$(PlatformToolset)&#39; == &#39;WindowsApplicationForDrivers8.0&#39;) and (&#39;$(VisualStudioVersion)&#39; != &#39;11.0&#39;)">
    ```

    And change the not equals (!=) to less than ("&lt;").

    ```XML
        <When Condition="(&#39;$(PlatformToolset)&#39; == &#39;WindowsApplicationForDrivers8.0&#39;) and (&#39;$(VisualStudioVersion)&#39; &lt;&#39;11.0&#39;)">
    ```

    After you make the changes, save both \*.props files.

2.  **Correct the project file for the driver.**

    Open the project file (\*.vcxproj) for your driver.

    Locate the Vista target configurations in your project file (release and debug). For example:

    ```XML
       <PropertyGroup Label="Configuration" Condition="&#39;$(Configuration)|$(Platform)&#39;==&#39;Vista Debug|Win32&#39;">
        <TargetVersion>Vista</TargetVersion>
        <UseDebugLibraries>True</UseDebugLibraries>
        <PlatformToolset>WindowsKernelModeDriver8.0</PlatformToolset>
      </PropertyGroup>
    ```

    Add the **PackageDir** property to your Windows Vista configuration settings. In most instances, you should use the default values: `<PackageDir>$(OutDir)\$(Intdir)</PackageDir>`.

    ```XML
       <PropertyGroup Label="Configuration" Condition="&#39;$(Configuration)|$(Platform)&#39;==&#39;Vista Debug|Win32&#39;">
        <TargetVersion>Vista</TargetVersion>
        <PackageDir>$(OutDir)\$(Intdir)</PackageDir>
        <UseDebugLibraries>True</UseDebugLibraries>
        <PlatformToolset>WindowsKernelModeDriver8.0</PlatformToolset>
      </PropertyGroup>
    ```

    Make the same change for your other configurations.

    ```XML
        <PropertyGroup Label="Configuration" Condition="&#39;$(Configuration)|$(Platform)&#39;==&#39;Vista Release|Win32&#39;">
        <TargetVersion>Vista</TargetVersion>
        <PackageDir>$(OutDir)\$(Intdir)</PackageDir>
        <UseDebugLibraries>False</UseDebugLibraries>
        <PlatformToolset>WindowsKernelModeDriver8.0</PlatformToolset>
      </PropertyGroup>
    ```

    After you make these changes and save the file you can open and build the project in Visual Studio 2013. The project should continue to work with Visual Studio 2012. Note that even after these changes, you still need to have WDK 8 and Visual Studio 2012 installed on the computer.

## <span id="related_topics"></span>Related topics


[Building a Driver](https://msdn.microsoft.com/windows-drivers/develop/building_a_driver)

[WDK and Visual Studio build environment](wdk-and-visual-studio-build-environment.md)










