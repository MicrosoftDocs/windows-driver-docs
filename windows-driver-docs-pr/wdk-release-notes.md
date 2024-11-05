---
title: Windows Drivers Kit (WDK) release notes
description: Highlights the latest features in new WDK releases.
ms.date: 11/05/2024
---

# Windows Driver Kit (WDK) release notes

The following features and bug fixes are in Windows 11 24H2 WDK update.

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
