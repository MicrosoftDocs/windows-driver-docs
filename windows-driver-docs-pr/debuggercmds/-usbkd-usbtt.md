---
title: "!usbkd.usbtt"
description: "The !usbkd.usbtt command displays information from a USBPORT _TRANSACTION_TRANSLATOR structure."
keywords: ["!usbkd.usbtt Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- usbkd.usbtt
api_type:
- NA
---

# !usbkd.usbtt

The **!usbkd.usbtt** command displays information from a **USBPORT!\_TRANSACTION\_TRANSLATOR** structure.

```dbgcmd
!usbkd.usbtt StructAddr
```

## Parameters

<span id="_______StructAddr______"></span><span id="_______structaddr______"></span><span id="_______STRUCTADDR______"></span> *StructAddr*   
Address of a **usbport!\_TRANSACTION\_TRANSLATOR** structure. To get the transaction translator list for a USB host controller, use the [**!usbkd.usbhcdext**](-usbkd-usbhcdext.md) command.

## DLL

Usbkd.dll

## Examples

Here is one way to find the address of a **usbport!\_TRANSACTION\_TRANSLATOR** structure. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```dbgcmd
0: kd> !usbkd.usb2tree
...
2)!ehci_info ffffe00001ca11a0 !devobj ffffe00001ca1050 PCI: VendorId 8086 DeviceId 293c RevisionId 0002 
...
```

In the preceding output, the address of the device extension of the FDO is displayed as the argument of the [DML](../debugger/debugger-markup-language-commands.md) command **!ehci\_info ffffe00001ca11a0**.

Either click the DML command or pass the address of the device extension to [**!usbhcdext**](-usbkd-usbhcdext.md) to get the address of `GlobalTtListHead`. Pass that address to [**!usbkd.usblist**](-usbkd-usblist.md), which will display addresses of **\_TRANSACTION\_TRANSLATOR** structures.

## See also

[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](../usbcon/index.md)
