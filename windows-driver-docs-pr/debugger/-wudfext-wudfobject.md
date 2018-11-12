---
title: wudfext.wudfobject
description: The wudfext.wudfobject extension displays information about a WDF object, as well as its parent and child relationships.
ms.assetid: cb9398fb-24f5-4692-9a08-543bf1317b19
keywords: ["wudfext.wudfobject Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wudfext.wudfobject
api_type:
- NA
ms.localizationpriority: medium
---

# !wudfext.wudfobject


The **!wudfext.wudfobject** extension displays information about a WDF object, as well as its parent and child relationships.

```dbgcmd
!wudfext.wudfobject pWDFObject Flags TypeName
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______pWDFObject______"></span><span id="_______pwdfobject______"></span><span id="_______PWDFOBJECT______"></span> *pWDFObject*   
Specifies the address of the WDF interface to display information about.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. Specifies the type of information to be displayed. *Flags* can be any combination of the following bits. The default value is 0x01.

<span id="Bit_0__0x01_"></span><span id="bit_0__0x01_"></span><span id="BIT_0__0X01_"></span>Bit 0 (0x01)  
Steps recursively through the object hierarchy to obtain the parent and child relationships, which are displayed.

<span id="Bit_1__0x02_"></span><span id="bit_1__0x02_"></span><span id="BIT_1__0X02_"></span>Bit 1 (0x02)  
Displays only summary information about the object.

<span id="Bit_8__0x80_"></span><span id="bit_8__0x80_"></span><span id="BIT_8__0X80_"></span>Bit 8 (0x80)  
Steps recursively through the object hierarchy, and displays details about the internal framework.

<span id="_______TypeName______"></span><span id="_______typename______"></span><span id="_______TYPENAME______"></span> *TypeName*   
Optional. Specifies the type of the interface (for example, **IWDFDevice**). If a value for *TypeName* is supplied, the extension uses the value as the type of the interface. If an asterisk (\*) is supplied as *TypeName*, or if *TypeName* is omitted, the extension attempts to automatically determine the type of the supplied interface.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Wudfext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [User-Mode Driver Framework Debugging](user-mode-driver-framework-debugging.md).

Remarks
-------

You can use **!wudfext.wudfobject** to list, for example, the child objects of an **IWDFDevice** object, which generally include the device's queues.

You can also use **!wudfext.wudfobject** to find WDF objects that are associated with a particular device, to check the state of a WDF object (for example, whether the WDF object is in the process of deletion), or to determine the WDF object's current reference count.

The **!wudfext.wudfobject** extension also displays the callback functions and context objects that the driver associated with each framework object and attempts to determine the framework object's type. This last feature might not work with certain compilers.

The following are some examples. In the first example, [**!wudfext.umdevstacks**](-wudfext-umdevstack.md) gives 0x03050E70 as the address of a device object, and this address is then passed to **!wudfext.wudfobject**. The 0x1 flag is included to display all the children of this object.

```dbgcmd
0: kd> !umdevstacks 
Number of device stacks: 1
  Device Stack: 0x038f6f08    Pdo Name: \Device\USBPDO-11
    Number of UM devices: 1
    Device 0
      Driver Config Registry Path: WUDFOsrUsbFx2
      UMDriver Image Path: D:\Windows\system32\DRIVERS\UMDF\WUDFOsrUsbFx2.dll
      Fx Driver: IWDFDriver 0x3044ff0
      Fx Device: IWDFDevice 0x3050e70
        IDriverEntry: WUDFOsrUsbFx2!CMyDriver 0x0303eff8
      Open UM files (use !umfile <addr> for details): 
        0x049baf84
      Device XFerMode: CopyImmediately RW: Buffered CTL: Buffered
      Object Tracker Address: 0x00000000
        Object   Tracking OFF
        Refcount Tracking OFF
    DevStack XFerMode: CopyImmediately RW: Buffered CTL: Buffered

0: kd> !wudfobject 0x3050e70 1 
IWDFDevice 0x3050e70 Fx: 0x3050e30 [Ref 2]
  15 Children
    00: IWDFIoTarget 0x3056f90 Fx: 0x3056f50 [Ref 3]
        No Children
    01: <Internal>
    02: <Internal>
    03: <Internal>
    04: IWDFIoQueue 0x305ae98 Fx: 0x305ae58 [Ref 8]
        No Children
    05: IWDFIoQueue 0x305ee98 Fx: 0x305ee58 [Ref 2]
        No Children
    06: IWDFIoQueue 0x3060e98 Fx: 0x3060e58 [Ref 2]
        No Children
    07: IWDFIoTarget 0x3066f80 Fx: 0x3066f40 [Ref 2]
        1 Children
          00: IWDFUsbInterface 0x306efd8 Fx: 0x306ef98 [Ref 1]
              3 Children
                00: IWDFIoTarget 0x3074f70 Fx: 0x3074f30 [Ref 2]
                    2 Children
                      00: IWDFMemory 0x30a4ff0 Fx: 0x30a4fb0 [Ref 2]
                          No Children
                      01: IWDFMemory 0x30aaff0 Fx: 0x30aafb0 [Ref 2]
                          No Children
                01: IWDFIoTarget 0x3078f70 Fx: 0x3078f30 [Ref 1]
                    No Children
```

Here is an example of **!wudfext.wudfobject** displaying a file object:

```dbgcmd
kd> !wudfobject 0xf5060 
IWDFFile 0xf5060 Fx: 0xf4fe8 [Ref 1]
  State: Created   Parent: 0xf2f80
  No Children
```

Here is an example of **!wudfext.wudfobject** displaying a driver object:

```dbgcmd
kd> !wudfobject 0xf2db8 0x01 
IWDFDriver 0xf2db8 Fx: 0xf2d40 [Ref 2]
  Callback: (WUDFEchoDriver!CMyDriver, 0xf2c68)
  State: Created   Parent: 0
  1 Children:
    00: IWDFDevice 0xf2f80 Fx: 0xf2f08 [Ref 2]
        State: Created   Parent: 0xf2db8
        5 Children:
          00: IWDFIoTarget 0xf33c0 Fx: 0xf3348 [Ref 3]
              State: Created   Parent: 0xf2f80
              No Children
          01: IWDFIoQueue 0xf3500 Fx: 0xf3488 [Ref 3]
              State: Created   Parent: 0xf2f80
              No Children
          02: IWDFFile 0xf5060 Fx: 0xf4fe8 [Ref 1]
              State: Created   Parent: 0xf2f80
              No Children
          03: IWDFFile 0xf5100 Fx: 0xf5088 [Ref 101]
              State: Created   Parent: 0xf2f80
              No Children
          04: IWDFFile 0xf51a0 Fx: 0xf5128 [Ref 101]
              State: Created   Parent: 0xf2f80
              No Children
```

 

 





