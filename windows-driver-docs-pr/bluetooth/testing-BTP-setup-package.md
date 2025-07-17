---
title: Install Bluetooth Test Platform Package - BTP
description: Learn how to install the Microsoft Bluetooth Test Platform (BTP) software package, read descriptions of architecture files, and find changes made in specific versions.
ms.date: 07/14/2025
ms.topic: install-set-up-deploy
---

# Get the Microsoft Bluetooth Test Platform software package

The Bluetooth Test Platform (BTP) software package contains everything that needs to be installed on your test machine to test the interoperability of Bluetooth enabled devices with the Windows Bluetooth stack. The documentation included in the installation provides information about how to configure the hardware and suggests topologies for the best test coverage. It also describes the details for how to run the tests and collect logs.

## Download the BTP software package

Use the following button to download the latest version of the BTP software package:

> [!div class="nextstepaction"]
> [Download the current release of BTP](https://download.microsoft.com/download/e/e/e/eeed3cd5-bdbd-47db-9b8e-ca9d2df2cd29/BluetoothTestPlatformPack-1.14.0.msi)

> [!TIP]
> Run the installer on the same machine you plan to use for executing your tests.
>
> After installation, don't copy, move, or delete the installed files.
> If you have a problem with your installation, use the Windows **Add or Remove Programs** feature to completely uninstall the BTP package. Then, do a clean install with the Windows package installer (_.msi_).

## Review BTP package updates by version

The following table describes changes to the BTP software package for each released version.

| Version | Changes |
|---------|-------- |
| 1.14.0  | - Added audio tests that can use a custom audio file for playback instead of a generated test tone. </br>- Fixed an issue that caused unpairing the Bluefruit Feather to fail for some central devices. </br>- Improved reliability of the Traduci audio analyzer in tests. </br>- Several other fixes and improvements to test reliability.
| 1.12.2  | - Added support for the BM62 radio. </br>- Added explicit firmware version checks for ESP32 Wi-Fi. </br>- Other Wi-Fi Coexistence fixes and improvements to test reliability.
| 1.11.1  | - Fixed crash when running standby HID power tests without an installed virtual power button. </br>- Added explicit firmware version checks for Bluefruit Feather. </br>- Several other fixes and improvements to test reliability. |
| 1.10.1  | - Added power state HID tests. </br>- Several other fixes and improvements to test reliability. |
| 1.9.0   | - Improved support for BTP devices by using custom DLL plugins. </br>- Fixed an issue affecting the audio mute/unmute tests in certain Windows builds. </br>- Several other fixes and improvements to test reliability. |
| 1.8.0   | - Added Wi-Fi with Bluetooth audio and HID coexistence tests. </br>- Added mute and unmute audio tests. </br>- Added option to record audio played during tests to a local file. </br>- Fixed issue that could cause the Bluefruit Feather to incorrectly report its Bluetooth address. </br>- Fixed issue with running current audio tests on older Windows builds. </br>- Several other fixes and improvements to test reliability. |
| 1.7.2   | - Added Wi-Fi and Bluetooth audio coexistence tests. </br>- Added support for Bluefruit Feather (nRF52840) with full parity to existing Bluefruit support. </br>- Added tests for all types of pairing key negotiations by using the Bluefruit Feather. </br>- Fixed issue where failures would occur in a tight loop if a device was unplugged mid-test. </br>- Several fixes and improvements to test reliability. |
| 1.6.2   | - No longer require a Windows Driver Kit (WDK) installation to run BTP tests. </br>- Added quick keystroke HID tests to more easily catch key repeats and other performance issues. </br>- Added quick keystroke and mouse movement after idle HID tests that are useful for loop execution. </br>- Added reconnection latency measurement to HID tests. </br>- Added reconnection after idle disconnection HID tests. </br>- Several fixes and improvements to test reliability. |
| 1.5.1   | - Added Bluetooth Virtual Sniffer (BTVS) and Bluetooth Event Trace Log (ETL) parse (_BTETLParse.exe_) diagnostic tools. </br>- Several fixes and improvements to test reliability. |
| 1.4.0   | - Added keyboard latency test to HID tests. </br>- Added mouse tests to HID tests. </br>- Added audio + HID scenario tests. </br>- Added battery tests. </br>- Fixed issue causing tests to fail to load when running in older Windows releases. </br>- Fixed scripts that failed when running on non-native CMD/PowerShell environments. </br>- Several fixes and improvements to test reliability. |
| 1.3.1   | - Added audio tests capable of exercising Advanced Audio Distribution Profile (A2DP) and Hands-Free Profile (HFP). </br>- Added audio volume validation and glitch detection via a field-programmable gate array (FPGA) on the Traduci. </br>- Renamed tests to shorter and more user friendly names. </br>- Several fixes and improvements to test reliability. |
| 1.2.1   | - Moved BTP from private preview to public. </br>- Added experimental SleepTests demonstrating a new capability of the Traduci of executing delayed commands. </br>- Several fixes and improvements to test reliability. |

## Tools in the package

The next sections list the tools provided in the BTP software package.

### Architecture independent files

The following tools in the BTP software package exist as independent files.

| Test tool | Description | Tool files |
|-----------|-------------|------------|
| **ConfigureMachineForBtp** | - Provided as a CMD script and a PowerShell script. </br>- Configures a test machine for running BTP tests. /br>- Intended to run before first test runs on a new machine or operating system install. | _ConfigureMachineForBtp.bat_ </br> _ConfigureMachineForBtp.ps1_ |
| **GetProcessorArchitectureName** | - Provided as a PowerShell script. </br>- Allows other scripts to identify the current machine's architecture. | _GetProcessorArchitectureName.ps1_ |
| **RunTaefTest** | PowerShell helper script for running TAEF tests given the test DLL name and test parameters. | _RunTeafTests.ps1_ |
| **RunPairingTests** | - Provided as a CMD script and a PowerShell script. </br>- Runs the Bluetooth pairing tests. </br>- Supports custom arguments, if provided. | _RunPairingTests.bat_ </br> _RunPairingTests.ps1_ |
| **RunHidTests** | - Provided as a CMD script and a PowerShell script. </br>- Runs the Bluetooth HID tests. </br>- Supports custom arguments, if provided. | _RunHidTests.bat_ </br> _RunHidTests.ps1_ |
| **RunAudioTests** | - Provided as a CMD script and a PowerShell script. </br>- Runs audio tests, including glitch detection and audio volume validation. </br>- Supports custom arguments, if provided. | _RunAudioTests.bat</br>RunAudioTests.ps1_ |
| **RunAudioHidScenarioTests** | - Provided as a CMD script and a PowerShell script. </br>- Runs audio and HID scenario tests. </br>- Supports custom arguments, if provided. | _RunAudioHidScenarioTests.bat_ </br> _RunAudioHidScenarioTests.ps1_ |
| **RunBatteryTests** | - Provided as a CMD script and a PowerShell script. </br>- Runs battery tests. </br>- Supports custom arguments, if provided. | _RunBatteryTests.bat_ </br> _RunBatteryTests.ps1_ |
| **RunWiFiAudioScenarioTests** | - Provided as a CMD script and a PowerShell script. </br>- Runs Wi-Fi and audio scenario tests. </br>- Supports custom arguments, if provided. | _RunWiFiAudioScenarioTests.bat_ </br> _RunWiFiAudioScenarioTests.ps1_ |
| **RunWiFiAudioHidScenarioTests** | - Provided as a CMD script and a PowerShell script. </br>- Runs Wi-Fi, audio, and HID scenario tests. </br>- Supports custom arguments, if provided. | _RunWiFiAudioHidScenarioTests.bat_ </br> _RunWiFiAudioHidScenarioTests.ps1_ |
| **RunPowerStateTests** | - Provided as a CMD script and a PowerShell script. </br>- Runs the power state tests. </br>- Supports custom arguments, if provided. | _RunPowerStateTests.bat_ </br> _RunPowerStateTests.ps1_ |
| **Bluefruit Feather Firmware** | Compiled binaries for Bluefruit Feather device. | _BtpBluefruit_nRF52840.ino.zip_ |
| **ESP32 Firmware** | Compiled binaries for ESP32wifi device. | _WiFi-ESP32.ino.bin</br>WiFi-ESP32.ino.partitions.bin_ |

### Architecture dependent binaries

The files listed in this table are available in X86, AMD64, and Arm64 architectures. The installer extracts one instance of each file per architecture.

| Test tool | Description | Tool file |
|-----------|-------------|-----------|
| **TAEF** | For more information, see [Test Authoring and Execution Framework (TAEF)](../taef/index.md). | _C:\BTP\\\<version\>\TAEF_ |
| **BtpDevicePlugin** | Binary needed to support tests that use a local Windows Bluetooth radio. | _Microsoft.Bluetooth.TestPlatform.BtpDevicePlugin.dll_ |
| **GenericSerialIO** | Binary needed to support BTP devices that use Windows serial communication. | _Microsoft.Bluetooth.TestPlatform.GenericSerialIO.dll_ |
| **HidTests** | - Test binary for Bluetooth HID tests. <br/>- Can run with TAEF or by using the provided scripts. | _TaefHidTests.dll_ |
| **PairingTests** | - Test binary for Bluetooth Pairing tests. <br/>- Can run with TAEF or by using the provided scripts. | _TaefPairingTests.dll_ |
| **AudioTests** | - Test binary for Bluetooth Audio tests. <br/>- Can run with TAEF. | _TaefAudioTests.dll_ |
| **AudioHidScenarioTests** | - Test binary for Bluetooth Audio and HID scenario tests. <br/>- Can run with TAEF. | _TaefAudioHidScenarioTests.dll_ |
| **BatteryTests** | - Test binary for Bluetooth battery tests. <br/>- Can run with TAEF. | _TaefBatteryTests.dll_ |
| **WiFiCoexScenarioTests** | - Test binary for Bluetooth and Wi-Fi coexistence tests. <br/>- Can run with TAEF. | _TaefWiFiCoexScenarioTests.dll_ |
| **PowerStateTests** | - Test binary for Bluetooth power state tests. <br/>- Can run with TAEF. | _TaefPowerStateTests.dll_ |
| **TraduciCmd** | - Command line tool for querying and changing the state of the Traduci, including debug commands. <br/>- Used for firmware update to Traduci hardware. |  _TraduciCmd.exe_ |
| **BTETLParse** | Command line tool for extracting Host Controller Interface (HCI) traces from supported ETL files. | _BTETLParse.exe_ |
| **BTVS** | - Graphical tool for streaming live HCI traces in supported formats (such as Ellisys, Frontline, and Wireshark). <br/>- Available for the x86 architecture only. | _btvs.exe_ | 
