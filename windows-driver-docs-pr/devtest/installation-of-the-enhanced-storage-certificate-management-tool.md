---
title: Installation of the Enhanced Storage Certificate Management Tool
description: Installation of the Enhanced Storage Certificate Management Tool
ms.assetid: 1494a911-73a4-4a8c-a29d-aecb65c846dd
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installation of the Enhanced Storage Certificate Management Tool


The Enhanced Storage Certificate Management tool is available for x86-based, Itanium-based, and x64-based computers that run Windows 7 and later versions of Windows. To install the Enhanced Storage Certificate Management tool on a computer, complete the following steps:

1.  Copy EhStorCertMgrCmd.exe from WDKPath\\tools\\EnhancedStorage\\ProcessorArchitecture to %SystemRoot%\\System32 on the computer, where:

    -   *WDKPath* is the path of the directory that you installed the Windows Driver Kit (WDK) on.
    -   *ProcessorArchitecture* is the processor architecture of the computer that the Enhanced Storage Certificate Management tool will be installed and running on. The WDK installs processor-specific versions of the files in the tools\\EnhancedStorage\\amd64, tools\\EnhancedStorage\\i386, and tools\\EnhancedStorage\\ia64 subdirectories under the *WDKPath* directory.

    For example, if the test computer is running the 32-bit version of Windows, you have to copy tools\\EnhancedStorage\\i386\\EhStorCertMgrCmd.exe to %SystemRoot%\\System32.

2.  Copy EhStorCertMgrComponent.dll from WDKPath\\tools\\EnhancedStorage\\ProcessorArchitecture to %SystemRoot%\\System32 on the computer.

3.  Copy EhStorCertMgrCmd.exe.mui and EhStorCertMgrComponent.dll.mui from WDKPath\\tools\\EnhancedStorage\\ProcessorArchitecture to the locale-specific subdirectory in %SystemRoot%\\System32 on the computer.

    For example, if your locale is the United States, you must copy all of the .mui files to %SystemRoot%\\System32\\EN-US.

4.  Click **Start**.

5.  Right-click **Command Prompt** and click **Run as administrator**.

6.  At the command prompt, type the following command:
    ```
    regsvr32 /s %SystemRoot%/System32/EhStorCertMgrComponent.dll
    ```

**Note**  The files for the Enhanced Storage Certificate Management tool can be copied and installed on other computers that do not have the WDK installed.

 

 

 





