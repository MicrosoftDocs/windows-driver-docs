---
title: Microsoft Bluetooth Test Platform - Pairing
description: Bluetooth Test Platform (BTP) pairing tests.
ms.date: 06/09/2021
ms.localizationpriority: medium
---

# BTP Pairing Tests

The BTP pairing tests verify the ability of the local system to pair to and unpair from a remote device over BR/EDR or LE.

## Setting up for testing

When using a Pmod device with the Traduci, first check that the green power indicator, an optional yellow test LED, and 3 orange LEDs on the Traduci are on. Confirm that the SUT's Bluetooth radio is powered on and that the appropriate device(s) are correctly plugged in to the Traduci. Currently the RN42 device can **only** be plugged into JB. Similarly, the Bluefruit device can **only** be plugged into JC. More detailed information on setting up can be found at [Setting up BTP](testing-BTP-setup.md).

When using the BM-64-EVB, two red LEDs should be on (one of which may turn off after a bit). Confirm the switches, jumpers, and ports are configured for testing as decribed in the [BM-64-EVB board overview](testing-BTP-hw-bm64.md#getting-started).

Features and purchasing information for supported devices can be found at [Supported BTP Hardware](testing-BTP-hw.md).

## Supported devices

- [RN42](testing-BTP-hw-rn42.md)
- [Bluefruit Friend](testing-BTP-hw-bluefruit-Friend.md)
- [Bluefruit Feather](testing-BTP-hw-bluefruit-Feather.md)
- [BM 64-EVB](testing-BTP-hw-bm64.md)
- [RN52](testing-BTP-hw-rn52.md) 
- [Human Device Adapter](testing-BTP-human-device-adapter.md)

## Running the pairing tests

Navigate to the folder where the BTP package was extracted. It will typically be under `C:\BTP`. In a folder named after the version of the package, you will find the scripts referenced below. Then run either:

- `RunPairingTests.bat <device name>` from an elevated command prompt or
- `RunPairingTests.ps1 <device name>` from an elevated PowerShell console

Information on available device name parameters can be found in [Bluetooth Testing Platform supported hardware](testing-BTP-hw.md#supported-devices).

You can also include the optional parameter `-VerboseLogs` at the end to get a more verbose output of inner operations of BTP.

When using the Traduci, as a test starts the red LED next to the 12-pin adapter will turn on once the command from the test to power the Pmod device has been sent. This LED will be turned off at the end of every test. If it is on at the start of the next test due the previous test failing, we will attempt to power it down and power it back on to return it to a known state. If the power cycle fails, the test will fail due to the Pmod device being in an unknown state.

When using the BM-64-EVB, red and blue LEDs will flash in patterns for indicting steps of the process such as powering on and pairing.

## Capturing logs

To capture the Bluetooth logs follow the instructions for the [busiotools for Windows Repo on GitHub](https://github.com/microsoft/busiotools/blob/master/bluetooth/tracing/readme.md).

To parse the Bluetooth logs, follow the instructions for the [BTETLParse tool](testing-BTP-tools-btetlparse.md).

## Known issues

- Stress tests: Tests run in a tight loop using an LE device may cause pairing or unpairing to fail.
