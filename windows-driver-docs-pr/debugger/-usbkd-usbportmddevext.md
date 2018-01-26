---
title: usbkd.usbportmddevext
description: The usbkd.usbportmddevext command displays a usbport _DEVICE_EXTENSION structure if one is present in a crash dump that was generated as a result Bug Check 0xFE.
ms.assetid: 07DE5D4A-E909-4D9B-B906-B74C9CC8AE49
keywords: ["usbkd.usbportmddevext Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usbkd.usbportmddevext
api_type:
- NA
---

# !usbkd.usbportmddevext


The **!usbkd.usbportmddevext** command displays a **usbport!\_DEVICE\_EXTENSION** structure if one is present in a crash dump that was generated as a result [**Bug Check 0xFE**](bug-check-0xfe--bugcode-usb-driver.md).

```
!usbkd.usbportmddevext
```

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Remarks
-------

Use this command only when you are debugging a crash dump file that was generated as a result of [**Bug Check 0xFE: BUGCODE\_USB\_DRIVER**](bug-check-0xfe--bugcode-usb-driver.md).

Examples
--------

Here is an example of the output of **!usbportmddevext**.

```
1: kd> !analyze -v
*** ...
BUGCODE_USB_DRIVER (fe) 
...
1: kd> !usbkd.usbportmddevext
USBPORT.SYS DEVICE_EXTENSION DATA: 
Hcd FDO Extension:
Sig:4f444648 HFDO
CurrentPnpFunc: 0x00000008
PnpFuncHistoryIdx: 0x0000000d
CurrentPowerFunc: 0x00000000
PowerFuncHistoryIdx: 0x00000000
PnpLogIdx: 0x00000002
IoRequestCount: 0x00000007
IoRequestAsyncCallbackCount: 0xffffffff
IoRequestAllow: 0x00000000
Pnp Func History (idx 13)
...
[02] pnp 13 (0d) IRP_MN_FILTER_RESOURCE_REQUIREMENTS
[...
Power Func History (idx 0)
[01] pnp 255 (ff) ??? (x0) PowerDeviceUnspecified
...
    **Power and Wake -----------------------------------------------
    selective suspend:on (1)
    PowerFlags (00000080):
*---FDO---*
PMDebug: 0x00000000
MinAllocedBw: 0x00000000
MaxAllocedBw: 0x00000000
## ...

## XDPC HISTORY_UsbHcIntDpc

State History (idx 2)
EVENT, STATE, NEXT 
Log[3] @ 000000d9e7c615cc  
Ev_Xdpc_Worker       XDPC_DpcQueued          XDPC_Running            
## ...        

## XDPC HISTORY_UsbDoneDpc

State History (idx 0)
EVENT, STATE, NEXT 
Log[1] @ 000000d9e7c61774  
Ev_Xdpc_Worker       XDPC_DpcQueued          XDPC_Running            
## ...          

## XDPC HISTORY_UsbMapDpc

State History (idx 3)
EVENT, STATE, NEXT 
Log[4] @ 000000d9e7c6196c  
## ...         

## XDPC HISTORY_UsbIocDpc

State History (idx 0)
EVENT, STATE, NEXT 
Log[1] @ 000000d9e7c61b04  
Ev_Xdpc_Worker       XDPC_DpcQueued          XDPC_Running            
...           
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usbkd.usbportmddevext%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





