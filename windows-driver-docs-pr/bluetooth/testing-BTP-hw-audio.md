---
title: Microsoft Bluetooth Test Platform
description: Bluetooth Test Platform (BTP) supported hardware (audio).
ms.assetid: a6beeecb-5967-4e08-bfe2-b8aae26861ad
ms.date: 4/17/2019
ms.localizationpriority: medium

---

# Audio Capable Peripheral Radios #

The Traduci requires a 12-pin connector to communicate with any radio module. The audio radios and breakouts listed here take a radio module and break out the necessary pins to a 12 pin layout.

<table>
    <colgroup>
        <col width="15%" />
        <col width="33%" />
        <col width="33%" />
    </colgroup>
    <thead>
        <tr class="header">
            <th>Radio</th>
            <th>Capabilities</th>
            <th>Parameter</th>
        </tr>
    </thead>
    <tbody>
    <tr class="even">
        <td>RN52</a></td>
        <td>
            <ul>
                <li>Basic Rate (BR) radio</li>
            </ul>
        </td>
        <td>
            <p>rn52 (ex. RunPairingTests.bat rn52)</p>
        </td>
    </tr>
</table>

## Audio Sled (RN52 radio) ##

<img src="images/RN52.png" alt="Photo of the RN52 Radio" width="150"/>
<img src="images/Traduci_and_RN52.jpg" alt="Photo of the RN52 Radio on a sled" width="400"/>

The RN52 is a Basic Rate (BR) radio from Roving Networks capable of behaving as an Audio peripheral (like a speaker or headset). It is currently planned to be supported upcoming BTP audio tests. More info can be found via the RN52 page from [**MicroChip**](https://www.microchip.com/wwwproducts/en/RN52). This sled breaks out the audio out data from the radio and routes it to an audio codec and audio processing FPGA on the Traduci in order to aid with validation.

> [!NOTE] 
> Currently the RN52 radio can **only** be plugged into JA.

- UART data connection with AT commands to configure software
- Supports SPP, A2DP, HFP, and AVRCP profiles
- Version 3.0 audio module
- Fully certified Class 2 BR Bluetooth 2.1+EDR
- Small form factor, low power, surface mount module
