---
title: Troubleshooting KMDF and UMDF Driver Installation
description: Troubleshooting KMDF and UMDF Driver Installation
ms.assetid: b0b71adc-cb6e-4b84-a5bf-bd1269bcf315
keywords:
- Kernel-Mode Driver Framework WDK , installing drivers
- framework-based drivers WDK KMDF , installing
- INF files WDK KMDF , debugging
- debugging drivers WDK KMDF , installations
- driver debugging WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Troubleshooting KMDF and UMDF Driver Installation


The framework's co-installer creates debugging messages. You can see these messages in a debugger if you are running a checked build of Windows.

Additionally, the co-installer writes its debugging messages to the [Setup action log](https://msdn.microsoft.com/library/windows/hardware/ff550900) (*%windir%\\setupact.log*) file. The Setup action log contains the version of the co-installer and the driver specified in the driver's INF file. You should verify that these are as expected.

## Examining KMDF Installation


The following output in the Setup action log is from the successful installation of a KMDF driver:

```cpp
WdfCoInstaller: DIF_INSTALLDEVICE: Pre-Processing
WdfCoInstaller: ReadComponents:  WdfSection for Driver Service ECHO using KMDF lib version Major 0x1, minor 0x9 
WdfCoInstaller: DIF_INSTALLDEVICE: Coinstaller version: 1.9.7100
WdfCoInstaller: DIF_INSTALLDEVICE: KMDF in-memory version: 1.9.7100
WdfCoInstaller: DIF_INSTALLDEVICE: KMDF on-disk version: 1.9.7100
WdfCoInstaller: Service Wdf01000 is running
WdfCoInstaller: DIF_INSTALLDEVICE: Update is not required. The on-disk KMDF version is newer than or same as the version of the coinstaller
WdfCoInstaller: DIF_INSTALLDEVICE: Post-Processing
```

In the above scenario, no update was necessary because the on-disk version and in-memory framework version is KMDF 1.9, which is the same version of the co-installer.

Consider the following output, which details an unsuccessful installation:

```cpp
WdfCoInstaller: ReadComponents:  WdfSection for Driver Service ECHO using KMDF lib version Major 0x1, minor 0x9  
WdfCoInstaller: DIF_INSTALLDEVICE: Coinstaller version: 1.9.7100
WdfCoInstaller: DIF_INSTALLDEVICE: KMDF in-memory version: 1.7.6000
WdfCoInstaller: DIF_INSTALLDEVICE: KMDF on-disk version: 1.7.6000
WdfCoInstaller: Service Wdf01000 is running
WdfCoInstaller: DIF_INSTALLDEVICE: Reboot is required, because the in-memory KMDF version is older than the coinstaller&#39;s version.
WdfCoInstaller: DIF_INSTALLDEVICE: Update is required, because the on-disk KMDF version is older than the coinstaller
WdfCoInstaller: VerifyMSRoot: exit: error(0) The operation completed successfully.
WdfCoInstaller: Invoking "D:\Windows\system32\wusa.exe "D:\Windows\Temp\WdfTemp\Microsoft Kernel-Mode Driver Framework Install-v1.9-Vista.msu" /quiet /norestart".
WdfCoInstaller: The update process returned error code :error(265) <no error text>. 
WdfCoInstaller: For additional information please look at the log files %windir%\windowsupdate.log and %windir%\Logs\CBS\CBS.log
```

In this scenario, both an update and a reboot were necessary because the in-memory version and the on-disk version of the KMDF runtime were older than the version of the co-installer. However, the update was unsuccessful. The co-installer points to additional log files where you can find more information about the failure.

You can also check the system event log for errors related to the dynamic binding of the KMDF driver to the runtime library. Such an error may generate an **Wdf**&lt;*MajorVersionNumber*&gt;&lt;*MinorVersionNumber*&gt; entry in the system event log. In this case, reboot the computer. You can also force a reinstallation of the KMDF runtime by deleting **Wdf**&lt;*MajorVersionNumber*&gt;&lt;*MinorVersionNumber*&gt;**.sys** from the *%windir%\\system32\\drivers* folder.

## Examining UMDF Installation


The following output in the Setup action log describes a successful UMDF driver installation.

```cpp
WudfUpdate: installing version (1,9,0,7100).
WudfUpdate: Checking for presence of previous UMDF installation.
WudfUpdate: Found binary %WINDIR%\system32\drivers\wudfrd.sys version (1.9.0.7100)
WudfUpdate: Found binary %WINDIR%\system32\drivers\wudfpf.sys version (1.9.0.7100)
WudfUpdate: Found binary %WINDIR%\system32\wudfhost.exe version (1.9.0.7100)
WudfUpdate: Found binary %WINDIR%\system32\wudfsvc.dll version (1.9.0.7100)
WudfUpdate: Found binary %WINDIR%\system32\wudfx.dll version (1.9.0.7100)
WudfUpdate: Found binary %WINDIR%\system32\wudfplatform.dll version (1.9.0.7100)
WudfUpdate: Found binary %WINDIR%\system32\wudfcoinstaller.dll version (1.9.0.7100)
WudfUpdate: UMDF installation is same as update. WudfUpdate: Loading configuration coinstaller from D:\Windows\system32\wudfcoinstaller.dll.
WudfCoInstaller: ReadWdfSection: Checking WdfSection [Echo_Install.NT.Wdf]
WudfCoInstaller: Configuring UMDF Service  WUDFEchoDriver.
WudfCoInstaller: Service WudfSvc is already running.
WudfCoInstaller: Final status: error(0) The operation completed successfully.
```

In the above scenario, no update is necessary because the on-disk version of the runtime is UMDF 1.9, which is the same as the version of the co-installer.

Consider the following output, which details an unsuccessful installation.

```cpp
WudfUpdate: installing version (1,9,0,7100).
WudfUpdate: Checking for presence of previous UMDF installation.
WudfUpdate: Found binary %WINDIR%\system32\drivers\wudfrd.sys version (1.5.0.6000)
WudfUpdate: Found binary %WINDIR%\system32\drivers\wudfpf.sys version (1.5.0.6000)
WudfUpdate: Found binary %WINDIR%\system32\wudfhost.exe version (1.5.0.6000)
WudfUpdate: Found binary %WINDIR%\system32\wudfsvc.dll version (1.5.0.6000)
WudfUpdate: Found binary %WINDIR%\system32\wudfx.dll version (1.5.0.6000)
WudfUpdate: Found binary %WINDIR%\system32\wudfplatform.dll version (1.5.0.6000)
WudfUpdate: Found binary %WINDIR%\system32\wudfcoinstaller.dll version (1.5.0.6000)
WudfUpdate: UMDF installation is older than current.
WudfUpdate: Locating resource stream WUDF_UPDATE_VISTA-RTM.
WudfUpdate: unpacking update from resource to Microsoft User-Mode Driver Framework Install-v1.9-Vista.msu.
WudfUpdate: Temporary path is D:\Windows\Temp\WDF7625.tmp.
WudfUpdate: Invoking update "%SYSTEMROOT%\system32\wusa.exe" with command line "D:\Windows\Temp\WDF7625.tmp\Microsoft User-Mode Driver Framework Install-v1.9-Vista.msu /quiet /norestart".
WudfUpdate: Waiting for update to terminate.
WudfUpdate: Update process returned 22.
WudfUpdate: update returned error 0x16 - error(22) The device does not recognize the command.
WudfUpdate: For additional information please look at the log files %windir%\windowsupdate.log and %windir%\Logs\CBS\CBS.log
WudfUpdate: Cleaning up update.
WudfUpdate: Error updating UMDF - error(22) The device does not recognize the command. Aborting installation.
```

In this scenario, the on-disk version of the UMDF runtime was older than the version of the co-installer. However, in this case the update was unsuccessful. The co-installer points to additional log files where you can find more information regarding the reason for the failure.









