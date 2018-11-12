---
title: usbkd.usbhcdpnp
description: The usbkd.usbhcdpnp command displays the Plug and Play (PnP) state history for a USB host controller or root hub.
ms.assetid: 1153F3C2-5878-4223-AA18-5AE6FA056851
keywords: ["usbkd.usbhcdpnp Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.usbhcdpnp
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.usbhcdpnp


The **!usbkd.usbhcdpnp** command displays the Plug and Play (PnP) state history for a USB host controller or root hub.

```dbgcmd
!usbkd.usbhcdpnp DeviceExtension
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______DeviceExtension______"></span><span id="_______deviceextension______"></span><span id="_______DEVICEEXTENSION______"></span> *DeviceExtension*   
Address of one of the following:

-   The device extension for the functional device object (FDO) of a USB host controller.
-   The device extension for the physical device object (PDO) a USB root hub.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is one way to find the address of the device extension for the FDO of USB host controller. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```dbgcmd
0: kd> !usbkd.usb2tree

UHCI MINIPORT(s) dt usbport!_USBPORT_MINIPORT_DRIVER ffffe0000090c3d0
...
4)!uhci_info ffffe00001c8f1a0 !devobj ffffe00001c8f050 PCI: VendorId 8086 DeviceId 2938 RevisionId 0002 
...
```

In the preceding output, the address of the device extension of the FDO is displayed as the argument of the [DML](debugger-markup-language-commands.md) command **!uhci\_info ffffe00001c8f1a0**.

Now pass the address of the device extension to the **!usbhcdpnp** command.

```dbgcmd
0: kd> !usbkd.usbhcdpnp ffffe00001c8f1a0

## PNP STATE LOG (latest at bottom)

##      EVENT                         STATE               NEXT

[01] EvFDO_IRP_MN_START_DEVICE      PnpNotStarted       PnpStarted          
[02] EvFDO_IRP_MN_QBR_RH            PnpStarted          PnpStarted
```

Here is one way to find the address of the device extension for the PDO of a root hub. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```dbgcmd
4)!uhci_info ffffe00001c8f1a0 !devobj ffffe00001c8f050 PCI: VendorId 8086 DeviceId 2938 RevisionId 0002 
    RootHub !hub2_info ffffe00000d941a0 !devstack ffffe00000d94050
```

In the preceding output, you can see the address of the FDO of the root hub displayed as the argument to the command **!devstack ffffe00000d94050**. Use the [**!devstack**](-devstack.md) command to find the address of the PDO and the PDO device extension.

```dbgcmd
0: kd> !kdexts.devstack ffffe00000d94050
  !DevObj           !DrvObj            !DevExt           ObjectName
> ffffe00000d94050  \Driver\usbhub     ffffe00000d941a0  0000006b
  ffffe00000ed4050  \Driver\usbuhci    ffffe00000ed41a0  USBPDO-2
```

In the preceding output, you can see that the address of the device extension for the PDO of the root hub is `ffffe00000ed41a0`.

Now pass the address of the device extension to the **!usbhcdpnp** command.

```dbgcmd
0: kd> !usbkd.usbhcdpnp ffffe00000ed41a0

## PNP STATE LOG (latest at bottom)

##      EVENT                         STATE               NEXT

[01] EvPDO_IRP_MN_START_DEVICE      PnpNotStarted       PnpStarted          
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






