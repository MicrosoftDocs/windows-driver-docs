---
title: elog_str
description: The elog_str extension adds a string to the event log.
ms.assetid: 142ef480-8095-428e-9b7d-f4c8bfb78075
keywords: ["event log", "elog_str Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- elog_str
api_type:
- NA
---

# !elog\_str


The **!elog\_str** extension adds a string to the event log.

```
!elog_str String
```

## <span id="ddk__elog_str_dbg"></span><span id="DDK__ELOG_STR_DBG"></span>Parameters


<span id="_______String______"></span><span id="_______string______"></span><span id="_______STRING______"></span> *String*   
Specifies the string to add to the event log.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Because a registered event source does not send *String*, the string appears in the event log with a warning that no event ID was determined.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!elog_str%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




