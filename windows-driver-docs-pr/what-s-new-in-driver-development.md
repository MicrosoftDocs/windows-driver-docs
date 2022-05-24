---
title: What's new in driver development
description: This section describes new features for driver development in Windows 11, version 22H2.
ms.date: 05/24/2022
---

# <a name="top"></a>What's new in driver development for Windows 11, version 22H2

This section describes new features and updates for driver development in Windows 11, version 22H2.

## WPP Recorder

Drivers can add timestamps to Inflight Trace Recorder (IFR) log entries. Timestamps can specify millisecond or tenth of a microsecond granularity.

- [Inflight Trace Recorder](/windows-hardware/drivers/devtest/using-wpp-recorder)
- [WPP_RECORDER_TRI_STATE](/windows-hardware/drivers/ddi/wpprecorder/ne-wpprecorder-wpp_recorder_tri_state) enumeration
- [RECORDER_LOG_CREATE_PARAMS](/windows-hardware/drivers/ddi/wpprecorder/ns-wpprecorder-_recorder_log_create_params) structure
- [WppRecorderLogCreate](/windows-hardware/drivers/ddi/wpprecorder/nf-wpprecorder-wpprecorderlogcreate) macro (wpprecorder.h)

## ACPI

The ACPI documentation has been updated with new _OSI string information for Windows 11, version 22H2.

- [How to Identify the Windows Version in ACPI by Using _OSI](/windows-hardware/drivers/acpi/winacpi-osi) (Updated)

## Camera and streaming media drivers

The camera driver documentation has been updated with information on background segmentation and eye gaze modes available in Windows 11, version 22H2.

- [Background segmentation portrait mode and eye gaze stare mode driver sample](/windows-hardware/drivers/stream/background-segmentation-portrait-mode-eye-gaze-stare-mode-driver-sample) (New)
- [KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION](/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-backgroundsegmentation) (Updated)
- [KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION](/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-eyegazecorrection) (Updated)
- [USB Video Class (UVC) camera implementation guide](/windows-hardware/drivers/stream/uvc-camera-implementation-guide) (Updated)

## Print device apps

The [Print support app (PSA) design guide](/windows-hardware/drivers/devapps/print-support-app-design-guide) has been updated with information about new PSA functionality available starting in Windows 11, version 22H2.

- [Display name localization and PDL Passthrough API integration](/windows-hardware/drivers/devapps/print-support-app-design-guide?branch=release-nickel#display-name-localization-and-pdl-passthrough-api-integration)
- [Page level feature support and operation attributes](/windows-hardware/drivers/devapps/print-support-app-design-guide?branch=release-nickel#page-level-feature-support-and-operation-attributes)
- [Enhancing the print dialog with PSA](/windows-hardware/drivers/devapps/print-support-app-design-guide?branch=release-nickel#enhancing-the-print-dialog-with-psa)
- [PDL conversion with host-based processing flags](/windows-hardware/drivers/devapps/print-support-app-design-guide?branch=release-nickel#pdl-conversion-with-host-based-processing-flags)
- [Set Print Device Capabilities (PDC) update policy](/windows-hardware/drivers/devapps/print-support-app-design-guide?branch=release-nickel#set-print-device-capabilities-pdc-update-policy)


## Mobile broadband

Windows 11, version 22H2 introduces the following mobile broadband features:

- [MBIM Extensions Release number 4.0 (MBIMEx 4.0)](/windows-hardware/drivers/network/mbimex-4.0-5g-sa-phase-2-support) introduces support for 5G SA Phase 2 features. The 5G SA Phase 2 feature set includes support for end-to-end URSP handling and multiple concurrent eMBB network slices.

- MBIMEx 4.0 introduces [access to an eSIM in the inactive SIM slot](/windows-hardware/drivers/network/access-to-esim-in-inactive-sim-slot).

- An [errata for MBIMEx 3.0](/windows-hardware/drivers/network/mbimex-3.0-5g-sa-phase-1-support) updates the original MBIMEx 3.0 specification.

## Audio

- To improve reliability and debuggability new [Windows 11 APIs for Audio Processing Objects](/windows-hardware/drivers/audio/windows-11-apis-for-audio-processing-objects) are available.
- Windows 11 provides additional capabilities with the use of *resource groups* and these are now discussed [Audio Hardware Resource Management](/windows-hardware/drivers/audio/audio-hardware-resource-management).
- Audio experience for these devices can be optimized for specific device postures, such as when a device is held in portrait mode. This is described in [Supporting Audio Posture](/windows-hardware/drivers/audio/supporting-audio-posture).
- KSStudio documentation is now available on line at [KsStudio Utility](/windows-hardware/drivers/audio/ksstudio-utility).

## Windows Debugging Tools

- Debugging Tools for Windows supports kernel debugging over a network cable using multiple Physical Functions (PFs) on the supported NICs. This approach improves efficiency of debugging, particularly in traffic heavy cloud environments. For more information see, [Setting Up 2PF Kernel-Mode Debugging using KDNET](/windows-hardware/drivers/debugger/setting-up-kernel-mode-debugging-using-2pf).
- A new low level OS independent debugger transport – EXDI is described in [Configuring the EXDI Debugger Transport](/windows-hardware/drivers/debugger/configuring-the-exdi-debugger-transport). This transport can connect to virtualized environments such as QEMU, this is described in [Setting Up QEMU Kernel-Mode Debugging using EXDI]( /windows-hardware/drivers/debugger/setting-up-qemu-kernel-mode-debugging-using-exdi).
- AppVerifier test content is now updated and the documentation is now available online – [Application Verifier - Overview]( /windows-hardware/drivers/devtest/application-verifier).

## Driver Security

- New  code scanning CodeQL rules and updated installation directions, are now available. For more information, see [CodeQL and the Static Tools Logo Test]( /windows-hardware/drivers/devtest/static-tools-and-codeq).

## Provisioning support for loading pre-production drivers

- [How to test pre-production drivers with Secure Boot enabled](./install/preproduction-driver-signing-and-install.md)

## TechName2

- link
- link

New API pages:

- link
- link
- 
## TechName3

- link
- link

New API pages:

- link
- link

## Related Topics

For information on what was new for drivers in past Windows releases, see the following pages:

- [Driver development changes for Windows 11, version 21H2](driver-changes-for-windows-11.md)
- [Driver development changes for Windows Server 2022](driver-changes-for-windows-server-2022.md)
- [Driver development changes for Windows 10, version 2004](driver-changes-for-windows-10-version-2004.md)
- [Driver development changes for Windows 10, version 1903](driver-changes-for-windows-10-version-1903.md)

[Back to Top](#top)
