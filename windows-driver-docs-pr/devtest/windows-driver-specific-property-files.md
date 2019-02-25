---
title: Windows driver-specific property files
description: The driver property sheets have default settings for all of the tools that MSBuild uses to build any driver project.
ms.assetid: 696EE510-266B-457A-B74E-491D7804B833
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# <span id="devtest.windows_driver-specific_property_files"></span>Windows driver-specific property files


The driver property sheets have default settings for all of the tools that MSBuild uses to build any driver project.

The following table summarizes these property sheets and their use in terms of the default settings that MSBuild uses to build different drivers.

**Note**  In the Windows Driver Kit (WDK) 8, the names of the driver property sheet files included the kit version number (8.0), for example, **WindowsDriver8.0.KernelMode.ExportDriver.props**.

 

<span id="__WDKContentRoot_"></span><span id="__wdkcontentroot_"></span><span id="__WDKCONTENTROOT_"></span>**$(WDKContentRoot)**  
By default, WDKContentRoot is defined in the registry as: <strong>$(Registry:HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows Kits\\WDK@WDKContentRoot)</strong> which points to **%programfiles%\\Windows Kits\\*version***.

$(WDKContentRoot)\\build will have all the core build extensions that are needed to build a driver.

<span id="WindowsDriver.Default.props"></span><span id="windowsdriver.default.props"></span><span id="WINDOWSDRIVER.DEFAULT.PROPS"></span>**WindowsDriver.Default.props**  
Defines the versioning constants that are used by any driver. For example, **&lt;\_NT\_TARGET\_VERSION\_WIN7&gt;0x0601&lt;/\_NT\_TARGET\_VERSION\_WIN7&gt;**.

<span id="WindowsDriver.Common.props"></span><span id="windowsdriver.common.props"></span><span id="WINDOWSDRIVER.COMMON.PROPS"></span>**WindowsDriver.Common.props**  
Common settings that are required to build all drivers - both kernel mode and user mode.

<span id="WindowsDriver.Shared.props"></span><span id="windowsdriver.shared.props"></span><span id="WINDOWSDRIVER.SHARED.PROPS"></span>**WindowsDriver.Shared.props**  
This property file contains shared build settings that are required to build an application as well as a driver. This file is used in all of the WDK toolsets, for example, WindowsKernelModeDriver8.1, WindowsUserModeDriver8.1, and WindowsApplicationForDrivers8.1.

<span id="WindowsDriver.__Platform_.props"></span><span id="windowsdriver.__platform_.props"></span><span id="WINDOWSDRIVER.__PLATFORM_.PROPS"></span>**WindowsDriver.$(Platform).props**  
These settings are common driver settings that MSBuild applies depending upon the target architecture. **$(Platform)=Win32|x64**

<span id="WindowsDriver.KernelMode.props"></span><span id="windowsdriver.kernelmode.props"></span><span id="WINDOWSDRIVER.KERNELMODE.PROPS"></span>**WindowsDriver.KernelMode.props**  
This property file has common settings that are required to build any kernel-mode binary only. In other words, these settings don’t apply for user-mode drivers and applications.

<span id="WindowsDriver.KernelMode.Driver.props"></span><span id="windowsdriver.kernelmode.driver.props"></span><span id="WINDOWSDRIVER.KERNELMODE.DRIVER.PROPS"></span>**WindowsDriver.KernelMode.Driver.props**  
This property file imports the specific kernel-mode driver type props files (for example, WindowsDriver.8.1.KernelMode.KMDF.props)

<span id="WindowsDriver.KernelMode.KMDF.props"></span><span id="windowsdriver.kernelmode.kmdf.props"></span><span id="WINDOWSDRIVER.KERNELMODE.KMDF.PROPS"></span>**WindowsDriver.KernelMode.KMDF.props**  
These property settings contain special settings that have to be applied only when you are building a KMDF driver. MSBuild uses the **$(DriverType)** property to specify the driver type as **KMDF**, as in the following example: *&lt;DriverType&gt;KMDF&lt;/DriverType&gt;*

<span id="WindowsDriver.KernelMode.Wdm.props"></span><span id="windowsdriver.kernelmode.wdm.props"></span><span id="WINDOWSDRIVER.KERNELMODE.WDM.PROPS"></span>**WindowsDriver.KernelMode.Wdm.props**  
These property settings contain special settings that have to be applied only when you are building a WDM driver. MSBuild uses the **$(DriverType)** property to specify the driver type as **WDM**, as in the following example: *&lt;DriverType&gt;wdm&lt;/DriverType&gt;*.

<span id="WindowsDriver.KernelMode.Gdidriver.props"></span><span id="windowsdriver.kernelmode.gdidriver.props"></span><span id="WINDOWSDRIVER.KERNELMODE.GDIDRIVER.PROPS"></span>**WindowsDriver.KernelMode.Gdidriver.props**  
These property settings contain special settings that have to be applied only when you are building a GDI driver. MSBuild uses the **$(DriverType)** property to specify the driver type as **Gdidriver**, as in the following example: *&lt;DriverType&gt;Gdidriver&lt;/DriverType&gt;*.

<span id="WindowsDriver.KernelMode.ExportDriver.props"></span><span id="windowsdriver.kernelmode.exportdriver.props"></span><span id="WINDOWSDRIVER.KERNELMODE.EXPORTDRIVER.PROPS"></span>**WindowsDriver.KernelMode.ExportDriver.props**  
These property settings contain special settings that have to be applied only when you are building an export driver. MSBuild uses the **$(DriverType)** property to specify the driver type as **ExportDriver**, as in the following example: *&lt;DriverType&gt;ExportDriver&lt;/DriverType&gt;*.

<span id="WindowsDriver.KernelMode.Miniport.props"></span><span id="windowsdriver.kernelmode.miniport.props"></span><span id="WINDOWSDRIVER.KERNELMODE.MINIPORT.PROPS"></span>**WindowsDriver.KernelMode.Miniport.props**  
These property settings are the special settings that you must apply when you build a miniport driver. MSBuild uses the **$(DriverType)** property to specify driver type as **Miniport**, as in the following example: *&lt;DriverType&gt;Miniport&lt;/DriverType&gt;*.

<span id="WindowsDriver.LateEvaluation.props_"></span><span id="windowsdriver.lateevaluation.props_"></span><span id="WINDOWSDRIVER.LATEEVALUATION.PROPS_"></span>**WindowsDriver.LateEvaluation.props**   
Internal use only. Do not edit or use.

<span id="WindowsDriver.masm.props"></span><span id="windowsdriver.masm.props"></span><span id="WINDOWSDRIVER.MASM.PROPS"></span>**WindowsDriver.masm.props**  
These property settings contain the settings for building assembly files (MASM) for the supported architectures (platforms).

<span id="WindowsDriver.UserMode.props"></span><span id="windowsdriver.usermode.props"></span><span id="WINDOWSDRIVER.USERMODE.PROPS"></span>**WindowsDriver.UserMode.props**  
These property settings are the common settings that are required to build any user-mode driver only. In other words, do not apply these settings for kernel-mode drivers and applications.

<span id="WindowsDriver.UserMode.UMDF"></span><span id="windowsdriver.usermode.umdf"></span><span id="WINDOWSDRIVER.USERMODE.UMDF"></span>**WindowsDriver.UserMode.UMDF**  
These property settings are the special settings that you must apply when you build a UMDF driver. MSBuild uses the **$(DriverType)** property to specify the driver type as **UMDF**, as in the following example: *&lt;DriverType&gt;UMDF&lt;/DriverType&gt;*.

 

 





