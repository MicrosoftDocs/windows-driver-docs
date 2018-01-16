---
title: usbkd.usbhcdpnp
description: The usbkd.usbhcdpnp command displays the Plug and Play (PnP) state history for a USB host controller or root hub.
ms.assetid: 1153F3C2-5878-4223-AA18-5AE6FA056851
keywords: ["usbkd.usbhcdpnp Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usbkd.usbhcdpnp
api_type:
- NA
---

# !usbkd.usbhcdpnp


The **!usbkd.usbhcdpnp** command displays the Plug and Play (PnP) state history for a USB host controller or root hub.

```
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

```
0: kd> !usbkd.usb2tree

UHCI MINIPORT(s) dt usbport!_USBPORT_MINIPORT_DRIVER ffffe0000090c3d0
...
4)!uhci_info ffffe00001c8f1a0 !devobj ffffe00001c8f050 PCI: VendorId 8086 DeviceId 2938 RevisionId 0002 
...
```

In the preceding output, the address of the device extension of the FDO is displayed as the argument of the [DML](debugger-markup-language-commands.md) command **!uhci\_info ffffe00001c8f1a0**.

Now pass the address of the device extension to the **!usbhcdpnp** command.

```
0: kd> !usbkd.usbhcdpnp ffffe00001c8f1a0

## PNP STATE LOG (latest at bottom)

##      EVENT                         STATE               NEXT

[01] EvFDO_IRP_MN_START_DEVICE      PnpNotStarted       PnpStarted          
[02] EvFDO_IRP_MN_QBR_RH            PnpStarted          PnpStarted
```

Here is one way to find the address of the device extension for the PDO of a root hub. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```
4)!uhci_info ffffe00001c8f1a0 !devobj ffffe00001c8f050 PCI: VendorId 8086 DeviceId 2938 RevisionId 0002 
    RootHub !hub2_info ffffe00000d941a0 !devstack ffffe00000d94050
```

In the preceding output, you can see the address of the FDO of the root hub displayed as the argument to the command **!devstack ffffe00000d94050**. Use the [**!devstack**](-devstack.md) command to find the address of the PDO and the PDO device extension.

```
0: kd> !kdexts.devstack ffffe00000d94050
  !DevObj           !DrvObj            !DevExt           ObjectName
> ffffe00000d94050  \Driver\usbhub     ffffe00000d941a0  0000006b
  ffffe00000ed4050  \Driver\usbuhci    ffffe00000ed41a0  USBPDO-2
```

In the preceding output, you can see that the address of the device extension for the PDO of the root hub is `ffffe00000ed41a0`.

Now pass the address of the device extension to the **!usbhcdpnp** command.

```
0: kd> !usbkd.usbhcdpnp ffffe00000ed41a0

## PNP STATE LOG (latest at bottom)

##      EVENT                         STATE               NEXT

[01] EvPDO_IRP_MN_START_DEVICE      PnpNotStarted       PnpStarted          
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usbkd.usbhcdpnp%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





