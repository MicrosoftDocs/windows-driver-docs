---
title: wudfext.wudfdumpobjects
description: The wudfext.wudfdumpobjects extension displays outstanding UMDF objects.
ms.assetid: 2ede7f2e-124c-494d-9188-5a28617a0bdb
keywords: ["wudfext.wudfdumpobjects Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wudfext.wudfdumpobjects
api_type:
- NA
ms.localizationpriority: medium
---

# !wudfext.wudfdumpobjects


The **!wudfext.wudfdumpobjects** extension displays outstanding UMDF objects.

```dbgcmd
!wudfext.wudfdumpobjects ObjTrackerAddress
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______ObjTrackerAddress______"></span><span id="_______objtrackeraddress______"></span><span id="_______OBJTRACKERADDRESS______"></span> *ObjTrackerAddress*   
Specifies the address to track leaked objects. This address is displayed in the driver-stop message in the debugger when a leak occurs.

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
<td align="left"><p><strong>Windows XP with UMDF version 1.7 and later</strong></p></td>
<td align="left"><p>Wudfext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [User-Mode Driver Framework Debugging](user-mode-driver-framework-debugging.md).

Remarks
-------

If the UMDF object tracking option (**TrackObjects**) has been enabled in WDF Verifier, you can use **!wudfext.wudfdumpobjects** to see any leaked objects that remain after the driver unloads.

If the **TrackObjects** option has been enabled, the address of the object tracker is automatically displayed when a leak is detected. Use this address as *ObjTrackerAddress* when executing **!wudfext.wudfdumpobjects**.

This extension can be used at any time, even if UMDF has not broken in to the debugger.

If UMDF is version 1.9 or above, you can use either [**!wudfext.umdevstack**](-wudfext-umdevstack.md) or [**!wudfext.umdevstacks**](-wudfext-umdevstacks.md) to determine the address of the object tracker. This address can then be passed to **!wudfext.wudfdumpobjects**. Here is an example:

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

0: kd> !wudfdumpobjects 0x03074fd8 
WdfTypeDriver    Object: 0x03076fb0, Interface: 0x03076ff0
WdfTypeDevice   Object: 0x03082e30, Interface: 0x03082e70
WdfTypeIoTarget Object: 0x03088f50, Interface: 0x03088f90
WdfTypeIoQueue                Object: 0x0308ce58, Interface: 0x0308ce98
WdfTypeIoQueue                Object: 0x03090e58, Interface: 0x03090e98
WdfTypeIoQueue                Object: 0x03092e58, Interface: 0x03092e98
WdfTypeIoTarget Object: 0x03098f40, Interface: 0x03098f80
WdfTypeFile         Object: 0x0309cfa0, Interface: 0x0309cfe0
WdfTypeUsbInterface         Object: 0x030a0f98, Interface: 0x030a0fd8
WdfTypeRequest Object: 0x030a2ef8, Interface: 0x030a2f38
WdfTypeIoTarget Object: 0x030a6f30, Interface: 0x030a6f70
WdfTypeIoTarget Object: 0x030aaf30, Interface: 0x030aaf70
WdfTypeIoTarget Object: 0x030aef30, Interface: 0x030aef70
WdfTypeRequest Object: 0x030c6ef8, Interface: 0x030c6f38
WdfTypeRequest Object: 0x030ceef8, Interface: 0x030cef38
WdfTypeMemoryObject    Object: 0x030d6fb0, Interface: 0x030d6ff0
WdfTypeMemoryObject    Object: 0x030dcfb0, Interface: 0x030dcff0
WdfTypeFile         Object: 0x030e4fa8, Interface: 0x030e4fe8
WdfTypeFile         Object: 0x030e6fa8, Interface: 0x030e6fe8
WdfTypeFile         Object: 0x030e8fa8, Interface: 0x030e8fe8
WdfTypeRequest Object: 0x030eaef8, Interface: 0x030eaf38
WdfTypeMemoryObject    Object: 0x030ecfb0, Interface: 0x030ecff0
WdfTypeMemoryObject    Object: 0x030eefb0, Interface: 0x030eeff0
```

 

 





