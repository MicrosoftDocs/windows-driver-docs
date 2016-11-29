---
title: Installation of the Enhanced Storage Certificate Management Tool
description: Installation of the Enhanced Storage Certificate Management Tool
ms.assetid: 1494a911-73a4-4a8c-a29d-aecb65c846dd
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Installation%20of%20the%20Enhanced%20Storage%20Certificate%20Management%20Tool%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




