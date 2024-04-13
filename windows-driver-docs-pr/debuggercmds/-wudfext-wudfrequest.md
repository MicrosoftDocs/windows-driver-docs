---
title: "!wudfext.wudfrequest"
description: "The !wudfext.wudfrequest extension displays information about an I/O request."
keywords: ["!wudfext.wudfrequest Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wudfext.wudfrequest
api_type:
- NA
---

# !wudfext.wudfrequest

The **!wudfext.wudfrequest** extension displays information about an I/O request.

```dbgcmd
!wudfext.wudfrequest pWDFRequest
```

## Parameters

<span id="_______pWDFRequest______"></span><span id="_______pwdfrequest______"></span><span id="_______PWDFREQUEST______"></span> *pWDFRequest*   
Specifies the address of the **WDFIoRequest** interface to display information about. The [**!wudfext.wudfqueue**](-wudfext-wudfqueue.md) extension command determines the address of **WDFIoRequest**.

## DLL

Wudfext.dll

## Additional Information

For more information, see [User-Mode Driver Framework Debugging](../debugger/user-mode-driver-framework-debugging.md).

## Remarks

The following is an example of the **!wudfext.wudfrequest** display:

```dbgcmd
kd> !wudfrequest 0x000fa530 
CWdfIoRequest  0x000fa4b8
Type: WdfRequestRead
  IWDFIoQueue: 0x000f3500
Completed: No
Canceled: No
UM IRP: 0x00429108  UniqueId: 0xf4  Kernel Irp: 0x0x936ef160
  Type: WudfMsg_READ
  ClientProcessId: 0x1248
  Device Stack: 0x003be4e0
  IoStatus
    hrStatus: 0x0
    Information: 0x0
  Driver/Framework created IRP: No
  Data Buffer: 0x00000000 / 0
  IsFrom32BitProcess: Yes
  CancelFlagSet: No
  Cancel callback: 0x000fa534
  Total number of stack locations: 2
  CurrentStackLocation: 2 (StackLocation[ 1 ])
    StackLocation[ 0 ]
      UNINITIALIZED
  > StackLocation[ 1 ]
      IWDFRequest:  ????
      IWDFDevice:   0x000f2f80
      IWDFFile:     0x00418cf0
      Completion:
        Callback:   0x00000000
        Context:    0x00000000
      Parameters: (RequestType: WdfRequestRead)
        Buffer length:        0x400
        Key:                  0x00000000
        Offset:               0x0
```
