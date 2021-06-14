---
title: Driver development changes for Windows 10, version 2004
description: This section describes new features for driver development in Windows 10, version 2004.
ms.date: 05/22/2020
ms.localizationpriority: medium
---

# <a name="top"></a>What's new in Windows 10, version 2004

This section describes new features and updates for driver development in Windows 10, version 2004 (Windows 10 May 2020 Update).

### Windows Drivers

Windows 10, version 2004 is a transition release for universal drivers. In this release, universal drivers still exist, but are being replaced by Windows Drivers. A Windows Driver is a universal driver with a few additional requirements.

Windows Drivers are distinguished from Windows Desktop Drivers. While Windows Drivers run on Windows 10X and Windows 10 Desktop editions,  Windows Desktop Drivers run only on Windows 10 Desktop editions.

No changes are required to universal drivers for the version 2004 release, but documentation is available now so that you can plan ahead for upcoming changes.

For information about how to build, install, deploy, and debug a Windows Driver, see [Getting Started with Windows Drivers](./develop/getting-started-with-windows-drivers.md).

### Windows Hardware Error Architecture (WHEA)

WHEA includes a new interface (v2). For info about how to register as an error source and report errors, see [Using WHEA on Windows 10](whea/using-whea-on-windows-10.md).

### Display and Graphics Drivers

Several new and enhanced display and graphics driver features are available in Windows 10, version 2004, including D3D12 mesh shader support, sampler support, raytracing extensions, video motion estimation, and video protected resources support. See [What's New for Windows 10 Display and Graphics Drivers](./display/what-s-new-for-windows-10-display-and-graphics-drivers.md) for more details about these new features.

### Storage Drivers

A storage miniport driver can now get and set more information about a device's internal state, including the ability to reset a device. See [**IOCTL_STORAGE_GET_DEVICE_INTERNAL_LOG**](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_get_device_internal_log) and [**StorPortHardwareReset**](/windows-hardware/drivers/ddi/storport/nf-storport-storporthardwarereset) as good starting points.

### Windows Debugger

#### WinDbg Preview

Updates to [WinDbg Preview](./debugger/debugging-using-windbg-preview.md) to cover new features such as [WinDbg Preview - Timelines](./debugger/windbg-timeline-preview.md). Time travel timelines allows for the visualization of time travel code execution traces.

#### Stop Codes

- Updates to the [Bug Check Code Reference](./debugger/bug-check-code-reference2.md) topics and the addition of new parameters to topics such as [Bug Check 0x1A: MEMORY_MANAGEMENT](./debugger/bug-check-0x1a--memory-management.md) and [Bug Check 0xC4: DRIVER_VERIFIER_DETECTED_VIOLATION](./debugger/bug-check-0xc4--driver-verifier-detected-violation.md).

- New stop codes such as [Bug Check 0x1DA: HAL_BLOCKED_PROCESSOR_INTERNAL_ERROR](./debugger/bug-check-0x1da--hal-blocked-processor-internal-error.md), [Bug Check 0x1A2: WIN32K_CALLOUT_WATCHDOG_BUGCHECK](./debugger/bug-check-0x1a2--win32k-callout-watchdog-bugcheck.md) and  [Bug Check 0x119: VIDEO_SCHEDULER_INTERNAL_ERROR](./debugger/bug-check-0x119---video-scheduler-internal-error.md).

### Driver Security

Updates to the [Driver security checklist](./driversecurity/driver-security-checklist.md) to use the BinSkim tool.

## Related Topics

For information on what was new for drivers in past Windows releases, see the following pages:

* [Driver development changes for Windows 10, version 1903](driver-changes-for-windows-10-version-1903.md)
* [Driver development changes for Windows 10, version 1809](driver-changes-for-windows-10-version-1809.md)
* [Driver development changes for Windows 10, version 1803](driver-changes-for-windows-10-version-1803.md)
* [Driver development changes for Windows 10, version 1709](./what-s-new-in-driver-development.md)

[Back to Top](#top)

## Deprecated features

The following table describes Windows driver development features that have been removed in Windows 10.

| Driver technology | Feature | Deprecated in |
|---|---|---|
| GNSS/Location | [Geolocation driver sample for Windows 8.1](./gnss/sensors-geolocation-driver-sample.md) and related documentation | Windows 10, version 1709 |
| Mobile Operator Scenarios (Networking) | [AllowStandardUserPinUnlock](./mobilebroadband/allowstandarduserpinunlock.md) | Windows 10, version 1709 |
| Scan/Image | [WSD (Web Services for Devices) Challenger](./image/challenging-a-disconnected-scanner-with-the-wsd-challenger.md) functionality and related documentation | Windows 10, version 1709 |
|Mobile Operators| Mobile broadband app experience apps with Sysdev metadata packages are deprecated in favor of MO UWP APPS and COSA. | Windows 10, version 1803|