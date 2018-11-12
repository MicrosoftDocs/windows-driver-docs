---
title: Platform Toolset
description: The Windows Driver Kit (WDK) takes advantage of the MSBuild platform toolset feature to provide tools and libraries that are specific to driver development.
ms.assetid: 9F585CA3-B863-408A-B785-2456460D6626
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Platform Toolset


The Windows Driver Kit (WDK) takes advantage of the MSBuild platform toolset feature to provide tools and libraries that are specific to driver development. The MSBuild platform toolset feature is extensible. The specific version of the platform toolset that you want to use is controlled by an MSBuild property called **PlatformToolset**. Projects can switch between tools and libraries by setting the **PlatformToolset** property in the project file.

The Windows Driver Kit (WDK) 8.1 provides the following platform toolsets for driver development.

| **PlatformToolset** (WDK 8.1)       | Use                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WindowsKernelModeDriver8.1**      | For kernel-mode drivers and components.                                                                                                                                                                                                                                                                                                                                                     |
| **WindowsUserModeDriver8.1**        | For user-mode drivers and components.                                                                                                                                                                                                                                                                                                                                                       |
| **WindowsApplicationForDrivers8.1** | For any type of application. This platform toolset provides compatibility with the build options used in the Windows Driver Kit (WDK) for Windows 7 (WDK 7.1), and also uses the default settings that are common for development of user-mode applications that interact with drivers. You might use this setting if you are migrating or converting a project that was built using WDK 7. |
| **Visual Studio 2013 (v120)**       | Use for any type of Windows application (default).                                                                                                                                                                                                                                                                                                                                          |

 

The Windows Driver Kit (WDK) 8 provided the following platform toolsets for driver development. This information is provided for reference only.

| **PlatformToolset** (WDK 8)         | Use                                                                                                                                                                                                                                           |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WindowsKernelModeDriver8.0**      | For kernel-mode drivers and components.                                                                                                                                                                                                       |
| **WindowsUserModeDriver8.0**        | For user-mode drivers and components.                                                                                                                                                                                                         |
| **WindowsApplicationForDrivers8.0** | For any type of application. This platform toolset provides compatibility with the build options used in the WDK for Windows 7 (WDK 7.1). You might use this setting if you are migrating or converting a project that was built using WDK 7. |
| **Visual Studio 2012 (v110)**       | Use for any type of Windows application (default).                                                                                                                                                                                            |

 

**Note**  If you create a driver from one of the available Windows driver templates in Visual Studio, the **PlatformToolset** property is set for you. You can also select the **PlatformToolset** by using the driver project property page in Visual Studio.
**Setting the Platform Toolset in Visual Studio**

1.  Open the property pages for your driver project. Right-click the driver project in **Solution Explorer** and select **Properties**.
2.  In the property pages for the driver project, click **Configuration Properties** and then click **General**.
3.  Select the **Platform Toolset** property for the project from the drop-down list.

 

## <span id="Example_-_Setting_the_PlatformToolset_property_in_a_Visual_Studio_project_file__.vcxproj_"></span><span id="example_-_setting_the_platformtoolset_property_in_a_visual_studio_project_file__.vcxproj_"></span><span id="EXAMPLE_-_SETTING_THE_PLATFORMTOOLSET_PROPERTY_IN_A_VISUAL_STUDIO_PROJECT_FILE__.VCXPROJ_"></span>Example - Setting the **PlatformToolset** property in a Visual Studio project file (.vcxproj)


The following example shows how the **PlatformToolset** property is set in the project file.

```XML
<PropertyGroup Condition="&#39;$(Configuration)|$(Platform)&#39;==&#39;Debug|Win32&#39;"
      Label="Configuration">
  <ConfigurationType>Driver</ConfigurationType>
  <DriverType>KMDF</DriverType>
  <PlatformToolset>WindowsKernelModeDriver8.1</PlatformToolset>
</PropertyGroup>
```

The **ConfigurationType** property controls the target extension and the output type for the binary that is being built. Some of the possible values for this property are **Application**, **DynamicLibrary**, **StaticLibrary**, and **Utility**.

The WDK introduces a new value for this property called **Driver** to build a kernel-mode driver. If you set this property to **Driver**, MSBuild will generate a driver file with .sys as its extension. In the example, the **PlatformToolset** property is set to **WindowsKernelModeDriver8.1** to build a kernel-mode driver. **WindowsKernelModeDriver8.1** is the only WDK platform toolset that requires the **DriverConfigurationType**. In this example, the **DriverType** is set to KMDF.

## <span id="About_the_PlatformToolset_property_for_drivers"></span><span id="about_the_platformtoolset_property_for_drivers"></span><span id="ABOUT_THE_PLATFORMTOOLSET_PROPERTY_FOR_DRIVERS"></span>About the **PlatformToolset** property for drivers


The **PlatformToolset** is a set of property sheets, targets, tools, and tasks that work together to extend and modify a platform in order to build drivers or kernel-mode components for that particular platform. For drivers and related components and applications, the **PlatformToolset** property should be set to **WindowsKernelModeDriver8.1**, **WindowsUserModeDriver8.1**, or **WindowsApplicationForDrivers8.1** in the project file. These platform toolsets are designed to extend the existing Visual Studio C\\C++ tool chain compiler and linker with other WDK-specific build tools and target the WDK headers and libraries. The **WindowsApplicationForDrivers8.1** toolset provides compatibility with the build option settings that were available in the WDK for Windows 7 (WDK 7.1), and also the default settings that are common for development of user-mode applications that interact with drivers.

The **Platform Toolset** has the default platform-level settings and targets to build any driver project. You use default switches for build tools such as the compiler or linker, system information such as the INCLUDE or LIBRARY paths for the WDK, and feature settings such as various properties to set when using Unicode or ANSI strings to build a driver project. If you are developing a Windows application for the desktop, do not use the **WindowsKernelModeDriver8.1**, **WindowsUserModeDriver8.1**, or **WindowsApplicationForDrivers8.1** platform toolset. Instead, use the **Visual Studio 2013 (v120)** platform toolset.

By default, the **PlatformToolset** property is **Visual Studio 2013 (v120)** for both newly created Win32 user mode C++ projects and projects that were converted to Visual Studio 2013. In both cases, the **PlatformToolset** property is not written to the project file.

When you select one of the platform toolsets for drivers, the following properties are set.

-   ExecutablePath and NativeExecutablePath (PATH)
-   IncludePath (INCLUDE)
-   ReferencePath (LIBPATH)
-   LibraryPath (LIB)
-   SourcePath
-   ExcludedPath

**Note**  When **UseEnv** is not set to **TRUE**, PATH, LIB, INCLUDE, LIBPATH will be set from the corresponding property values in the platform toolset. When **UseEnv** is set to **TRUE**, as in the old build system, the values from the environment variables for PATH, INCLUDE, LIB, and LIBPATH will be used instead.

 

## <span id="Where_the_WDK_installs_files_that_enable_the_driver-specific_platform_toolsets"></span><span id="where_the_wdk_installs_files_that_enable_the_driver-specific_platform_toolsets"></span><span id="WHERE_THE_WDK_INSTALLS_FILES_THAT_ENABLE_THE_DRIVER-SPECIFIC_PLATFORM_TOOLSETS"></span>Where the WDK installs files that enable the driver-specific platform toolsets


The following table summarizes the places where the WDK installs files to enable the platform toolsets for driver development.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Path variable</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>$(VCTargetsPath)</p></td>
<td align="left"><p>By default, $(VCTargetsPath) is defined in the registry as $(MSBuildExtensionsPath)&lt;em&gt;&lt;FOLDER&gt;</em>&amp;lt;MSBUILDSYNTAXVERSION&gt;)</p>
<p>The version number is included in case a new build process is used for the same platform, which has new syntax and requires a later MSBuild.</p>
<p>The <em>&lt;FOLDER&gt;</em> is the <strong>Microsoft.Cpp</strong> folder - $(MSBuildExtensionsPath)\Microsoft.Cpp\4.0\v120.</p>
<p>This is called <em>syntax version</em> rather than <em>tools version</em>. It is the assembly version of the first <strong>Microsoft.Build.Engine</strong> that supports all of the necessary syntax. <strong>Microsoft.Cpp</strong> indicates the only folder where Visual Studio will look for platforms.</p></td>
</tr>
<tr class="even">
<td align="left"><p>$(VCTargetsPath)\Platforms$(Platform)\ImportAfter<em>.props</p></td>
<td align="left"><p>Optional folder that does not normally contain files. You can customize the platform by saving MSBuild format files in this folder. They will be imported at the bottom of the platform settings file, as indicated by the folder that they are currently in. The order in which files are imported from this location is undefined. The files that MSBuild creates are $(VCTargetsPath)\Platforms$(Platform)\ImportAfter\Microsoft.Cpp.<em>&lt;Platform&gt;</em>.WindowsKernelModeDriver8.1.props and Microsoft.Cpp.<em>&lt;Platform&gt;</em>.WindowsUserModeDriver8.1.props, which import several WDK-specific props files.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>$(VCTargetsPath)\Platforms$(Platform)\PlatformToolsets$(PlatformToolset)&lt;/p&gt;</td>
<td align="left"><p>For the WDK:</p>
<p>The <strong>$(PlatformToolset)</strong> must be set to <strong>WindowsKernelModeDriver8.1</strong> for building kernel mode drivers, set to <strong>WindowsUserModeDriver8.1</strong> for building user mode drivers, and set to <strong>WindowsApplicationForDrivers8.1</strong> for compatibility with the build options used in the Windows 7 WDK (WDK 7).</p>
<p><strong>PlatformToolset Directory</strong></p>
<p>For example, C:\Program Files\MSBuild\Microsoft.Cpp\v4.0\v120\Platforms\Win32\PlatformToolsets\WindowsKernelModeDriver8.1.</p>
<p>The PlatformToolsets directory allows you to add other types of files later – in their own subfolder.</p>
<p></p></td>
</tr>
<tr class="even">
<td align="left"><p>Microsoft.Cpp.$(Platform).$(PlatformToolset).props</p></td>
<td align="left"><p><strong>Platform Toolset Props file</strong></p>
<p>Imports props files to build a driver. Also imports v120 props file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Microsoft.Cpp.$(Platform).$(PlatformToolset).targets</p></td>
<td align="left"><p><strong>Platform Toolset Targets file</strong></p>
<p>Imports target files to build a driver. These files contain &lt;UsingTask&gt; tags to pull in the WDK tasks. This feature also imports v120 targets.</p></td>
</tr>
<tr class="even">
<td align="left"><p>$(WDKContentRoot)\build</em>.props</p></td>
<td align="left"><p>All driver specific props files. These files contain default settings to build a driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>$(WDKContentRoot)\build*.targets</p></td>
<td align="left"><p>All driver specific targets file. This file identifies the targets to build a driver.</p></td>
</tr>
</tbody>
</table>

 

 

 





