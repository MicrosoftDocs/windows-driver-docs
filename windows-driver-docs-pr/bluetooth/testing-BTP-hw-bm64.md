---
title: Microsoft Bluetooth Test Platform - BM-64-EVB board
description: Bluetooth Test Platform (BTP) supported hardware (BM64).
ms.date: 06/09/2021
ms.localizationpriority: medium
---

# BM-64-EVB board

## Overview

The BM64 is a dual-mode Bluetooth v5.0 radio designed for use in headsets, speakers, or multi-speaker peripherals. More information can be found via the BM64 page from [**Microchip Technology Incorporated**](https://www.microchip.com/wwwproducts/en/BM64). The BM-64-EVB allows the BM64 to be utilized as a stand-alone device, allowing for connection to a test machine without the need for a Traduci. More information can be found via the BM-64-EVB page from [**Microchip**](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/BM-64-EVB-C2).

| Device Name | Parameter | Usage Example |
| --- | --- | --- |
| BM64 | bm64 | RunPairingTests.bat bm64 |

:::image type="content" source="images/BM64.png" alt-text="Photo of the BM64 device.":::

## Supported tests

- [Pairing tests](testing-BTP-tests-pairing.md)
- [Audio tests](testing-BTP-tests-audio.md)
- [Audio & HID tests](testing-BTP-tests-audio-hid.md) (as an audio device)

## Required Hardware

The BM-64-EVB-C2 can be purchased via [DigiKey](https://www.digikey.com/en/products/detail/microchip-technology/BM-64-EVB-C2/6152245).

> [!NOTE]
> The BM-64-EVB development occurred with the Class 2 stereo audio module version (BM-64-EVB-C2) but should be compatible with the Class 1 audio module (BM-64-EVB-C1).

### BM64 Device on BM64 Evaluation Board

:::image type="content" source="images/BM64-EVB-alpha.png" alt-text="Photo of the BM-64-EVB.":::

## Getting Started

> [!CAUTION]
> Before powering on the board via USB or barrel connector, remove the jumper on JP33, if it is installed. Failure to do so may result in a boot loop that prevents enumeration during future power ups and may render the board unusable for the purposes of BTP testing.

In order to use the BM-64-EVB with BTP, the firmware and EEPROM settings for the BM64 must be updated from the factory default. Additionally, the PIC microcontroller should also be updated to ensure stability.

Download and extract the newest BM64 software kit from [**Microchip**](https://www.microchip.com/wwwproducts/en/BM64) on the *Documents/Software Libraries/Firmware* tab (DSPK v2.1.3 was used for this development).

Some configuration notes before starting:

- For using external MCU / PC control **(For running BM64 firmware, EEPROM updates, BTP tests)**
  - SW13 should have all positions switched to OFF
  - SW46 should have all positions switched to OFF
  - SW47 should have all positions switched to OFF
- For using internal MCU control **(For running stand-alone Microchip examples)**
  - SW46 should have all positions switched to ON except for #2
  - SW47 should have all positions switched to ON
- JP33 should be connected **ONLY** if uploading new firmware to the PIC microcontroller.
- SW9 should be configured based on the current goal

| Goal | 1 State | 2 State |
| --- | --- | --- |
| Run Application (BTP Tests) | OFF | OFF |
| Upload new firmware to BM64 | ON | ON |
| Upload new EEPROM to BM64 | ON | OFF |

> [!NOTE]
>
> - All firmware and EEPROM files should come from the **same** software package.
> - When running the tools included in the DSPK, a Microsoft Defender SmartScreen notification of running the app putting your PC at risk may appear the first time it is run.
> Click *More Info* and then *Run anyway*.

## Flashing Firmware for the BM64

This section will explain how to upload new firmware for the BM64. The `isupdate.exe` tool (found at `DSPK v2.x.y Package\Tools\FlashUpdate Tool`) will be used to upload new hex files to the BM64.

1. Set SW9 position 1 and 2 to both ON and ensure JP33 is removed.
1. Plug the Micro-B USB cable into P3 (labeled *UART* on the EVB).
1. Start the `isupdate.exe` tool and select the COM port associated with the BM-64-EVB (use `Device Manager` and look for *Ports (COM & LPT)*).
1. The settings should be a *baud rate* set to *115200*, *image num* set to *16*, *memory* set to *flash*, *subtype* set to *Serial Flash*. After being set, click *Connect*.
     - If the connection is correct, then *Device* on the right should be populated with information and *Port connect -> COM#* should be in the bottom pane. It should look like the image below (with corresponding COM ports).
     - The given *baud rate* only applies to the default device for this example. If EEPROM changes have occured to modify the baud rate of the BM64, use that new value instead.

        :::image type="content" source="images/btp-bm64-isupdate.png" alt-text="Photo of the isUpdate tool after connection.":::

1. Click *Browse* and navigate to the BM64 hex files in the DSPK (found at `DSPK v2.x.y Package\Software\Firmware Image\BM64 Firmware`). Highlight all 16 files (`BT5506_SHS_FLASH.H00` through `BT5506_SHS_FLASH.H15`) simultaneously and click *Open*.
1. Click *Update* to update the BM64's firmware. The bottom pane will show progress as the update occurs. **DO NOT INTERRUPT THIS PROCESS AT THE RISK OF CORRUPTING THE DEVICE.**
1. *End of Write Memory* will appear in the bottom pane once the update process is completed. Afterwards, click *Disconnect*. Wait until *port disconnect* message in the bottom pane appears.
1. Remove the Micro-B USB cable, **set SW9 position 1 and 2 to both OFF**, and then plug the Micro-B USB back into P3.

## Updating EEPROM for the BM64

This section will explain how to upload new EEPROM parameters for the BM64. The EEPROM update process involves using the `UITool_IS206x_012_DualModeSPK_v2.x.y.exe`
tool (found at `DSPK v2.x.y Package\Tools\UI Tool`) to make a user interface files to set parameters such as baud rate or enabling UART. It then involves using the `DSPTool_IS206X_012_DUALMODESPK2.1_E1.0_V13.exe` tool (found at `DSPK v2.x.y Package\Tools\DSP Tool`) to make a DSP file for setting speaker and input filtering configurations.
After a UI and DSP file are generated, the process utilizes the `MPET.exe` tool (found at `DSPK v2.x.y Package\Tools\MP_V2.x.y`) to combine for the full EEPROM *.ipf* file. Using
the generated *.ipf* tool, the actual upload of the EEPROM to the BM64 will occur with the `EEPROM_Tool.exe` tool (found at `DSPK v2.x.y Package\Tools\EEPROM_Tool`).

Follow the [**guide**](http://ww1.microchip.com/downloads/en/DeviceDoc/50002514B.pdf) provided by Microchip for updating the BM64 EEPROM,
specifically sections 3.4 - "CONFIGURING BM64 MODULE" and 3.5 - "UPDATING EEPROM PARAMETERS". Below are some important modifications to the guide:

- Section 3.4.1 - "UI Tool Configuration" Modifications:
  - 3.4.1.3: Load the *UITool_IS206x_012_DualModeSPK_v2.x.y_BM64_EVB.txt* UI parameters starting text file.
  - 3.4.1.4: Select "BM64CLS2" for the *IC Package* if using a BM-64-EVB-C2 and "BM64CLS1" if using a BM-64-EVB-C1 board.
  - 3.4.1.6: Changing the *Name Fragment* is optional and will not impact use (if changed, make sure the name is more than 0 and less than 32 ASCII characters).
  - 3.4.1.12: Do not overwrite an existing table in case of wanting to use the default table if there is a critical error with the board.
- Section 3.4.2 - "DSP Tool Configuration" Modifications:
  - 3.4.2.1: Select "IS206X_012_DUALMODESPK2.1_E1.0" (or similar) for the *IC Version*.
- Section 3.4.3 - "MPET Tool Configuration" Modifications:
  - 3.4.3.3: Select "IS206X_012_DUALMODESPK2.1_E1.0.4.1_1214.bin" (or similar) for the default *.bin* file.
  - 3.4.3.5: Add and merge the files created in Section 3.4.1 and Section 3.4.2 of the guide.
  - 3.4.3.8: The popup may not occur depending on the version of DPSK being used, which will not impact performance.
- Section 3.5 - "UPDATING EEPROM PARAMETERS" Modifications:
  - 3.5.1: Unplug the USB, if not alread, before starting.
  - 3.5.5: Use the *.ipf* generated from Section 3.4.3. Additionally, a pop up may occur warning of the size of file of the *.ipf*. Click *OK* (this happens with default tables as well).
  - 3.5.6: **DO NOT INTERRUPT THIS PROCESS AT THE RISK OF CORRUPTING THE DEVICE**.

## Verifying Installation with SPKCommand

After firmware and EEPROM updates occur, the UART messaging capabilies of the BM-64-EVB necessary for communicating with BTP can be verified using the SPKCommand tool included in the DSPK.

1. Set SW9 position 1 and 2 to both OFF and ensure JP33 jumper is removed.
1. Plug the Micro-B USB cable into P3 (labeled *UART* on the EVB).
1. Start the `SPKCommandSetTool vA.B.exe` (found at `DSPK v2.x.y Package\Tools\SPKCommandSetTool`).

    - Set the *Port* to the COM port associated with the BM-64-EVB.
    - Set the *Baudrate* to *19200* per the EEPROM updates. 

1. Click on the *Open* button. Messages may appear in the bottom log to the right.
1. Click on the *Information* tab and click on the *Update* button.

    - If UART messages are being communicated correctly, the information such as the *Local Device Name* and *Bluetooth Address* will be populated on the left and the logs on the right will show both *Event:* and *Command:* messages followed by hex codes representing the UART message contents.
    - If no BM64 information is populated and only *Command:* messages are seen in the logs, try closing and reopening the connection. If the expected behavior still does not occur, refer to the [Further Help](testing-BTP-hw-bm64.md#further-help) section below.

    :::image type="content" source="images/btp-bm64-spkcommand.png" alt-text="Photo of the SPKCommand after the correct messages are sent.":::

## Using the BM-64-EVB

After new firmware and EEPROM is installed, make sure JP33 jumper is removed and SW9 positions 1 and 2 are both OFF. Additionally, set all positions of SW13, SW46 and SW47 to OFF. These are the same settings as in the [Verifying Installation with SPKCommand](testing-BTP-hw-bm64.md#verifying-installation-with-spkcommand).

After settings are verified, simply connect a Micro-B USB cable between P3 (labeled *UART* on the EVB) and the test machine. Optionally, 3.5mm jack headphones or speakers can be connected to P7 (labeled *SPK* on the EVB) for audio output if enabled in the EEPROM. If external speakers are to be used, the board must have the 15V barrel jack for powering the audio amp.

To run BTP using the BM-64-EVB, make sure the software is correctly installed following [Setting up BTP Software](testing-BTP-setup.md#software-setup). Additionally, refer to the
[pairing tests](testing-BTP-tests-pairing.md) and [audio test](testing-BTP-tests-audio.md) for running the tests that are currently supported by BTP for the BM-64-EVB.

## (Optional) Installing Firmware for the PIC Microcontroller

This section will explain how to upload new firmware for the on-board PIC microcontroller. The PIC microcontroller is only used for stand-alone Microchip BM-64-EVB examples (like controlling music with push-buttons) and is not necessary for using the BTP tests.

> [!NOTE]
>
> - Use the same DSPK version for the PIC Microcontroller firmware as was used for the firmware and EEPROM of the BM64 for compatibility
> - The steps were accomplished with the [**MPLAB Snap**](https://www.microchip.com/developmenttools/ProductDetails/PartNO/PG164100), but other
> ICSP compatible programmers may work.

1. Download the [**MPLAB X IDE/IPE**](https://www.microchip.com/mplab/mplab-x-ide) from Microchip.
1. Connect a jumper on JP33. Set SW9 positions 1 and 2 to both OFF, SW46 should have all positions switched to ON expect for #2, and SW47 should have all positions switched to ON.
1. Plug the 15V DC power adapter into the P2 jack for supplying power to MCU.
1. Plug the MPLAB Snap into the ICSP J5 header and the USB cable to the Snap.

    - Ensure the orientation is correct (arrow on Snap points to pin 1 on J5 header).

1. Open the `MPLAB X IPE.exe` and configure the given parameters:

    - For *Device*, select PIC18F85J10 (the product name of the target MCU).
    - For *Tool*, it should be auto populated by the Snap if plugged into USB.

1. Click *Connect* (if successful, the target device should be found in the output screen).
1. Load the hex file included in the DSPK (found at `DSPK v2.x.y Package\Software\Firmware Image\PIC18 Image`).
1. Most likely, a warning saying debug bits are set will appear after the Hex file is loaded. If so, go to the menu and click *Settings*->*Advanced Mode* and enter the password.
1. After the password is entered (and the hex file is still loaded correctly), click *Program*.
1. After successful programming (checksum should match), click *Disconnect* and remove the Snap.
1. **Remove the JP33 jumper** before attempting any other functions.

## Further Help

If after the firmware and EEPROM updates and [Verifying Installation with SPKCommand](testing-BTP-hw-bm64.md#verifying-installation-with-spkcommand) is not successful, this means that UART messages are not being passed between the computer and the BM64. There are a few methods to try to correct the issue.

### Confirm Setup and Power Cycle

The first common issue is the board is not configured correctly using switches and jumpers for running SPKCommand / BTP. A few key component configurations on the board to check are as follows:

- SW9: Ensure position 1 and 2 are both set to OFF.
- P3: Verify the Micro-B USB is plugged into the *UART* port.
- JP33: Verify the jumper is removed.
- SW13: Ensure all positions are switched to OFF
- SW46: Ensure all positions are switched to OFF (in the direction of the BM64 radio on the board)
- SW47: Ensure all positions are switched to OFF (in the direction of the BM64 radio on the board)

After these are verified, unplug, wait at least 10 seconds or longer, and replug the Micro-B USB. Even if the configurations are correct, a power cycle of unpluging and plugging may help. Afterwards, try the [Verifying Installation with SPKCommand](testing-BTP-hw-bm64.md#verifying-installation-with-spkcommand) section again. If this still does not work, continue with the further suggestions below.

### Using MSPK SPKCommand

Another solution is using a different version of the SPKCommand. To do so, download and extract the MSPK v1.35 BM64 software kit from [**Microchip**](https://www.microchip.com/wwwproducts/en/BM64) on the *Documents/Software Libraries/Firmware* tab. Inside the MSPK v1.35 kit, locate the `SPKCommandSetTool v192.006.exe` tool (found at `BM64 Software & Tools (MSPKv1.35)\Tools\SPK CommandSet Tool`). Run through the same instructions in the [Verifying Installation with SPKCommand](testing-BTP-hw-bm64.md#verifying-installation-with-spkcommand) using the MSPK v1.35 version of the SPKCommand tool. If BM-64-EVB correctly responds using the MSPK v1.35 tool, then the board can be used with BTP.

## Features

- UART data connection with custom packet structure
- Supports SPP, A2DP, HFP, and AVRCP profiles
- Bluetooth v5.0
- Supports Bluetooth dual-mode (BDR/EDR/BLE)
- Supports AAC and SBC codecs
- Heavily featured, surface mount module
- Using BM-64-EVB does not require a Traduci

## Known test failures

 With version 1.7.2 both standalone audio tests will fail as will some audio-HID tests due to backend architecture changes. If this breaks you, please file a bug or email btpsupport@microsoft.com
