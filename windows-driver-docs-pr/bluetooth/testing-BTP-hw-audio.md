---
title: Microsoft Bluetooth Test Platform
description: Bluetooth Test Platform (BTP) supported hardware (audio).
ms.assetid: a6beeecb-5967-4e08-bfe2-b8aae26861ad
ms.date: 2/14/2020
ms.localizationpriority: medium

---

# Audio Capable Peripheral Radios #

The Bluetooth Test Platform (BTP) Traduci board requires a 12-pin connector to communicate with any radio module. The audio radios and breakouts listed here take a radio module and break out the necessary pins to the required 12-pin layout.

| Radio | Capabilities | Parameter |
| --- | --- | --- |
| RN52 | Basic Rate (BR) radio | rn52 (ex. RunPairingTests.bat rn52) |

## Audio Sled (RN52 radio) ##

The RN52 is a Basic Rate (BR) radio from Roving Networks capable of behaving as an Audio peripheral such as a speaker or headset). It is currently planned to be supported upcoming BTP audio tests. More information can be found via the RN52 page from [**MicroChip**](https://www.microchip.com/wwwproducts/en/RN52). This sled breaks out the audio out data from the radio and routes it to an audio codec and audio processing FPGA on the Traduci in order to aid with validation.

### RN52 Radio ###

![Photo of the RN52 Radio](images/RN52.png)

### RN52 Radio on BTP-compatible sled ###

![Photo of the RN52 Radio on a sled](images/Traduci_and_RN52.jpg)

> [!NOTE]
> The RN52 radio can **only** be plugged into the Traduci board 12-pin port labeled 'JA'.

- UART data connection with AT commands to configure software
- Supports SPP, A2DP, HFP, and AVRCP profiles
- Version 3.0 audio module
- Fully certified Class 2 BR Bluetooth 2.1+EDR
- Small form factor, low power, surface mount module
