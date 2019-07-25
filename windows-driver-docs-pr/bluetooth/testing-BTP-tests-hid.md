---
title: Microsoft Bluetooth Test Platform
description: Bluetooth Test Platform (BTP) overview.
ms.assetid: b5b039bb-af0f-446f-9657-aa0e137a3437
ms.date: 4/17/2019
ms.localizationpriority: medium

---

# Setup

The Bluetooth Test Platform (BTP) is a software package to for automating testing of bluetooth hardware & software. It can be used to exercise bluetooth radios in the host (inside the PC) and peripheral radios. 

The Bluetooth Test Platform (BTP) is the software component of Microsoft's latest automated Bluetooth testing. The Traduci is the hardware platform that the BTP runs on and supports peripheral radios to be plugged into it. The package consists of software tests, a firmware package, a provisioning tool  the Traduci board and a set of peripheral radios used for testing basic functionality.

As this time the only supported radio is the RN42. Purchasing information for the Traduci, RN42 and future radios can be found below.


### Running HID Tests ##
Once the system has rebooted, check that the green power indicator & the 3 orange LEDs on the Traduci are on. Confirm that the SUT's Bluetooth Radio is powered on. Then from an elevated command prompt, run `test-hid.bat` to run the HID tests with the RN42.  

This script will check the firmware version to ensure that the latest version is present on the Traduci. If the version in the package is newer, the script will update it. Once the firmware has been checked, the HID test will run. The red LED next to the 12 pin adapter will turn on once the command from the test to power the radio has been sent. This LED will be turned off at the end of every test. If it is on at the start of the next test due the previous test failing, we will attempt to power it down and power it back on to return it to a known state. If the power cycle fails, the test will fail due to the radio being in an unknown state.

### Interpreting Results ###

### Capturing Logs ###

To capture the Bluetooth logs, follow the instructions at https://aka.ms/BluetoothTracing.



#### Known issues ####

- Power: If the device is plugged into a non-powered hub or VCC is not able to supply 5V intermittent failures may be seen. Please remedy by using a powered USB hub or use a 9V AC-DC Barrel adapter.

- Stress tests: If the test is run in a tight loop there an issue where the radios will not have finished disconnecting after the pairing test reports success before the next test attempts to pair resulting in a failure.