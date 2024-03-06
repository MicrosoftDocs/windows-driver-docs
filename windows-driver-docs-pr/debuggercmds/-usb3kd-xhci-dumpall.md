---
title: usb3kd.xhci_dumpall
description: The usb3kd.xhci_dumpall command displays information about all USB 3.0 host controllers on the computer. The display is based on the data structures maintained by UsbXhci.sys.
keywords: ["usb3kd.xhci_dumpall Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- usb3kd.xhci_dumpall
api_type:
- NA
---

# !usb3kd.xhci\_dumpall

The [**!usb3kd.xhci\_dumpall**](-usb3kd-device-info.md) command displays information about all USB 3.0 host controllers on the computer. The display is based on the data structures maintained by the USB 3.0 host controller driver (UsbXhci.sys).

```dbgcmd
!usb3kd.xhci_dumpall [1]
```

## Parameters

<span id="_____________1"></span> **1**  
Runs all of the XHCI commands and displays the output of each command.

## Examples

The following screen shot show the output of the **!xhci\_dumpall**l command.

:::image type="content" source="images/xhcidumpall01.png" alt-text="Screenshot of the !xhci-dumpall command output displaying XHCI controller information.":::

The output shows that there is one USB 3.0 host controller.

The output uses [Using Debugger Markup Language (DML)](../debugger/debugger-markup-language-commands.md) to provide links. The links execute commands that give detailed information about the state of the host controller as it is maintained by the USB 3.0 host controller driver. For example, you could get detailed information about the host controller capabilities by clicking the [**!xhci\_capability**](-usb3kd-xhci-capability.md) link. As an alternative to clicking a link, you can enter a command. For example, to see information about the host controller's resource usage, you could enter the command **!xhci\_resourceusage 0xfffffa800536e2d0**.

**Note**  The DML feature is available in WinDbg, but not in Visual Studio or KD.

## DLL

Usb3kd.dll

## Remarks

The **!xhci\_dumpall** command is the parent command for this set of commands.

- [**!xhci\_capability**](-usb3kd-xhci-capability.md)
- [**!xhci\_info**](-usb3kd-xhci-info.md)
- [**!xhci\_deviceslots**](-usb3kd-xhci-deviceslots.md)
- [**!xhci\_commandring**](-usb3kd-xhci-commandring.md)
- [**!xhci\_eventring**](-usb3kd-xhci-eventring.md)
- [**!xhci\_transferring**](-usb3kd-xhci-transferring.md)
- [**!xhci\_trb**](-usb3kd-xhci-trb.md)
- [**!xhci\_registers**](-usb3kd-xhci-registers.md)
- [**!xhci\_resourceusage**](-usb3kd-xhci-resourceusage.md)

The information displayed by the **!xhci\_dumpall** family of commands is based on data structures maintained by the USB 3.0 host controller driver. For information about the USB 3.0 host controller driver and other drivers in the USB 3.0 stack, see [USB Driver Stack Architecture](../usbcon/usb-3-0-driver-stack-architecture.md). For an explanation of the data structures used by the drivers in the USB 3.0 stack, see Part 2 of the [USB Debugging Innovations in Windows 8](/events/build-build2011/hw-258p) video.

## See also

[USB 3.0 Extensions](usb-3-extensions.md)

[Universal Serial Bus (USB) Drivers](../usbcon/index.md)
