---
title: "!storagekd.storunit"
description: "The !storagekd.storunit extension displays information about the specified Storport logical unit."
keywords: ["!storagekd.storunit Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- storagekd.storunit
api_type:
- NA
---

# !storagekd.storunit

The **!storagekd.storunit** extension displays information about the specified Storport logical unit.

```dbgcmd
!storagekd.storunit [Address] 
```

## Parameters

<span id="_______Address"></span><span id="_______address"></span><span id="_______ADDRESS"></span> *Address*  
Specifies the address of a Storport unit device object. If *Address* is omitted, a list of all Storport units are displayed.

## DLL

Storagekd.dll

## Remarks

Here is an example of the **!storagekd.storunit** display:

**0: kd&gt; !storagekd.storunit**

```dbgcmd
# STORPORT Units:
==================
## Product                 SCSI ID  Object            Extension         Pnd Out Ct  State
--------------------------------------------------------------------------------------
Msft       Virtual Di   0  0  1  fffffa800658a060  fffffa800658a1b0    0   0  0  Working
```

**0: kd&gt; !storagekd.storunit fffffa800658a060**

```dbgcmd
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
