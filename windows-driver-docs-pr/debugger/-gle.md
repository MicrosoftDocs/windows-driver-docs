---
title: gle
description: The gle extension displays the last error value for the current thread.
ms.assetid: bed3ce17-6860-421f-ae20-11faa50310ed
keywords: ["thread, error value", "error value", "gle Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- gle
api_type:
- NA
---

# !gle


The **!gle** extension displays the last error value for the current thread.

```
!gle [-all]
```

## <span id="ddk__gle_dbg"></span><span id="DDK__GLE_DBG"></span>Parameters


<span id="_______-all______"></span><span id="_______-ALL______"></span> **-all**   
Displays the last error for each user-mode thread on the target system. If you omit this parameter in user mode, the debugger displays the last error for the current thread. If you omit this parameter in kernel mode, the debugger displays the last error for the thread that the current [register context](changing-contexts.md#register-context) specifies.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p></p>
Ext.dll
Ntsdexts.dll</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) routine, see the Micorosft Windows SDK documentation.

Remarks
-------

The **!gle** extension displays the value of [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) and tries to decode this value.

In kernel mode, the **!gle** extension work only if the debugger can read the thread environment block (TEB).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!gle%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




