---
title: Relationship between Microsoft Windows and the System Firmware
description: Relationship between Microsoft Windows and the System Firmware
keywords:
- Windows Hardware Error Architecture WDK , Windows and firmware
- WHEA WDK , Windows and firmware
- hardware errors WDK WHEA , Windows and firmware
- errors WDK WHEA , Windows and firmware
- firmware WDK WHEA
ms.date: 03/03/2023
---

# Relationship between Microsoft Windows and the System Firmware


Both the Microsoft Windows operating system and the system firmware play important roles in hardware error handling. The Windows Hardware Error Architecture (WHEA) improves the methods by which both can contribute to the task of hardware error handling. With WHEA, the hardware platform vendor can determine whether the firmware or the operating system will own key hardware error resources. Additionally, with WHEA the firmware can pass control of hardware error resources to the operating system when appropriate.

The operating system should own as much of the hardware error resources as is practical. However, the system firmware must continue to manage some of these resources due to the lack of hardware error resource standardization. As more hardware error reporting standards are defined and adopted, Microsoft believes that more of the hardware error handling mechanisms can be put under operating system control.

 

 




