---
title: Microsoft Bluetooth Test Platform Setup
description: How to set up the Microsoft Bluetooth Test Platform Setup 
ms.date: 06/09/2021
---

# Hardware Setup for BTP

For a full list of supported peripherals and further links to any peripheral specific setup, please refer to [Supported Hardware](testing-BTP-hw.md). Use the hardware setup process for the peripheral you will be using for your test pass.
<br><br>

## Human Device Adapter (HDA)
The HDA allows you to test with a variety of peripherals. These could be off-the-shelf peripherals, development-stage peripherals, development boards, or a Windows PC. You will run the tests on your host machine and manually manipulate the remote device when prompted. You do not need to do anything specific to set up the remote device. You can proceed to the [Software Setup](testing-BTP-setup-software.md) section.

<br><br>
## BM64EVB, Bluefruit 52
todo: add setup information

<br><br>
## RN42, RN52, Bluefruit, BM62
These devices connect to the Traduci which then connects to the PC.
### <b>Connecting Traduci to the PC</b>
Using the supplied USB A-to-B cable, plug the Traduci into a USB port on the system under test (SUT). Performance is best if the Traduci is plugged directly into an A port on the PC and the Traduci is powered by a [9v, 2A power adapter](https://www.digikey.com/product-detail/en/qualtek/QFWB-18-9-US01/Q1181-ND/8260129) through the barrel connector to the right of the USB connector. Do not connect the Traduci to a USB hub.

:::image type="content" source="images/Traduci_USBPortSidejpg.jpg" alt-text="An angled side-view of the Traduci circuit board showing USB and power ports.":::

### <b>Connecting peripherals to the Traduci</b>

The Traduci has four 12-pin ports (labeled JA, JB, JC, JD) used for test peripherals.

:::image type="content" source="images/Traduci_12PinPortSide.jpg" alt-text="Traduci showing USB and power ports.":::

To plug a peripheral device into a port on the Traduci, orient the Traduci so that LEDs and buttons are face up. Next orient the device sled such that the printed label on the device containing the MAC address and any switches are face up. Keeping this orientation, plug the peripheral device in the appropriate 12-pin port.

> [!NOTE]
> Some peripherals may only plug into certain ports.  Please refer to the [supported hardware page](testing-BTP-hw.md) for more information.

:::image type="content" source="images/Traduci_and_DigilentRN42.jpg" alt-text="Traduci with peripheral plugged in.":::

<br><br>
## Known issues

- Power: Intermittent failures may be seen if VCC is not able to supply a steady 5V. In these cases use a 9V AC-DC barrel adapter. These issues are more common during tests utilizing more than 1 device.
