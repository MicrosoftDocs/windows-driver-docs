---
title: verifier
description: The verifier extension displays the status of Driver Verifier and its actions.
ms.assetid: e84993e1-da10-4041-8fc7-7f40806ee454
keywords: ["Driver Verifier", "verifier Windows Debugging"]
ms.author: domars
ms.date: 05/03/2018
topic_type:
- apiref
api_name:
- verifier
api_type:
- NA
ms.localizationpriority: medium
---

# !verifier


The **!verifier** extension displays the status of Driver Verifier and its actions.

Driver Verifier is included in Windows. It works on both checked and free builds. For information about Driver Verifier, see the [Driver Verifier](https://go.microsoft.com/fwlink/p/?linkid=120480) topic in the Windows Driver Kit (WDK) documentation.

Syntax

```dbgcmd
!verifier [Flags [Image]] 
!verifier 4 [Quantity] 
!verifier 8 [Quantity]  
!verifier 0x40 [Quantity] 
!verifier 0x80 [Quantity]
!verifier 0x80 Address
!verifier 0x100 [Quantity]
!verifier 0x100 Address
!verifier 0x200 [Address]
!verifier 0x400 [Address]
!verifier -disable
!verifier ?
```

## <span id="ddk__verifier_dbg"></span><span id="DDK__VERIFIER_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies what information is displayed in the output from this command. If *Flags* is equal to the value 4, 8, 0x20, 0x40, 0x80, or 0x100, then the remaining arguments to **!verifier** are interpreted based on the specific arguments associated with those values. If *Flags* is equal to any other value, even if one or more of these bits are set, only the *Flags* and *Image* arguments are permitted. *Flags* can be any sum of the following bits; the default is 0:

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Displays the names of all drivers being verified. The number of bytes currently allocated to each driver from the nonpaged pool and the paged pool is also displayed.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Displays information about pools (pool size, headers, and pool tags) and outstanding memory allocations left by unloaded drivers. This flag has no effect unless bit 0 (0x1) is also set.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
(Windows XP and later) Displays fault injection information. The return address, symbol name, and displacement of the code requesting each allocation are displayed. If *Flags* is exactly 0x4 and the *Quantity* parameter is included, the number of these records displayed can be chosen. Otherwise, four records are displayed.

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
(Windows XP and later) Displays the most recent IRQL changes made by the drivers being verified. The old IRQL, new IRQL, processor, and time stamp are displayed. If *Flags* is exactly 0x8 and the *Quantity* parameter is included, the number of these records displayed can be chosen. Otherwise, four records are displayed.

**Warning**  In 64-bit versions of Windows, some of the kernel functions that raise or lower the IRQL are implemented as inline code rather than as exported functions. Driver Verifier does not report IRQL changes made by inline code, so it is possible for the IRQL transition log produced by Driver Verifier to be incomplete. See Remarks for an example of a missing IRQL transition entry.

 

<span id="Bit_6__0x40_"></span><span id="bit_6__0x40_"></span><span id="BIT_6__0X40_"></span>Bit 6 (0x40)  
(Windows Vista and later) Displays information from the **Force Pending I/O Requests** option of Driver Verifier, including traces from the log of forced pending IRPs.

The *Quantity* parameter specifies the number of traces to be displayed. By default, the entire log is displayed.

<span id="Bit_7__0x80_"></span><span id="bit_7__0x80_"></span><span id="BIT_7__0X80_"></span>Bit 7 (0x80)  
(Windows Vista and later) Displays information from the kernel pool Allocate/Free log.

The *Quantity* parameter specifies the number of traces to be displayed. By default, the entire log is displayed.

If *Address* is specified, only traces associated with the specified address within the kernel pool Allocate/Free log are displayed.

<span id="Bit_8__0x100_"></span><span id="bit_8__0x100_"></span><span id="BIT_8__0X100_"></span>Bit 8 (0x100)  
(Windows Vista and later) Displays information from the log of IoAllocateIrp, IoCompleteRequest and IoCancelIrp calls.

The Quantity parameter specifies the number of traces to be displayed. By default, the entire log is displayed.

If *Address* is specified, only traces associated with the specified IRP address are displayed.

<span id="Bit_9__0x200_"></span><span id="bit_9__0x200_"></span><span id="BIT_9__0X200_"></span>Bit 9 (0x200)  
(Windows Vista and later) Displays entries in the Critical Region log.

If *Address* is specified, only entries associated with the specified thread address are displayed.

<span id="Bit_10__0x400_"></span><span id="bit_10__0x400_"></span><span id="BIT_10__0X400_"></span>Bit 10 (0x400)  
(Windows Vista and later) Displays cancelled IRPs that are currently being watched by Driver Verifier.

If *Address* is specified, only the IRP with the specified address is displayed.

<span id="Bit_11__0x800_"></span><span id="bit_11__0x800_"></span><span id="BIT_11__0X800_"></span>Bit 11 (0x800)  
(Windows 8.1 and later) Display entries from the fault injection log that is created when you select the [Systematic low resource simulation](https://msdn.microsoft.com/library/windows/hardware/dn312130) option.

<span id="_______Image______"></span><span id="_______image______"></span><span id="_______IMAGE______"></span> *Image*   
If *Flags* is used and is not equal to 4, 8, or 0x10, *Image* specifies the name of a driver. *Image* is used to filter the information displayed by *Flags* values of 0x1 and 0x2: only the specified driver is considered. This driver must be currently verified.

<span id="_______Quantity______"></span><span id="_______quantity______"></span><span id="_______QUANTITY______"></span> *Quantity*   
(Windows XP and later) If *Flags* is exactly equal to 0x4, *Quantity* specifies the number of fault injection records to display. If *Flags* is exactly equal to 0x8, *Quantity* specifies the number of IRQL log entries to display. If *Flags* is exactly equal to 0x40, *Quantity* specifies the number of traces displayed from the log of forced pending IRPs. If Flags is exactly equal to 0x80, Quantity specifies the number of traces displayed from the kernel pool Allocate/Free log. If Flags is exactly equal to 0x100, Quantity specifies the number of traces displayed from the log of IoAllocateIrp, IoCompleteRequest and IoCancelIrp calls.

<span id="_______-disable______"></span><span id="_______-DISABLE______"></span> **-disable**   
(Windows XP and later) Clears the current Driver Verifier settings on the debug target. The clearing of these settings does not persist through a reboot. If you need to disable the Driver Verifier settings to successfully boot, set a breakpoint at nt!VerifierInitSystem and use the **!verifier -disable** command at that point.

<span id="______________"></span> **?**   
(Windows XP and later) Displays some brief Help text for this extension in the Debugger Command window.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about [Driver Verifier](https://go.microsoft.com/fwlink/p/?linkid=120480), see the Windows Driver Kit (WDK) documentation.


Remarks
-------

The following example illustrates that on 64-bit versions of Windows, the IRQL transition log is not always complete. The two entries shown are consecutive entries in the log for Processor 2. The first entry shows the IRQL going from 2 to 0. The second entry shows the IRQL going from 2 to 2. Information about how the IRQL got raised from 0 to 2 is missing.

```dbgcmd
Thread:             fffffa80068c9400
Old irql:           0000000000000002
New irql:           0000000000000000
Processor:          0000000000000002
Time stamp:         0000000000000857

    fffff8800140f12a ndis!ndisNsiGetInterfaceInformation+0x20a
    fffff88001509478 NETIO!NsiGetParameterEx+0x178
    fffff88005f062f2 nsiproxy!NsippGetParameter+0x24a
    fffff88005f086db nsiproxy!NsippDispatchDeviceControl+0xa3
    fffff88005f087a0 nsiproxy!NsippDispatch+0x48

Thread:             fffffa80068c9400
Old irql:           0000000000000002
New irql:           0000000000000002
Processor:          0000000000000002
Time stamp:         0000000000000857

    fffff8800140d48d ndis!ndisReferenceTopMiniportByNameForNsi+0x1ce
    fffff8800140f072 ndis!ndisNsiGetInterfaceInformation+0x152
    fffff88001509478 NETIO!NsiGetParameterEx+0x178
    fffff88005f062f2 nsiproxy!NsippGetParameter+0x24a
    fffff88005f086db nsiproxy!NsippDispatchDeviceControl+0xa3
```

When using Driver Verifier to test graphics drivers, use the [**!gdikdx.verifier**](-gdikdx-verifier.md) extension instead of **!verifier**.

The values of 4, 8, and 0x20, 0x40, 0x80, and 0x100 are special values for *Flags*. If these values are used, the special arguments listed in the **Parameters** section can be used, and the display will include only the information associated with that flag value.

If any other value for *Flags* is used, even if one or more of these bits are set, only the *Flags* and *Image* arguments are permitted. In this situation, in addition to all the other information displayed, **!verifier** will display the Driver Verifier options that are active, along with statistics on pool allocations, IRQL raises, spin locks, and trims.

If *Flags* equals 0x20, the values specified for *CompletionTime*, *CancelTime*, and *ForceCancellation* are used by the Driver Hang Verification option of Driver Verifier. These new values take effect immediately and last until the next boot. When you reboot, they revert to their default values.

Also, if *Flags* equals 0x20 (with or without additional parameters), the Driver Hang Verification log is printed. For information on interpreting the log, see the Driver Hang Verification section of the Driver Verifier documentation in the Windows Driver Kit (WDK) documentation.

Here is an example of the **!verifier** extension on a Windows 7 computer.

```dbgcmd
2: kd> !verifier 0xf

Verify Level 9bb ... enabled options are:
    Special pool
    Special irql
    All pool allocations checked on unload
    Io subsystem checking enabled
    Deadlock detection enabled
    DMA checking enabled
    Security checks enabled
    Miscellaneous checks enabled

Summary of All Verifier Statistics

RaiseIrqls                             0x0
AcquireSpinLocks                       0x362
Synch Executions                       0x0
Trims                                  0xa34a

Pool Allocations Attempted             0x7b058
Pool Allocations Succeeded             0x7b058
Pool Allocations Succeeded SpecialPool 0x7b058
Pool Allocations With NO TAG           0x0
Pool Allocations Failed                0x0
Resource Allocations Failed Deliberately   0x0

Current paged pool allocations         0x1a for 00000950 bytes
Peak paged pool allocations            0x1b for 00000AC4 bytes
Current nonpaged pool allocations      0xe3 for 00046110 bytes
Peak nonpaged pool allocations         0x10f for 00048E40 bytes

Driver Verification List

Entry     State           NonPagedPool   PagedPool   Module

fffffa8003b6f670 Loaded           000000a0       00000854    videoprt.sys

Current Pool Allocations  00000002    00000013
Current Pool Bytes        000000a0    00000854
Peak Pool Allocations     00000006    00000014
Peak Pool Bytes           000008c0    000009c8

PoolAddress  SizeInBytes    Tag       CallersAddress
fffff9800157efc0     0x0000003c     Vprt      fffff88002c62963
fffff9800146afc0     0x00000034     Vprt      fffff88002c62963
fffff980015bafe0     0x00000018     Vprt      fffff88002c628f7
...

fffffa8003b6f620 Loaded           00046070       000000fc    usbport.sys

Current Pool Allocations  000000e1    00000007
Current Pool Bytes        00046070    000000fc
Peak Pool Allocations     0000010d    0000000a
Peak Pool Bytes           00048da0    00000254

PoolAddress  SizeInBytes    Tag       CallersAddress
fffff98003a38fc0     0x00000038     usbp      fffff88004215e34
fffff98003a2cfc0     0x00000038     usbp      fffff88004215e34
fffff9800415efc0     0x00000038     usbp      fffff88004215e34
...

----------------------------------------------- 
Fault injection trace log                       
----------------------------------------------- 

Driver Verifier didn't inject any faults.

----------------------------------------------- 
Track irql trace log                            
----------------------------------------------- 

Displaying most recent 0x0000000000000004 entries from the IRQL transition log.
There are up to 0x100 entries in the log.

Thread:             fffff80002bf8c40
Old irql:           0000000000000002
New irql:           0000000000000002
Processor:          0000000000000000
Time stamp:         000000000000495e

    fffff8800420f2ca USBPORT!USBPORT_DM_IoTimerDpc+0x9a
    fffff80002a5b5bf nt!IopTimerDispatch+0x132
    fffff80002a7c29e nt!KiProcessTimerDpcTable+0x66
    fffff80002a7bdd6 nt!KiProcessExpiredTimerList+0xc6
    fffff80002a7c4be nt!KiTimerExpiration+0x1be

Thread:             fffff80002bf8c40
Old irql:           0000000000000002
New irql:           0000000000000002
Processor:          0000000000000000
Time stamp:         000000000000495e

    fffff88004205f3a USBPORT!USBPORT_AcquireEpListLock+0x2e
    fffff880042172df USBPORT!USBPORT_Core_TimeoutAllTransfers+0x1f
    fffff8800420f2ca USBPORT!USBPORT_DM_IoTimerDpc+0x9a
    fffff80002a5b5bf nt!IopTimerDispatch+0x132
    fffff80002a7c29e nt!KiProcessTimerDpcTable+0x66

Thread:             fffff80002bf8c40
Old irql:           0000000000000002
New irql:           0000000000000002
Processor:          0000000000000000
Time stamp:         000000000000495e

    fffff88004201694 USBPORT!MPf_CheckController+0x4c
    fffff8800420f26a USBPORT!USBPORT_DM_IoTimerDpc+0x3a
    fffff80002a5b5bf nt!IopTimerDispatch+0x132
    fffff80002a7c29e nt!KiProcessTimerDpcTable+0x66
    fffff80002a7bdd6 nt!KiProcessExpiredTimerList+0xc6

Thread:             fffff80002bf8c40
Old irql:           0000000000000002
New irql:           0000000000000002
Processor:          0000000000000000
Time stamp:         000000000000495e

    fffff8800420167c USBPORT!MPf_CheckController+0x34
    fffff8800420f26a USBPORT!USBPORT_DM_IoTimerDpc+0x3a
    fffff80002a5b5bf nt!IopTimerDispatch+0x132
    fffff80002a7c29e nt!KiProcessTimerDpcTable+0x66
    fffff80002a7bdd6 nt!KiProcessExpiredTimerList+0xc6
```

Here is an example of the **!verifier** extension on a Windows Vista computer with bit 7 turned on and *Address* specified.

```dbgcmd
0: kd> !verifier 80 a2b1cf20
# Parsing 00004000 array entries, searching for address a2b1cf20.

Pool block a2b1ce98, Size 00000168, Thread a2b1ce98
808f1be6 ndis!ndisFreeToNPagedPool+0x39
808f11c1 ndis!ndisPplFree+0x47
808f100f ndis!NdisFreeNetBufferList+0x3b
8088db41 NETIO!NetioFreeNetBufferAndNetBufferList+0xe
8c588d68 tcpip!UdpEndSendMessages+0xdf
8c588cb5 tcpip!UdpSendMessagesDatagramsComplete+0x22
8088d622 NETIO!NetioDereferenceNetBufferListChain+0xcf
8c5954ea tcpip!FlSendNetBufferListChainComplete+0x1c
809b2370 ndis!ndisMSendCompleteNetBufferListsInternal+0x67
808f1781 ndis!NdisFSendNetBufferListsComplete+0x1a
8c04c68e pacer!PcFilterSendNetBufferListsComplete+0xb2
809b230c ndis!NdisMSendNetBufferListsComplete+0x70
# 8ac4a8ba test1!HandleCompletedTxPacket+0xea

Pool block a2b1ce98, Size 00000164, Thread a2b1ce98
822af87f nt!VerifierExAllocatePoolWithTagPriority+0x5d
808f1c88 ndis!ndisAllocateFromNPagedPool+0x1d
808f11f3 ndis!ndisPplAllocate+0x60
808f1257 ndis!NdisAllocateNetBufferList+0x26
80890933 NETIO!NetioAllocateAndReferenceNetBufferListNetBufferMdlAndData+0x14
8c5889c2 tcpip!UdpSendMessages+0x503
8c05c565 afd!AfdTLSendMessages+0x27
8c07a087 afd!AfdTLFastDgramSend+0x7d
8c079f82 afd!AfdFastDatagramSend+0x5ae
8c06f3ea afd!AfdFastIoDeviceControl+0x3c1
8217474f nt!IopXxxControlFile+0x268
821797a1 nt!NtDeviceIoControlFile+0x2a
8204d16a nt!KiFastCallEntry+0x127
```

 

 





