---
title: Microsoft Bluetooth Test Platform - BTP Power State HID Tests
description: Bluetooth Test Platform (BTP) Power State HID tests.
ms.date: 01/10/2024
ms.localizationpriority: medium
---

# BTP power state HID tests

The BTP power state HID tests verify the ability of the system to transition between various power states while maintaining correct Bluetooth HID functionality.

## Setting up for testing

Before using a Pmod device with the Traduci, check that the green power indicator, an optional yellow test LED, and 3 orange LEDs on the Traduci are on. Make sure the system's Bluetooth radio is on and that the devices are correctly plugged into the Traduci or connected directly to the system under test (SUT). More detailed information on setting up can be found in [BTP overview](testing-btp-overview.md).

Features and purchasing information for supported devices can be found in [Supported BTP hardware](testing-BTP-hw.md).

An external power adapter for the Traduci is required for these tests. USB power isn't sufficient. Requirements for the necessary adapter can be found on [Power Adapter](testing-BTP-hw-power-adapter.md). If a non-Traduci based device is being used, like the [Bluefruit Feather](testing-BTP-hw-bluefruit-Feather.md), it requires a powered USB hub in order to remain powered throughout the tests. Ensure that the USB hub is correctly powered, and the device is connected to the hub via a USB cable. Also, make sure that the hub is plugged into the SUT using a USB cable.

A single Windows test device can't run all power state tests. Some power states, such as standby and sleep, are mutually exclusive on a SUT. The BTP script `RunPowerStateTests.bat` or `RunPowerStateTests.ps1` should automatically select and run the tests compatible with the SUT. Any test that isn't compatible with the SUT is skipped.

## Provisioning the System Under Test

Systems under test (SUTs) must be provisioned for the power state tests before they're run. Follow the instructions to prepare the PC for power tests provided by the WDK 10 document [Provision a computer for driver deployment and testing (WDK 10)](../gettingstarted/provision-a-target-computer-wdk-8-1.md)

## Supported devices

- [RN42](testing-BTP-hw-rn42.md)
- [Bluefruit Feather](testing-BTP-hw-bluefruit-Feather.md)

## Running the Power State HID tests

Navigate to the folder where the BTP package was extracted. It's typically located under `C:\BTP`. In a folder named after the version of the package, you'll find the following scripts. Run either:

- `RunPowerStateTests.bat <device name>` from an elevated command prompt or
- `RunPowerStateTests.ps1 <device name>` from an elevated PowerShell console

Information on available device name parameters can be found in [Bluetooth Test Platform supported hardware](testing-BTP-hw.md).

You can also include the optional parameter `-VerboseLogs` at the end to get a more verbose output of inner operations of BTP.

As a test starts on the Traduci, the red LED next to the 12-pin adapter turns on once the command from the test to power the Pmod device has been sent. This LED is turned off at the end of every test. If it is on at the start of the next test due to the previous test failing, power it down and power it back on to return it to a known state. If the power cycle fails, the test fails due to the Pmod device being in an unknown state.

## Capturing logs

To capture the Bluetooth logs, follow the instructions for the [busiotools for Windows Repo on GitHub](https://github.com/microsoft/busiotools/blob/master/bluetooth/tracing/readme.md).

To parse the Bluetooth logs, follow the instructions for the [BTETLParse tool](testing-BTP-tools-btetlparse.md).
