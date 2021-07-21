---
title: Microsoft Bluetooth Test Platform - Audio
description: Bluetooth Test Platform (BTP) Audio tests.
ms.date: 06/09/2021
ms.localizationpriority: medium
---

# BTP Audio Tests

The BTP audio tests verify the ability of the local system to pair with a remote device over BR/EDR and validate audio functionality including volume validation and audio glitch detection.

## Setting Up

When using a Pmod device with the Traduci, first check that the green power indicator, an optional yellow test LED, and 3 orange LEDs on the Traduci are on. Confirm that the SUT's Bluetooth radio is powered on and that the appropriate device(s) are correctly plugged in to the Traduci. Currently the RN52 device can **only** be plugged into JA. More detailed information on setting up can be found at [Setting up BTP](testing-BTP-setup.md).

When using the BM-64-EVB, two red LEDs should be on (one of which may turn off after a bit). Confirm the switches, jumpers, and ports are configured for testing as described in the [BM-64-EVB board overview](testing-BTP-hw-bm64.md#getting-started).

Features and purchasing information for supported devices can be found at [Supported BTP Hardware](testing-BTP-hw.md).

## Supported devices

- [BM 64-EVB](testing-BTP-hw-bm64.md)
- [RN52](testing-BTP-hw-rn52.md) 

## Running the Audio Tests

Navigate to the folder where the BTP package was extracted. It will typically be under `C:\BTP`. In a folder named after the version of the package, you will find the scripts referenced below. Then run either:

- `RunAudioTests.bat <device name>` from an elevated command prompt or
- `RunAudioTests.ps1 <device name>` from an elevated PowerShell console

Information on available device name parameters can be found at [Bluetooth Testing Platform supported hardware](testing-BTP-hw.md#supported-devices)

You can also include the optional parameter `-VerboseLogs` at the end to get a more verbose output of inner operations of BTP.

When using the Traduci, as a test starts the red LED next to the 12-pin adapter will turn on once the command from the test to power the Pmod device has been sent. This LED will be turned off at the end of every test. If it is on at the start of the next test due the previous test failing, we will attempt to power it down and power it back on to return it to a known state. If the power cycle fails, the test will fail due to the Pmod device being in an unknown state.

When using the BM-64-EVB, red and blue LEDs will flash in patterns for indicting steps of the process such as powering on, pairing, and playing audio.

## Capturing Logs

To capture the Bluetooth logs, follow the instructions for the [busiotools for Windows Repo on GitHub](https://github.com/microsoft/busiotools/blob/master/bluetooth/tracing/readme.md).

To parse the Bluetooth logs, follow the instructions for the [BTETLParse tool](testing-BTP-tools-btetlparse.md).

## Known issues

- BM64 EVB has the following 4 known test failures:

  - `BluetoothTests::TaefAudioTests::VoiceSinkVolumeUpTest`
  - `BluetoothTests::TaefAudioTests::VoiceSinkVolumeDownTest`
  - `BluetoothTests::TaefAudioTests::VoiceSourceVolumeUpTest`
  - `BluetoothTests::TaefAudioTests::VoiceSourceVolumeDownTest`
