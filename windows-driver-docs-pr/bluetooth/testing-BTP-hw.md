---
title: Microsoft Bluetooth Test Platform supported hardware
description: Bluetooth Test Platform (BTP) supported hardware.
ms.date: 06/09/2021
ms.localizationpriority: medium
---

# Bluetooth Testing Platform supported hardware

The Bluetooth Test Platform (BTP) makes use of specialized hardware to make Bluetooth testing easier. The Traduci board enables software on a host device (like a PC) to communicate with external devices over a sideband.

For example, an LE pairing test requires a peripheral device to be powered on, have certain IO capabilities, and be advertising as connectable/discoverable before it can be paired to. The peripheral device has well defined commands that can make this happen, so the BTP software on the host sends these commands over USB to the Traduci which in turn routes it to the appropriate device. After successful completion of the commands, the BTP software would then proceed with the test by requesting that the host pair to the peripheral device which is now ready to accept the pairing.

In the above scenario the Traduci makes several things simpler: It is able to provide and cut-off power with the correct voltage to the devices, it can route different commands to different devices, and it will mediate this communication through the correct protocols and baud rate.

Additionally, it is important to note that BTP tests do not have a tight dependency on the Traduci. If other external hardware is needed for a test, the BTP is designed to allow easy extensibility to support that scenario.

## Traduci board

The Traduci board is produced by [MCCI](https://mcci.com/usb/dev-tools/model-2411/)

:::image type="content" source="images/Traduci_Overhead.jpg" alt-text="Photo of a Traduci board.":::

- 4 12-pin ports to support 4 devices simultaneously
- Able to route data to and from multiple devices simultaneously
- 3 FPGAs connected to ports JA, JB, and JC respectively
- Supports audio testing via the integrated audio codec
- Unlabeled pins can easily be statically assigned to HIGH or LOW depending on the needs of the device plugged into the port
- The Traduci does not currently support hardware handshaking using CTS and RTS

## Supported devices

More information about officially supported devices can be reviewed at the following pages:

| Device | Capabilities | Parameter | Applicable tests | Sample cmd line |
| --- | --- | --- | --- | --- |
| [RN42](testing-BTP-hw-rn42.md) | Bluetooth Basic Rate (BR) radio | rn42 | pairing, HID, audio HID scenario | RunPairingTests.bat rn42 |
| [Bluefruit Feather](testing-BTP-hw-bluefruit-Feather.md) | Low Energy (LE) radio | bluefruit52 |  pairing, HID, audio HID scenario, battery | RunPairingTests.bat bluefruit52 |
| [Bluefruit Friend](testing-BTP-hw-bluefruit-Friend.md) | Low Energy (LE) radio | bluefruit | pairing, HID, audio HID scenario, battery | RunPairingTests.bat bluefruit |
| [RN52](testing-BTP-hw-rn52.md) | Bluetooth Basic Rate (BR) radio | rn42 | pairing, audio, audio HID scenario, Wi-Fi coexistence | RunPairingTests.bat rn52 |
| [BM64](testing-BTP-hw-bm64.md) | Dual Mode radio | bm64 | pairing, audio, audio HID scenario | RunPairingTests.bat bm64 |
| [ESP32](testing-BTP-hw-esp32.md) | Wi-Fi soft AP and server | esp32wifi | Wi-Fi coexistence | RunWiFiCoexScenarioTests.bat rn52 esp32wifi |
| [Human Device Adapter](testing-BTP-human-device-adapter.md) | BR, LE, Dual Mode | HDA | pairing, audio, audio HID scenario, battery | RunPairingTests.bat HDA |
