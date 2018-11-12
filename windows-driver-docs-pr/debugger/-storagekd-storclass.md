---
title: storagekd.storclass
description: The storagekd.storclass extension displays information about the specified classpnp device.
ms.assetid: EC5B44F5-540E-4F25-80AA-09BE4F78BF72
keywords: ["storagekd.storclass Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- storagekd.storclass
api_type:
- NA
ms.localizationpriority: medium
---

# !storagekd.storclass


The **!storagekd.storclass** extension displays information about the specified *classpnp* device.

```dbgcmd
!storagekd.storclass [Address [Level]] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address"></span><span id="_______address"></span><span id="_______ADDRESS"></span> *Address*  
Specifies the address to the device object or device extension of a classpnp device. If *Address* is omitted, a list of all classpnp extensions is displayed.

<span id="_______Level"></span><span id="_______level"></span><span id="_______LEVEL"></span> *Level*  
Specifies the amount of detail to display. This parameter can be set to 0, 1, or 2, with 2 giving the most detail and 0 the least. The default is 0.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 8 and later</strong></p></td>
<td align="left"><p>Storagekd.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Here is an example of the **!storagekd.storclass** display:

**1: kd&gt; !storagekd.storclass**

```dbgcmd
Storage class devices:

* !storclass fffffa80043dc060 [1,2] ST3160812AS Paging Disk       
  !storclass fffffa8006581740 [1,2] Msft Virtual Disk Disk       

Usage: !storclass <class device> <level [0-2]>
```

**1: kd&gt; !storagekd.storclass fffffa80043dc060 1**

```dbgcmd
Storage class device fffffa80043dc060 with extension at fffffa80043dc1b0

Classpnp Internal Information at fffffa8003bec360

    Transfer Packet Engine:

     Packet          Status  DL Irp          Opcode  Sector/ListId   UL Irp 
    --------         ------ --------         ------ --------------- --------

    Pending Idle Requests: 0x0


    -- dt classpnp!_CLASS_PRIVATE_FDO_DATA fffffa8003bec360 --

Classpnp External Information at fffffa80043dc1b0

    ST3160812AS 3.ADH             9LS20QRL 

    Minidriver information at fffffa80043dc670
    Attached device object at fffffa800410a060
    Physical device object at fffffa800410a060

    Media Geometry:

        Bytes in a Sector = 512
        Sectors per Track = 63
        Tracks / Cylinder = 255
        Media Length      = 160000000000 bytes = ~149 GB

    -- dt classpnp!_FUNCTIONAL_DEVICE_EXTENSION fffffa80043dc1b0 --
```

 

 





