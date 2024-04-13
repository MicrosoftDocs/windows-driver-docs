---
title: Storport Verification
description: Storport Verification
ms.date: 04/20/2017
---

# Storport Verification

The Storport Verification feature monitors the interaction between a Storport miniport driver and the port driver. If the miniport driver misuses a routine, responds incorrectly to a request from the port driver, or takes an excessive amount of time to respond to a request, a bug check is issued.

>[!NOTE]
>The Storport Verification feature is only available in Windows Vista and later versions of Windows.

## Violations Detected by Storport Verification

The Storport Verification feature can detect several misuses of Storport routines. It is also possible to individually disable some of these checks.

The Storport Verification feature issues bug check 0xF1 or bug check 0xC4 if a Storport miniport driver commits one of the following violations:

- The miniport driver passes a bad argument (a NULL pointer) to the [**StorPortInitialize**](/windows-hardware/drivers/ddi/storport/nf-storport-storportinitialize) routine.

- The miniport driver calls [**StorPortStallExecution**](/windows-hardware/drivers/ddi/storport/nf-storport-storportstallexecution) and specifies a delay longer than 0.1 second, stalling the processor for an excessive length of time.

- [**StorPortFreeDeviceBase**](/windows-hardware/drivers/ddi/storport/nf-storport-storportfreedevicebase) can be called only from the miniport driver's **HwStorFindAdapter** routine.

- [**StorPortGetUncachedExtension**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetuncachedextension) can be called only from the miniport driver's **HwStorFindAdapter** routine and can be called only for a bus-master adapter. A miniport must set the **SrbExtensionSize** of the [**HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/storport/ns-storport-_hw_initialization_data-r1) (Storport) structure before calling **StorPortGetUncachedExtension**.

- The [**StorPortGetDeviceBase**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetdevicebase) routine supports only those addresses that were assigned to the driver by the system Plug and Play (PnP) manager.

- The miniport driver passes an invalid virtual address to one of the **StorPortRead***xxx* or **StorPortWrite***xxx* routines (for example, [**StorPortReadRegisterUchar**](/windows-hardware/drivers/ddi/storport/nf-storport-storportreadregisteruchar) or [**StorPortWritePortBufferUlong**](/windows-hardware/drivers/ddi/storport/nf-storport-storportwriteportbufferulong)). This usually means that the address supplied doesn't map to the common buffer area. The specified *Register* or *Port* must be in mapped memory-space range returned by [**StorPortGetDeviceBase**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetdevicebase) routine. This check is supported only on x86-based systems.

For a list of the bug check parameters that Storport Verification uses, see [**Bug Check 0xF1**](../debugger/bug-check-0xf1--scsi-verifier-detected-violation.md) (SCSI\_VERIFIER\_DETECTED\_VIOLATION). In addition to Bug Check 0xF1, Storport Verification also makes use of [**Bug Check 0xC4**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (DRIVER\_VERIFIER\_DETECTED\_VIOLATION).

>[!NOTE]
>[**Bug Check 0xF1**](../debugger/bug-check-0xf1--scsi-verifier-detected-violation.md) is used for both SCSI Verification and Storport Verification.

### Activating the Storport Verification Option

The procedure for activating the Storport Verification option is different from the procedures for activating other Driver Verifier options.

1. Using Driver Verifier Manager or the *Verifier.exe* command line, start a verification of the miniport driver. Because Storport Verification will not be available as an option, you must select at least one *other* Driver Verifier option. For more information, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md) and [Selecting Drivers to be Verified](selecting-drivers-to-be-verified.md).

2. Open the registry using *regedit.exe*. In the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\StorPort** key, add a subkey named **Verifier**. If the **StorPort** key does not exist, you need to create it. Within the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\STORPort\\Verifier** key, add a **REG\_DWORD** entry named **VerifyLevel**. The value assigned to this entry will determine which Storport Verification tests will be active. The value 0x1 will give maximum verification.

3. Restart the computer.

If the **VerifyLevel** value does not exist, or is equal to 0xFFFFFFFF, Storport Verification will be disabled.

### Activating without Rebooting

In general, you cannot activate or deactivate Storport Verification without restarting (rebooting) the computer on any Windows operating system. The *StorPort.sys* driver reads the **VerifyLevel** registry entry only when it loads, which is typically at boot time. However, if the *StorPort.sys* driver is not loaded when you add the registry entry, or if it is unloaded and reloaded, you can enable Storport Verification on Windows Vista and later versions of Windows without restarting the computer.
