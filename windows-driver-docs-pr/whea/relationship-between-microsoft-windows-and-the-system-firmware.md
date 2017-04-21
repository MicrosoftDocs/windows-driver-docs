---
title: Relationship between Microsoft Windows and the System Firmware
author: windows-driver-content
description: Relationship between Microsoft Windows and the System Firmware
ms.assetid: 83a43e49-cb06-4007-88d0-88f024c22825
keywords:
- Windows Hardware Error Architecture WDK , Windows and firmware
- WHEA WDK , Windows and firmware
- hardware errors WDK WHEA , Windows and firmware
- errors WDK WHEA , Windows and firmware
- firmware WDK WHEA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Relationship between Microsoft Windows and the System Firmware


Both the Microsoft Windows operating system and the system firmware play important roles in hardware error handling. The Windows Hardware Error Architecture (WHEA) improves the methods by which both can contribute to the task of hardware error handling. With WHEA, the hardware platform vendor can determine whether the firmware or the operating system will own key hardware error resources. Additionally, with WHEA the firmware can pass control of hardware error resources to the operating system when appropriate.

The operating system should own as much of the hardware error resources as is practical. However, the system firmware must continue to manage some of these resources due to the lack of hardware error resource standardization. As more hardware error reporting standards are defined and adopted, Microsoft believes that more of the hardware error handling mechanisms can be put under operating system control.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Relationship%20between%20Microsoft%20Windows%20and%20the%20System%20Firmware%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


