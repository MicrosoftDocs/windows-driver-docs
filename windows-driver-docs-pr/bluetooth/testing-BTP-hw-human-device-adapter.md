---
title: Microsoft Bluetooth Test Platform - Human Device Adapter
description: Bluetooth Test Platform (BTP) Human Device Adapter (HDA) Setup and Pairing 
ms.date: 01/10/2024
---

# Human Device Adapter

The Human Device Adapter (HDA) is a do-it-yourself way to manually interact with [Bluetooth Test Platform (BTP)](testing-BTP-Overview.md), allowing use of devices with BTP that haven't yet been automated. For example, the HDA would make it possible to interact with a purchased headset that otherwise has no clear way to connect to BTP. The HDA enables manual user testing between a Windows Device and your prototyping hardware without the use of external hardware, such as Traduci. As such, all that is required to set up is a PC that supports Bluetooth and your own test device.  

## HDA set-up

Install the software as described in [BTP Software Setup](testing-btp-setup-software.md) to support the HDA.

## HDA configuration file

Create a configuration file named after your test device, for example: *mytestdevice.txt*. The filename and extension aren't important. The configuration file should contain the following information:

```console
name=myTestDevice
baseband=BR
br_address=B4:F1:DA:96:C0:A4
```

## HDA pairing tests

Navigate to the folder where the BTP software package was extracted, typically `C:\BTP`. The scripts are in a subfolder of the package directory. Run the appropriate script for the desired command environment:

| Command environment | Script |
| --- | --- |
| Elevated command prompt | `RunPairingTests.bat HDA,conf_file=<configuration file name>` |
| Elevated PowerShell console | `RunPairingTests.ps1 HDA,conf_file=<configuration file name>` |

The optional parameter `-VerboseLogs` can be added to provide a more verbose output of inner operations of BTP to assist with debugging.

## HDA manual pairing

1. The script asks if the device has been paired before. If you respond with **y**, the script deletes the pairing. If you respond with **n**, the process continues with no action.

    ```console
    Verify: SUCCEEDED(WEX::TestExecution::RuntimeParameters::TryGetValue(deviceParameterName.c_str(), deviceParametersStr)): Getting required runtime parameter 'central'
    [BluetoothTests::PairingTestsImpl::PairingTestsImpl]: Using central device named: MyCentralDevice
    [BluetoothTests::PairingTestsImpl::PairingTestsImpl]: Using peripheral device named: MyTestDevice
    [BluetoothTestHelpers::Pairing::Unpair]: Unpairing device with address B4F1DA96C0A4 from the device with address D83BBFAC35607
    [BluetoothTestHelpers::Pairing::Unpair]: Unpaired successfully
    [BluetoothTestHelpers::Pairing::WaitForDisconnection]: Waiting for disconnection of device with address B4F1DA96C0A4
    [BluetoothTestHelpers::Pairing::WaitForDisconnection]: Asserted: connectionModule.WaitForDisconnection(otherDeviceAddress, c_disconnectionAfterUnpairingTimeout)
    [BluetoothTestHelpers::Pairing::WaitForDisconnection]: Disconnected successfully
    Is MyTestDevice paired to the device with address D83BBFAC35607?
    Enter (y/n): y
    ```

    The following example shows the HDA deleting the pairing. It also prompts you to delete any pairing information on the device (here named "MyTestDevice"). Press any key to continue once any pairing information has been deleted.

    ```console
    [BluetoothTestHelpers::Pairing::Unpair]: Unpairing device with address D83BBFAC35607 Public from the device with address D83BBFAC35607 Public
    If possible, delete the pairing on MyTestDevice
    Press any key to continue
    ```

1. The script then begins the pairing process by running checks, then prompting the user to enter their device (here named "MyTestDevice") into "*Band* Pairing Mode". After putting the device in pairing mode, press any key to continue.

    ```console
    StartGroup: BluetoothTests::TaefPairingTests::OutgoingJustWorksPairingTest
    [BluetoothTests::PairingTestsImpl::OutgoingJustWorksPairingTest]: Will attempt an outgoing pairing to the peripheral device and validate that a JustWorks ceremony was used
    [BluetoothTestHelpers::Pairing::Pair]: Asserted: (originDeviceAssociationModule) != nullptr
    [BluetoothTestHelpers::Pairing::Pair]: Asserted: originDeviceAssociationModule->CanInitiatePairing()
    [BluetoothTestHelpers::Pairing::Pair]: Asserted: originDeviceAssociationModule->CanCheckPairingStatus()
    [BluetoothTestHelpers::Pairing::Pair]: Asserted: !(originDeviceAssociationModule->IsPairedTo(destinationDeviceAddress))
    If not already, put MyTestDevice in BR pairing mode
    Press any key to continue . . .
    ```

1. The script initiates pairing. If pairing is successful, you see the following the output. Respond to any notifications on the device or on the test PC to confirm and finish pairing. The test then prompts you to take the device out of pairing mode. After you to take the device out of pairing mode, press any key to continue.

    ```console
    [BluetoothTestHelpers::Pairing::Pair]: Initiating pairing request from device with address D83BBFAC35607 to device with address B4F1DA96C0A4
    [BluetoothTestHelpers::Pairing::DefaultPairingCeremonyHandler::OnJustWorks]: JustWorks ceremony used
    [BluetoothTestHelpers::Pairing::Pair]: Asserted: originDeviceAssociationModule->IsPairedTo(destinationDeviceAddress)
    [BluetoothTestHelpers::Pairing::Pair]: Asserted: ceremonyHandler.GetLastCeremonyUsed().has_value()
    [BluetoothTestHelpers::Pairing::Pair]: Asserted: ceremonyHandler.GetLastCeremonyUsed().value() == expectedCeremony
    [BluetoothTestHelpers::Pairing::Pair]: Paired successfully
    If the device is in pairing mode, exit pairing mode if possible.
    Press any key to continue . . .
    ```

1. After pairing is complete, the script continues onto the tests available in the test suite. Documentation on available tests and how to run them can be found in [Currently supported BTP tests](testing-BTP-Tests.md)

## HDA log capture

If problems are encountered Bluetooth logs can be captured Bluetooth logs by following instructions at [Busiotools for Windows Repo on GitHub for Log Capturing](https://github.com/Microsoft/busiotools/tree/master/bluetooth/tracing), or by using the script option `-VerboseLogs` when starting the tests.

## See also

- [Bluetooth Test Platform Homepage](testing-BTP-Overview.md)
- [Bluetooth Test Platform Software Setup](testing-btp-setup-software.md)
- [Bluetooth Test Platform Available Tests](testing-btp-tests.md)
- [Busiotools for Windows Repo on GitHub for Log Capturing](https://github.com/Microsoft/busiotools/tree/master/bluetooth/tracing)
