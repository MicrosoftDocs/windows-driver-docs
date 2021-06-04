---
title: Introduction to the Directed Power Management Framework
description: Describes the Directed Power Management Framework, or DFx, which is part of the Power Framework, or PoFx, version 3.
ms.date: 04/02/2021
ms.custom: 19H1
---

# Introduction to the Directed Power Management Framework

Starting in Windows 10, version 1903, version 3 of the run-time power management framework ([PoFx](./overview-of-the-power-management-framework.md)) provides an optional directed power model, Directed PoFx (DFx).

With DFx, the operating system directs device stacks to enter their appropriate low-power idle states when the system transitions to idle and there is no [activator](/windows-hardware/design/device-experiences/activators)-brokered software activity, and thereby enables the system to enter low power more reliably.

The objective is to make systems more power-efficient and to reduce energy consumption for Windows devices across form factors.

DFx is currently supported for devices with D-state constraints only.  DFx skips any device subtree with an F-state constraint.

DFx does not power down paging or debug devices.

## Requirements for WDF (non-miniport) drivers

A WDF driver that specifies **SystemManagedIdleTimeout** or **SystemManagedIdleTimeoutWithHint** in the [WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings) structure can opt into DFx by adding the following registry key to the INF's [AddReg directive section](../install/inf-addreg-directive.md) within the [DDInstall.HW section](../install/inf-ddinstall-hw-section.md):

`HKR,"WDF","WdfDirectedPowerTransitionEnable",0x00010001,1`

A WDF driver targeting version 31 and above will enable DFx by default. If this is undesired, the driver can opt out of DFx by setting the registry key to 0: 

`HKR,"WDF","WdfDirectedPowerTransitionEnable",0x00010001,0`

Because requesting system-managed idle timeout causes WDF to register with PoFx on the driver's behalf, the driver does not need to register with PoFx in this scenario.

If the driver specifies **DriverManagedIdleTimeout**, consider switching to system-managed idle timeout.  If that is not feasible, use the guidelines in the WDM section below to opt into DFx.

If the WDF driver does not use runtime power management, add support for it and use system-managed idle timeout.  To do so, provide an [WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings) structure as input to [**WdfDeviceAssignS0IdleSettings**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings).

## Requirements for WDM (non-miniport) drivers

If your driver does not use the system-managed idle support provided by WDF (the driver is either a WDF driver using [driver-managed idle](/windows-hardware/drivers/ddi/wdfdevice/ne-wdfdevice-_wdf_power_policy_idle_timeout_type), or a WDM driver), it can still get DFx support by registering itself with PoFx.  In this scenario, the driver registers with PoFx by implementing:

- [PO_FX_DIRECTED_POWER_DOWN_CALLBACK callback function](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_directed_power_down_callback)
- [PO_FX_DIRECTED_POWER_UP_CALLBACK callback function](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_directed_power_up_callback)


Provide pointers to these callbacks in a [PO_FX_DEVICE_V3](/windows-hardware/drivers/ddi/wdm/ns-wdm-po_fx_device_v3) structure that is input to the [**PoFxRegisterDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxregisterdevice) function.

To get DFx support, a driver must:

* Provide the `PO_FX_DIRECTED_POWER*` callbacks when registering for PoFx
* Call [**PoFxReportDevicePoweredOn**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxreportdevicepoweredon) from its [PO_FX_DIRECTED_POWER_UP_CALLBACK](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_directed_power_up_callback) callback function on resume from Sx transitions

## Example

The following example shows the self-registration option described above:

```
PO_FX_DEVICE_V3 MyPoFxDevice;
POHANDLE MyPoFxHandle;

RtlZeroMemory(&MyPoFxDevice, sizeof(PO_FX_DEVICE_V3));
MyPoFxDevice.Version = PO_FX_VERSION_V3;

// Initialize other PoFx callbacks and other fields like
// components and their idle states.

MyPoFxDevice.DirectedPowerUpCallback = <Driver's DFx power up callback>
MyPoFxDevice.DirectedPowerDownCallback = <Driver's DFx power down callback>

Status = PoFxRegisterDevice(
  <Driver's device object>,
  (PPO_FX_DEVICE)&MyPoFxDevice,
  &MyPoFxHandle);
  if (!NT_SUCCESS(Status)) {
  return Status;
}
```

If your driver specified `PO_FX_VERSION_V1` previously, note that `PO_FX_DEVICE_V3` structures uses `PO_FX_COMPONENT_V2` for the component array structure.

## Requirements for miniport drivers

For device classes that follow a port/miniport driver model, system-supplied port drivers typically handle power policy ownership.  Most miniports are not expected to require any code changes to opt into DFx, as the corresponding port driver is expected to handle DFx support.

## Testing

Microsoft provides three tests for DFx: a single-device test in the [Windows Driver Kit](../download-the-wdk.md) intended for testing user-specified devices, a device-level HLK test, and a system-level HLK test intended for testing all devices on a system.

The single-device test is available as part of the [PwrTest](../devtest/pwrtest.md) tool that ships with the WDK.  To access it, run the tool with the `/directedfx` switch.  For more information, see [PwrTest DirectedFx Scenario](../devtest/pwrtest-directedfx-scenario.md).

For information about HLK tests, please see the following pages:

- [Directed FX Single Device Test](/windows-hardware/test/hlk/testref/34cfdfa6-7826-443c-9717-bc28c3166092)
- [Directed FX System Verification Test](/windows-hardware/test/hlk/testref/def16163-9118-4d4a-b559-37873befa12e)

Testing DFx after an S4 transition is recommended in order to catch any cases where a driver may not be correctly calling [PoFxReportDevicePoweredOn](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxreportdevicepoweredon) after resume from S4.

## DFx and S-state transitions

- The target D-state for DFx transitions should match that for Runtime D3 (RTD3), which may be different than the target D-state for S3/S4 transitions.  Consider a scenario in which a device enters D2 for RTD3, but enters D3 for S3/S4.  In this case, the target D-state for DFx should be D2.
- Similarly, the arm-for-wake behavior for DFx should match that for RTD3, which may differ from that used in S3/S4 transitions.  For example, a device may enter D2/wake-armed for RTD3, but enter D3/no-wake-armed for S3/S4.  In this scenario, DFx transitions should also enter D2/wake-armed.

## DFx and Runtime D3 (RTD3)

- With RTD3, a device typically enters a lower power D-state when it goes idle.  If new work arrives, the device immediately wakes to D0.  With DFx, the device should continue to remain in its target D-state (and pend new work on its queues) until PoFx directs it to power back up.


## See Also

- [Directed power management](/windows-hardware/design/device-experiences/directed-power-management)
- [Prepare hardware for modern standby](/windows-hardware/design/device-experiences/prepare-hardware-for-modern-standby)
- [PwrTest](../devtest/pwrtest.md)
- [PO_FX_DEVICE_V3 structure](/windows-hardware/drivers/ddi/wdm/ns-wdm-po_fx_device_v3)
- [PO_FX_DIRECTED_POWER_DOWN_CALLBACK callback function](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_directed_power_down_callback)
- [PO_FX_DIRECTED_POWER_UP_CALLBACK callback function](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_directed_power_up_callback)
- [PoFxCompleteDirectedPowerDown function](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxcompletedirectedpowerdown) 
- [PwrTest DirectedFx Scenario](../devtest/pwrtest-directedfx-scenario.md)
- [Directed FX Single Device Test](/windows-hardware/test/hlk/testref/34cfdfa6-7826-443c-9717-bc28c3166092)
- [Directed FX System Verification Test](/windows-hardware/test/hlk/testref/def16163-9118-4d4a-b559-37873befa12e)
