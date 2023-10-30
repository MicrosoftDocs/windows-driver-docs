---
title: What's new in driver development
description: This section describes new features for driver development in Windows 11, version 23H2.
ms.date: 10/24/2023
---

# <a name="top"></a>What's new in driver development for Windows 11, version 23H2

This section describes new features and updates for driver development in Windows 11, version 23H2. To target this version of Windows, you can use [WDK 10.0.22621.2428](./download-the-wdk.md) (released October 24, 2023).

## Audio

To allow audio drivers to be more reliable and offer the best possible experience for PC users, the Audio Class eXtension (ACX) is now available. For more information, see [ACX audio class extensions overview](./audio/acx-audio-class-extensions-overview.md)

[Windows 11 APIs for Audio Processing Objects](./audio/windows-11-apis-for-audio-processing-objects.md) provides information on new features designed to improve the quality and reliability of Windows Audio Processing Objects (APOs).

## Bluetooth Low Energy (LE) Audio

Bluetooth LE Audio enables streaming unicast or broadcast audio to Bluetooth LE devices over an isochronous transport. As of version 5.3 of the Bluetooth core specification, there's no standard defined host controller interface (HCI) for host platforms to send and receive isochronous data to and from the Bluetooth controller. The Windows Bluetooth vendor specific audio path (VSAP) allows platforms to use vendor-specific solutions to enable Bluetooth LE Audio streaming. The VSAP software interface uses Windows audio class extensions (ACX) and more interface properties defined in this document. For more information, see [Bluetooth Low Energy (LE) Audio](./bluetooth/bluetooth-low-energy-audio.md).

## Camera and streaming media

The camera driver documentation has been updated with information about the camera profile v2 developer specification.

[Camera Profile V2 developer specification](./stream/camera-profile-v2-specification.md)

## Display and graphics drivers

* Windows 11, version 23H2 includes version 1.10 of the Indirect Display Driver (IDD) model. This latest IddCx version adds HDR10 (high dynamic range) and SDR (standard dynamic range) Wide Color Gamut (WCG) support for indirect displays.

  [Updates for IddCx versions 1.10 and later](./display/iddcx1.10-updates.md)

* WDDM 3.0 and later drivers can support DisplayPort monitors connected over USB4.

  [WDDM support for DisplayPort monitors over USB4](./display/supporting-usb4.md)

* WDDM 3.0 and later drivers can support the Hardware flip queue feature.

  [Hardware flip queue](./display/hardware-flip-queue.md)

## Dynamic lighting

Dynamic Lighting provides Windows users and developers with native control of lighting devices implementing the open HID LampArray standard. By adopting an open standard, and by working with our OEM and ODM partners, Microsoft seeks to improve the RGB device and software ecosystem for users by increasing interoperability of devices and apps. Device manufacturers can use standardized firmware for the first time, enabling new native experiences across the Windows OS and apps without the high costs of proprietary firmware and software development.

Examples of experiences include synchronizing devices from different brands together in Windows Settings, applying effects intelligently across available devices, and leveraging app integrations to drive device lighting. For the first time, device manufacturers are empowered to focus purely on innovation and differentiation because their devices will be able to take advantage of a myriad of OS and app experiences. For more information, see [Dynamic Lighting devices](/windows-hardware/design/component-guidelines/dynamic-lighting-devices)

## File system and filter drivers

* Flags were added to support [Dev Drive](/windows/dev-drive/). A minifilter driver receives these flags via its [**PFLT_INSTANCE_SETUP_CALLBACK**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_instance_setup_callback) routine.

* [Minifilter guidance for file system placeholders](./ifs/placeholders_guidance.md) was added.

## Human presence sensors

With the release of Windows 11, Microsoft now natively supports the presence sensing feature set in Windows. For Windows 11 PCs that have a presence sensor built in, users can have their screen turn off automatically when they leave (see [Lock on leave](/windows-hardware/design/device-experiences/sensors-presence-lock-on-leave)), and then have their device wake up quickly when they approach (see [Wake on approach](/windows-hardware/design/device-experiences/sensors-presence-wake-on-approach)). This can help keep their PC more secure, help save battery power, and help users get back to work more quickly. For more information, see [Presence Sensing](/windows-hardware/design/device-experiences/sensors-presence-sensing).

## Print devices

The print driver documentation has been updated with information on the end of servicing plan for third-party printer drivers on Windows.

[End of servicing plan for third-party printer drivers on Windows](./print/end-of-servicing-plan-for-third-party-printer-drivers-on-windows.md)

## Storage drivers

* StorNVMe [command set support](./storage/stornvme-command-set-support.md) and [feature support](./storage/stornvme-feature-support.md) has been updated.

* StorPort miniport drivers can now [acquire and release](/windows-hardware/drivers/ddi/storport/nf-storport-storportacquirespinlockex) spin locks.

## USB

Starting in Windows 11 build 22621.1778 (KB5026446), the Windows Settings app now lists attached USB4 hubs and devices and their capabilities. For USB4-capable systems, navigate in the Settings app to **Bluetooth & devices** > **USB** > **USB4 Hubs and Devices**. For more information, see [Universal Serial Bus 4 (USB4™) settings enablement](/windows-hardware/design/component-guidelines/usb4-settings-enablement).

Starting in Windows 11, version 22H2 September Update, the Windows UCM-UCSI ACPI device drivers support UCSI specification version 2.0 and 2.1. The UCSI specification 2.0 has breaking changes in the memory mapping of its data structures as defined in [UCSI specification Table 3-1 Data Structures](https://www.intel.com/content/www/us/en/products/docs/io/universal-serial-bus/usb-type-c-ucsi-spec.html). To maintain backward compatibility, Windows requires the UCSI PPM of specification version 2.0 or greater to implement a _DSM function under the UCM-UCSI ACPI device in ACPI firmware and return a nonzero value to indicate that UCSI OPM should follow the reported UCSI specification version. For more information, see [UCM-UCSI ACPI device for UCSI 2.0 and greater](usbcon/ucsi.md#ucm-ucsi-acpi-device-for-ucsi-20-and-greater).

## Getting started

[From Sample Code to Production Driver - What to Change in the Samples](./gettingstarted/from-sample-code-to-production-driver.md) describes changes that need to be made to the WDK sample drivers before releasing device drivers based on the sample code.

## Driver security  

A new topic provides important driver security guidance – [Windows drivers security best practices for driver developers](./driversecurity/driver-security-dev-best-practices.md). Updates to the Semmle CodeQL rules and new information on the Microsoft Vulnerable and Malicious Driver Reporting Center as well as an updated [Driver security checklist](./driversecurity/driver-security-checklist.md).

## Windows debugging tools

Formerly released as WinDbg Preview in the Microsoft Store, WinDbg leverages the same underlying engine as WinDbg (Classic) and supports all the same commands, extensions, and workflows. For more information, see [What is WinDbg?](./debuggercmds/windbg-overview.md)

Expanded bug check information including new bug checks described in [Bug Check Code Reference](./debugger/bug-check-code-reference2.md) such as [Bug Check 0x1DE: BUGCODE_WIFIADAPTER_DRIVER](./debugger/bug-check-0x1de--bugcode-wifiadapter-driver.md).

Use the new [Time Travel Debugging - TTD.exe command line utility](./debuggercmds/time-travel-debugging-ttd-exe-command-line-util.md) to capture time travel code execution traces.

The new TaskManager live dump feature built into Windows, is described in [Task Manager live memory dump](./debugger/task-manager-live-dump.md)

New [Source Code Extended Access](./debugger/source-code-extended-access.md) DebugInfoD topic that is now available in the debugger. This supports file retrieval from DebugInfoD servers through the `DebugInfoD*` tag.

[Debugger 2PF KDNET Support](./network/debugger-2pf-kdnet-support.md) describes how to enable your miniport NDIS driver for 2PF debugger support to allow increased performance for high speed adapters, often used in data centers.

Three new EXDI debugging topics including [Setting Up QEMU Kernel-Mode Debugging using EXDI](./debugger/setting-up-qemu-kernel-mode-debugging-using-exdi.md).

Published [Supported Ethernet NICs for Network Kernel Debugging in Windows 11](./debugger/supported-ethernet-nics-for-network-kernel-debugging-in-windows-11.md) with updated information on NICs.

The AppVerifier docs formerly only available in a local “CHM” file are now available online. [Application Verifier](./devtest/application-verifier.md) (AppVerifier) is a runtime verification tool for unmanaged code that assists in finding subtle programming errors, security issues and limited user account privilege problems that can be difficult to identify with normal application testing techniques.

## Related Topics

For information on what was new for drivers in past Windows releases, see the following pages:

- [Driver development changes for Windows 11, version 22H2](driver-changes-for-windows-11-version-22h2.md)
- [Driver development changes for Windows 11, version 21H2](driver-changes-for-windows-11-version-21h2.md)
- [Driver development changes for Windows Server 2022](driver-changes-for-windows-server-2022.md)
- [Driver development changes for Windows 10, version 2004](driver-changes-for-windows-10-version-2004.md)

[Back to Top](#top)
