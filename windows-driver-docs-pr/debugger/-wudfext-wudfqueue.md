---
title: wudfext.wudfqueue
description: The wudfext.wudfqueue extension displays information about an I/O queue.
ms.assetid: b3ede1af-c85a-42d6-a8e5-e4094dd80d1c
keywords: ["wudfext.wudfqueue Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- wudfext.wudfqueue
api_type:
- NA
---

# !wudfext.wudfqueue


The **!wudfext.wudfqueue** extension displays information about an I/O queue.

```
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

```
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
    Driver&#39;s callback interfaces.
      IQueueCallbackRead 0x000f343c
      IQueueCallbackDeviceIoControl 0x000f3438
      IQueueCallbackWrite 0x000f3440
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!wudfext.wudfqueue%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




