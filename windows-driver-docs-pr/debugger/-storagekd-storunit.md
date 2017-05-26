---
title: storagekd.storunit
description: The storagekd.storunit extension displays information about the specified Storport logical unit.
ms.assetid: 73A2632C-962E-4075-97B9-5D7D843E9D0F
keywords: ["storagekd.storunit Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- storagekd.storunit
api_type:
- NA
---

# !storagekd.storunit


The **!storagekd.storunit** extension displays information about the specified Storport logical unit.

```
    !storagekd.storunit [Address] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address"></span><span id="_______address"></span><span id="_______ADDRESS"></span> *Address*  
Specifies the address of a Storport unit device object. If *Address* is omitted, a list of all Storport units are displayed.

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

Here is an example of the **!storagekd.storunit** display:

**0: kd&gt; !storagekd.storunit**

```
# STORPORT Units:
==================
## Product                 SCSI ID  Object            Extension         Pnd Out Ct  State
--------------------------------------------------------------------------------------
Msft       Virtual Di   0  0  1  fffffa800658a060  fffffa800658a1b0    0   0  0  Working
```

**0: kd&gt; !storagekd.storunit fffffa800658a060**

```
   DO fffffa800658a060   Ext fffffa800658a1b0   Adapter fffffa800649a1a0   Working
   Vendor: Msft       Product: Virtual Disk       SCSI ID: (0, 0, 1)   
   Claimed Enumerated 
   SlowLock Free   RemLock 1   PageCount 0
   QueueTagList: fffffa800658a270      Outstanding: Head fffffa800658a398  Tail fffffa800658a398  Timeout -1
   DeviceQueue fffffa800658a2a0   Depth: 250   Status: Not Frozen   PauseCount: 0   BusyCount: 0   
   IO Gateway: Busy Count 0   Pause Count 0
   Requests: Outstanding 0   Device 0   ByPass 0


[Device-Queued Requests]

## IRP               SRB Type   SRB               XRB               Command           MDL               SGList            Timeout
-----------------------------------------------------------------------------------------------------------------------------------


[Bypass-Queued Requests]

## IRP               SRB Type   SRB               XRB               Command           MDL               SGList            Timeout
-----------------------------------------------------------------------------------------------------------------------------------


[Outstanding Requests]

## IRP               SRB Type   SRB               XRB               Command           MDL               SGList            Timeout
-----------------------------------------------------------------------------------------------------------------------------------


[Completed Requests]

IRP               SRB Type   SRB               XRB               Command           MDL               SGList            Timeout
-----------------------------------------------------------------------------------------------------------------------------------
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!storagekd.storunit%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




