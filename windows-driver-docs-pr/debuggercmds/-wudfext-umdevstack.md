---
title: "!wudfext.umdevstack"
description: "The !wudfext.umdevstack extension displays detailed information about a device stack in the host process."
keywords: ["!wudfext.umdevstack Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wudfext.umdevstack
api_type:
- NA
---

# !wudfext.umdevstack

The **!wudfext.umdevstack** extension displays detailed information about a device stack in the host process.

```dbgcmd
!wudfext.umdevstack DevstackAddress [Flags] 
```

## Parameters

<span id="_______DevstackAddress______"></span><span id="_______devstackaddress______"></span><span id="_______DEVSTACKADDRESS______"></span> *DevstackAddress*   
Specifies the address of the device stack to display information about.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. Specifies the type of information to be displayed. *Flags* can be any combination of the following bits. The default value is 0x01.

<span id="Bit_0__0x01_"></span><span id="bit_0__0x01_"></span><span id="BIT_0__0X01_"></span>Bit 0 (0x01)  
Displays detailed information about the device stack.

<span id="Bit_8__0x80_"></span><span id="bit_8__0x80_"></span><span id="BIT_8__0X80_"></span>Bit 8 (0x80)  
Displays information about the internal framework.

## DLL

Wudfext.dll

## Additional Information

For more information, see [User-Mode Driver Framework Debugging](../debugger/user-mode-driver-framework-debugging.md).

## Remarks

The following is an example of the **!wudfext.umdevstack** display:

```dbgcmd
kd> !umdevstack 0x0034e4e0
Device Stack: 0x0034e4e0  Pdo Name: \Device\00000057
 Number of UM drivers: 0x1
  Driver 00:
    Driver Config Registry Path: WUDFEchoDriver
    UMDriver Image Path: C:\Windows\system32\DRIVERS\UMDF\WUDFEchoDriver.dll
    Fx Driver: IWDFDriver 0xf2db8
    Fx Device: IWDFDevice 0xf2f80
        IDriverEntry: WUDFEchoDriver!CMyDriver 0x000f2c70
```
