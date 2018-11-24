---
title: Using KMDF Verifier
description: Using KMDF Verifier
ms.assetid: ab6a0149-9341-435b-b7e7-9c5d6520ebd8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using KMDF Verifier


The framework provides built-in verification functionality that you can use to test a running KMDF driver. This functionality, called KMDF Verifier, extensively validates your driver's state and the arguments that the driver passes to framework object methods. You can use the framework's verifier by itself or together with the general-purpose [Driver Verifier (Verifier.exe)](https://msdn.microsoft.com/library/windows/hardware/ff545448) tool.

If KMDF Verifier is enabled, the framework checks lock acquisition and hierarchies, ensures that calls to the framework occur at the correct IRQL, verifies correct I/O cancellation and queue usage, and ensures that the driver and framework follow the documented contracts. It can also simulate out-of-memory conditions so that the driver developer can test whether the driver responds properly without crashing, hanging, or failing to unload.

When KMDF Verifier is enabled, the framework breaks into the debugger if a default time-out period of 60 seconds expires before some of the events described previously have completed. At this point, you can debug the issue, or type "g" in the debugger to restart the time-out period. You can change the default time-out period by using the **DbgWaitForSignalTimeoutInSec** registry value described in [Controlling the Verifier's Behavior](#verifier-reg-values).

We recommend running Driver Verifier (Verifier.exe) during testing, and adding your own driver and wdf01000.sys to the verify list.

If your driver was built with KMDF version 1.9 or later and you run Verifier.exe, KMDF Verifier is automatically enabled.

You can also use the [WDF Verifier Control Application (WdfVerifier.exe)](https://msdn.microsoft.com/library/windows/hardware/ff556129) to enable and disable KMDF Verifier.

## Enabling and Disabling the Framework's Built-in Verification


You can manually enable KMDF Verifier using this procedure:

1.  If your driver is already loaded, use Device Manager to disable the device. Disabling the device causes the driver to be unloaded.
2.  Use RegEdit to set **VerifierOn** to a nonzero value in the driver's **Parameters\\Wdf** subkey of the **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services** key in the Windows registry. A nonzero value indicates that KMDF Verifier is enabled.

    You may need to add **VerifierOn** manually to the subkey if it is not already present.

3.  Use Device Manager to reenable the device, thereby loading the driver.
4.  When the driver calls [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175), the framework examines the registry and enables the framework's verifier if **VerifierOn** to a nonzero value.

To disable the framework's verifier, follow the same steps, but set the value of **VerifierOn** to zero.

To determine whether the framework's verifier is enabled, set a breakpoint at a location after your driver calls [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175) and use the [**!wdfdriverinfo**](https://msdn.microsoft.com/library/windows/hardware/ff565724) debugger extension command:

**!wdfkd.wdfdriverinfo** *&lt;your drivername&gt;* **** **0x1**

For more information about the debugger extension commands, see [Debugger Extensions for Framework-based Drivers](debugger-extensions-for-kmdf-drivers.md).

## Controlling the Verifier's Behavior


We recommend that you use the [WDF Verifier control application](https://msdn.microsoft.com/library/windows/hardware/ff556129) to control the options below. However, you can directly modify the following values in the registry.

The relevant values are located under the **Parameters\\Wdf** subkey of the **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services** key.

<a href="" id="verifyon-----------------reg-dword-"></a>**VerifyOn** (**REG\_DWORD**)  
Set this value to a nonzero value to enable the [**WDFVERIFY**](https://msdn.microsoft.com/library/windows/hardware/ff551167) macro.

<a href="" id="dbgbreakonerror-----------------------------reg-dword-"></a>**DbgBreakOnError** (**REG\_DWORD**)  
If this value is set to a nonzero value, the framework will break into the debugger (if available) each time that a driver calls [**WdfVerifierDbgBreakPoint**](https://msdn.microsoft.com/library/windows/hardware/ff551164).

<a href="" id="dbgwaitforsignaltimeoutinsec---------------reg-dword-"></a>**DbgWaitForSignalTimeoutInSec** (**REG\_DWORD**)  
Starting in Windows 8, when **VerifierOn** and **DbgBreakOnError** are set to nonzero values, the driver can change the default time-out period by setting **DbgWaitForSignalTimeoutInSec**.

<a href="" id="verifierallocatefailcount------------------------------reg-dword-"></a>**VerifierAllocateFailCount** (**REG\_DWORD**)  
If this value is set to a value *n*, the framework fails every attempt to allocate memory for the driver's objects after the *nth* allocation.

<a href="" id="trackhandles---------------reg-multi-sz-"></a>**TrackHandles** (**REG\_MULTI\_SZ**)  
If this value is set to a list of one or more type names of framework object handles, the framework tracks references to all object handles that match the specified handle types.

<a href="" id="enhancedverifieroptions-----------------------------reg-dword-"></a>**EnhancedVerifierOptions** (**REG\_DWORD**)  
**KMDF only**

Contains a bitmap that you can use to enable optional features of the framework's verifier.

<a href="" id="verifydownlevel--------------reg-dword-"></a>**VerifyDownLevel** (**REG\_DWORD**)  
If set to a nonzero value, and if the driver was built with a version of the framework that is older than the current version, the framework's verifier includes tests that were added after the driver was built.

As a general rule, if you set the above registry values, delete them when they are no longer needed.

For full descriptions of these registry values, see [Registry Values for Debugging Framework-based Drivers](registry-values-for-debugging-kmdf-drivers.md).

 

 





