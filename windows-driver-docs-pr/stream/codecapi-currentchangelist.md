---
title: CODECAPI\_CURRENTCHANGELIST
description: CODECAPI\_CURRENTCHANGELIST
ms.assetid: f783857f-d1a1-417f-8f69-198b6f328a69
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CODECAPI\_CURRENTCHANGELIST


## <span id="ddk_codecapi_currentchangelist_ks"></span><span id="DDK_CODECAPI_CURRENTCHANGELIST_KS"></span>


The CODECAPI\_CURRENTCHANGELIST property is used to indicate which parameters changed in a previous property "set" call, such as [CODECAPI\_ALLSETTINGS](codecapi-allsettings.md) and [CODECAPI\_SETALLDEFAULTS](codecapi-setalldefaults.md).

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p>KSPROPERTY</p></td>
<td><p>Array of GUIDs</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is an array of GUIDs.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

On a property get call:

If an application makes a property get call with a nonzero buffer size, the minidriver returns STATUS\_BUFFER\_TOO\_SMALL if the supplied buffer is too small for the data block. If there are no items to return, the minidrivers returns STATUS\_SUCCESS. Otherwise a list of GUIDs is returned (that is, where the sizeof(GUID) bytes equals 16 bytes). The returned size is the length of the list in bytes (that is, the number of GUIDS \* sizeof(GUID)).

On a property set call:

The current list of changed GUIDs is reset.

### <span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262), [CODECAPI\_ALLSETTINGS](codecapi-allsettings.md), [CODECAPI\_SETALLDEFAULTS](codecapi-setalldefaults.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20CODECAPI_CURRENTCHANGELIST%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




