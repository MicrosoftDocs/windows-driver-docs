---
title: Microsoft Bluetooth Test Platform
description: Bluetooth Test Platform (BTP) HID tests.
ms.assetid: b5b039bb-af0f-446f-9657-aa0e137a3437
ms.date: 4/17/2019
ms.localizationpriority: medium

---

# BTP HID Tests

The BTP HID tests will test the ability of the local system to pair with a remote radio over BR/EDR or LE and validate HID functionality.

### Setting Up ##

First check that the green power indicator, an optional yellow test LED, and 3 orange LEDs on the Traduci are on. Confirm that the SUT's Bluetooth radio is powered on and that the appropriate radio(s) are correctly plugged in to the Traduci. Currently the RN42 radio can **only** be plugged into JB. Simlarly the Bluefruit radio can **only** be plugged into JC. More detailed information on setting up can be found [here](testing-BTP-setup.md).

At this time the only supported radios for HID tests are the RN42 and Bluefruit. Purchasing information for the Traduci, RN42, Bluefruit, and future radios can be found [here](testing-BTP-hw.md).

### Running the HID Tests ##

Navigate to the folder where the BTP package was extracted. It will typically be under `C:\BTP`. In a folder named after the version of the package, you will find the scripts referenced below. Then run either:

- `RunHidTests.bat` from an elevated command prompt or
- `RunHidTests.ps1` from an elevated PowerShell console

This will run the HID tests with the RN42. The RN42 is a BR/EDR only radio.

You may also run tests with the Bluefruit radio. The Bluefruit is an LE only radio. After following the same precautions as the RN42 described above, run either:

- `RunHidTests.bat bluefruit` from an elevated command prompt or
- `RunHidTests.ps1 bluefruit` from an elevated PowerShell console

You can also include the optional parameter `-VerboseLogs` at the end to get a more verbose output of inner operations of BTP.

As a test starts the red LED next to the 12 pin adapter will turn on once the command from the test to power the radio has been sent. This LED will be turned off at the end of every test. If it is on at the start of the next test due the previous test failing, we will attempt to power it down and power it back on to return it to a known state. If the power cycle fails, the test will fail due to the radio being in an unknown state.

### Capturing Logs ###

To capture the Bluetooth logs, follow the instructions at https://aka.ms/BluetoothTracing.

### Known issues ###
- Stress tests: If a test is run in a tight loop using an LE radio it may hit a problem that can cause pairing or unpairing to fail.