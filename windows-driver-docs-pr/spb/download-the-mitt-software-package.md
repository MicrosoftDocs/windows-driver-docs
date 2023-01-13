---
title: Download the MITT software package
description: Download the MITT software package.
ms.date: 01/13/2023
---

# Download the MITT software package

The MITT software package contains several tools to be used to test simple peripheral buses such as I2C, SPI, and GPIO with the MITT board. The suite of tools include utilities to update firmware, send requests to simulate test cases, and test driver packages, test the functionality of the bus, its controller and devices connected to the bus.

**[Download the MITT software package](https://download.microsoft.com/download/7/7/0/7703F03C-9D1F-45FC-A625-9647DC495EE2/MITT.msi)**

## Tools in the software package

| Modules | Description |
|---|---|
| MuttUtil | MuttUtil.exe</br><ul><li>Sends requests to communicate with various programmable blocks on the MITT board, such as the GPIO, I2C, SPI interfaces.</li><li>Updates the firmware on the MITT board.</li></ul></br>MuttUtil.dll is the user mode library that sends requests to the MITT board, which are initiated by MuttUtil.exe. |
| MITTI2CTest.dll</br></br>MITTSPITest.dll</br></br>WITTTest driver package</br></br>SPBCmd.exe | <ul><li>MITTI2CTest.dll &mdash; Test binary for I2C controller and bus verification.</li><li>MITTSPITTest.dll &mdash; Test binary for SPI controller and bus that validates bus-level activity.</li><li>WITTTest driver package &mdash; Installation (.inf), catalog (.cat), and binary (.sys) for the test driver for devices connected to simple peripheral buses.</li><li>SPBCmd.exe &mdash; Sends requests to the test driver to manually validate data transfers over I2C and SPI buses.</li></ul> |
| WinUSB driver package | Installation (.inf), catalog (.cat), and binary (.sys) for the WinUSB driver required to update MITT firmware to run tests included in the MITT software package. |
| WDTFMittSimpleIoAction.dll</br></br>AudioUnitSimpleIo.dll</br></br>SimpleIO_MITT_Audio_Sample.vbs</br></br>GpioSimpleIoExtension.dll</br></br>SimpleIO_MITT_GPIO_Sample.vbs</br></br>McattSimpleIoExtension.dll</br></br>SimpleIO_MITT_MCATT_Sample.vbs | <ul><li>WDTFMittSimpleIoAction.dll is a helper module.</li><li>SimpleIO module for audio testing.</li><li>SimpleIO module for GPIO button testing.</li><li>SimpleIO module for MCATT testing.</li></ul> |

> [!NOTE]
> To run the VBS files, you must install Windows Device Testing Framework (WDTF). WDTF is installed with the Windows Driver Kit (WDK).

## Related topics

- [Get started with MITT](./get-started-with-mitt---.md)
