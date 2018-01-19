---
title: usbkd.usbportmdportlog
description: The usbkd.usbportmdportlog command displays the USBPORT debug log if it is present in a crash dump that was generated as a result of Bug Check 0xFE.
ms.assetid: C0E32BDE-8186-4477-AB57-530B0AF6F27F
keywords: ["usbkd.usbportmdportlog Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usbkd.usbportmdportlog
api_type:
- NA
---

# !usbkd.usbportmdportlog


The **!usbkd.usbportmdportlog** command displays the USBPORT debug log if it is present in a crash dump that was generated as a result of [**Bug Check 0xFE**](bug-check-0xfe--bugcode-usb-driver.md).

```
!usbkd.usbportmdportlog
```

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Remarks
-------

Use this command only when you are debugging a crash dump file that was generated as a result of [**Bug Check 0xFE: BUGCODE\_USB\_DRIVER**](bug-check-0xfe--bugcode-usb-driver.md).

Examples
--------

Here is an example of a portion of the output of **!usbportmdportlog**.

```
1: kd> !analyze -v
*** ...
BUGCODE_USB_DRIVER (fe) 
...
1: kd> !usbkd.usbportmdportlog
Minidump USBPORT DEBUG_LOG buffer size 32768, entries 1024, index 400
*LOG: 0000000113be9600  LOGSTART: 0000000113be6400 *LOGEND: 0000000113bee3e0 # 1024 
[ 000] 0000000113be9600 Bfe2 ffffe0001416802c ffffe000020a44f0 ffffe0001416801c 
[ 001] 0000000113be9620 Bfe0 0000000000000000 ffffe000039f4720 ffffe00000b76cb0 
[ 002] 0000000113be9640 epr+ ffffe000043ee010 ffffe000008f5b80 ffffe00002820a0c 
[ 003] 0000000113be9660 alTR ffffe00002820a0c ffffe000039f4720 ffffe00000b76cb0 
//
// USBPORT_Core_AllocTransferEx()
// transfer:                ffffe00002820a0c
// Urb:                     ffffe000039f4720
// Irp:                     ffffe00000b76cb0

[ 004] 0000000113be9680 TRcs 0000000000000060 0000000000000468 0000000000000001 
[ 005] 0000000113be96a0 urbi ffffe0001422c4cc 0000000000000012 000000000000000b 
[ 006] 0000000113be96c0 dURB ffffe000039f4720 ffffe00000b76cb0 000000000000000b 
//
// USBPORT_ProcessURB() - Device Handle valid and has been referenced
// Urb:                     ffffe000039f4720
// Irp:                     ffffe00000b76cb0
// function:                URB_FUNCTION_GET_DESCRIPTOR_FROM_DEVICE

[ 007] 0000000113be96e0 vld> ffffe0001421ddd0 0000000000000004 ffffe000039f4720 
//
// USBPORT_NeoValidDeviceHandle()
// DeviceHandle:            ffffe0001421ddd0
// ReferenceObj:            ffffe000039f4720

[ 008] 0000000113be9700 devH ffffe0001421ddd0 ffffe000039f4720 0000000000000000 
[ 009] 0000000113be9720 pURB ffffe000039f4720 ffffe00000b76cb0 000000000000000b 
//
// USBPORT_ProcessURB()
// Urb:                     ffffe000039f4720
// Irp:                     ffffe00000b76cb0
// function:                URB_FUNCTION_GET_DESCRIPTOR_FROM_DEVICE

[ 010] 0000000113be9740 PURB ffffe000039f4720 ffffe000020a44f0 000000000000000b 
//
// USBPORT_ProcessURB() - Exit STATUS_PENDING
// Urb:                     ffffe000039f4720
// Irp:                     ffffe000020a44f0
// function:                URB_FUNCTION_GET_DESCRIPTOR_FROM_DEVICE

[ 011] 0000000113be9760 Urb< 0000000000000103 000000000000000b 0000000000000000 
[ 012] 0000000113be9780 xSt0 ffffe000012bbf18 0000000000000006 0000000000000001 
[ 013] 0000000113be97a0 xnd8 ffffe000012bbf18 ffffe000012bb050 0000000000000000 
[ 014] 0000000113be97c0 xnd0 ffffe000012bbf18 ffffe000012bb050 0000000000000000 
//
// USBPORT_Xdpc_End()

[ 015] 0000000113be97e0 mapF 0000000000000000 0000000000000000 0000000000000000 
[ 016] 0000000113be9800 map5 0000000000000000 0000000000000000 0000000000000000 
[ 017] 0000000113be9820 DMAx 0000000000000000 0000000000000000 0000000000000000 
[ 018] 0000000113be9840 subx 0000000000000000 0000000000000000 ffffe0001416801c 
[ 019] 0000000113be9860 tmoZ 0000000000000000 ffffe0001416801c ffffe000141680a4 
...
...
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usbkd.usbportmdportlog%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





