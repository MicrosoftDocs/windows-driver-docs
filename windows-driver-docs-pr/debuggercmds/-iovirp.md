---
title: "!iovirp (WinDbg)"
description: "The !iovirp extension displays detailed information for a specified I/O Verifier IRP."
keywords: ["I/O Verifier", "!iovirp Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- iovirp
api_type:
- NA
---

# !iovirp

The **!iovirp** extension displays detailed information for a specified I/O Verifier IRP.

```dbgcmd
!iovirp [IRP]
```

## Parameters


<span id="_______IRP______"></span><span id="_______irp______"></span> *IRP*   
Specifies the address of an IRP tracked by the Driver Verifier. If *IRP* is 0 or is omitted, the summary information for each outstanding IRP is displayed.

## DLL

Kdexts.dll

 

## Remarks

Here is an example of the output from this extension:

```dbgcmd
kd> !iovirp 947cef68
IovPacket       84509af0
TrackedIrp      947cef68
HeaderLock      84509d61
LockIrql        0
ReferenceCount  1
PointerCount    1
HeaderFlags     00000000
ChainHead       84509af0
Flags           00200009
DepartureIrql   0
ArrivalIrql     0
StackCount      1
QuotaCharge     00000000
QuotaProcess    0
RealIrpCompletionRoutine        0
RealIrpControl                  0
RealIrpContext                  0
TopStackLocation        2
PriorityBoost           0
LastLocation            0
RefTrackingCount        0
SystemDestVA            0
VerifierSettings        84509d08
pIovSessionData         84509380
Allocation Stack:
  nt!IovAllocateIrp+1a  (817df356)
 nt!IopXxxControlFile+40c  (8162de20)
  nt!NtDeviceIoControlFile+2a  (81633090)
 nt!KiFastCallEntry+164  (81513c64)
  nt!EtwpFlushBuffer+10f  (817606d7)
  nt!EtwpFlushBuffersWithMarker+bd  (817608cb)
  nt!EtwpFlushActiveBuffers+2b4  (81760bc2)
  nt!EtwpLogger+213  (8176036f)
```

You can stop execution at any point by pressing CTRL+BREAK (in WinDbg) or CTRL+C (in KD).

