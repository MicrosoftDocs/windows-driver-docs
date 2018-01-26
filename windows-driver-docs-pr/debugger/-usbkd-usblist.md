---
title: usbkd.usblist
description: The usbkd.usblist command displays a linked list of structures of a specified type.
ms.assetid: 503466EE-2246-4CE3-BCE7-6DC7D42DB86A
keywords: ["usbkd.usblist Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usbkd.usblist
api_type:
- NA
---

# !usbkd.usblist


The **!usbkd.usblist** command displays a linked list of structures of a specified type.

```
!usbkd.usblist ListAddr, ListType
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______ListAddr______"></span><span id="_______listaddr______"></span><span id="_______LISTADDR______"></span> *ListAddr*   
Address of a linked list of structures. To find addresses of linked lists maintained by the USB port driver, use [**!usbhcdext**](-usbkd-usbhcdext.md). To find addresses of linked list maintained by the USB hub driver, use [**!usbhubext**](-usbkd-usbhubext.md).

<span id="_______ListType______"></span><span id="_______listtype______"></span><span id="_______LISTTYPE______"></span> *ListType*   
One of the following list types.

| List type | Structure                                |
|-----------|------------------------------------------|
| **BC**    | **usbport!\_BUS\_CONTEXT**               |
| **EP**    | **usbport!\_HCD\_ENDPOINT**              |
| **TT**    | **usbport!\_TRANSACTION\_TRANSLATOR**    |
| **DL**    | **usbport!\_USBD\_DEVICE\_HANDLE**       |
| **PL**    | **usbhub!\_DEVICE\_EXTENSION\_PDO**      |
| **EL**    | **usbhub!\_HUB\_EXCEPTION\_RECORD**      |
| **RL**    | **usbhub!\_HUB\_REFERENCE\_LIST\_ENTRY** |
| **TL**    | **usbhub!\_HUB\_TIMER\_OBJECT**          |
| **WI**    | **usbhub!\_HUB\_WORKITEM**               |
| **IO**    | **usbhub!\_IO\_LIST\_ENTRY**             |
| **LA**    | **usbhub!\_LATCH\_LIST\_ENTRY**          |
| **CL**    | **usbhub!\_PORT\_CHANGE\_CONTEXT**       |
| **BL**    | **usbhub!\_SSP\_BUSY\_HANDLE**           |

 

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is one way to find the address of a linked list. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```
0: kd> !usbkd.usb2tree
...
2)!ehci_info ffffe00001ca11a0 !devobj ffffe00001ca1050 ...
   ...
```

In the preceding output, the address of the device extension of the FDO is displayed as the argument of the [DML](debugger-markup-language-commands.md) command **!ehci\_info ffffe00001ca11a0**.

Either click the DML command or pass the address of the device extension to [**!usbhcdext**](https://msdn.microsoft.com/library/windows/hardware/dn367072).

```
0: kd> !usbkd.usbhcdext ffffe00001ca11a0

HC Flavor 1000  FDO ffffe00001ca1050
Root Hub: FDO ffffe00002320050 !hub2_info ffffe000023201a0
...
DeviceHandleList: !usblist ffffe00001ca23b8, DL
...
```

In the preceding output, ffffe00001ca23b8 is the address of a linked list of **usbport!\_USBD\_DEVICE\_HANDLE** structures.

Now pass the address of the linked list to **!usblist**.

```
0: kd> !usblist ffffe00001ca23b8, DL
list: ffffe00001ca23b8 DL
----------
!usbdevh ffffe000020f9590
SSP [IdleReady] (0)
PCI\VEN_Xxxx  Xxxx Corporation
Root Hub
DriverName :  
----------
!usbdevh ffffe00001bce250
SSP [IdleReady] (0)
USB\Xxxx  Xxxx Corporation
Speed: HIGH, Address:  1, PortPathDepth: 1, PortPath: [3 0 0 0 0 0]
DriverName :\Driver\USBSTOR      !devstack ffffe000053ef2a0
----------
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usbkd.usblist%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





