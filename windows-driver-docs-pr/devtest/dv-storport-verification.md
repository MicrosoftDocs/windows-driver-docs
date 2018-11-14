---
title: Storport Verification
description: Storport Verification
ms.assetid: 3731C877-1A69-447C-A5DB-0BDD1B753D3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storport Verification


## <span id="ddk_storport_verification_tools"></span><span id="DDK_STORPORT_VERIFICATION_TOOLS"></span>


The Storport Verification feature monitors the interaction between a Storport miniport driver and the port driver. If the miniport driver misuses a routine, responds incorrectly to a request from the port driver, or takes an excessive amount of time to respond to a request, a bug check is issued.

**Note**  The Storport Verification feature is only available in Windows Vista and later versions of Windows.

 

### <span id="violations_detected_by_storport_verification"></span><span id="VIOLATIONS_DETECTED_BY_STORPORT_VERIFICATION"></span>Violations Detected by Storport Verification

The Storport Verification feature can detect several misuses of Storport routines. It is also possible to individually disable some of these checks.

The Storport Verification feature issues bug check 0xF1 or bug check 0xC4 if a Storport miniport driver commits one of the following violations:

-   The miniport driver passes a bad argument (a NULL pointer) to the [**StorPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff567108) routine.

-   The miniport driver calls [**StorPortStallExecution**](https://msdn.microsoft.com/library/windows/hardware/ff567508) and specifies a delay longer than 0.1 second, stalling the processor for an excessive length of time.

-   [**StorPortFreeDeviceBase**](https://msdn.microsoft.com/library/windows/hardware/ff567061) can be called only from the miniport driver's **HwStorFindAdapter** routine.

-   [**StorPortGetUncachedExtension**](https://msdn.microsoft.com/library/windows/hardware/ff567103) can be called only from the miniport driver's **HwStorFindAdapter** routine and can be called only for a bus-master adapter. A miniport must set the **SrbExtensionSize** of the [**HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff557459) (Storport) structure before calling **StorPortGetUncachedExtension**.

-   The [**StorPortGetDeviceBase**](https://msdn.microsoft.com/library/windows/hardware/ff567080) routine supports only those addresses that were assigned to the driver by the system Plug and Play (PnP) manager.

-   The miniport driver passes an invalid virtual address to one of the **StorPortRead***xxx* or **StorPortWrite***xxx* routines (for example, [**StorPortReadRegisterUchar**](https://msdn.microsoft.com/library/windows/hardware/ff567483) or [**StorPortWritePortBufferUlong**](https://msdn.microsoft.com/library/windows/hardware/ff567517)). This usually means that the address supplied doesn't map to the common buffer area. The specified *Register* or *Port* must be in mapped memory-space range returned by [**StorPortGetDeviceBase**](https://msdn.microsoft.com/library/windows/hardware/ff567080) routine. This check is supported only on x86-based systems.

For a list of the bug check parameters that Storport Verification uses, see [**Bug Check 0xF1**](https://msdn.microsoft.com/library/windows/hardware/ff560365) (SCSI\_VERIFIER\_DETECTED\_VIOLATION). In addition to Bug Check 0xF1, Storport Verification also makes use of [**Bug Check 0xC4**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (DRIVER\_VERIFIER\_DETECTED\_VIOLATION).

**Note**  [**Bug Check 0xF1**](https://msdn.microsoft.com/library/windows/hardware/ff560365) is used for both SCSI Verification and Storport Verification.

 

### <span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating This Option

The procedure for activating the Storport Verification option is different from the procedures for activating other Driver Verifier options.

**To activate Storport Verification**

1.  Using Driver Verifier Manager or the *Verifier.exe* command line, start a verification of the miniport driver. Because Storport Verification will not be available as an option, you must select at least one *other* Driver Verifier option. For more information, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md) and [Selecting Drivers to be Verified](selecting-drivers-to-be-verified.md).

2.  Open the registry using *regedit.exe*. In the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\StorPort** key, add a subkey named **Verifier**. If the **StorPort** key does not exist, you need to create it. Within the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\STORPort\\Verifier** key, add a **REG\_DWORD** entry named **VerifyLevel**. The value assigned to this entry will determine which Storport Verification tests will be active. The value 0x1 will give maximum verification.

3.  Restart the computer.

If the **VerifyLevel** value does not exist, or is equal to 0xFFFFFFFF, Storport Verification will be disabled.

### <span id="activating_without_rebooting"></span><span id="ACTIVATING_WITHOUT_REBOOTING"></span>Activating without Rebooting

In general, you cannot activate or deactivate Storport Verification without restarting (rebooting) the computer on any Windows operating system. The *StorPort.sys* driver reads the **VerifyLevel** registry entry only when it loads, which is typically at boot time. However, if the *StorPort.sys* driver is not loaded when you add the registry entry, or if it is unloaded and reloaded, you can enable Storport Verification on Windows Vista and later versions of Windows without restarting the computer.

 

 





