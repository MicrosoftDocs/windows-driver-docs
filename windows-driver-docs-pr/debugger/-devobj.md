---
title: devobj
description: The devobj extension displays detailed information about a DEVICE_OBJECT structure.
ms.assetid: cf722d95-fbd3-4d80-8679-f8fb348ab4b0
keywords: ["devobj Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- devobj
api_type:
- NA
ms.localizationpriority: medium
---

# !devobj


The **!devobj** extension displays detailed information about a DEVICE\_OBJECT structure.

```dbgcmd
!devobj DeviceObject 
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______DeviceObject______"></span><span id="_______deviceobject______"></span><span id="_______DEVICEOBJECT______"></span> *DeviceObject*   
Specifies the device object. This can be the hexadecimal address of this structure or the name of the device.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

See [Plug and Play Debugging](plug-and-play-debugging.md) for examples and applications of this extension command. For information about device objects, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

Remarks
-------

If *DeviceObject* specifies the name of the device but supplies no prefix, the prefix "\\Device\\" is assumed. Note that this command will check to see if *DeviceObject* is a valid address or device name before using the expression evaluator.

The information displayed includes the device name of the object, information about the device's current IRP, and a list of addresses of any pending IRPs in the device's queue. It also includes information about device objects layered on top of this object (listed as "AttachedDevice") and those layered under this object (listed as "AttachedTo").

The address of a device object can be obtained using the [**!drvobj**](-drvobj.md) or [**!devnode**](-devnode.md) extensions.

Here is one example:

```dbgcmd
kd> !devnode
Dumping IopRootDeviceNode (= 0x80e203b8)
DevNode 0x80e203b8 for PDO 0x80e204f8
 Parent 0000000000   Sibling 0000000000   Child 0x80e56dc8
  InstancePath is "HTREE\ROOT\0"
  State = DeviceNodeStarted (0x308)
  Previous State = DeviceNodeEnumerateCompletion (0x30d)
  StateHistory[04] = DeviceNodeEnumerateCompletion (0x30d)
  StateHistory[03] = DeviceNodeStarted (0x308)
  StateHistory[02] = DeviceNodeEnumerateCompletion (0x30d)
  StateHistory[01] = DeviceNodeStarted (0x308)
  StateHistory[00] = DeviceNodeUninitialized (0x301)
  StateHistory[19] = Unknown State (0x0)
  .....
  StateHistory[05] = Unknown State (0x0)
  Flags (0x00000131)  DNF_MADEUP, DNF_ENUMERATED, 
                      DNF_IDS_QUERIED, DNF_NO_RESOURCE_REQUIRED
  DisableableDepends = 11 (from children)

kd> !devobj 80e204f8
Device object (80e204f8) is for:
  \Driver\PnpManager DriverObject 80e20610
Current Irp 00000000 RefCount 0 Type 00000004 Flags 00001000
DevExt 80e205b0 DevObjExt 80e205b8 DevNode 80e203b8 
ExtensionFlags (0000000000)  
Device queue is not busy.
```

 

 





