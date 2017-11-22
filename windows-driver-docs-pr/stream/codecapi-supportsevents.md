---
title: CODECAPI\_SUPPORTSEVENTS
description: CODECAPI\_SUPPORTSEVENTS
MS-HAID:
- 'encoderef\_837cb88f-4655-4f46-90fd-6adbf15e36ab.xml'
- 'stream.codecapi\_supportsevents'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: feb6d110-9a9c-4e2b-bc19-259f80f3947a
---

# CODECAPI\_SUPPORTSEVENTS


## <span id="ddk_codecapi_supportsevents_ks"></span><span id="DDK_CODECAPI_SUPPORTSEVENTS_KS"></span>


The CODECAPI\_SUPPORTSEVENTS property is used to indicate whether the minidriver supports user-mode events. That is, the minidriver implements the [CODECAPI\_CHANGELISTS](codecapi-changelists.md) event.

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
<td><p>BOOL</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type BOOL, which specifies whether the minidriver supports user-mode events. A value of **TRUE** indicates the minidriver provides support. The minidriver should not support this GUID if it does not support the event mechanism.

### <span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20CODECAPI_SUPPORTSEVENTS%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




