---
title: Microsoft Bluetooth Test Platform Setup
description: BTP setup
ms.date: 4/17/2019
ms.assetid: 85ac7c5b-b5f7-49e0-85f8-72e191c00974
ms.localizationpriority: medium

---

# Setting up BTP


### Setting up Traduci Hardware ###

Using the supplied USB A-to-B cable plug the Traduci into a USB port on the system under test (SUT). Performance is best if the Traduci is plgged directly into an A port on the PC and the Traduci is powered through the barrel connector to the right of the USB connector.  Do not connect the Traduci to a USB hub.

![Traduci showing USB and power ports](images/Traduci_USBPortSidejpg.jpg)

 Orient the Traduci so that LEDs and buttons are face up. Next orient the RN42 radio sled such that the printed label on the radio containing the MAC address is face up. Keeping this orientation, plug the RN42 radio in the 12 Pin port labeled JB.

#### Getting TAEF ####

Follow the instructions to download TAEF from [**docs.microsoft.com**](https://docs.microsoft.com/en-us/windows-hardware/drivers/taef/getting-started)

To enable the use of the scripts for running tests, copy the TAEF binaries to:

- `c:\Taef`

#### Getting BTP binaries ####

Download the test binaries from link
  
Extract the files from the zip file to:
- `c:\BTP`

### Setting up the System ###

- Disable secure boot (if enabled) in order to enable test signing. From an elevated command line on the SUT, run `setup-test.bat` to enable test signing and to reboot the machine.

## Test Scripts ##

### Pairing Script ###

Once the system has rebooted, check that the green power indicator & the 3 orange LEDs on the Traduci are on. Confirm that the SUT's Bluetooth Radio is powered on. Then from an elevated command prompt, run `test-pair.bat` to run the pairing tests with the RN42.  

This script will check the firmware version to ensure that the latest version is present on the Traduci. If the version in the package is newer, the script will update it. Once the firmware has been checked, the pairing test will run. The red LED next to the 12 pin adapter will turn on once the command from the test to power the radio has been sent. This LED will be turned off at the end of every test. If it is on at the start of the next test due the previous test failing, we will attempt to power it down and power it back on to return it to a known state. If the power cycle fails, the test will fail due to the radio being in an unknown state.

### HID Script ##
Once the system has rebooted, check that the green power indicator & the 3 orange LEDs on the Traduci are on. Confirm that the SUT's Bluetooth Radio is powered on. Then from an elevated command prompt, run `test-hid.bat` to run the HID tests with the RN42.  

This script will check the firmware version to ensure that the latest version is present on the Traduci. If the version in the package is newer, the script will update it. Once the firmware has been checked, the HID test will run. The red LED next to the 12 pin adapter will turn on once the command from the test to power the radio has been sent. This LED will be turned off at the end of every test. If it is on at the start of the next test due the previous test failing, we will attempt to power it down and power it back on to return it to a known state. If the power cycle fails, the test will fail due to the radio being in an unknown state.

### Capturing Logs ###

To capture the Bluetooth logs, follow the instructions at https://aka.ms/BluetoothTracing.

### Support ###

Questions and comments about the tests should be sent to BTPSupport@microsoft.com.

#### Known issues ####

- Power: If the device is plugged into a non-powered hub or VCC is not able to supply 5V intermittent failures may be seen. Please remedy by using a powered USB hub or use a 9V AC-DC Barrel adapter.
