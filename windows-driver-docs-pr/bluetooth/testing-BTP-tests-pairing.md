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

First check that the green power indicator and the 3 orange LEDs on the Traduci are on. Confirm that the SUT's Bluetooth radio is powered on and that the appropriate radio(s) are correctly plugged in to the Traduci. More detailed information on this can be found [here](testing-BTP-setup.md).

At this time the only supported radios for HID tests are the RN42 and the Bluefruit. Purchasing information for the Traduci, RN42, Bluefruit, and future radios can be found [here](testing-BTP-supported-hardware.md).

### Running the Pairing Tests ##

Navigate to the folder where the BTP package was extracted. It will tipically be under `C:\BluetoothTestPlatform`. In a folder named after the version of the package, you will find the scripts referenced below. Then run either:

- `RunPairingTests.bat` from an elevated command prompt or
- `RunPairingTests.ps1` from an elevated PowerShell console

This will run the pairing tests with the RN42. The RN42 is a BR/EDR only radio.

You may also run tests with the Bluefruit radio. The Bluefruit is an LE only radio. After following the same precautions as the RN42 described above, run either:

- `RunPairingTests.bat bluefruit` from an elevated command prompt or
- `RunPairingTests.ps1 bluefruit` from an elevated PowerShell console

You can also include the optional parameter `-VerboseLogs` at the end to get a more verbose output of inner operations of BTP.

As a test starts the red LED next to the 12 pin adapter will turn on once the command from the test to power the radio has been sent. This LED will be turned off at the end of every test. If it is on at the start of the next test due the previous test failing, we will attempt to power it down and power it back on to return it to a known state. If the power cycle fails, the test will fail due to the radio being in an unknown state.

### Capturing Logs ###

To capture the Bluetooth logs, follow the instructions at https://aka.ms/BluetoothTracing.

### Known issues ###

- Power: If the device is plugged into a non-powered hub or VCC is not able to supply 5V intermittent failures may be seen. Please remedy by using a powered USB hub or use a 9V AC-DC Barrel adapter.

- Stress tests: If a test is run in a tight loop using an LE radio it may hit a problem that can cause pairing or unpairing to fail.