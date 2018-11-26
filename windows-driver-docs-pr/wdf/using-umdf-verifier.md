---
title: Using UMDF Verifier
description: Using UMDF Verifier
ms.assetid: 95D85894-86AF-4312-B5BD-F1C9E8F8B2E5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using UMDF Verifier


The framework provides built-in verification functionality that you can use to test a running User-Mode Driver Framework (UMDF) driver. This functionality, sometimes called UMDF Verifier, extensively validates your driver's state and the arguments that the driver passes to framework object methods. You can use UMDF Verifier by itself or together with the general-purpose [Application Verifier (AppVerif.exe)](../debugger/debugger-download-tools.md) tool.

UMDF Verifier checks lock acquisition and hierarchies, verifies correct I/O cancellation and queue usage, and ensures that the driver and framework follow the documented contracts.

UMDF Verifier causes failures in UMDF driver code to *bug check* the host process. However, a UMDF bug check does not cause a blue text screen to appear with information about the error. Instead, a UMDF bug check:

-   Creates a memory dump file and saves the file to the computer's log file directory (for example, %windir%\\System32\\LogFiles\\WUDF\\*Xxx*.dmp).

    **Note**  Starting in UMDF 2.15, the log directory is *%ProgramData%*\\Microsoft\\WDF.

     

-   Creates an [error report](how-umdf-reports-errors.md) for Microsoft (opt-in).

-   Breaks into the debugger if one is attached to the computer.

-   Terminates the host process and disables the device.

Starting in UMDF 2.0, UMDF Verifier issues breakpoints in some cases, and causes a UMDF bug check in others. This behavior is similar to that of KMDF Verifier.

We strongly recommend doing all development and testing of your driver after enabling [Application Verifier (AppVerif.exe)](../debugger/debugger-download-tools.md) on WUDFHost.exe. Use the following command, attach a debugger and then reboot.

```cpp
AppVerif –enable Heaps Exceptions Handles Locks Memory TLS Leak –for WudfHost.exe
```

Starting in version 2.0 of UMDF, if you run [Application Verifier](../debugger/debugger-download-tools.md) on the driver host process (Wudfhost), UMDF Verifier is automatically enabled for all UMDF 2.0 drivers in that host, as well as all UMDF 2.0 drivers in future driver host processes.

In UMDF 1.11 and earlier, the framework's verifier is always on and you cannot turn it off.

## Enabling and Disabling UMDF Verifier


You can manually enable UMDF Verifier by setting **VerifierOn** to a nonzero value in the driver's **Parameters\\Wdf** subkey of the **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\WUDF\\Services\\&lt;driver name&gt;** registry key.

**Note**  The existence of a **VerifierOn** value at all, even set to zero, overrides the linkage with Application Verifier. As a result, we recommend deleting the value if you're not forcing it on, rather than setting it to zero.

 

To determine whether UMDF Verifier is enabled, set a breakpoint at a location after your driver calls [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175) and use the [**!wdfdriverinfo**](https://msdn.microsoft.com/library/windows/hardware/ff565724) debugger extension command:

**!wdfkd.wdfdriverinfo** *&lt;your drivername&gt;* **** **0x1**

For more information about the debugger extension commands, see [Debugger Extensions for Framework-based Drivers](debugger-extensions-for-kmdf-drivers.md).

## Controlling the Verifier's Behavior


You can control the behavior of UMDF Verifier by modifying values in the registry. Alternatively, you can use the [WDF Verifier control application](https://msdn.microsoft.com/library/windows/hardware/ff556129) to set these values.

The following registry values can be used with UMDF 1.*x* drivers, as well as UMDF 2.0 and later drivers.

<a href="" id="verifydownlevel--------------reg-dword-"></a>**VerifyDownLevel** (**REG\_DWORD**)  
If **VerifyDownLevel** is set to a nonzero value, and if the driver was built with a version of the framework that is older than the current version, the framework's verifier includes tests that were added after the driver was built. If this value does not exist or is set to zero, the framework's verifier includes only the tests that existed when the driver was built.

For example, if your driver was built with version 1.7 of the framework, and if version 1.9 of the framework is installed on the computer, setting **VerifyDownLevel** to nonzero causes the verifier to include tests that were added to version 1.9 of the verifier when your driver runs.

This value is located in the **Parameters\\Wdf** subkey of the **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\WUDF\\Services\\*DriverName*** registry key.

<a href="" id="trackobjects-----------------------------reg-dword-"></a>**TrackObjects** (**REG\_DWORD**)  
If **TrackObjects** is set to a nonzero value, the framework enters the debugger when the driver is unloaded, if any framework-based objects have [leaked](determining-if-a-driver-leaks-framework-objects.md) (not been deleted).

During regular testing, you should enable **TrackObjects** and not **TrackRefCounts**. If the verifier reports that the driver is leaking framework objects, then use the control application to enable the **TrackRefCounts** verifier option.

This value is located in the *DefaultHostProcessGuid* subkey of the **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\WUDF\\Services** registry key, where *DefaultHostProcessGuid* is a value that you can find in the **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\WUDF** subkey.

<a href="" id="trackrefcounts-----------------------------reg-dword-"></a>**TrackRefCounts** (**REG\_DWORD**)  
If **TrackRefCounts** is set to a nonzero value, the framework maintains a count of the number of references to each framework-based object. You can use the [!wudfrefhist](using-umdf-debugger-extensions.md) debugger extension to view the changes of an object's reference count.

Setting **TrackRefCounts** to a nonzero value degrades the driver's performance, so you should leave the value at zero unless you are debugging an object deletion bug.

This value is located in the *DefaultHostProcessGuid* subkey of the **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\WUDF\\Services** registry key, where *DefaultHostProcessGuid* is a value that you can find in the **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\WUDF** subkey.

In addition to the registry values listed above, UMDF 2.0 and later drivers can also use many of the registry values listed in [Using KMDF Verifier](using-kmdf-verifier.md).

 

 





