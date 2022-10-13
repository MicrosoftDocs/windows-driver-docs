---
title: INF PS2_Inst.NoInterruptInit.Bioses section
description: INF PS2_Inst.NoInterruptInit.Bioses section
keywords:
- INF files WDK non-HID keyboard/mouse
- PS2_Inst.NoInterruptInit.Bioses section
ms.date: 10/11/2022
---

# INF PS2_Inst.NoInterruptInit.Bioses section

**\[PS2_Inst.NoInterruptInit.Bioses\]**

*Disable*=*disable-string*

The mouse class installer checks if *disable-string* is a substring of the string value of **HKLM\\Hardware\\Description\\System\\SystemBiosVersion**. If it is, the class installer executes the INF directives specified in an [INF PS2_Inst.NoInterruptInit section](inf-ps2-inst-nointerruptinit-section.md).

## Entries and Values

- *Disable*: Set to the *disable-string* value.

- *disable-string*: Specifies a substring in **HKLM\\Hardware\\Description\\System\\SystemBiosVersion** that uniquely identifies the system BIOS.

## Remarks

This section is used only with PS/2 mouse devices and only in combination with an [INF PS2_Inst.NoInterruptInit section](inf-ps2-inst-nointerruptinit-section.md).
