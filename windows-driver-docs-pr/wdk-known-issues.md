---
title: WDK Known Issues
description: List of known issues for released versions of the Windows Driver Kit (WDK)
keywords:
- Windows Driver Kit
- WDK
- drivers
- known issues
ms.date: 12/16/2020
ms.localizationpriority: medium
---

# Windows Driver Kit (WDK) known issues

This topic details known issues concerning the WDK.

## WDK for Windows 10, version 2004

### Issue in ExAllocatePoolZero, ExAllocatePoolQuotaZero, and ExAllocatePoolPriorityZero functions FIXED

In May 2020, [OSR](https://www.osr.com/) discovered that the new down-level support for automatic zeroing of pool allocations had an issue that could lead to an allocation not getting zero-initialized on systems running Windows 10, version 1909. This has now been fixed with a security refresh of the WDK for Windows 10, version 2004 and the Enterprise WDK (EWDK) for Windows 10, version 2004 on Dec 16th. Microsoft took advantage of the security refresh and updated the EWDK to include the Visual Studio build tools 16.7. Microsoft recommends all driver developers uninstall the original SDK and WDK (version 2004) and install the refresh SDK and WDK or EWDK.

To ensure there was a complete security solution in place, an OS fix was released for Windows 10, version 1909 in November, so if there was a driver created with the security issue the OS would be protected from it.

In addition to downloading the updated WDK/EWDK, Microsoft recommends that all drivers switch all kernel allocations to use the new pool zeroing DDIs which return zeroed memory by default. This will increase driver security and reliability. In order to help with this transition, Microsoft has created a Static Driver Verifier rule which is available in preview Windows 10 WDK versions 20236 and above. The rule will identify all instances in a driver’s source code where the old pool allocation DDIs are being used and will recommend replacing them with the new, safer equivalent DDI. The rule is applicable to WDM, WDF and NDIS based drivers.

### Installing WDK no longer enables Spectre mitigations for all C++ projects as seen in WDK 1903

While the WDK install will enable Spectre mitigation by default for all drivers, it no longer enables them for all C++ projects.

### Error ‘A WDK corresponding to target ’10.0.19041.0’ was not found.’

When selecting [Windows SDK Version] to '10.0 (latest installed version)' with WDK 10.0.19041.0 causes the "A WDK corresponding to target version '10.0.19041.0' was not found" error even if the SDK version is installed.

**Workaround:** In the properties page for the driver project (Configuration Properties >General) set Windows SDK Version to $(LatestTargetPlatformVersion). If this option is not available to select then select the option **inherit from parent or project default**.

### EWDK and SDV running on Server have .NET requirements

Running Static Driver Verifier from the EWDK requires .Net Framework 4.7.2. Depending on the version of Windows on your system, .NET may be installed, may be installed but need to be enabled, or may not be installed. For more information about what version of .NET is installed or the state of .NET installation please review [.NET Framework versions and dependencies](/dotnet/framework/migration-guide/versions-and-dependencies).

### DVL generation fails with System.IO.FileNotFoundException

When attempting to create a Driver Verification Log (DVL), the following error will be presented:

```console
Unhandled Exception: System.IO.FileNotFoundException: 
Could not load file or assembly 
'System.Runtime, Version=4.2.1.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a' 
or one of its dependencies. 
The system cannot find the file specified.
```

This can occur in both the command-line and GUI environments.  This issue is resolved in a future version of the WDK and can be seen in the [Windows Insider Preview WDK](https://www.microsoft.com/software-download/windowsinsiderpreviewWDK). Unfortunately, no workaround exists for the current version.

### SDV fails in the EWDK if VS is not installed

SDV has a dependency on VCRUNTIME140D.dll as part of Visual Studio.  As such, running the EWDK on a machine without VS installed will fail.  Install Visual Studio on the machine to work around this issue.

### Driver Verifier does not get enabled/disabled when using WDK test explorer

Driver Verifier does not get enabled/disabled when Device Fundamental tests are run using the WDK Test Explorer.

**Workaround:** On the client machine manually enable/disable driver verifier per these instructions.

### WDK Side by Side installations of Windows 10, version 2004 and WDK Windows 10, version 1903 or version 1803

With both versions of kits installed on the same PC the ‘Deploy driver’ feature won’t work for older version.

**Workaround:** Use 1803 on a separate machine if Deploy driver feature is needed.

### Windows Device Testing Framework (WDTF) tests now only run on systems with matching Windows 10 versions as the WDK

In WDK for Windows 10, version 1809, changes were made to WDTF in order to support this version of Windows 10, version 1809. The effect of this is that WDTF will no longer run on down-level OS. The change continues with WDK for Windows 10, version 2004.

#### Alterative for down-level testing

The WDTF tests in WDK for Windows 10, version 1803 can be run on previous Windows versions.

### APIValidator

On an x86 arch machine APIValidator is unable to run against x64 binaries. If building x64 drivers on an x86 machine APIValidator should be turned off.

**Workaround:**

1. Go to the properties page of the driver solution.

2. Select **APIValidator**, then **General**, and then change **Run ApiValidator** from **Yes** to **No**.

### WDK running on Windows 7 systems requires KB 3033929

You must install Microsoft Security Advisory 3033929 (KB3033929) prior to installing the WDK on systems running Windows 7.  KB3033929 can be downloaded from the [Microsoft Download Center](https://www.microsoft.com/download/details.aspx?id=46148).

### Installing the WDK generates an error from Visual Studio that the add-in component is already installed

This error message can be seen if the WDK was uninstalled but the WDK drivers extension for Visual Studio was not uninstalled.

**Resolution:** In Visual Studio, go to the **Extension** dropdown menu, choose **Manage Extensions**, select the **Windows Driver Kit**, and then click **Uninstall**.

## FAQ

### How do I tell if the WDK or EWDK versions I have contains the fix for the zeroing of pool allocations?

In **System Settings** go to **Add or Remove programs**, search for **Windows Driver Kit** and note the version. The original WDK for Windows 10, version 2004 has a version of 10.0.19041.1, the refreshed WDK version is 10.0.19041.685
For the EWDK, once the EWDK environment is launched, look at the title of the command window. The refreshed version will contain **vb_release_svc_prod1.19041.685**. Additionally, when looking at the environment variables, the **BuildLab** variable should show **vb_release_svc_prod1.19041.685**.  

### The Windows Software Development Kit (SDK) was also refreshed, is this needed as well?

No, however the refreshed Windows Software Development Kit (SDK) contains a fix for onecore.lib that may be nice to have. Also, it’s generally a good idea to keep the SDK and WDK aligned.

### If I already have the WDK for Windows 10, version 2004 installed, do I need to uninstall it before installing the refreshed version?

It is highly recommended that if you have the original 2004 SDK and WDK that these be uninstalled and the security refresh SDK and WDK be installed. That said if the refreshed WDK is installed on top of the original WDK the refreshed version will overwrite the original. Note: In this scenario “Add or remove programs”, both versions will be listed.
