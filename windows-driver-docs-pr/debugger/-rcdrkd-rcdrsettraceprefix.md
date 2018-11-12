---
title: rcdrkd.rcdrsettraceprefix
description: The rcdrkd.rcdrsettraceprefix extension sets the trace message prefix.
ms.assetid: BFA987B8-7013-4112-A674-064ED59741C0
keywords: ["rcdrkd.rcdrsettraceprefix Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- rcdrkd.rcdrsettraceprefix
api_type:
- NA
ms.localizationpriority: medium
---

# !rcdrkd.rcdrsettraceprefix


The **!rcdrkd.rcdrsettraceprefix** extension sets the trace message prefix.

```dbgcmd
!rcdrkd.rcdrsettraceprefix TracePrefixString 
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______TracePrefixString______"></span><span id="_______traceprefixstring______"></span><span id="_______TRACEPREFIXSTRING______"></span> *TracePrefixString*   
The trace message prefix string.

## <span id="DLL"></span><span id="dll"></span>DLL


Rcdrkd.dll

Remarks
-------

Each message in a recorder log has a prefix that you can control by specifying a trace message prefix string. For more information, see [Trace Message Prefix](https://msdn.microsoft.com/library/windows/hardware/ff553941).

Examples
--------

In the following example, the trace message prefix is originally **%7!u!: %!FUNC! -** . The parameter **%7!u!** specifies that the prefix includes the message sequence number. The parameter **%!FUNC!** specifies that the prefix includes the name of the function that generated the message. The example calls **!rcdrsettraceprefix** to change the prefix string to **%7!u!**. After that, the log display includes message sequence numbers, but does not include function names.

```dbgcmd
0: kd> !rcdrlogdump USBXHCI -a 0xfffffa8010737b60
Trace searchpath is: 

Trace format prefix is: %7!u!: %!FUNC! - 
Trying to extract TMF information from - C:\ProgramData\dbg\sym\usbxhci.pdb\D4C85D5D3E2843879EDE226A334D69552\usbxhci.pdb
--- start of log ---
405: TransferRing_DispatchEventsAndReleaseLock - 1.8.1: Mapping Begin : Path 1 TransferRingState_Mapping Events 0x00000000
406: TransferRing_StageRetrieveFromRequest - 1.8.1: WdfRequest 0x0000057FEE117A88 TransferData 0xFFFFFA8011EE8700 Function 0x9 Length 500 TransferSize 500 BytesProcessed 0
...
---- end of log ----

0: kd> !rcdrsettraceprefix %7!u!: 
SetTracePrefix: "%7!u!: "
0: kd> !rcdrlogdump USBXHCI -a 0xfffffa8010737b60
Trace searchpath is: 

Trace format prefix is: %7!u!: 
Trying to extract TMF information from - C:\ProgramData\dbg\sym\usbxhci.pdb\D4C85D5D3E2843879EDE226A334D69552\usbxhci.pdb
--- start of log ---
405: 1.8.1: Mapping Begin : Path 1 TransferRingState_Mapping Events 0x00000000
406: 1.8.1: WdfRequest 0x0000057FEE117A88 TransferData 0xFFFFFA8011EE8700 Function 0x9 Length 500 TransferSize 500 BytesProcessed 0
...
---- end of log ----
```

## <span id="see_also"></span>See also


[RCDRKD Extensions](rcdrkd-extensions.md)

 

 






