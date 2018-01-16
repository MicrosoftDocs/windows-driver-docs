---
title: wdfkd.wdfchildlist
description: The wdfkd.wdfchildlist extension displays a child list's state and information about all of the device identification descriptions that are in the child list.
ms.assetid: b224e898-0e49-431e-a748-ea12ff3b3513
keywords: ["wdfkd.wdfchildlist Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- wdfkd.wdfchildlist
api_type:
- NA
---

# !wdfkd.wdfchildlist


The **!wdfkd.wdfchildlist** extension displays a child list's state and information about all of the device identification descriptions that are in the child list.

```
!wdfkd.wdfchildlist Handle 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A WDFCHILDLIST-typed handle to the child list.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

The following example shows a **!wdfkd.wdfchildlist** display.

```
kd> !wdfchildlist 0x7cc090c8 

## Dumping WDFCHILDLIST 0x7cc090c8
---------------------------------------
owning !WDFDEVICE 0x7ca7b1c0
ID description size 0x8

State:
-----
List is unlocked, changes will be applied immediately
No scans or enumerations are active on the list

Descriptions:
------------
 PDO !WDFDEVICE 0x7cad31c8, ID description 0x83ac4ff4
 +Device WDM !devobj 0x81fb00e8, WDF pnp state WdfDevStatePnpStarted (0x119)
 +Device found in last scan

No pending insertions are in the list.

Callbacks:
---------
 EvtChildListCreateDevice:  wdfrawbusenumtest!RawBus_RawPdo_Create (f22263b0)
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!wdfkd.wdfchildlist%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




