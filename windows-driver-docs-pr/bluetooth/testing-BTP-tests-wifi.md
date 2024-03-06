---
title: Microsoft Bluetooth Test Platform - Wi-Fi and Bluetooth Coexistence
description: Bluetooth Test Platform (BTP) Wi-Fi and Bluetooth coexistence tests.
ms.date: 01/10/2024
---

# BTP Wi-Fi and Bluetooth coexistence tests

The BTP Bluetooth and Wi-Fi coexistence tests check if the system can pair with Bluetooth devices, connect to a Wi-Fi access point, and stream data over Wi-Fi. These tests also validate Bluetooth functionality and monitor Bluetooth throughput at the same time. Bluetooth and Wi-Fi performance are reported to the user, and performance of Bluetooth audio and HID streams are validated using glitch detection and traffic analysis.

## Setting up for testing

Before using a Pmod device with the Traduci, check that the green power indicator, an optional yellow test LED, and 3 orange LEDs on the Traduci are on. Confirm that the SUT's Bluetooth radio is powered on and that the appropriate device(s) are correctly plugged in to the Traduci. Currently the ESP32 device can **only** be plugged into JD. Similarly, the audio device (RN52 or BM62) device can **only** be plugged into JA. More detailed information on setting up can be found at [BTP overview](testing-btp-overview.md).

Features and purchasing information for supported devices can be found at [Supported BTP Hardware](testing-BTP-hw.md).

## Supported devices

- [ESP32](testing-BTP-hw-esp32.md) (as Wi-Fi Access Point device)
- [BM62](testing-BTP-hw-bm62.md) (as Audio Device)
- [RN52](testing-BTP-hw-rn52.md) (as Audio Device)
- [RN42](testing-BTP-hw-rn42.md) (as HID Device)
- [Bluefruit Friend](testing-BTP-hw-bluefruit-Friend.md) (as HID Device)
- [Bluefruit Feather](testing-BTP-hw-bluefruit-Feather.md) (as HID Device)

## Running the Wi-Fi and Bluetooth coexistence tests

Navigate to the folder where the BTP package was extracted. It's typically located under `C:\BTP`. In a folder named after the version of the package, you'll find the following scripts. Ensure that all existing network and VPN connections are disconnected, and that "Connect Automatically" is unchecked. Then, run either:

- `RunWiFiAudioScenarioTests.bat <Wi-Fi device name> <Bluetooth audio device name>` from an elevated command prompt or
- `RunWiFiAudioScenarioTests.ps1 <Wi-Fi device name> <Bluetooth audio device name>` from an elevated PowerShell console

If you would like to also validate HID functionality at the same time, then run either:

- `RunWiFiAudioHidScenarioTests.bat <Wi-Fi device name> <Bluetooth audio device name> <Bluetooth HID device name>` from an elevated command prompt or
- `RunWiFiAudioHidScenarioTests.ps1 <Wi-Fi device name> <Bluetooth audio device name> <Bluetooth HID device name>` from an elevated PowerShell console

Information on available device name parameters can be found in [Bluetooth Test Platform supported hardware](testing-BTP-hw.md).

You can also include the optional parameter `-VerboseLogs` at the end to get a more verbose output of inner operations of BTP.

As a test starts on the Traduci, the red LED next to the 12-pin adapter turns on once the command from the test to power the Pmod device has been sent. This LED is turned off at the end of every test. If it is on at the start of the next test due to the previous test failing, power it down and power it back on to return it to a known state. If the power cycle fails, the test fails due to the Pmod device being in an unknown state.

## Capturing logs

To capture the Bluetooth logs, follow the instructions for the [busiotools for Windows Repo on GitHub](https://github.com/microsoft/busiotools/blob/master/bluetooth/tracing/readme.md).

To parse the Bluetooth logs, follow the instructions for the [BTETLParse tool](testing-BTP-tools-btetlparse.md).

## Known issues

- Stress tests: Tests run in a tight loop using an LE device may cause pairing or unpairing to fail.
- Running Wi-Fi and Bluetooth coexistence tests without disconnecting from any VPN sessions cause failures.
- Currently these tests may fail for some Arm64 devices. We're working on resolving this issue.
