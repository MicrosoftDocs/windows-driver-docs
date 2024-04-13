---
title: "!wudfext.umdevstacks"
description: "The !wudfext.umdevstacks extension displays information about all device stacks in the current host process."
keywords: ["!wudfext.umdevstacks Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wudfext.umdevstacks
api_type:
- NA
---

# !wudfext.umdevstacks

The **!wudfext.umdevstacks** extension displays information about all device stacks in the current host process.

```dbgcmd
!wudfext.umdevstacks [Flags] 
```

## Parameters

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. Specifies the type of information to be displayed. *Flags* can be any combination of the following bits. The default value is 0x01.

<span id="Bit_0__0x01_"></span><span id="bit_0__0x01_"></span><span id="BIT_0__0X01_"></span>Bit 0 (0x01)  
Displays detailed information about each device stack.

<span id="Bit_8__0x80_"></span><span id="bit_8__0x80_"></span><span id="BIT_8__0X80_"></span>Bit 8 (0x80)  
Displays information about the internal framework.

## DLL

Wudfext.dll
 
### Remarks

The **!wudfext.umdevstacks** extension displays the framework interface objects that are associated with each device stack. For more information about using the output from **!wudfext.umdevstacks**, see [**!wudfext.umdevstack**](-wudfext-umdevstack.md).

The **!wudfext.umdevstacks** output includes two fields entitled "Object Tracking" and "Refcount Tracking". These indicate whether the object tracking option (**TrackObjects**) and the reference count tracking option (**TrackRefCounts**) have been enabled in WDF Verifier, respectively. If the object tracking option has been enabled, the display includes the object tracker address; this address can be passed to [**!wudfext.wudfdumpobjects**](-wudfext-wudfdumpobjects.md) to display tracking information.

Here is an example of the **!wudfext.umdevstacks** display:

```dbgcmd
0: kd> !umdevstacks 
Number of device stacks: 1
  Device Stack: 0x038c6f08    Pdo Name: \Device\USBPDO-11
    Number of UM devices: 1
    Device 0
      Driver Config Registry Path: WUDFOsrUsbFx2
      UMDriver Image Path: D:\Windows\system32\DRIVERS\UMDF\WUDFOsrUsbFx2.dll
      Fx Driver: IWDFDriver 0x3076ff0
      Fx Device: IWDFDevice 0x3082e70
        IDriverEntry: WUDFOsrUsbFx2!CMyDriver 0x0306eff8
      Open UM files (use !umfile <addr> for details): 
        0x04a8ef84
      Device XFerMode: CopyImmediately RW: Buffered CTL: Buffered
      Object Tracker Address: 0x03074fd8
        Object   Tracking ON
        Refcount Tracking OFF
    DevStack XFerMode: CopyImmediately RW: Buffered CTL: Buffered
```

## Additional Information

For more information, see [User-Mode Driver Framework Debugging](../debugger/user-mode-driver-framework-debugging.md).
