---
title: MB Radio Power State Operations
description: MB Radio Power State Operations
ms.assetid: 9b745ff3-c00b-4a43-9bf3-52f9bf61e062
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB Radio Power State Operations


This topic describes the operations used to set and read an MB device's radio power state(s). The following values from the WWAN\_RADIO enumeration describe the two power states supported by the MB Service:

-   *WwanRadioOn*: the radio is on, the stack is loaded, and the device is able to perform cellular procedures as well as answer host commands.

-   *WwanRadioOff*: the radio is turned off. In this state, the device has power and should respond to the commands. However no radio-related operations should be carried out except the host command to turn on the radio.

Radio power states are controlled either by the MB Service, or by the hardware switch (if present).

Be aware that the radio power state may change on portable computers (laptops) because of the following reasons:

-   Most portable computers are equipped with a switch that you can use to turn the radio on and off. Switching off the button effectively cuts off the power from the computer backplane to the MB module. Eventually, the radio is completely powered off.

-   The MB Service may send a command to the miniport driver to put the radio into a low power state to conserve power or to avoid radio interference with the environment (such as on an airplane).

For more information about radio power state operations, see [OID\_WWAN\_RADIO\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569832).

 

 





