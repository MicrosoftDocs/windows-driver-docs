---
title: Microsoft Bluetooth Test Platform - Human Device Adapter
description: Bluetooth Test Platform (BTP) Human Device Adapter (HDA) Setup and Pairing 
ms.date: 11/13/2020
ms.localizationpriority: medium

---

# Bluetooth Test Platform - Human Device Adapter

The Human Device Adapter (HDA) is a do-it-yourself way to manually interact with [Bluetooth Test Platform (BTP)](testing-BTP-Overview.md), allowing use of devices with BTP that have not yet been automated. For example, the HDA would make it possible to interact with a purchased headset that otherwise has no clear way to connect to BTP. The HDA enables manual user testing between a Windows Device and your prototyping hardware without the use of external hardware, such as Traduci. As such, all that is required to set up is a PC that supports Bluetooth and your own test device.  

## HDA set-up

Install the software as described in [BTP Software Setup](testing-BTP-setup.md#software-setup) to support the HDA.

## HDA configuration file

<<<<<<< HEAD
Create a configuration file named after your test device. For example: Sarah_Phone.txt 

Note: The name of the file does not matter. 

Contents of the Configuration File: 

```
name=Sarah_Phone
baseband=BR
br_address=B4:F1:DA:96:C0:A4
=======
Create a configuration file as below named after your test device, for example: *mytestdevice.txt*. **Note** neither the name of the file nor the extension is important.

```console
sink=hda
source=windows
name=mytestdevice
baseband=le
le_address=40ca6ca8e7ce (or 40:ca:6c:a8:e7:ce)
>>>>>>> 0b391513895054714e787989f7799b6b0301b71c
```

## HDA audio tests

<<<<<<< HEAD
`RunPairingTests.bat HDA,conf_file=<configuration file name>` from an elevated command prompt  
=======
Navigate to the folder where the BTP software package was extracted, typically `C:\BTP`. The scripts referenced below will be in a subfolder of the package directory. Run the appropriate script for the desired command environment:
>>>>>>> 0b391513895054714e787989f7799b6b0301b71c

| Command environment | Script |
| --- | --- |
| Elevated command prompt | `RunAudioTests.bat HDA,conf_file=<configuration file name>` |
| Elevated PowerShell console | `RunAudioTests.ps1 HDA,conf_file=<configuration file name>` |

<<<<<<< HEAD
`RunPairingTests.ps1 HDA,conf_file=<configuration file name>` from an elevated PowerShell console 

You can also include the optional parameter `-VerboseLogs` at the end to get a more verbose output of inner operations of BTP to assist with debugging failures locally. 
=======
The optional parameter `-VerboseLogs` can be added to provide a more verbose output of inner operations of BTP to assist with debugging.

## HDA manual pairing
>>>>>>> 0b391513895054714e787989f7799b6b0301b71c

1. The script will respond as below and ask if the device has been paired before. If 'y' is entered it will delete the pairing; if 'n' is entered the process will continue with no action.

    ```console
     [BluetoothTestHelpers::AudioDevice::AudioDevice]: Using remote device named: MyTestDevice
     Is MyTestDevice paired to the device with address D83BBFAC3207 Public?
     Enter (y/n):
    ```

<<<<<<< HEAD
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
=======
    Below is an example of the HDA deleting the pairing. It will prompt to also delete any pairing information on the device (here named “MyTestDevice”). Press any key to continue once any pairing information has been deleted.

    ```console
    [BluetoothTestHelpers::Pairing::Unpair]: Unapiring device with address D83BBFAC3207 Public from the device with address GA0DGC9C4893 Public
    If possible, delete the pairing on MyTestDevice
    Press any key to continue
    ```

2. The script then begins the pairing process by running checks and then prompting the user to enter their device (here named “MyTestDevice”) into "*Band* Pairing Mode”. Press any key to continue once this has been done.

    ```console
    [BluetoothTestHelpers::AudioDevice::AudioDevice]: Will attempt an outgoing pairing to the remote device and validate that a JustWorks Ceremony was used
    [BluetoothTestHelpers::Pairing::Pair]: Asserted: (originDeviceAssociationModule) != nullptr
    [BluetoothTestHelpers::Pairing::Pair]: Asserted: originDeviceAssociationModule->CanInitiatePairing()
    [BluetoothTestHelpers::Pairing::Pair]: Asserted: originDeviceAssociationModuleCanCheckPairingStatus()
    [BluetoothTestHelpers::Pairing::Pair]: Asserted: !(originDeviceAssociationModule->IsPairedTo(destinationDeviceAddress))
    If not already, put MyTestDevice in LE pairing mode.
    Press any key to continue . . .
    ```

3. The script will then initiate pairing. If pairing was successful the output will look exactly as below. Respond to any notifications on the device or on the test PC to confirm and finish pairing. The script then prompts the user to take their device out of pairing mode. Press any key to continue once this has been done.
>>>>>>> 0b391513895054714e787989f7799b6b0301b71c

    ```console
    [BluetoothTestHelpers::AudioDevice::Pairing::Pair]:Initiating Pairing request from device with address D83BBFAC3207 Public to device with address GA0DGC9C4893 Public
    [BluetoothTestHelpers::Pairing::DefaultPairingCeremonyHandler::OnJustWorks]: JustWorks ceremony used
    BluetoothTestHelpers::Pairing::Pair]: Asserted: originDeviceAssociationModule->IsPairedTo(destinationDeviceAddress)
    [BluetoothTestHelpers::Pairing::Pair]: Asserted: ceremonyHandler.GetLastCeremonyUsed().has_value()
    [BluetoothTestHelpers::Pairing::Pair]: Asserted: ceremonyHandler.GetLastCeremonyUser().value() == expectedCeremony
    [BluetoothTestHelpers::Pairing::Pair]: Paired successfully
    If the device is in pairing mode, exit pairing mode if possible.
    Press any key to continue . . .
    ```

4. After pairing is complete the script continues onto the tests available in the test suite. Documentation on available tests and how to run them can be found in [Currently supported BTP tests](testing-BTP-Tests.md)

## HDA log capture

If problems are encountered, Bluetooth logs can be captured Bluetooth logs by following instructions at [Busiotools for Windows Repo on GitHub for Log Capturing](https://github.com/Microsoft/busiotools/tree/master/bluetooth/tracing), or the `-VerboseLogs` option can be used when starting the tests.

## See also

[Bluetooth Test Platform Homepage](testing-BTP-Overview.md)

[Bluetooth Test Platform Software Setup](testing-BTP-setup.md#software-setup)

[Bluetooth Test Platform Available Tests](testing-btp-tests.md)

[Busiotools for Windows Repo on GitHub for Log Capturing](https://github.com/Microsoft/busiotools/tree/master/bluetooth/tracing)
