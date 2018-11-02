---
title: usbkd.usbdevh
description: The usbkd.usbdevh command displays information about a USB device handle.
ms.assetid: 463DAA72-F3EB-4C76-BB63-DA2EFA1EE9B1
keywords: ["usbkd.usbdevh Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.usbdevh
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.usbdevh


The **!usbkd.usbdevh** command displays information about a USB device handle.

```dbgcmd
!usbkd.usbdevh StructAddr
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______StructAddr______"></span><span id="_______structaddr______"></span><span id="_______STRUCTADDR______"></span> *StructAddr*   
Address of a **usbport!\_USBD\_DEVICE\_HANDLE** structure. To get the device handle list for a USB host controller, use the [**!usbkd.usbhcdext**](-usbkd-usbhcdext.md) command.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is one way to find the address of a **usbport!\_USBD\_DEVICE\_HANDLE** structure. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```dbgcmd
0: kd> !usbkd.usb2tree
...
2)!ehci_info ffffe00001ca11a0 !devobj ffffe00001ca1050 PCI: VendorId 8086 DeviceId 293c RevisionId 0002 
     ...
```

In the preceding output, the address of the device extension of the FDO is displayed as the argument of the [DML](debugger-markup-language-commands.md) command **!ehci\_info ffffe00001ca11a0**.

Either click the DML command or pass the address of the device extension to [**!usbhcdext**](https://msdn.microsoft.com/library/windows/hardware/dn367072) to get the device handle list.

```dbgcmd
0: kd> !usbkd.usbhcdext ffffe00001ca11a0

HC Flavor 1000  FDO ffffe00001ca1050
Root Hub: FDO ffffe00002320050 !hub2_info ffffe000023201a0
Operational Registers ffffd000228bf020
Device Data ffffe00001ca2da0
dt USBPORT!_FDO_EXTENSION ffffe00001ca15a0
DM Timer Flags ffffe00001ca16d4
FDO Flags ffffe00001ca16d0
HCD Log ffffe00001ca11a0

DeviceHandleList: !usblist ffffe00001ca23b8, DL 
DeviceHandleDeletedList: !usblist ffffe00001ca23c8, DL [Empty]
...
```

Now use the [**!usbkd.usblist**](-usbkd-usblist.md) command to get the addresses of **usbport!\_USBD\_DEVICE\_HANDLE** structures.

```dbgcmd
0: kd> !usblist ffffe00001ca23b8, DL
list: ffffe00001ca23b8 DL
----------
!usbdevh ffffe000020f9590
SSP [IdleReady] (0)
...
```

In the preceding output, `ffffe000020f9590` is the address of a **\_USBD\_DEVICE\_HANDLE** structure. Pass this address to **!usbdevh**.

```dbgcmd
0: kd> !usbkd.usbdevh ffffe000020f9590

dt USBPORT!_USBD_DEVICE_HANDLE ffffe000020f9590
SSP [IdleReady] (0)
PCI\VEN_8086&DEV_293C  Intel Corporation
Root Hub
DriverName :  

## DEVICE HANDLE HISTORY (latest at boottom)

##      EVENT                        STATE                        NEXT

[01] Ev_CreateRoothub_Success     Devh_Created                 Devh_Valid                   

## Referene List: Head(ffffe000020f9668)

[00] dt USBPORT!_DEVH_REF_OBJ ffffe000021944a0  Object: ffffe000020f9590 Tag: dvh+ PendingFlag(0)
[01] dt USBPORT!_DEVH_REF_OBJ ffffe000020bbcb0  Object: ffffe000020ba7e0 Tag: bsCT PendingFlag(0)
[02] dt USBPORT!_DEVH_REF_OBJ ffffe000032b91a0  Object: ffffe0000269e670 Tag: UrbT PendingFlag(1)

## TtList: Head(ffffe000020f9658)


## PipeHandleList: Head(ffffe000020f9640)

[00] dt USBPORT!_USBD_PIPE_HANDLE_I ffffe000020f95e0 !usbep ffffe000020f6970
        Device Address: 0x00, Endpoint Address 0x00 Endpoint Type: Control 
[01] dt USBPORT!_USBD_PIPE_HANDLE_I ffffe000023bd278 !usbep ffffe0000212d970
        Device Address: 0x00, Endpoint Address 0x81 Endpoint Type: Interrupt In

Config Information: dt USBPORT!_USBD_CONFIG_HANDLE ffffe000023cd0b0

## Interface List:

[00] dt USBPORT!_USBD_INTERFACE_HANDLE_I ffffe000023bd250
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






