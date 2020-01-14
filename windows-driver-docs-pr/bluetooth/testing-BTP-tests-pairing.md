---
title: Microsoft Bluetooth Test Platform
description: Bluetooth Test Platform (BTP) pairing tests.
ms.assetid: 19caf4db-9303-47d1-be12-5ff4b2710bc8
ms.date: 4/17/2019
ms.localizationpriority: medium

---

# BTP Pairing Tests

The BTP pairing tests will test the ability of the local system to pair to and unpair from a remote radio over BR/EDR or LE.

### Setting Up ##

First check that the green power indicator, an optional yellow test LED, and 3 orange LEDs on the Traduci are on. Confirm that the SUT's Bluetooth radio is powered on and that the appropriate radio(s) are correctly plugged in to the Traduci. Currently the RN42 radios can **only** be plugged into JB. Simlarly the Bluefruit radio can **only** be plugged into JC. More detailed information on setting up can be found [here](testing-BTP-setup.md).

Information and purchasing information for supported radios can be found [here](testing-BTP-hw.md).

### Running the Pairing Tests ##

Navigate to the folder where the BTP package was extracted. It will typically be under `C:\BTP`. In a folder named after the version of the package, you will find the scripts referenced below. Then run either:

- `RunPairingTests.bat <radio name>` from an elevated command prompt or
- `RunPairingTests.ps1 <radio name>` from an elevated PowerShell console

Information on available radio name parameters can be found [here](testing-BTP-hw.md#supported-radios)

You can also include the optional parameter `-VerboseLogs` at the end to get a more verbose output of inner operations of BTP.

As a test starts the red LED next to the 12 pin adapter will turn on once the command from the test to power the radio has been sent. This LED will be turned off at the end of every test. If it is on at the start of the next test due the previous test failing, we will attempt to power it down and power it back on to return it to a known state. If the power cycle fails, the test will fail due to the radio being in an unknown state.

### Capturing Logs ###

To capture the Bluetooth logs, follow the instructions at https://aka.ms/BluetoothTracing.

### Known issues ###
- Stress tests: If a test is run in a tight loop using an LE radio it may hit a problem that can cause pairing or unpairing to fail.