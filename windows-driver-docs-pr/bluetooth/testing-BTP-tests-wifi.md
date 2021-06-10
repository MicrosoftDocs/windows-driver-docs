---
title: Microsoft Bluetooth Test Platform - Wi-Fi and Bluetooth audio coexistence
description: Bluetooth Test Platform (BTP) Wi-Fi and Bluetooth audio coexistence tests.
ms.date: 06/09/2021
ms.localizationpriority: medium
---

# BTP Wi-Fi and Bluetooth audio coexistence tests

The BTP Bluetooth audio and Wi-Fi coexistence tests verify the ability of the local system to pair with a remote device over BR/EDR, connect to a specified access point and stream Bluetooth audio data over an A2DP/HFP endpoint while simultaneously sending get requests to a server hosted on the access point. Bluetooth and Wi-Fi performance are reported to the user, and performance of A2DP and HFP audio streams are validated using glitch detection and traffic analysis.

## Setting up for testing

When using a Pmod device with the Traduci, first check that the green power indicator, an optional yellow test LED, and 3 orange LEDs on the Traduci are on. Confirm that the SUT's Bluetooth radio is powered on and that the appropriate device(s) are correctly plugged in to the Traduci. Currently the ESP32 device can **only** be plugged into JD. Similarly, the RN52 device can **only** be plugged into JA. More detailed information on setting up can be found at [Setting up BTP](testing-BTP-setup.md).

When using the BM-64-EVB, two red LEDs should be on, one of which may turn off after a bit. Confirm the switches, jumpers, and ports are configured for testing as described in the [BM-64-EVB board overview](testing-BTP-hw-bm64.md#getting-started).

Features and purchasing information for supported devices can be found at [Supported BTP Hardware](testing-BTP-hw.md).

## Supported devices

- [RN52](testing-BTP-hw-rn52.md) (as Audio Device)
- [ESP32](testing-BTP-hw-esp32.md) (as Access Point device)

## Running the Wi-Fi and Bluetooth audio coexistence tests

Navigate to the folder where the BTP package was extracted. It will typically be under `C:\BTP`. In a folder named after the version of the package, you will find the scripts referenced below. Ensure that all existing network and VPN connections are disconnected, and that "Connect Automatically" is unchecked. Then run either:

- `RunWiFiCoexScenarioTests.bat <Bluetooth device name> <Wi-Fi device name>` from an elevated command prompt or
- `RunWiFiCoexScenarioTests.ps1 <Bluetooth device name> <Wi-Fi device name>` from an elevated PowerShell console

Information on available device name parameters can be found in [Bluetooth Testing Platform supported hardware](testing-BTP-hw.md#supported-devices).

You can also include the optional parameter `-VerboseLogs` at the end to get a more verbose output of inner operations of BTP.

When using the Traduci, as a test starts the red LED next to the 12-pin adapter will turn on once the command from the test to power the Pmod device has been sent. This LED will be turned off at the end of every test. If it is on at the start of the next test due the previous test failing, we will attempt to power it down and power it back on to return it to a known state. If the power cycle fails, the test will fail due to the Pmod device being in an unknown state.

When using the BM-64-EVB, red and blue LEDs will flash in patterns for indicting steps of the process such as powering on and pairing.

## Capturing logs

To capture the Bluetooth logs follow the instructions for the [busiotools for Windows Repo on GitHub](https://github.com/microsoft/busiotools/blob/master/bluetooth/tracing/readme.md).

To parse the Bluetooth logs, follow the instructions for the [BTETLParse tool](testing-BTP-tools-btetlparse.md).

## Known issues

- Stress tests: Tests run in a tight loop using an LE device may cause pairing or unpairing to fail.
- Running Wi-Fi and Bluetooth audio coexistence tests without disconnecting from any VPN sessions will cause failures.
