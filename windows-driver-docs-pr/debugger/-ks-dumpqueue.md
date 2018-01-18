---
title: ks.dumpqueue
description: The ks.dumpqueue extension displays information about the queues associated with a given AVStream object, or the stream associated with a port class object.
ms.assetid: d641b4e6-73d9-4c44-b2c6-0b6c688da368
keywords: ["ks.dumpqueue Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ks.dumpqueue
api_type:
- NA
---

# !ks.dumpqueue


The **!ks.dumpqueue** extension displays information about the queues associated with a given AVStream object, or the stream associated with a port class object.

```
!ks.dumpqueue Object [Level] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Object______"></span><span id="_______object______"></span><span id="_______OBJECT______"></span> *Object*   
Specifies a pointer to the object for which to display the queue. *Object* must be of type PKSPIN, PKSFILTER, CKsPin\*, CKsFilter\*, CKsQueue\*, CPortPin\*, or CPortFilter\*.

<span id="_______Level______"></span><span id="_______level______"></span><span id="_______LEVEL______"></span> *Level*   
Optional. Specifies the level of detail to display on a 0-7 scale with progressively more information displayed for higher values. To display all available details, supply a value of 7.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>winxp\Ks.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ks.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel Streaming Debugging](kernel-streaming-debugging.md).

Remarks
-------

*Object* must be a filter or a pin. For a pin, a single queue is displayed. For a filter, multiple queues are displayed.

This command can take some time to execute.

Here is an example of the **!ks.dumpqueue** display:

```
kd> !dumpqueue 829493c4
Filter 829493c4: Output Queue 82990e20:
 Queue 82990e20:
        Frames Received  : 1889
        Frames Waiting   : 3
        Frames Cancelled : 0
        And Gate 82949464 : count = 1, next = 00000000
    Frame Gate NULL
        Frame Header 82aaef78:
 NextFrameHeaderInIrp = 00000000
            OriginalIrp = 82169e48
            Mdl = 8292e358
            Irp = 82169e48
 StreamHeader = 8298dea0
            FrameBuffer = edba3000
            StreamHeaderSize = 00000000
            FrameBufferSize = 00025800
            Context = 00000000
            Refcount = 1
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ks.dumpqueue%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




