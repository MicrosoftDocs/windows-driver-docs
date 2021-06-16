---
title: Microsoft Bluetooth Test Platform package
description: Bluetooth Test Platform (BTP) software package.
ms.date: 06/09/2021
ms.localizationpriority: medium
---

# The BTP Software Package

The BTP software package contains several tools to be used for testing Bluetooth scenarios.

## Download the BTP Software Package

The Bluetooth Test Platform (BTP) software package contains tools for testing the interoperability of Bluetooth enabled peripherals and systems with the Windows Bluetooth stack. The included documentation provides a brief overview of the ways to configure the hardware and suggests topologies for best test coverage. Procedural information about how to run the tests and collect trace events from the Bluetooth Windows stack are included. Click the following button to download the latest version.

[![Download the Bluetooth Test Platform software package.](images/download.png)](https://download.microsoft.com/download/e/e/e/eeed3cd5-bdbd-47db-9b8e-ca9d2df2cd29/BluetoothTestPlatformPack-1.7.2.msi)

## Version Updates

| Version | Changes |
|---------|---------|
|1.7.2     | - Added Wi-Fi and Bluetooth audio co-existence tests.</br>- Added support for Bluefruit Feather (nRF52840) with full parity to existing Bluefruit support.</br>- Added tests for all types of pairing key negotiations using the Bluefruit Feather.</br>- Fixed issue where failures would occur in a tight loop if a device was unplugged mid-test.</br>- Several fixes and improvements to test reliability. |
|1.6.2     | - No longer require a WDK installation to run BTP tests.</br>- Added quick keystroke HID tests to more easily catch key repeats and other performance issues.</br>- Added quick keystroke and mouse movement after idle HID tests that are useful for loop execution.</br>- Added reconnection latency measurement to HID tests.</br>- Added reconnection after idle disconnection HID tests.</br>- Several fixes and improvements to test reliability. |
|1.5.1     | - Added BTVS and BTETLParse diagnostic tools.</br>- Several fixes and improvements to test reliability. |
|1.4.0     | - Added keyboard latency test to HID tests.</br> - Added mouse tests to HID tests.</br> - Added audio + HID scenario tests. </br> - Added battery tests.</br> - Fixed issue causing tests to fail to load when running in older Windows releases.</br> - Fixed scripts that failed when running on non-native CMD/PowerShell environments.</br> - Several fixes and improvements to test reliability. |
|1.3.1     | -  Added audio tests capable of exercising A2DP and HFP.</br> - Added audio volume validation and glitch detection via an FPGA on the Traduci.</br> - Renamed tests to shorter and more user friendly names.</br> - Several fixes and improvements to test reliability. |
|1.2.1     | - Moving BTP from private preview to public.</br> - Added experimental SleepTests demonstrating a new capability of the Traduci of executing delayed commands.</br> - Several fixes and improvements to test reliability. |

## Tools in the package

### Architecture Independent Files

| Test Tool | Description | Filename |
| --- | --- | --- |
| ConfigureMachineForBtp | - Provided as a CMD script and a PowerShell script.</br>- Configures a test machine for running BTP tests.</br>- Intended to be run before first test is run on a new machine or OS install.</br> | ConfigureMachineForBtp.bat</br>ConfigureMachineForBtp.ps1 |
| GetProcessorArchitectureName | - Provided as a PowerShell script.</br>- Allows other scripts to identify the current machine's architecture | GetProcessorArchitectureName.ps1 |
| RunTaefTest | - PowerShell helper script for running TAEF tests given the test dll name and test parameters.</br> | RunTeafTests.ps1 |
| RunPairingTests | - Provided as a CMD script and a PowerShell script.</br>- Runs the Bluetooth pairing tests.</br>- Supports custom arguments if provided.</br> | RunPairingTests.bat</br>RunPairingTests.ps1 |
| RunHidTests | - Provided as a CMD script and a PowerShell script.</br>- Runs the Bluetooth HID tests.</br>- Supports custom arguments if provided.</br> | RunHidTests.bat</br>RunHidTests.ps1 |
| RunAudioTests | - Provided as a CMD script and a PowerShell script.</br>- Runs audio tests including glitch detection and audio volume validation.</br>- Supports custom arguments if provided</br> | RunAudioTests.bat</br>RunAudioTests.ps1 |
| RunAudioHidScenarioTests | - Provided as a CMD script and a PowerShell script.</br>- Runs audio and HID scenario tests.</br>- Supports custom arguments if provided</br> | RunAudioHidScenarioTests.bat</br>RunAudioHidScenarioTests.ps1 |
| RunBatteryTests | - Provided as a CMD script and a PowerShell script.</br>- Runs battery tests.</br>- Supports custom arguments if provided</br> | RunBatteryTests.bat</br>RunBatteryTests.ps1 |
| RunWiFiCoexScenarioTests | - Provided as a CMD script and a PowerShell script.</br>- Runs Wi-Fi coexistence scenario tests.</br>- Supports custom arguments if provided</br> | RunWiFiCoexScenarioTests.bat</br>RunWiFiCoexScenarioTests.ps1 |
| Bluefruit Feather Firmware | - Compiled binaries for Bluefruit Feather device. | BtpBluefruit_nRF52840.ino.zip |
| ESP32 Firmware | - Compiled binaries for ESP32wifi device. | WiFi-ESP32.ino</br>WiFi-ESP32.ino.partitions |

### Architecture Dependent Binaries

The files listed in this table are available in X86, AMD64, and ARM64 architectures. The installer will extract one instance of each per architecture.

| Test Tool | Description | Filename |
| --- | --- | --- |
| TAEF | - [Test Authoring and Execution Framework (TAEF)](../taef/index.md) | C:\BTP\\\<version\>\TAEF |
| BtpDevicePlugin | - Binary needed to support tests that use a local Windows Bluetooth radio. | Microsoft.Bluetooth.TestPlatform.BtpDevicePlugin.dll |
| GenericSerialIO | - Binary needed to support BTP devices that use Windows serial communication. | Microsoft.Bluetooth.TestPlatform.GenericSerialIO.dll |
| HidTests | - Test binary for Bluetooth HID tests.</br> - Can be run using TAEF or via the provided scripts. | TaefHidTests.dll |
| PairingTests | - Test binary for Bluetooth Pairing tests.</br> - Can be run using TAEF or via the provided scripts. | TaefPairingTests.dll |
| SleepTests | - Experimental test binary for Bluetooth Sleep tests.</br> - Can be run using TAEF. </br>**Note:** This is not currently fully supported. | TaefSleepTests.dll |
| AudioTests | -  Test binary for Bluetooth Audio tests.</br> - Can be run using TAEF. | TaefAudioTests.dll |
| AudioHidScenarioTests | - Test binary for Bluetooth Audio and HID scenario tests.</br> - Can be run using TAEF. | TaefAudioHidScenarioTests.dll |
| BatteryTests | - Test binary for Bluetooth battery tests.</br> - Can be run using TAEF. | TaefBatteryTests.dll |
| WiFiCoexScenarioTests | - Test binary for Bluetooth and Wi-Fi coexistence tests.</br> - Can be run using TAEF. | TaefWiFiCoexScenarioTests.dll |
| TraduciCmd | - Command line tool for querying and changing the state of the Traduci, including debug commands.</br> - Used for firmware update to Traduci hardware. | TraduciCmd.exe |
| BTETLParse | - Command line tool for extracting HCI traces from supported ETL files. | BTETLParse.exe |
| BTVS | - Graphical tool for streaming live HCI traces in supported formats (such as Ellisys, Frontline, and Wireshark).</br> - Only available for the x86 architecture. | btvs.exe |
