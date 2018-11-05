---
title: wudfext.wudfqueue
description: The wudfext.wudfqueue extension displays information about an I/O queue.
ms.assetid: b3ede1af-c85a-42d6-a8e5-e4094dd80d1c
keywords: ["wudfext.wudfqueue Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wudfext.wudfqueue
api_type:
- NA
ms.localizationpriority: medium
---

# !wudfext.wudfqueue


The **!wudfext.wudfqueue** extension displays information about an I/O queue.

```dbgcmd
!wudfext.wudfqueue pWDFQueue
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______pWDFQueue______"></span><span id="_______pwdfqueue______"></span><span id="_______PWDFQUEUE______"></span> *pWDFQueue*   
Specifies the address of the **IWDFIoQueue** interface to display information about. The [**!wudfext.wudfdevicequeues**](-wudfext-wudfdevicequeues.md) extension command determines the address of **IWDFIoQueue**.

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

The following is an example of the **!wudfext.wudfqueue** display:

```dbgcmd
kd> !wudfqueue 0x000f3500 
    WdfIoQueueDispatchSequential, POWER MANAGED, WdfIoQueuePowerOn, CAN ACCEPT, CAN DISPATCH
    Number of driver owned requests: 1
      IWDFIoRequest 0x000fa7c0     CWdfIoRequest 0x000fa748
    Number of waiting requests: 199
      IWDFIoRequest 0x000fa908     CWdfIoRequest 0x000fa890
      IWDFIoRequest 0x000faa50     CWdfIoRequest 0x000fa9d8
      IWDFIoRequest 0x000fab98     CWdfIoRequest 0x000fab20
      ...
      IWDFIoRequest 0x000fa530     CWdfIoRequest 0x000fa4b8
      IWDFIoRequest 0x000fa678     CWdfIoRequest 0x000fa600
    Driver's callback interfaces.
      IQueueCallbackRead 0x000f343c
      IQueueCallbackDeviceIoControl 0x000f3438
      IQueueCallbackWrite 0x000f3440
```

 

 





