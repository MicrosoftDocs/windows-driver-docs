---
title: Microsoft Bluetooth Test Platform Setup
description: BTP setup
ms.date: 4/17/2019
ms.assetid: 85ac7c5b-b5f7-49e0-85f8-72e191c00974
ms.localizationpriority: medium

---

# Setting up BTP
## Hardware setup 
### Connecting Traduci to the PC 
Using the supplied USB A-to-B cable, plug the Traduci into a USB port on the system under test (SUT). Performance is best if the Traduci is plgged directly into an A port on the PC and the Traduci is powered through the barrel connector to the right of the USB connector.  Do not connect the Traduci to a USB hub.

![Traduci showing USB and power ports](images/Traduci_USBPortSidejpg.jpg)

### Connecting peripherals to the Traduci 
The Traduci has four 12 pin ports (labeled JA, JB, JC, JD) used for test peripherals.

![Traduci showing USB and power ports](images/Traduci_12PinPortSide.jpg)

To plug a peripheral radio into a port on the Tradui, orient the Traduci so that LEDs and buttons are face up. Next orient the peripheral radio (sled) such that the printed label on the radio containing the MAC address is face up. Keeping this orientation, plug the peripheral radio in the appropriate 12 Pin port.

> [!NOTE] 
> Some peripherals may only plug into certain ports.  Please refer to the supported hardware page for more information.

![Traduci with peripheral plugged in](images/Traduci_and_DigilentRN42.jpg)

## Software setup 
### Step 1 - Get TAEF

- Follow the instructions to download TAEF from [**docs.microsoft.com**](https://docs.microsoft.com/en-us/windows-hardware/drivers/taef/getting-started)
- Copy the TAEF binaries to `c:\Taef`.

### Step 2 - Getting BTP binaries 

- Download the [BTP software package](testing-BTP-software-package.md).  
- Extract the files from the zip file to `c:\BTP`.

### Step 3 - Setting up the System 

- Ensure secure boot is [disabled](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-secure-boot).
- From an elevated command line on the SUT, run `setup-test.bat` to enable test signing
- Reboot the machine under test.


## Known issues

- Power: If the device is plugged into a non-powered hub or VCC is not able to supply 5V intermittent failures may be seen. Please remedy by using a powered USB hub or use a 9V AC-DC Barrel adapter.
