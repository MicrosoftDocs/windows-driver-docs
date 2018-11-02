---
title: vpb
description: The vpb extension displays a volume parameter block (VPB).
ms.assetid: 978d4ec8-6141-4656-9e5c-266de91c9440
keywords: ["vpb Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- vpb
api_type:
- NA
ms.localizationpriority: medium
---

# !vpb


The **!vpb** extension displays a volume parameter block (VPB).

```dbgcmd
!vpb Address
```

## <span id="ddk__vpb_dbg"></span><span id="DDK__VPB_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the VPB.

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

For information about VPBs, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

Here is an example. First, the device tree is displayed with the [**!devnode**](-devnode.md) extension:

```dbgcmd
kd> !devnode 0 1
Dumping IopRootDeviceNode (= 0x80e203b8)
DevNode 0x80e203b8 for PDO 0x80e204f8
  InstancePath is "HTREE\ROOT\0"
  State = DeviceNodeStarted (0x308)
  Previous State = DeviceNodeEnumerateCompletion (0x30d)
  DevNode 0x80e56dc8 for PDO 0x80e56f18
    InstancePath is "Root\dmio\0000"
    ServiceName is "dmio"
    State = DeviceNodeStarted (0x308)
    Previous State = DeviceNodeEnumerateCompletion (0x30d)
  DevNode 0x80e56ae8 for PDO 0x80e56c38
    InstancePath is "Root\ftdisk\0000"
    ServiceName is "ftdisk"
    State = DeviceNodeStarted (0x308)
    Previous State = DeviceNodeEnumerateCompletion (0x30d)
 DevNode 0x80e152a0 for PDO 0x80e15cb8
      InstancePath is "STORAGE\Volume\1&30a96598&0&Signature5C34D70COffset7E00Length60170A00"
      ServiceName is "VolSnap"
      TargetDeviceNotify List - f 0xe1250938  b 0xe14b9198
      State = DeviceNodeStarted (0x308)
      Previous State = DeviceNodeEnumerateCompletion (0x30d)
    .....
```

The last device node listed is a volume. Examine its physical device object (PDO) with the [**!devobj**](-devobj.md) extension:

```dbgcmd
kd> !devobj 80e15cb8
Device object (80e15cb8) is for:
 HarddiskVolume1 \Driver\Ftdisk DriverObject 80e4e248
Current Irp 00000000 RefCount 14 Type 00000007 Flags 00001050
Vpb 80e15c30 DevExt 80e15d70 DevObjExt 80e15e40 Dope 80e15bd8 DevNode 80e152a0 
ExtensionFlags (0000000000)  
AttachedDevice (Upper) 80e14c60 \Driver\VolSnap
Device queue is not busy.
```

The address of this device's VPB is included in this listing. Use this address with the **!vpb** extension:

```dbgcmd
kd> !vpb 80e15c30
Vpb at 0x80e15c30
Flags: 0x1 mounted 
DeviceObject: 0x80de5020
RealDevice:   0x80e15cb8
RefCount: 14
Volume Label:           MY-DISK-C
```

 

 





