---
title: Microsoft Bluetooth Test Platform - BTP Power State HID tests
description: Bluetooth Test Platform (BTP) Power State HID tests.
ms.date: 05/05/2022
ms.localizationpriority: medium
---

# BTP Power State HID Tests

The BTP Power State HID tests verify the ability of the local system to transition to and resume from various power states (standby, sleep, and hibernation) while maintaining correct Bluetooth HID functionality.

## Setting up for testing

When using a Pmod device with the Traduci, first check that the green power indicator, an optional yellow test LED, and 3 orange LEDs on the Traduci are on. Confirm that the system under test's Bluetooth radio is powered on and that the appropriate device(s) are correctly plugged in to the Traduci or directly connected to the SUT when appropriate.  More detailed information on setting up can be found in [BTP overview](testing-btp-overview.md).

Features and purchasing information for supported devices can be found in [Supported BTP hardware](testing-BTP-hw.md).

An external power adapter for the Traduci is required for these tests. USB power is not sufficient. Requirements for the necessary adapter can be found on [Power Adapter](testing-BTP-hw-power-adapter.md). If a non-Traduci based device is being used, like the [Bluefruit Feather](testing-BTP-hw-bluefruit-Feather.md), it will require a powered USB hub in order to remain powered throughout the tests. In such case, make sure that the USB hub is properly powered, the device is plugged into the hub via a USB cable, and the hub is plugged into the system under test (SUT) using a USB cable.

A single Windows test device will not be able to run all power state tests, as some power states, such as standby and sleep, are mutually exclusive on a SUT. The BTP script `RunPowerStateTests.bat` or `RunPowerStateTests.ps1` should automatically select and run the tests compatible with the SUT. Any test that is not compatible with the SUT will be skipped.

## Provisioning the System Under Test

Systems under test (SUTs) must be provisioned for the power state tests before they are run. Follow the instructions to provision the PC for power tests provided by the WDK 10 document [Provision a computer for driver deployment and testing (WDK 10)](../gettingstarted/provision-a-target-computer-wdk-8-1.md)

## Supported devices

- [RN42](testing-BTP-hw-rn42.md)
- [Bluefruit Feather](testing-BTP-hw-bluefruit-Feather.md)

## Running the Power State HID tests

Navigate to the folder where the BTP package was extracted. It will typically be under `C:\BTP`. In a folder named after the version of the package, you will find the scripts referenced below. Then run either:

- `RunPowerStateTests.bat <device name>` from an elevated command prompt or
- `RunPowerStateTests.ps1 <device name>` from an elevated PowerShell console

Information on available device name parameters can be found in [Bluetooth Test Platform supported hardware](testing-BTP-hw.md).

You can also include the optional parameter `-VerboseLogs` at the end to get a more verbose output of inner operations of BTP.

When using the Traduci, as a test starts the red LED next to the 12-pin adapter will turn on once the command from the test to power the Pmod device has been sent. This LED will be turned off at the end of every test. If it is on at the start of the next test due the previous test failing, we will attempt to power it down and power it back on to return it to a known state. If the power cycle fails, the test will fail due to the Pmod device being in an unknown state.

## Capturing logs

To capture the Bluetooth logs follow the instructions for the [busiotools for Windows Repo on GitHub](https://github.com/microsoft/busiotools/blob/master/bluetooth/tracing/readme.md).

To parse the Bluetooth logs, follow the instructions for the [BTETLParse tool](testing-BTP-tools-btetlparse.md).