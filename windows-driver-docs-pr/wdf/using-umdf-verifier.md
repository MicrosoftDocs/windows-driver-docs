---
title: Using UMDF Verifier
description: Using UMDF Verifier
ms.assetid: 95D85894-86AF-4312-B5BD-F1C9E8F8B2E5
---

# Using UMDF Verifier


The framework provides built-in verification functionality that you can use to test a running User-Mode Driver Framework (UMDF) driver. This functionality, sometimes called UMDF Verifier, extensively validates your driver's state and the arguments that the driver passes to framework object methods. You can use UMDF Verifier by itself or together with the general-purpose [Application Verifier (AppVerif.exe)](http://www.microsoft.com/download/details.aspx?id=20028) tool.

UMDF Verifier checks lock acquisition and hierarchies, verifies correct I/O cancellation and queue usage, and ensures that the driver and framework follow the documented contracts.

UMDF Verifier causes failures in UMDF driver code to *bug check* the host process. However, a UMDF bug check does not cause a blue text screen to appear with information about the error. Instead, a UMDF bug check:

-   Creates a memory dump file and saves the file to the computer's log file directory (for example, %windir%\\System32\\LogFiles\\WUDF\\*Xxx*.dmp).

    **Note**  Starting in UMDF 2.15, the log directory is *%ProgramData%*\\Microsoft\\WDF.

     

-   Creates an [error report](how-umdf-reports-errors.md) for Microsoft (opt-in).

-   Breaks into the debugger if one is attached to the computer.

-   Terminates the host process and disables the device.

Starting in UMDF 2.0, UMDF Verifier issues breakpoints in some cases, and causes a UMDF bug check in others. This behavior is similar to that of KMDF Verifier.

We recommend running [Application Verifier (AppVerif.exe)](http://www.microsoft.com/download/details.aspx?id=20028) on WUDFHost.exe while testing or debugging your UMDF driver. Use the following command, and then reboot.

``` syntax
AppVerif –enable Heaps Exceptions Handles Locks Memory TLS Leak –for WudfHost.exe
```

Starting in version 2.0 of UMDF, if you run [Application Verifier](http://www.microsoft.com/download/details.aspx?id=20028) on the driver host process (Wudfhost), UMDF Verifier is automatically enabled for all UMDF 2.0 drivers in that host, as well as all UMDF 2.0 drivers in future driver host processes.

In UMDF 1.11 and earlier, the framework's verifier is always on and you cannot turn it off.

## Enabling and Disabling UMDF Verifier


You can manually enable UMDF Verifier by setting **VerifierOn** to a nonzero value in the driver's **Parameters\\Wdf** subkey of the **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\WUDF\\Services\\&lt;driver name&gt;** registry key.

**Note**  The existence of a **VerifierOn** value at all, even set to zero, overrides the linkage with Application Verifier. As a result, we recommend deleting the value if you're not forcing it on, rather than setting it to zero.

 

To determine whether UMDF Verifier is enabled, set a breakpoint at a location after your driver calls [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175) and use the [**!wdfdriverinfo**](https://msdn.microsoft.com/library/windows/hardware/ff565724) debugger extension command:

**!wdfkd.wdfdriverinfo** *&lt;your drivername&gt;* **** **0x1**

For more information about the debugger extension commands, see [Debugger Extensions for Framework-based Drivers](debugger-extensions-for-kmdf-drivers.md).

## <a href="" id="verifier-reg-values"></a>Controlling the Verifier's Behavior


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Using%20UMDF%20Verifier%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




