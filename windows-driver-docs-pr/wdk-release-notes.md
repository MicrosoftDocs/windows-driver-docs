---
title: Windows Drivers Kit (WDK) release notes
description: Highlights the latest features in new WDK releases.
ms.date: 10/01/2025
ms.topic: release-notes
---

# Windows Driver Kit (WDK) release notes

The following features and bug fixes are in Windows 11 24H2 WDK update.

## Version 10.0.26100.6584

*Released Nov 01, 2025*


### SoundWire Device Class for Audio (SDCA)

The SDCA driver stack now supports the SDCA Companion Amp Function and Multichannel Capture scenarios. All SDCA drivers are included Inbox.
Enable connectivity to Wi-Fi 7 enterprise networks.

The WDK adds changes to the WiFiCx public header and library to enable Ihv drivers to connect to Wi-Fi 7 Enterprise networks. The WiFiCx driver tlv parser version is bumped up to 2.0.13 and capabilities are added to enable both the OS and the driver to be aware of Wi-Fi 7 enterprise connectivity support from the other.

### Icekeymaninterface.h

- Adds new flag to capabilities structure for implementation to attest FIPS module compliance. 
- Introduces new interface API for validating a wrapped key can be unwrapped by the system.

### Packet Monitor Clnt NPIs

Pktmon Clnt NPIs are available for kernel-mode drivers to push network packet notifications into the PktMon platform. You can use these NPIs to diagnose performance and network connectivity issues. The NPIs allow run-time registration with the PktMon platform so that drivers can safely run on systems without Pktmon support.

### usermode_accessors.h

Contains dedicated functions for the kernel to use when reading from and writing to the user-mode virtual address space.


## Version 10.0.26100.4202

*Released June 16, 2025*

### Windows Driver Kit End User License Agreement (EULA)

The Windows Driver Kit EULA is updated. This update includes a routine review, and some fixed broken links.

### Bluetooth Stereo Render Feature

Audio Configuration 8 is now available, enabling stereo render with concurrent mono capture. This enhancement supports Spatial Audio in Microsoft Teams and delivers an improved wireless gaming audio experience.

### Enclave Access Restriction Update

The [IMAGE_ENCLAVE_CONFIG32](/windows/win32/api/winnt/ns-winnt-image_enclave_config32) flag now enforces a policy that restricts enclave access to the containing process's address space. Enclaves must use [EnclaveCopyIntoEnclave](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclavecopyintoenclave) and [EnclaveCopyOutOfEnclave](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclavecopyoutofenclave) APIs for memory access. Additionally, the [EnclaveRestrictContainingProcessAccess](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclaverestrictcontainingprocessaccess) API can be used to modify this restriction at runtime.

## Version 10.0.26100.3323

*Released March 14, 2025*.

### SoundWire Device Class for Audio (SDCA)

The SdcaClass driver now sends notifications to the attached SDCA XU driver for changes in the hardware Function Status control along with system posture changes.

### Bluetooth LE Audio Bidirectional Multichannel Streaming

A new set of data structures are added to support bidirectional multichannel streaming. For example, stereo render with mono capture for Bluetooth LE Audio. There are now flags to specify the audio codec location for bidirectional multichannel streaming support.

## Version 10.0.26100.2454

*Released November 27, 2024*.

### Packet Monitor APIs

Pktmon APIs are available for kernel-mode drivers to send and receive network package notifications. You can use these APIs to diagnose performance and network connectivity issues.

### Bug Fixes

WDK installer unexpectedly launches the bundled VSIX installation at the end of installation if an earlier WDK was already present on the computer. The WDK VSIX is no longer part of the WDK MSI, so the installer no longer exhibits this behavior.

## Version 10.0.26100.2161

*Released November 4, 2024*.

### KASAN support

Kernel Address Sanitizer (KASAN), a bug-detection technology now supported on Windows drivers, enables the detection of several classes of illegal memory access. For more information, see [Kernel Address Sanitizer (KASAN)](./devtest/kasan.md).

### Azure file sync

Azure file sync reparse tag definition is updated. For details, see [Azure File Sync](https://support.microsoft.com/topic/azure-file-sync-agent-v18-2-release-july-2024-613d00dc-998b-4885-86b9-73750195baf5).

### EWDK VS build tools (10.0.26100.2161)

The Visual Studio build tools in EWDK are updated to version 17.11.4.

### WDK MSI update

The WDK VSIX no longer ships with the WDK MSI because the WDK VSIX is now included as part of Visual Studio individual components. When you try to install WDK MSI on a machine without WDK VSIX installed, the following warning message is shown at the beginning of installation.

:::image type="content" source="images/install_wdk_vsix_msg.png" alt-text="Screenshot of the WDK VSIX install notification.":::

However, if the WDK is installed on a machine with the WDK VSIX installed, a message confirming successful installation is displayed.

:::image type="content" source="images/WDK_Install_After_VSIX.png" alt-text="Screenshot of the WDK install success message.":::

## Version 10.0.26100.1882

*Released October 14, 2024*.

### Audio headers

Added *audioAggregation.h* and *audioSensors.h* for enabling SoundWire Device Class for Audio (SDCA) speaker aggregation and ultrasound support.

### EWDK VS build tools (10.0.26100.1882)

The Visual Studio build tools in EWDK are updated to version 17.10.5.

## Version 10.0.26100.1591

*Released September 18, 2024*.

### WDK VSIX installation

The WDK VSIX is added as a Visual Studio individual component starting with the VS 17.11 release. For more information, see the [Windows Drivers Kits download page](download-the-wdk.md).

:::image type="content" source="images/vs-wdk-selection.png" alt-text="Screenshot of Visual Studio WDK individual component selected.":::

### Static Tools Logo - Creating a driver verification log

To create a driver verification log (DVL) for the Static Tools Logo Test, see the [Creating a Driver Verification Log](./develop/creating-a-driver-verification-log.md) article.

Navigating to **Extensions > Drivers > Create Driver Verification Log** in Visual Studio now triggers the following redirection message.

:::image type="content" source="images/codeql-redirection.png" alt-text="Screenshot of Visual Studio notification for CodeQL DVL generation.":::

### Static Tools Logo - Placement requirement for CodeQL SARIF file

The process of generating DVL for CodeQL previously required placing the SARIF file in the same directory as the VCXProj file for the driver project. Recognizing the inconvenience posed for developers, we eliminated the requirement. Now users can generate the DVL and save it in any location of their choice by using this command:

```cmd
C:\Program Files (x86)\Windows Kits\10\Tools\dvl\dvl.exe" /manualCreate `<driverName>` `<driverArchitecture>` /`<path to sarif file>`'\
```

:::image type="content" source="images/sarif-placement-update.png" alt-text="Screenshot of SARIF placement updated.":::

### UMDF WiFiCX drivers

To support UMDF WiFiCX drivers, we added UMDF public header and library support. These changes ensure that WiFiCX drivers apply the [advantages of writing UMDF drivers](./wdf/advantages-of-writing-umdf-drivers.md). The following updates were made:

- Created a new UMDF version of WifiCxTlvGenParse.lib.
- Created UMDF equivalents of KMDF's dot11wificxintf.h, dot11wificxtypes.hpp, and WifiCxTlvGenParse.lib.

### Bug fixes for device fundamentals and WDTF test framework

Bugs associated with DevFund tests were fixed. This change improves the WDK bring up experience.
