---
title: Analyzing Stalled Drivers and Time-Outs
description: Analyzing Stalled Drivers and Time-Outs
ms.assetid: c305acba-48b9-4597-925a-8b1ded4f0048
keywords: ["SCSI Miniport Debugging, hangs and time-outs"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Analyzing Stalled Drivers and Time-Outs


When debugging a SCSI miniport driver, the three most common causes for hangs and time-outs are:

-   The SCSI miniport DPC is not running

-   The SCSI miniport fails to ask for the next request

-   A request is not being completed by the SCSI miniport, usually because it is waiting for map registers.

If you suspect that the SCSI miniport DPC is not running, use [**!pcr**](-pcr.md) to display the DPC queue for the current processor. If the SCSI port DPC routine is in the DPC queue, place a breakpoint on this routine to determine whether this routine is ever called. Otherwise, use [**!scsikd.scsiext**](-scsikd-scsiext.md) on each device. Consider the following sample output from the **!scsikd.scsiext** extension:

```dbgcmd
0: kd> !scsikd.scsiext 86353040 
Common Extension:
   < ..omitted.. >
Logical Unit Extension:
  Address (3, 0, 1, 0) Claimed  Enumerated Visible
  LuFlags (0x00000000):
  Retry 0x00          Key 0x008889ff
  Lock 0x00000000  Pause 0x00000000   CurrentLock: 0x00000000
  HwLuExt 0x862e6f00  Adapter 0x8633db28  Timeout 0x0000000a
  NextLun 0x00000000  ReadyLun 0x00000000
  Pending 0x00000000  Busy 0x00000000     Untagged 0x00000000
 
  . . .  
 
Request list @0x86353200:
      Tick count is 2526
      SrbData 8615d700  Srb 8611f4fc  Irp 8611f2b8   Key 60197  <1s
      SrbData 85e72868  Srb 86100c3c Irp 861009f8   Key e29dc7  <1s 
```

If the timeout slot is -1 and the untagged slot is nonzero, or the time-out slot is nonzero and there are requests shown, the miniport has failed to ask for the next request.

Alternatively, if the retry slot and the busy slot are nonzero, a request may not be completed by the SCSI miniport because it is waiting for map registers. Similarly, if the untagged and pending slots are nonzero, the SCSI miniport might be waiting for map registers. In either case, the address of the SCSI request block (SRB) is the address in the busy slot and the address of the request that is not being completed. For more information about the SRB, use the [**!minipkd.srb**](-minipkd-srb.md) extension with this address as input.

The [**!devobj**](-devobj.md) extension determines whether the SCSI miniport is waiting for map registers. Use the device object address of the device that is issuing the request as input to **!devobj**. If the current IRQ is nonzero, it is highly probable that the SCSI miniport is waiting for map registers.

 

 





