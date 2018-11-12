---
title: wdfkd.wdfumirp
description: The wdfkd.wdfumirp extension displays information about a user-mode I/O request packet (UM IRP).
ms.assetid: 8706E8F6-A387-48A9-AF14-ED2C0F94AD98
keywords: ["wdfkd.wdfumirp Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfumirp
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfumirp


The **!wdfkd.wdfumirp** extension displays information about a user-mode I/O request packet (UM IRP).

```dbgcmd
!wdfkd.wdfumirp Address
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the UM IRP to display information about. You can use [**!wdfkd.wdfumirps**](-wdfkd-wdfumirps.md) to get the addresses of UM IRPs in the [implicit process](controlling-threads-and-processes.md).

## <span id="DLL"></span><span id="dll"></span>DLL


Wdfkd.dll

## <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks


UMDF 2

## <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information


For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

You can use this command in a kernel-mode debugging session or in a user-mode debugging session that is attached to the UMDF host process (wudfhost.exe).

This command displays the same information as the user-mode command [**!wudfext.umirp**](-wudfext-umirp.md).

You can use [**!process**](-process.md) to get a list of all UMDF host processes, and you can use [**.process**](-process--set-process-context-.md) to set the implicit process to one of the UMDF host processes. For a detailed example, see [**!wdfkd.wdfumdevstacks**](-wdfkd-wdfumdevstacks.md).

The following shows how to use [**!wdfkd.wdfumirps**](-wdfkd-wdfumirps.md) and **!wdfkd.wdfumirp** to display information about an individual UM IRP.

```dbgcmd
0: kd> !wdfkd.wdfumirps
Number of pending IRPS: 0x4
####  CWudfIrp     Current Type           UniqueId KernelIrp         Device Stack
----  ----------------  --------------------------------------------------  ----
...
0003  1ab9eae370   Power (WAIT_WAKE)          0     ffffe00000c53010  1ab9eaa6d0

0: kd> !wdfkd.wdfumirp 1ab9eae370
UM IRP: 0x0000001ab9eae370  UniqueId: 0x0  Kernel Irp: 0xffffe00000c53010
  Type: Power (WAIT_WAKE)
  ClientProcessId: 0x0
  Device Stack: 0x0000001ab9eaa6d0
  IoStatus
    hrStatus: 0x0
    Information: 0x0
  Total number of stack locations: 2
  CurrentStackLocation: StackLocation[ 0 ]
  > StackLocation[ 0 ]
      FxDevice:   (None)
      Completion:
        Callback:   0x0000000000000000
        Context:    0x0000001ab9ebc750
    StackLocation[ 1 ]
    ...
```

 

 





