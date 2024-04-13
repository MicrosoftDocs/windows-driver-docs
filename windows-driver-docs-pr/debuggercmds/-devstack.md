---
title: "!devstack (WinDbg)"
description: "The !devstack extension displays a formatted view of the device stack associated with a device object."
keywords: ["!devstack Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- devstack
api_type:
- NA
---

# !devstack


The **!devstack** extension displays a formatted view of the device stack associated with a device object.

```dbgcmd
!devstack DeviceObject 
```

## <span id="ddk__devstack_dbg"></span><span id="DDK__DEVSTACK_DBG"></span>Parameters


<span id="_______DeviceObject______"></span><span id="_______deviceobject______"></span><span id="_______DEVICEOBJECT______"></span> *DeviceObject*   
Specifies the device object. This can be the hexadecimal address of the DEVICE\_OBJECT structure or the name of the device.

### DLL

Kdexts.dll

 

## Additional Information

For information about device stacks, see the Windows Driver Kit (WDK) documentation.

## Remarks

If *DeviceObject* specifies the name of the device but supplies no prefix, the prefix "\\Device\\" is assumed. Note that this command will check to see if *DeviceObject* is a valid address or device name before using the expression evaluator.

Here is an example:

```dbgcmd
kd> !devstack e000000085007b50
 !DevObj   !DrvObj            !DevExt   ObjectName
  e0000165fff32040  \Driver\kmixer     e0000165fff32190  
> e000000085007b50  \Driver\swenum     e000000085007ca0  KSENUM#00000005
!DevNode e0000165fff2e010 :
  DeviceInst is "SW\{b7eafdc0-a680-11d0-96d8-00aa0051e51d}\{9B365890-165F-11D0-A195-0020AFD156E4}"
 ServiceName is "kmixer"
```

