---
title: Microsoft Bluetooth Test Platform supported hardware
description: Bluetooth Test Platform (BTP) supported hardware.
ms.date: 06/09/2021
---

# Bluetooth Test Platform Hardware

## Test Execution hardware
The Bluetooth Test Platform (BTP) can validate Bluetooth scenarios with several different hardware platforms. 

* Retail devices and in-development can be validated using the [Human Device Adapter (HDA)](https://docs.microsoft.com/en-us/windows-hardware/drivers/bluetooth/testing-btp-human-device-adapter)
* Windows hardware and drivers can be validated with PC-to-PC testing.
* 3rd party peripherals can be validated with custom device adapters.
* Windows OS can be validated with the [Traduci board](https://docs.microsoft.com/en-us/windows-hardware/drivers/bluetooth/testing-btp-hw-Traduci) and specific peripherals. 

## Supported Peripherals

More information about officially supported devices can be reviewed at the following pages:

| Device | Capabilities | Parameter | Applicable tests | Sample cmd line |
| --- | --- | --- | --- | --- |
| [RN42](testing-BTP-hw-rn42.md) | Bluetooth Basic Rate (BR) radio | rn42 | pairing, HID, audio HID scenario, Wi-Fi coexistence, power states | RunPairingTests.bat rn42 |
| [Bluefruit Feather](testing-BTP-hw-bluefruit-Feather.md) | Low Energy (LE) radio | bluefruit52 |  pairing, HID, audio HID scenario, battery, Wi-Fi coexistence, power states | RunPairingTests.bat bluefruit52 |
| [Bluefruit Friend](testing-BTP-hw-bluefruit-Friend.md) | Low Energy (LE) radio | bluefruit | pairing, HID, audio HID scenario, battery, Wi-Fi coexistence | RunPairingTests.bat bluefruit |
| [RN52](testing-BTP-hw-rn52.md) | Bluetooth Basic Rate (BR) radio | rn52 | pairing, audio, audio HID scenario, Wi-Fi coexistence | RunPairingTests.bat rn52 |
| [BM62](testing-BTP-hw-bm62.md) | Dual Mode radio | bm62 | pairing, audio | RunPairingTests.bat bm62 |
| [BM64](testing-BTP-hw-bm64.md) | Dual Mode radio | bm64 | pairing, audio | RunPairingTests.bat bm64 |
| [ESP32](testing-BTP-hw-esp32.md) | Wi-Fi soft AP and server | esp32wifi | Wi-Fi coexistence | RunWiFiCoexScenarioTests.bat rn52 esp32wifi |
| [Human Device Adapter](testing-BTP-human-device-adapter.md) | BR, LE, Dual Mode | HDA | pairing, audio, audio HID scenario, battery | RunPairingTests.bat HDA |

## Power adapter

Some multi-radio tests and power tests may require an external power adapter for the Traduci as the USB will be unable to provide sufficient power for all devices. 

More information about power adapter requirements can be review on the [Power adapter](testing-BTP-hw-power-adapter.md) page.
