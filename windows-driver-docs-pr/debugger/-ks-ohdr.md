---
title: ks.ohdr
description: The ks.ohdr extension displays details of a kernel streaming object header.
ms.assetid: 0080565a-537d-44f4-9329-9ebe7fc926a1
keywords: ["ks.ohdr Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ks.ohdr
api_type:
- NA
---

# !ks.ohdr


The **!ks.ohdr** extension displays details of a kernel streaming object header.

```
!ks.ohdr Object [Level] [Flags]  
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Object______"></span><span id="_______object______"></span><span id="_______OBJECT______"></span> *Object*   
This parameter specifies a pointer to a KS object header. If *Object* is not valid, the command returns an error.

<span id="_______Level______"></span><span id="_______level______"></span><span id="_______LEVEL______"></span> *Level*   
Optional. Values are the same as those for [**!ks.dump**](-ks-dump.md).

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. Values are the same as those for [**!ks.dump**](-ks-dump.md).

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

The **!ks.ohdr** command works similarly to [**!ks.objhdr**](-ks-objhdr.md) in that it displays details of a KS object header. The difference is that the caller provides the direct address of the KS object header, instead of the address of the associated file object.

Levels and flags for **!ks.ohdr** are identical to those described in [**!ks.dump**](-ks-dump.md).

If the data you are querying is not paged out, consider using [**!ks.dump**](-ks-dump.md) instead of **!ks.ohdr**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ks.ohdr%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




