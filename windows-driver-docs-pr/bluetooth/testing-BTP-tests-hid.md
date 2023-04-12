---
title: Microsoft Bluetooth Test Platform - HID
description: Bluetooth Test Platform (BTP) HID tests.
ms.date: 04/11/2023
---

# BTP HID tests

The BTP HID tests verify the ability of the local system to pair with a remote radio over BR/EDR or LE and validate HID functionality.

## Setting Up

Before using a Pmod device with the Traduci, check that the green power indicator, an optional yellow test LED, and 3 orange LEDs on the Traduci are on. Confirm that the SUT's Bluetooth radio is powered on and that the appropriate device(s) are correctly plugged in to the Traduci. Currently the RN42 device can **only** be plugged into JB. Similarly, the Bluefruit device can **only** be plugged into JC. More detailed information on setting up can be found at [BTP overview](testing-btp-overview.md).

Information and purchasing information for supported devices can be found [Supported BTP Hardware](testing-BTP-hw.md).

## Supported devices

- [RN42](testing-BTP-hw-rn42.md)
- [Bluefruit Friend](testing-BTP-hw-bluefruit-Friend.md)
- [Bluefruit Feather](testing-BTP-hw-bluefruit-Feather.md)

## Running the HID Tests

Navigate to the folder where the BTP package was extracted. It's typically located under `C:\BTP`. In a folder named after the version of the package, you'll find the following scripts. Run either:

- `RunHidTests.bat <device name>` from an elevated command prompt or
- `RunHidTests.ps1 <device name>` from an elevated PowerShell console

Information on available device name parameters can be found [Bluetooth Test Platform supported hardware](testing-BTP-hw.md)

You can also include the optional parameter `-VerboseLogs` at the end to get a more verbose output of inner operations of BTP.

As a test starts on the Traduci, the red LED next to the 12-pin adapter turns on once the command from the test to power the Pmod device has been sent. This LED is turned off at the end of every test. If it is on at the start of the next test due to the previous test failing, power it down and power it back on to return it to a known state. If the power cycle fails, the test fails due to the Pmod device being in an unknown state.

## Capturing Logs

To capture the Bluetooth logs, follow the instructions at [The Bus tools for Windows Repo on GitHub](https://github.com/microsoft/busiotools/blob/master/bluetooth/tracing/readme.md).

To parse the Bluetooth logs, follow the instructions for the [BTETLParse tool](testing-BTP-tools-btetlparse.md).

## Known issues

- Stress tests: Tests run in a tight loop using an LE device may cause pairing or unpairing to fail.
- Tests may infrequently fail with an LE HID device due to validation intended to catch unexpected disconnections. Sometimes disconnections are automatically recovered (failures to establish), but the test still fails the validation. Failures can happen more frequently in noisy RF environments.
