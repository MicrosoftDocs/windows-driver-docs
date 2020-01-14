---
title: Microsoft Bluetooth Test Platform
description: Bluetooth Test Platform (BTP) supported hardware (HID).
ms.assetid: a6beeecb-5967-4e08-bfe2-b8aae26861ad
ms.date: 4/17/2019
ms.localizationpriority: medium

---

# HID Capable Peripheral Radios #

The Traduci requires a 12-pin connector to communicate with any radio module. The HID radios and breakouts listed here take a radio module and break out the necessary pins to a 12 pin layout.

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
        <td>RN42</a></td>
        <td>
            <ul>
                <li>Basic Rate (BR) radio</li>
            </ul>
        </td>
        <td>
            <p>rn42 (ex. RunPairingTests.bat rn42)</p>
        </td>
    </tr>
    <tr class="odd">
        <td>Bluefruit</a></td>
        <td>
            <ul>
                <li>Low Energy (LE) radio</li>
            </ul>
        </td>
        <td>
            <p>bluefruit (ex. RunPairingTests.bat bluefruit)</p>
        </td>
    </tr>
</table>

## PMOD BT2 (RN42 radio) ##
Purchasable via [**Digilent**](https://store.digilentinc.com/pmod-bt2-bluetooth-interface/)

<img src="images/RN42.png" alt="Photo of the RN42 Radio" width="150"/>
<img src="images/Traduci_and_DigilentRN42.jpg" alt="Photo of the RN42 Radio on a Digilent sled" width="400"/>

The RN42 is a Basic Rate (BR) radio from Roving Networks capable of behaving as a HID peripheral (like a keyboard or mouse). It is currently supported by the BTP pairing and HID tests. More info can be found via the Digilent link above and through the RN42 page from [**MicroChip**](https://www.microchip.com/wwwproducts/en/RN42).

> [!NOTE] 
> Currently the RN42 radio can **only** be plugged into JB.

- UART data connection
- Supports HID profile and Bluetooth data links
- Fully certified Class 2 BR Bluetooth 2.1+
- Small form factor, low power, surface mount module

## Bluefruit LE UART Friend (nRF51 radio) ##
Purchasable via [**Adafruit**](https://www.adafruit.com/product/2479)

The nRF51 is a Low Energy (LE) radio from Nordic Semiconductor capable of behaving as a HID peripheral (like a keyboard or mouse) among other things. It is currently supported by the BTP pairing and HID tests. More info can be found via the Adafruit link above and through the nRF51822 page from [**Nordic**](https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF51822).

> [!NOTE] 
> Currently the Bluefruit radio can **only** be plugged into JC.

- UART data connection
- Supports HID and other GATT based services
- Fully certified Low Energy Bluetooth 4.1 radio
- Configurable ATT database
- Small form factor, low power, surface mount module
