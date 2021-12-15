---
title: Microsoft Bluetooth Test Platform - BTP Power State HID tests
description: Bluetooth Test Platform (BTP) Power State HID tests.
ms.date: 12/13/2021
ms.localizationpriority: medium
---

# BTP Power State HID Tests

The BTP Power State HID tests verify the ability of the local system to resume from various power states.

## Setting up for testing

When using a Pmod device with the Traduci, first check that the green power indicator, an optional yellow test LED, and 3 orange LEDs on the Traduci are on. Confirm that the SUT's Bluetooth radio is powered on and that the appropriate device(s) are correctly plugged in to the Traduci.  More detailed information on setting up can be found in [Setting up BTP](testing-BTP-setup.md).

Features and purchasing information for supported devices can be found in [Supported BTP hardware](testing-BTP-hw.md). 

An external power adapter for the Traduci is required for these tests. USB power is not sufficient.  Requirements for the necessary adapter can be found on [Power Adapter](testing-BTP-hw-power-adapter.md)

A single test device will not be able to run all power state tests, as some power states, such as hibernate and sleep, are mutually exclusive on a system under test (SUT). The BTP script RunAudioHidScenarioTests.bat or RunAudioHidScenarioTests.ps1 should automatically select & run the tests compatible with the SUT. Any test that is not compatible with the SUT will be marked others as incompatible rather than failed.

## Provisioning the System Under Test

Systems under test (SUTs) must be provisioned for power state tests before they are run. Follow the instructions to provision the PC for power tests provided by the WDK 10 document, [Prepare the target computer for provisioning](/windows-hardware/drivers/gettingstarted/provision-a-target-computer-wdk-8-1#prepare-the-target-computer-for-provisioning)

## Supported devices

- [RN42](testing-BTP-hw-rn42.md)
- [Bluefruit Feather](testing-BTP-hw-bluefruit-Feather.md)

## Running the Power State HID tests

Navigate to the folder where the BTP package was extracted. It will typically be under `C:\BTP`. In a folder named after the version of the package, you will find the scripts referenced below. Then run either:

- `RunAudioHidScenarioTests.bat <device name>` from an elevated command prompt or
- `RunAudioHidScenarioTests.ps1 <device name>` from an elevated PowerShell console

Information on available device name parameters can be found in [Bluetooth Test Platform supported hardware](testing-BTP-hw.md#supported-devices).

You can also include the optional parameter `-VerboseLogs` at the end to get a more verbose output of inner operations of BTP.

When using the Traduci, as a test starts the red LED next to the 12-pin adapter will turn on once the command from the test to power the Pmod device has been sent. This LED will be turned off at the end of every test. If it is on at the start of the next test due the previous test failing, we will attempt to power it down and power it back on to return it to a known state. If the power cycle fails, the test will fail due to the Pmod device being in an unknown state.

## Capturing logs

To capture the Bluetooth logs follow the instructions for the [busiotools for Windows Repo on GitHub](https://github.com/microsoft/busiotools/blob/master/bluetooth/tracing/readme.md).

To parse the Bluetooth logs, follow the instructions for the [BTETLParse tool](testing-BTP-tools-btetlparse.md).
