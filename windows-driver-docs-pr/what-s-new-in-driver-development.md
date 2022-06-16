---
title: What's new in driver development
description: This section describes new features for driver development in Windows 11, version 22H2.
ms.date: 05/24/2022
---

# <a name="top"></a>What's new in driver development for Windows 11, version 22H2

This section describes new features and updates for driver development in Windows 11, version 22H2.

## WPP Recorder

Drivers can add timestamps to Inflight Trace Recorder (IFR) log entries. Timestamps can specify millisecond or tenth of a microsecond granularity.

- [Inflight Trace Recorder](./devtest/using-wpp-recorder.md)
- [WPP_RECORDER_TRI_STATE](/windows-hardware/drivers/ddi/wpprecorder/ne-wpprecorder-wpp_recorder_tri_state) enumeration
- [RECORDER_LOG_CREATE_PARAMS](/windows-hardware/drivers/ddi/wpprecorder/ns-wpprecorder-_recorder_log_create_params) structure
- [WppRecorderLogCreate](/windows-hardware/drivers/ddi/wpprecorder/nf-wpprecorder-wpprecorderlogcreate) macro (wpprecorder.h)

## ACPI

The ACPI documentation has been updated with new _OSI string information for Windows 11, version 22H2.

- [How to Identify the Windows Version in ACPI by Using _OSI](./acpi/winacpi-osi.md) (Updated)

## Camera and streaming media drivers

The camera driver documentation has been updated with information on background segmentation and eye gaze modes available in Windows 11, version 22H2.

- [Background segmentation portrait mode and eye gaze stare mode driver sample](./stream/background-segmentation-portrait-mode-eye-gaze-stare-mode-driver-sample.md) (New)
- [KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION](./stream/ksproperty-cameracontrol-extended-backgroundsegmentation.md) (Updated)
- [KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION](./stream/ksproperty-cameracontrol-extended-eyegazecorrection.md) (Updated)
- [USB Video Class (UVC) camera implementation guide](./stream/uvc-camera-implementation-guide.md) (Updated)

## Print device apps

The [Print support app (PSA) design guide](./devapps/print-support-app-design-guide.md) has been updated with information about new PSA functionality available starting in Windows 11, version 22H2.

- Display name localization and PDL Passthrough API integration
- Page level feature support and operation attributes
- Enhancing the print dialog with PSA
- PDL conversion with host-based processing flags
- Set Print Device Capabilities (PDC) update policy

## Mobile broadband

Windows 11, version 22H2 introduces the following mobile broadband features:

- [MBIM Extensions Release number 4.0 (MBIMEx 4.0)](./network/mbimex-4.0-5g-sa-phase-2-support.md) introduces support for 5G SA Phase 2 features. The 5G SA Phase 2 feature set includes support for end-to-end URSP handling and multiple concurrent eMBB network slices.

- MBIMEx 4.0 introduces [access to an eSIM in the inactive SIM slot](./network/access-to-esim-in-inactive-sim-slot.md).

- An [errata for MBIMEx 3.0](./network/mbimex-3.0-5g-sa-phase-1-support.md) updates the original MBIMEx 3.0 specification.

## Audio

- To improve reliability and debuggability new [Windows 11 APIs for Audio Processing Objects](./audio/windows-11-apis-for-audio-processing-objects.md) are available.
- Windows 11 provides additional capabilities with the use of *resource groups* and these are now discussed [Audio Hardware Resource Management](./audio/audio-hardware-resource-management.md).
- Audio experience for these devices can be optimized for specific device postures, such as when a device is held in portrait mode. This is described in [Supporting Audio Posture](./audio/supporting-audio-posture.md).
- KSStudio documentation is now available on line at [KsStudio Utility](./audio/ksstudio-utility.md).

## Windows Debugging Tools

- Debugging Tools for Windows supports kernel debugging over a network cable using multiple Physical Functions (PFs) on the supported NICs. This approach improves efficiency of debugging, particularly in traffic heavy cloud environments. For more information see, [Setting Up 2PF Kernel-Mode Debugging using KDNET](./debugger/setting-up-kernel-mode-debugging-using-2pf.md).
- A new low level OS independent debugger transport – EXDI is described in [Configuring the EXDI Debugger Transport](./debugger/configuring-the-exdi-debugger-transport.md). This transport can connect to virtualized environments such as QEMU, this is described in [Setting Up QEMU Kernel-Mode Debugging using EXDI]( /windows-hardware/drivers/debugger/setting-up-qemu-kernel-mode-debugging-using-exdi).
- AppVerifier test content is now updated and the documentation is now available online – [Application Verifier - Overview]( /windows-hardware/drivers/devtest/application-verifier).

## Driver Security

- New  code scanning CodeQL rules and updated installation directions, are now available. For more information, see [CodeQL and the Static Tools Logo Test](./devtest/static-tools-and-codeql.md).

## Provisioning support for loading pre-production drivers

- [How to test pre-production drivers with Secure Boot enabled](./install/preproduction-driver-signing-and-install.md)

## Related Topics

For information on what was new for drivers in past Windows releases, see the following pages:

- [Driver development changes for Windows 11, version 21H2](driver-changes-for-windows-11.md)
- [Driver development changes for Windows Server 2022](driver-changes-for-windows-server-2022.md)
- [Driver development changes for Windows 10, version 2004](driver-changes-for-windows-10-version-2004.md)
- [Driver development changes for Windows 10, version 1903](driver-changes-for-windows-10-version-1903.md)

[Back to Top](#top)
