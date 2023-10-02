---
title: Hardware setup for Bluetooth Test Platform
description: How to set up hardware for the Microsoft Bluetooth Test Platform
ms.date: 10/02/2023
---

# Hardware setup for Bluetooth Test Platform

For a full list of supported peripherals and further links to any peripheral specific setup, refer to [Supported Hardware](testing-BTP-hw.md). Use the hardware setup process for the peripheral you're using for your test pass.

## Human Device Adapter (HDA)

The HDA allows you to test with various peripherals. These peripherals could be off-the-shelf, development-stage peripherals, development boards, or a Windows PC. Run the tests on your host machine and manually manipulate the remote device when prompted. You don't need to do anything specific to set up the remote device. You can proceed to the [Software Setup](testing-BTP-setup-software.md) section.

## BM64EVB, Bluefruit 52

These devices connect to the system under test (SUT) directly using a USB cable and not through the Traduci. Refer to the specific peripheral page for further hardware setup.

## RN42, RN52, Bluefruit, BM62

These devices connect to the Traduci, which then connects to the PC.

### Connecting Traduci to the PC

Using the supplied USB A-to-B cable, plug the Traduci into a USB port on the system under test (SUT). Performance is best if the Traduci is plugged directly into an A port on the PC. Power the Traduci with a [9v, 2A power adapter](https://www.digikey.com/product-detail/en/qualtek/QFWB-18-9-US01/Q1181-ND/8260129) through the barrel connector to the right of the USB connector. Don't connect the Traduci to a USB hub.

:::image type="content" source="images/Traduci_USBPortSidejpg.jpg" alt-text="Angled side-view of Traduci circuit board displaying USB and power ports.":::

### Connecting peripherals to the Traduci

The Traduci has four 12-pin ports (labeled JA, JB, JC, JD) used for test peripherals.

:::image type="content" source="images/Traduci_12PinPortSide.jpg" alt-text="Photo of a Traduci circuit board with four 12-pin ports labeled JA, JB, JC, and JD.":::

To plug a peripheral device into a port on the Traduci, orient the Traduci so that LEDs and buttons are face up. Next orient the device sled such that the printed label on the device containing the MAC address and any switches are face up. Keeping this orientation, plug the peripheral device in the appropriate 12-pin port.

> [!NOTE]
> Some peripherals may only plug into certain ports. For more information, see to the [supported hardware page](testing-BTP-hw.md).

:::image type="content" source="images/Traduci_and_DigilentRN42.jpg" alt-text="Traduci circuit board with a peripheral device connected to one of the 12-pin ports.":::

## Known issues

- Power: Intermittent failures may be seen if VCC isn't able to supply a steady 5V. In these cases, use a 9V AC-DC barrel adapter. These issues are more common during tests utilizing more than one device.
