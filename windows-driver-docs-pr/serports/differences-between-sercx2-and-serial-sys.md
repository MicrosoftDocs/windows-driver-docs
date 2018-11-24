---
title: Differences Between SerCx2.sys and Serial.sys
description: Although the inbox Sercx2.sys and Serial.sys driver components both implement the serial I/O request interface, these components are not interchangeable. They are designed to meet different sets of requirements.
ms.assetid: 62FA69BB-FE04-4B5E-96CC-13764ED83AE6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Differences Between SerCx2.sys and Serial.sys


Although the inbox Sercx2.sys and Serial.sys driver components both implement the [serial I/O request interface](serial-i-o-request-interface.md), these components are not interchangeable. They are designed to meet different sets of requirements.

**Note**  Sercx2.sys replaces an earlier version of the serial framework extension, Sercx.sys, that was introduced in Windows 8. For more information, see [Serial Controller Drivers Overview](serial-drivers-overview.md).

 

## Serial.sys: Dynamic serial connections to external devices


Serial.sys is designed to control named COM ports that are driven by 16550A or similar UARTs. External peripheral devices can be dynamically plugged into and removed from these ports. Serial.sys is present in all supported versions of Windows, and many existing applications and drivers that use COM ports depend on the known behavior of Serial.sys. A client opens a COM port by name (for example, "COM1") and releases the port when it is no longer needed.

Serial.sys uses programmed I/O (PIO) instead of DMA to transmit and receive data through a serial port. The chief reason for using PIO is that the PC lacks a suitable system DMA controller. Although Serial.sys can be used to control serial ports on PCI or PCIe serial adapter cards, it is primarily designed to control UARTs on PC motherboards. These UARTs are subordinate devices that do not have built-in master DMA controllers. In principle, Serial.sys could use the system DMA controller, but, in a PC, this controller is an 8237 device with limited capabilities. A multiport board, which implements several serial ports, might contain a master DMA controller, but the hardware vendor for the board must write a custom serial driver to exploit these DMA capabilities.

Data transmission through a COM port on a PC is relatively slow and can be adequately handled by PIO. The speed at which the COM ports managed by Serial.sys can be driven is limited by the impedance and other electrical properties of the connectors and external cables that attach to these ports.

## Sercx2.sys: Dedicated serial connections between integrated circuits


Serial interfaces are now widely used to provide low-pin-count communication between integrated circuits on a printed circuit board. Data transmission rates through these interfaces can be relatively high due to the low impedance and short path lengths involved. Using PIO to move data to and from serial ports at these high data rates places too great a burden on the processor. Instead, DMA is needed to offload this work from the processor.

Sercx2.sys is designed to work with dedicated serial ports that are permanently connected to peripheral devices and that support high data rates. Unlike Serial.sys, Sercx2.sys can make use of the advanced capabilities of DMA controllers in SoC-based hardware platforms. These DMA controllers can do complex data transfers with little or no processor intervention.

Sercx2.sys is available across all versions of Windows, starting with Windows 8.1, but is widely used in hardware platforms that contain System on a Chip (SoC) integrated circuits and that run Windows RT. In these platforms, SoC chips contain 16550D or similar UARTs whose serial ports connect to off-chip peripheral devices. These peripheral devices reside inside the case of a mobile device such as a smart phone or a tablet computer, and might be soldered to the same board as the SoC chip. A serial port that is permanently connected to a peripheral device is assigned as a dedicated hardware resource to the driver for this device. Typically, only drivers—and not applications—send I/O requests directly to a serial controller that is managed by Sercx2.sys and an associated serial controller driver.

Sercx2.sys is flexible in its support for DMA. Complex data transfers that use system DMA are fully supported. In addition, Sercx2.sys provides an optional custom transfer mode to support, for example, a serial controller that has built-in bus-master DMA capability. Finally, DMA support is optional and need not be implemented by a serial controller that handles lower data rates for which PIO is sufficient.

## Other differences


A COM port controlled by Serial.sys is assigned a device name. A user-mode application can open this port by name, and then send I/O requests directly to the port.

In contrast, a serial port controlled by SerCx2.sys and a serial controller driver is unnamed. The driver that owns the peripheral device that is permanently connected to the port receives a special identifier (called a [*connection ID*](connection-ids-for-serially-connected-peripheral-devices.md)) that the driver uses to open the port. Typically, only this peripheral driver can send I/O requests directly to the port. An application that needs to configure the port or to transfer data through the port sends I/O requests to the peripheral driver. Then, acting as intermediary, this driver sends the corresponding I/O requests to the port.

Sercx2.sys and its associated serial controller driver enable the run-time [power management framework](https://msdn.microsoft.com/library/windows/hardware/hh406637) (PoFx) to manage power in serial controllers and in the peripheral devices that are connected to these controllers. PoFx, which is available starting with Windows 8, provides fine-tuned power management to enable mobile devices to run for extended periods on a battery charge.

In contrast, Serial.sys is not managed by PoFx, and instead relies on device power management capabilities that are supported in earlier versions of Windows.

Another difference is that Serial.sys implements software flow control, but Sercx2.sys does not. Both Serial.sys and Sercx2.sys support hardware flow control using the *request to send* (RTS) and *clear to send* (CTS) signals. For more information about flow control, see [**SERIAL\_HANDFLOW**](https://msdn.microsoft.com/library/windows/hardware/jj680685).

A final difference is that Serial.sys can work in conjunction with Serenum.sys, but Sercx2.sys cannot. Serenum.sys is a filter driver that enumerates devices that are connected to serial ports. For more information, see [Enumerating Serenum Devices](enumerating-serenum-devices.md).

 

 




