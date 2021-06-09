---
title: Registry Values for Debugging WDF Drivers
description: This topic describes the registry values that a Windows Driver Frameworks (WDF) driver can set. It applies to Kernel-Mode Driver Framework (KMDF) drivers and User-Mode Driver Framework (UMDF) drivers starting with UMDF version 2.
keywords:
- debugging drivers WDK KMDF , registry values
- registry values for debugging drivers WDK KMDF
ms.date: 04/28/2020
ms.localizationpriority: medium
---

# Registry Values for Debugging WDF Drivers


This article describes the registry values that a WDF driver can set. It applies to KMDF drivers and UMDF drivers starting with UMDF version 2.

Unless otherwise specified in sections below, the following registry values are located under a driver's `Parameters\Wdf` subkey.

* For a KMDF driver, this subkey is located in `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services`, under the driver's service name.
* For a UMDF driver, this subkey is located in `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\WUDF\Services`, under the driver's service name.

The subkey for the driver always uses the driver's service name, even if the driver binary's file name differs from the service name.


## DbgBreakOnError

*REG\_DWORD*

If set to a nonzero value, the framework breaks into the debugger when a driver calls [**WdfVerifierDbgBreakPoint**](/windows-hardware/drivers/ddi/wdfverifier/nf-wdfverifier-wdfverifierdbgbreakpoint). (If the **VerifierOn** value is set, the framework breaks into the debugger even if the **DbgBreakOnError** value does not exist.) See the code example in the [**VerifierOn**](#verifieron) section.

## DbgPrintOn

*REG\_DWORD*

* For a KMDF driver, set this value under the `HKLM\SYSTEM\CurrentControlSet\Control\Wdf\Kmdf\Diagnostics` registry key.
* For a UMDF driver, set this value under the `HKLM\System\CurrentControlSet\Control\Wdf\Umdf\Diagnostics` registry key.

The driver might need to create the optional **Diagnostics** subkey.

If set to a nonzero value, the framework's loader sends a variety of messages to the kernel debugger while it is loading a driver and binding it to a version of the framework library, or while it is unloading a driver.

## DbgWaitForSignalTimeoutInSec

*REG\_DWORD, framework versions 1.11 and later*

Starting in Windows 8, when **VerifierOn** and **DbgBreakOnError** are set to nonzero values, the driver can change the default timeout period for breaking into the debugger by setting **DbgWaitForSignalTimeoutInSec**.

## DebugModeBinaries

*REG\_MULTI\_SZ, UMDF-only*

This registry value is located in `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\WUDF\DebugMode`.

This value specifies the names of the driver binaries to be loaded in debug mode. To enable debug mode for driver binaries X.DLL, Y.DLL and Z.DLL, for example, this value would be set to `X.DLL\0Y.DLL\0Z.DLL\0\0`.

## DebugModeFlags

*REG\_DWORD, UMDF-only*

This registry value is located in `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\WUDF\DebugMode`.

|Value|Description|
|--- |--- |
|0x01|Enable debug mode. This setting turns off the automatic restart functionality described in [Using Device Pooling in UMDF Drivers](using-device-pooling-in-umdf-drivers.md).|
|0x02|Disable device pooling. For more information about device pooling, see [Using Device Pooling in UMDF Drivers](using-device-pooling-in-umdf-drivers.md).|
|0x04|Disable timeouts.|
 
When you use the F5 option in Microsoft Visual Studio, all three flags are set for the deployed driver.

## EnhancedVerifierOptions

*REG\_DWORD, framework versions 1.9 and later*

This value contains a bitmap. Each bit represents an additional verifier option that users can enable by setting the bit.

*Bit values:*

**0x1**: If set, the verifier checks whether each of the driver's event callback functions does the following:

-   Returns at the same IRQL at which it was called. If the values are different, a [**WDF\_VIOLATION**](../debugger/bug-check-0x10d---wdf-violation.md) bug check occurs with an error code of 0xE.

-   Before returning, exits all [critical regions](../kernel/critical-regions-and-guarded-regions.md) that it enters. If the callback function returns within a critical region that it entered, a [**WDF\_VIOLATION**](../debugger/bug-check-0x10d---wdf-violation.md) bug check occurs with an error code of 0xF.

**0x10000**: If set, and if the driver has enabled [guaranteed forward progress](guaranteeing-forward-progress-of-i-o-operations.md) for an I/O queue, the framework simulates a low-memory situation for each of the queue's I/O requests.

**0x20000**: If set, and if the driver has enabled guaranteed forward progress for an I/O queue, the framework simulates a low-memory situation for some randomly selected I/O requests.

## ForceLogsInMiniDump

*REG\_DWORD*

Set to a nonzero value to cause the framework to include information from its event logger in crash dump files.

## HostFailKdDebugBreak

*REG\_DWORD, UMDF-only*

This registry value is located in `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\WUDF`.

If this value is non-zero and a kernel debugger is connected to the machine, the reflector breaks into the kernel debugger before terminating the host process. **HostFailKdDebugBreak** is disabled by default in Windows 7 and earlier operating systems. Starting in Windows 8, **HostFailKdDebugBreak** is enabled by default.

The reflector also breaks into the kernel debugger if there is an unexpected termination of the host process (e.g. by a non-UMDF component or due to an unhandled exception). If there are multiple device stacks pooled in the host process that is being terminated, the reflector breaks into the debugger multiple times, once for each device stack loaded in the host process.


## HostProcessDbgBreakOnDriverLoad (driver-specific)

*REG\_DWORD*, UMDF-only, works with any UMDF 1.x/2.x driver running on a target computer with [UMDF version 2.31](umdf-version-history.md) or later

This registry value is located in `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\WUDF\Services\<service name>\Parameters\Wdf`.

This value affects only the specified UMDF driver.

Contains a delay value in seconds. Causes WUDFHost to try to connect to a debugger for the specified number of seconds after the driver has been loaded.

During the specified delay period, the host process looks for the user-mode debugger once a second and breaks in if one is connected. If a user-mode debugger is not attached within this period and the high bit in is set (0x80000000), the framework makes a single attempt to break into the kernel-mode debugger. See the section on **HostProcessDbgBreakOnStart** above for examples.

For changes to UMDF registry values to take effect, you must reboot the computer.


## HostProcessDbgBreakOnDriverLoad (global)

*REG\_DWORD, UMDF-only*

This registry value is located in `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\WUDF\Services\{193a1820-d9ac-4997-8c55-be817523f6aa}`. You can set it by using the [WDF Verifier tool](../devtest/global-wdf-settings-tab.md) (WdfVerifier.exe) in the WDK. This value affects all UMDF drivers on the system.

Contains a delay value in seconds. Causes WUDFHost to delay the specified number of seconds after the driver has been loaded. The behavior for **HostProcessDbgBreakOnDriverLoad** is otherwise the same as that described for **HostProcessDbgBreakOnStart**.

Specifying **HostProcessDbgBreakOnStart** or **HostProcessDbgBreakOnDriverLoad** causes the framework to disable other UMDF timeouts (for example, Plug and Play operations). This means that if your driver causes excessive timeouts, using these values might result in your driver causing a fatal crash on the target.


## HostProcessDbgBreakOnStart

*REG\_DWORD, UMDF-only*

This registry value is located in `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\WUDF\Services\{193a1820-d9ac-4997-8c55-be817523f6aa}`. You can set it by using the [WDF Verifier tool](../devtest/global-wdf-settings-tab.md) (WdfVerifier.exe) in the WDK. This value affects all UMDF drivers on the system.

Contains a delay value in seconds. During the specified delay period, the host process looks for the user-mode debugger once a second and breaks in if one is connected. If a user-mode debugger is not attached within this period and the high bit in **HostProcessDbgBreakOnStart** is set (0x80000000), the framework makes a single attempt to break into the kernel-mode debugger. For example:

|Value|Result|
|--- |--- |
|0x00000004|The framework attempts to connect to the user-mode debugger once a second for 4 seconds. The framework never tries to connect to the kernel-mode debugger.|
|0x80000000|The framework makes a single attempt to connect to the user-mode debugger. If the user-mode debugger is not attached, the framework tries to connect to the kernel-mode debugger.|
|0x80000004|The framework attempts to connect to the user-mode debugger once a second for 4 seconds. If the user-mode debugger is not attached within 4 seconds, the framework tries to connect to the kernel-mode debugger.|

You can also set this registry value by using the [WDF Verifier tool](../devtest/global-wdf-settings-tab.md) (WdfVerifier.exe) that is included in the WDK.


## LogPages

*REG\_DWORD*

Set to the number of memory pages that the framework assigns to its event logger. If the value is undefined, the framework uses a default value of one page. The maximum value that you can set is 16 for computers that have 4-kilobyte-sized memory pages (x86 and amd64 processors) and 8 for computers that have 8-kilobyte-sized memory pages (ia64 processors). (The operating system might not write the log contents to a crash dump file if a large number of pages is specified.) Use the [AddService directive](../install/inf-addservice-directive.md) and the [AddReg directive](../install/inf-addreg-directive.md) to set this value in your INF file, as follows:

```inf
[xxx.NT.Services]
AddService = yyy, 2, zzz.AddService

[zzz.AddService]
DisplayName   = %aaa\bbb%
ServiceType   = 1
StartType     = 3
ErrorControl  = 1
ServiceBinary = %12%\ddd.SYS
AddReg         = eee.AddReg

[eee.AddReg]
HKR, Parameters\Wdf, LogPages,   0x00010001, 3 ; KMDF IFR size
```

## TrackHandles

*REG\_MULTI\_SZ*

If set to a list of one or more type names of framework object handles, and if **VerifierOn** is set, the framework tracks references to all object handles that match the specified handle types. For example, if the handle type list consists of the "WDFREQUEST WDFQUEUE" string, the framework tracks references to all request objects and queue objects. If the list contains an asterisk ("\*"), the framework tracks all object handles.

## VerboseOn

*REG\_DWORD*

If set to a nonzero value, the framework's [event logger](using-the-framework-s-event-logger.md) records additional information that can help you debug your driver, such as entries into or exits from internal code paths. You should set this value only while you are developing your driver. See the code example in [**VerifierOn**](#verifieron).


## VerifierAllocateFailCount

*REG\_DWORD*

If set to a value *n*, and if **VerifierOn** is set, the framework fails every attempt to allocate memory for the driver's objects after the *nth* allocation. This failure helps you test your driver's handling of low-memory conditions. For example, if you set **VerifierAllocateFailCount** to 2, every memory allocation after the second allocation will fail. The default value for **VerifierAllocateFailCount** is 0xffffffff. After setting **VerifierAllocateFailCount**, you can turn it off by setting it to (DWORD) -1 or removing the value altogether.

Note that the verifier counts both the allocations that your driver requests and the allocations that the framework requests on behalf of your driver. Also note that the number of allocations that might occur for your driver can change from one release of the framework to the next.

## VerifierOn

*REG\_DWORD*

Set to a nonzero value to enable [KMDF Verifier](using-kmdf-verifier.md), which extensively validates a driver's state and function parameters. You should set **VerifierOn** and **DbgBreakOnError** when you are developing your driver. Use the [AddService directive](../install/inf-addservice-directive.md) and the [AddReg directive](../install/inf-addreg-directive.md) to set these values in the Services section of the INF file, for example:

```inf
[xxx_Inst.NT.Services]
AddService = xxx,%SPSVCINST_ASSOCSERVICE%,xxx_Service_Inst

[xxx_Service_Inst]
ServiceType   = %SERVICE_KERNEL_DRIVER%
StartType     = %SERVICE_BOOT_START%
ErrorControl  = %SERVICE_ERROR_NORMAL%
LoadOrderGroup = "Base"
ServiceBinary = %12%\xxx.sys
AddReg         = KMDFVerifierAddReg

[KMDFVerifierAddReg]
HKR, Parameters\Wdf,VerifierOn,0x00010001,1
HKR, Parameters\Wdf,VerboseOn,0x00010001,1
HKR, Parameters\Wdf,DbgBreakOnError,0x00010001,1
```

## VerifyDownLevel

*REG\_DWORD, framework versions 1.9 and later*

If set to a nonzero value, and if the driver was built with a version of the framework that is older than the current version, the framework's verifier includes tests that were added after the driver was built. If this value does not exist or is set to zero, the framework's verifier includes only the tests that existed when the driver was built.

For example, if your driver was built with version 1.7 of the framework, and if version 1.9 of the framework is installed on the computer, setting **VerifyDownLevel** to nonzero causes the verifier to include tests that were added to version 1.9 of the verifier when your driver runs.

## VerifyOn

*REG\_DWORD*

Set to a nonzero value to enable the [**WDFVERIFY**](./wdfverify.md) macro that is defined in Wdfassert.h, or set to zero to disable the macro. If the VerifierOn value is set, VerifyOn is implicitly set to nonzero.
