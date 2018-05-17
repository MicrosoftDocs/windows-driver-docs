---
title: INF PS2_Inst.NoInterruptInit.Bioses Section
author: windows-driver-content
description: INF PS2_Inst.NoInterruptInit.Bioses Section
ms.assetid: 2bf1dc0f-00b6-4f4a-99f0-e9843fe6e66b
keywords:
- INF files WDK non-HID keyboard/mouse
- PS2_Inst.NoInterruptInit.Bioses section
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# INF PS2\_Inst.NoInterruptInit.Bioses Section


## <a href="" id="ddk-inf-ps2-inst-nointerruptinit-bioses-section-kg"></a>


**\[PS2\_Inst.NoInterruptInit.Bioses\]**

*Disable*=*disable-string*
The mouse class installer checks if d*isable-string* is a substring of the string value of **HKLM\\Hardware\\Description\\System\\SystemBiosVersion**. If it is, the class installer executes the INF directives specified in an [INF PS2\_Inst.NoInterruptInit section](inf-ps2-inst-nointerruptinit-section.md).

### Entries and Values

<a href="" id="disable"></a>*Disable*  
Set to the d*isable-string* value.

<a href="" id="disable-string"></a>*disable-string*  
Specifies a substring in **HKLM\\Hardware\\Description\\System\\SystemBiosVersion** that uniquely identifies the system BIOS.

### <a href="" id="comments"></a>Remarks

This section is used only with PS/2 mouse devices and only in combination with an [INF **PS2\_Inst.NoInterruptInit** section](inf-ps2-inst-nointerruptinit-section.md).

 

 




