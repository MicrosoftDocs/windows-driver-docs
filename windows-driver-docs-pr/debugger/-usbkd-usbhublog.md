---
title: usbkd.usbhublog
description: The usbkd.usbhublog command displays the debug log for a USB hub.
ms.assetid: DFDF595E-3452-40C2-A6C7-94FB8954002C
keywords: ["usbkd.usbhublog Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.usbhublog
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.usbhublog


The **!usbkd.usbhublog** command displays the debug log for a USB hub.

```dbgcmd
!usbkd.usbhublog DeviceExtension[, NumberOfEntries]
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______DeviceExtension______"></span><span id="_______deviceextension______"></span><span id="_______DEVICEEXTENSION______"></span> *DeviceExtension*   
Address of the device extension for the functional device object (FDO) of a USB hub.

<span id="_______NumberOfEntries______"></span><span id="_______numberofentries______"></span><span id="_______NUMBEROFENTRIES______"></span> *NumberOfEntries*   
The number of log entries to display. To display the entire log, set this parameter to -1.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is one way to find the address of the device extension for the FDO of a USB hub. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```dbgcmd
0: kd> !usbkd.usb2tree
...
2)!ehci_info ffffe00001ca11a0 !devobj ffffe00001ca1050 PCI: VendorId 8086 DeviceId 293c RevisionId 0002 
    RootHub !hub2_info ffffe000023201a0 !devstack ffffe00002320050
      ...
```

In the preceding output, you can see the suggested command **!devstack ffffe00002320050**. Enter this command.

```dbgcmd
0: kd> !kdexts.devstack ffffe00002320050

  !DevObj           !DrvObj            !DevExt           ObjectName
> ffffe00002320050  \Driver\usbhub     ffffe000023201a0  0000002d
  ffffe0000213c050  \Driver\usbehci    ffffe0000213c1a0  USBPDO-3
...
```

In the preceding output, `ffffe000023201a0` is the address of the device extension for the FDO of the hub.

Now pass the address of the device extension to **!usbhublog**. In this example, the second argument limits the display to 10 log entries.

```dbgcmd
0: kd> !usbkd.usbhublog ffffe000023201a0, 10

LOG@: ffffe000023201a0 (usbhub!_DEVICE_EXTENSION_HUB)
>LOG mask = ff idx = ffffa333 (33)
*LOG: ffffe00002321ca0  LOGSTART: ffffe00002321640 *LOGEND: ffffe00002323620 # 20 
[ 000] ffffe00002321ca0 HDec 0000000000000000 ffffe000002904d0 0000000000000001 
[ 001] ffffe00002321cc0 HPCd 0000000000000000 0000000000000002 0000000000000004 
[ 002] ffffe00002321ce0 qwk- 0000000000000000 ffffe000021c11c0 0000000000000000 
[ 003] ffffe00002321d00 pq-- 0000000000000000 0000000000000002 0000000000000004 
[ 004] ffffe00002321d20 _6p4 0000000000000000 0000000000000000 0000000000000004 
[ 005] ffffe00002321d40 _6p1 0000000000000000 0000000000000003 0000000000000004 
[ 006] ffffe00002321d60 pq++ 0000000000000000 0000000000000003 0000000000000004 
[ 007] ffffe00002321d80 pq++ 0000000000000000 0000000000000006 0000000000000004 
[ 008] ffffe00002321da0 _6p0 0000000000000000 ffffe000021c11c0 0000000000000004 
[ 009] ffffe00002321dc0 pqDP 0000000000000000 ffffe000021c11d8 0000000000000006
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






