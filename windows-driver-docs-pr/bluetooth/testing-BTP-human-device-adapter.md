---
title: Microsoft Bluetooth Test Platform - Human Device Adapter
description: Bluetooth Test Platform (BTP) Human Device Adapter (HDA) Setup and Pairing 
ms.date: 11/13/2020
ms.localizationpriority: medium

---

# Human Device Adapter 

The Human Device Adapter (HDA) is a do-it-yourself way to manually interact with [Bluetooth Test Platform](testing-BTP-Overview.md) . This device adapter was created to allow you to use hardware with BTP that has not yet been automated. For example, a store-bought headset without a clear way to connect into BTP would be a great candidate for using the HDA. This document will walk users through how to use the HDA with their hardware. 

## Setup for Testing With the HDA 

To start working with BTP and the HDA, install the necessary software as described in [BTP Software Setup](testing-BTP-setup.md#software-setup) . 
 
The HDA enables manual user testing between a Windows Device and your prototyping hardware without the use of external hardware, such as Traduci. As such, all that is required to set up is a PC that supports Bluetooth and your own test hardware.  

## HDA Configuration File Step by Step 

Create a configuration file named after your test device. For example: Sarah_Phone.txt 

Note: The name of the file does not matter. 

Contents of the Configuration File: 

```
name=Sarah_Phone
baseband=BR
br_address=B4:F1:DA:96:C0:A4
```
## Running Audio Tests with the HDA 

Navigate to the folder where the BTP package was extracted. It will typically be under C:\BTP. In a folder named after the version of the package, you will find the scripts referenced below. Then run either: 

`RunPairingTests.bat HDA,conf_file=<configuration file name>` from an elevated command prompt  

or 

`RunPairingTests.ps1 HDA,conf_file=<configuration file name>` from an elevated PowerShell console 

You can also include the optional parameter `-VerboseLogs` at the end to get a more verbose output of inner operations of BTP to assist with debugging failures locally. 

## HDA Manual Pairing Step by Step 

### Step 1 

```bash
Verify: SUCCEEDED(WEX::TestExecution::RuntimeParameters::TryGetValue(deviceParameterName.c_str(), deviceParametersStr)): Getting required runtime parameter 'central'
[BluetoothTests::PairingTestsImpl::PairingTestsImpl]: Using central device named: MyTestDevice
[BluetoothTests::PairingTestsImpl::PairingTestsImpl]: Using peripheral device named: Sarahs_Phone
[BluetoothTestHelpers::Pairing::Unpair]: Unpairing device with address B4F1DA96C0A4 from the device with address D83BBFAC35607
[BluetoothTestHelpers::Pairing::Unpair]: Unpaired successfully
[BluetoothTestHelpers::Pairing::WaitForDisconnection]: Waiting for disconnection of device with address B4F1DA96C0A4
[BluetoothTestHelpers::Pairing::WaitForDisconnection]: Asserted: connectionModule.WaitForDisconnection(otherDeviceAddress, c_disconnectionAfterUnpairingTimeout)
[BluetoothTestHelpers::Pairing::WaitForDisconnection]: Disconnected successfully
Is Sarahs_Phone paired to the device with address D83BBFAC35607?
Enter (y/n): y
```

- The test will then ask if the device has been paired before. If “y” is entered it will delete the pairing. If “n” the process will continue with no action. 
 
```bash
[BluetoothTestHelpers::Pairing::Unpair]: Unapiring device with address D83BBFAC35607 Public from the device with address D83BBFAC35607 Public
If possible, delete the pairing on MyTestDevice
Press any key to continue
```

- Here is an example of the HDA deleting the pairing. It will prompt you to also delete any pairing information on the device (here named “MyTestDevice”). Press any key to continue once any pairing information has been deleted. 

### Step 2 

```
StartGroup: BluetoothTests::TaefPairingTests::OutgoingJustWorksPairingTest
[BluetoothTests::PairingTestsImpl::OutgoingJustWorksPairingTest]: Will attempt an outgoing pairing to the peripheral device and validate that a JustWorks ceremony was used
[BluetoothTestHelpers::Pairing::Pair]: Asserted: (originDeviceAssociationModule) != nullptr
[BluetoothTestHelpers::Pairing::Pair]: Asserted: originDeviceAssociationModule->CanInitiatePairing()
[BluetoothTestHelpers::Pairing::Pair]: Asserted: originDeviceAssociationModule->CanCheckPairingStatus()
[BluetoothTestHelpers::Pairing::Pair]: Asserted: !(originDeviceAssociationModule->IsPairedTo(destinationDeviceAddress))
If not already, put Sarahs_Phone in BR pairing mode
Press any key to continue . . .
```

- The test then begins the pairing process by running a few checks. Next, the test prompts the user to enter their device (here named “MyTestDevice”) into “<Band> Pairing Mode”. Press any key to continue once this has been done. 

### Step 3 

```bash
[BluetoothTestHelpers::Pairing::Pair]: Initiating pairing request from device with address D83BBFAC35607 to device with address B4F1DA96C0A4
[BluetoothTestHelpers::Pairing::DefaultPairingCeremonyHandler::OnJustWorks]: JustWorks ceremony used
[BluetoothTestHelpers::Pairing::Pair]: Asserted: originDeviceAssociationModule->IsPairedTo(destinationDeviceAddress)
[BluetoothTestHelpers::Pairing::Pair]: Asserted: ceremonyHandler.GetLastCeremonyUsed().has_value()
[BluetoothTestHelpers::Pairing::Pair]: Asserted: ceremonyHandler.GetLastCeremonyUsed().value() == expectedCeremony
[BluetoothTestHelpers::Pairing::Pair]: Paired successfully
If the device is in pairing mode, exit pairing mode if possible.
Press any key to continue . . .
```

- The test will then initiate pairing. If pairing was successful, the output will look exactly as above. Please respond to any notifications on the device or on the test PC to confirm and finish pairing. The test then prompts the user to take their device out of pairing mode. Press any key to continue once this has been done. 

After pairing, the test continues onto the tests available in the test suite. Documentation on available tests and how to run them can be found in [Currently supported BTP tests](testing-BTP-Tests.md)

## Capturing Logs 

If you encounter a problem with the Windows stack, please capture Bluetooth logs. To capture the logs, follow the instructions at  [aka.ms/BluetoothTracing](aka.ms/BluetoothTracing). Otherwise, use `-VerboseLogs` when starting the tests to receive more information about why a test failed. 

## Resources 

Bluetooth Test Platform Homepage - [aka.ms/btp](testing-BTP-Overview.md)

[Bluetooth Test Platform Software Setup](testing-BTP-setup.md#software-setup)

[Bluetooth Test Platform Available Tests](testing-btp-tests.md)

Busiotools for Windows Repo on GitHub for Log Capturing - [aka.ms/BluetoothTracing](aka.ms/BluetoothTracing)
