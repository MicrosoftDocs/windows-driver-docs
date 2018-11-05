---
title: wudfext.umirp
description: The wudfext.umirp extension displays information about a host user-mode I/O request packet (UM IRP).
ms.assetid: b31b864d-0c94-48b8-9ffd-f14639b9a551
keywords: ["wudfext.umirp Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wudfext.umirp
api_type:
- NA
ms.localizationpriority: medium
---

# !wudfext.umirp


The **!wudfext.umirp** extension displays information about a host user-mode I/O request packet (UM IRP).

```dbgcmd
!wudfext.umirp Address
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the UM IRP to display information about.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Wudfext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [User-Mode Driver Framework Debugging](user-mode-driver-framework-debugging.md).

Remarks
-------

You can use the [**!wudfext.umirps**](-wudfext-umirps.md) extension command to display a list of all outstanding UM IRPs in the host process.

Each UM IRP has one or more stack locations. Each stack location corresponds to the parameters that a single driver in the device stack will receive when it is called to handle a request.

**!wudfext.umirp** dumps all of the stack locations and marks the current location with a right angle bracket (&gt;). The current location corresponds to the driver that currently owns the request. The current location changes when a driver forwards a request to the next lower driver in the stack, or when the driver completes a request that the driver owns.

The following is an example of the **!wudfext.umirp** display:

```dbgcmd
kd> !umirp 3dd480 
UM IRP: 0x003dd480  UniqueId: 0xde  Kernel Irp: 0x0x85377850
  Type: WudfMsg_READ
  ClientProcessId: 0x338
  Device Stack: 0x0034e4e0
  IoStatus
    hrStatus: 0x0
    Information: 0x0
  Driver/Framework created IRP: No
  Data Buffer: 0x00000000 / 0
  IsFrom32BitProcess: Yes
  CancelFlagSet: No
  Cancel callback: 0x01102224
  Total number of stack locations: 2
  CurrentStackLocation: 2 (StackLocation[ 1 ])
    StackLocation[ 0 ]
      UNINITIALIZED
  > StackLocation[ 1 ]
      IWDFRequest:  ????
      IWDFDevice:   0x000f2f80
      IWDFFile:     0x003a7648
      Completion:
        Callback:   0x00000000
        Context:    0x00000000
      Parameters: (RequestType: WdfRequestRead)
        Buffer length:        0x400
        Key:                  0x00000000
        Offset:               0x0
```

 

 





