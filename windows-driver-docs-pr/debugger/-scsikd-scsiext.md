---
title: scsikd.scsiext
description: The scsikd.scsiext extension displays detailed information about the specified SCSI port extension.
ms.assetid: 0fcb0545-eb5a-4500-8e14-a5296624c80b
keywords: ["scsikd.scsiext Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- scsikd.scsiext
api_type:
- NA
---

# !scsikd.scsiext


The **!scsikd.scsiext** extension displays detailed information about the specified SCSI port extension.

``` syntax
    !scsikd.scsiext Device 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Device______"></span><span id="_______device______"></span><span id="_______DEVICE______"></span> *Device*   
Specifies the device object or device extension of a SCSI port extension.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Scsikd.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Scsikd.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [SCSI Miniport Debugging](scsi-miniport-debugging.md).

Remarks
-------

Here is an example of the **!scsikd.scsiext** display, where the SCSI port extension has been specified by a functional device object (FDO); this can be obtained from the **DO** field or **DevExt** field in the [**!minipkd.adapters**](-minipkd-adapters.md) display:

```
kd> !scsikd.scsiext 816f9a40 
Scsiport functional device extension at address 816f9af8
Common Extension:
  Initialized
  DO 0x816f9a40  LowerObject 0x816e8030  SRB Flags 00000000
  Current Power (D0,S0)  Desired Power D-1 Idle 00000000
  Current PnP state 0x0    Previous state 0xff
  DispatchTable f9aee200   UsePathCounts (P0, H0, C0)
Adapter Extension:
  Port 2     IsPnp VirtualSlot HasInterrupt
  LowerPdo 0x816e8030   HwDevExt 0x8170a004   Active Requests 0xffffffff
  MaxBus 0x01   MaxTarget 0x10   MaxLun 0x08
  Port Flags (0x00001000): PD_DISCONNECT_RUNNING
  NonCacheExt 0x81702000  IoBase 0x00002000   Int 0x1a
  RealBus# 0x0  RealSlot# 0x2
  Timeout 0xffffffff   DpcFlags 0x00000000   Sequence 0x00000003
  Srb Ext Header 0x817061a0   No. Requests 0x00000012
  QueueTag BitMap 0x00000000   Hint 0x00000000
  MaxQueueTag 0xfe (@0x816f9c58)
  LuExt Size 0x00000038   SrbExt Size 0x00000188
    SG List Size - Small 17   Large 0
    Emergency  - SrbData 0x816f9830  Blocked List @0x816f9e94
    CommonBuff - Size: 0x00006000    PA: 0x0000000001702000  VA: 0x81702000
    Ke Objects - Int1: 0x8175ba50    Int2: 0x00000000        Dma: 0x816f9340
    Lookaside  - SrbData @ 0x816f9e40 SgList @0x00000000  Remove: @0x00000000
    Resources  - Raw: 0x817ba190     Translated: 0x81709678
    Port Config 8177fde8
    DeviceMap Handles: Port 0000009c    Busses e12d7b38
  Interrupt Data @0x816f9ce4:
    Flags (0x00000000):
    Ready LUN 0x00000000   Wmi Events 0x00000000
    Completed Request List (@0x816f9ce8): 0 entries
    LUN 816ea0e8 @ (  0,  1,  0) c ev  pnp(00/ff) pow(0 ,0) DevObj 816ea030
```

Here is an example of the **!scsikd.scsiext** display, where the SCSI port extension has been specified by a physical device object (PDO); this can be obtained from the **DevObj** field or **LUN** field in the [**!minipkd.adapters**](-minipkd-adapters.md) display:

```
kd> !scsikd.scsiext 816ea030
Scsiport physical device extension at address 816ea0e8
Common Extension:
  Initialized
  DO 0x816ea030  LowerObject 0x816f9a40  SRB Flags 00000000
  Current Power (D0,S0)  Desired Power D-1 Idle 0x8176c780
  Current PnP state 0x0    Previous state 0xff
  DispatchTable f9aee180   UsePathCounts (P0, H0, C0)
Logical Unit Extension:
  Address (2, 0, 1, 0) Claimed  Enumerated Visible
  LuFlags (0x00000000):
  Retry 0x00          Key 0x00000000
  Lock 0x00000000  Pause 0x00000000   CurrentLock: 0x00000000
  HwLuExt 0x8177ce10  Adapter 0x816f9af8  Timeout 0xffffffff
  NextLun 0x00000000  ReadyLun 0x00000000
  Pending 0x00000000  Busy 0x00000000     Untagged 0x00000000
  Q Depth 000 (1628450047)   InquiryData 0x816ea206
  DeviceMap Keys: Target 0x0000d0   Lun 00000000
  Bypass SRB_DATA blocks 4 @ 816ea270   List 816ea810
  RS Irp 8177dd80  Srb @ 816eaa0c   MDL @ 816eaa4c
  Request List @0x816ea1f0 is empty
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!scsikd.scsiext%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




