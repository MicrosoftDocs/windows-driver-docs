---
title: INF PS2_Inst.NoInterruptInit section
description: INF PS2_Inst.NoInterruptInit section
keywords:
- INF files WDK non-HID keyboard/mouse
- PS2_Inst.NoInterruptInit section
ms.date: 10/11/2022
---

# INF PS2_Inst.NoInterruptInit section

**\[PS2_Inst.NoInterruptInit\]**

**AddReg** = *add-reg-section***.AddReg**

The mouse class installer executes the directives in this section if the *Disable* entry in an [INF PS2\_Inst.NoInterruptInit.Bios section](inf-ps2-inst-nointerruptinit-bioses-section.md) matches the system BIOS version.

## Entries and Values

- *add-reg-section*: Specifies an **AddReg** section that the mouse class installer uses to set registry values in a device's hardware key. The registry values determine whether the system initializes a mouse device by using interrupts or by polling.

## Remarks

This section is only used in combination with an [INF PS2_Inst.NoInterruptInit.Bioses section](inf-ps2-inst-nointerruptinit-bioses-section.md). The primary purpose of this section is to specify an **AddReg** section that adds registry values to a mouse device's hardware key.

### add-reg section Entries

**HKR**,,"**DisableInitializePolledUI**",0x00010001,1

**HKR**,,"**MouseInitializePolled**",0x00010001,1

**DisableInitializePolledUI**  
Specifies a REG\_DWORD flag that indicates whether the **Fast Initialization** check box on the property page will be available. If **DisableInitializePolledUI** is set to a nonzero value, the check box is unavailable; otherwise, the check box is available.

**MouseInitializedPolled**  
Specifies a REG\_DWORD flag that indicates whether the system must poll the device to initialize it. If **MouseInitializedPolled** is set to one, the system polls the mouse device; otherwise the system uses interrupts.
