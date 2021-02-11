---
title: Microsoft Bluetooth Test Platform package
description: Bluetooth Test Platform (BTP) software package.
ms.assetid: a6beeecb-5967-4e08-bfe2-b8aae26861ad
ms.date: 2/14/2020
ms.localizationpriority: medium

---

# The BTP Software Package

The BTP software package contains several tools to be used for testing Bluetooth scenarios.

## Download the BTP Software Package

The Bluetooth Test Platform (BTP) software package contains tools for testing the interoperability of Bluetooth enabled peripherals and systems with the Windows Bluetooth stack. The included documentation provides a brief overview of the ways to configure the hardware and suggests topologies for best test coverage. Procedural information about how to run the tests and collect trace events from the Bluetooth Windows stack are included.

[![Download the Bluetooth Test Platform Software Package](images/download.png)](//download.microsoft.com/download/e/e/e/eeed3cd5-bdbd-47db-9b8e-ca9d2df2cd29/BluetoothTestPlatformPack-1.5.1.msi)  Download the Bluetooth Test Platform Software Package.

## Version Updates

| Version | Changes |
|---------|---------|
|1.5.1     | <ul><li>Added BTVS and BTETLParse diagnostic tools.</li><li>Several fixes and improvements to test reliability.</li></ul> |
|1.4.0     | <ul><li>Added keyboard latency test to HID tests.</li><li>Added mouse tests to HID tests.</li><li>Added audio + HID scenario tests.</li><li>Added battery tests.</li><li>Fixed issue causing tests to fail to load when running in older Windows releases.</li><li>Fixed scripts that failed when running on non-native CMD/PowerShell environments.</li><li>Several fixes and improvements to test reliability.</li></ul> |
|1.3.1     | <ul><li>Added audio tests capable of exercising A2DP and HFP.</li><li>Added audio volume validation and glitch detection via an FPGA on the Traduci.</li><li>Renamed tests to shorter and more user friendly names.</li><li>Several fixes and improvements to test reliability.</li></ul> |
|1.2.1     | <ul><li>Moving BTP from private preview to public.</li><li>Added experimental SleepTests demonstrating a new capability of the Traduci of executing delayed commands.</li><li>Several fixes and improvements to test reliability.</li></ul>|

## Tools in the package

### Architecture Independent Files

| Test Tool | Description | Filename |
| --- | --- | --- |
| ConfigureMachineForBtp | <ul><li>Provided as a CMD script and a PowerShell script.</li><li>Configures a test machine for running BTP tests.</li><li>Intended to be run before first test is run on a new machine or OS install.</li> | ConfigureMachineForBtp.bat<br>ConfigureMachineForBtp.ps1 |
| RunPairingTests | <ul><li>Provided as a CMD script and a PowerShell script.</li><li>Runs the Bluetooth pairing tests.</li><li>Supports custom arguments if provided.</li></ul> | RunPairingTests.bat<br>RunPairingTests.ps1 |
| RunHIDTests | <ul><li>Provided as a CMD script and a PowerShell script.</li><li>Runs the Bluetooth HID tests.</li><li>Supports custom arguments if provided.</li></ul> | RunHIDTests.bat<br>RunHIDTests.ps1 |
| RunTaefTest | <ul><li>PowerShell helper script for running TAEF tests given the test dll name and test parameters.</li></ul> | RunTeafTests.ps1 |
| RunAudioTests | <ul><li>Provided as a CMD script and a PowerShell script.</li><li>Runs audio tests including glitch detection and audio volume validation.</li><li>Supports custom arguments if provided</li></ul> | RunAudioTests.bat<br>RunAudioTests.ps1 |
| RunAudioHidScenarioTests | <ul><li>Provided as a CMD script and a PowerShell script.</li><li>Runs audio and HID scenario tests.</li><li>Supports custom arguments if provided</li></ul> | RunAudioHidScenarioTests.bat<br>RunAudioHidScenarioTests.ps1 |
| RunBatteryTests | <ul><li>Provided as a CMD script and a PowerShell script.</li><li>Runs battery tests.</li><li>Supports custom arguments if provided</li></ul> | RunBatteryTests.bat<br>RunBatteryTests.ps1 |

### Architecture Dependent Binaries

The files listed in this table are available in X86, AMD64, and ARM64 architectures. The installer will extract one instance of each per architecture.

| Test Tool | Description | Filename |
| --- | --- | --- |
| BtpDevicePlugin | <ul><li>Binary needed to support tests that use a local Windows Bluetooth radio.</li></ul> | Microsoft.Bluetooth.TestPlatform.BtpDevicePlugin.dll |
| GenericSerialIO | <ul><li>Binary needed to support BTP devices that use Windows serial communication.</li></ul> | Microsoft.Bluetooth.TestPlatform.GenericSerialIO.dll |
| HidTests | <ul><li>Test binary for Bluetooth HID tests.</li><li>Can be run using TAEF or via the provided scripts.</li></ul> | TaefHidTests.dll |
| PairingTests | <ul><li>Test binary for Bluetooth Pairing tests.</li><li>Can be run using TAEF or via the provided scripts.</li></ul> | TaefPairingTests.dll |
| SleepTests | <ul><li>Experimental test binary for Bluetooth Sleep tests.</li><li>Can be run using TAEF.</li><li> <b>Note:</b> This is not currently fully supported.</li></ul> | TaefSleepTests.dll |
| AudioTests | <ul><li>Test binary for Bluetooth Audio tests.</li><li>Can be run using TAEF.</li></ul> | TaefAudioTests.dll |
| AudioHidScenarioTests | <ul><li>Test binary for Bluetooth Audio and HID scenario tests.</li><li>Can be run using TAEF.</li></ul> | TaefAudioHidScenarioTests.dll |
| BatteryTests | <ul><li>Test binary for Bluetooth battery tests.</li><li>Can be run using TAEF.</li></ul> | TaefBatteryTests.dll |
| TraduciCmd | <ul><li>Command line tool for querying and changing the state of the Traduci, including debug commands.</li><li>Used for firmware update to Traduci hardware.</li></ul> | TraduciCmd.exe |
| BTETLParse | <ul><li>Command line tool for extracting HCI traces from supported ETL files.</li></ul> | BTETLParse.exe |
| BTVS | <ul><li>Graphical tool for streaming live HCI traces in supported formats (such as Ellisys, Frontline, and Wireshark).</li><li>Only available for the x86 architecture.</li></ul> | btvs.exe |
