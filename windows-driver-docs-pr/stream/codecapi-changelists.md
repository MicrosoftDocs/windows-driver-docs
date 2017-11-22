---
title: CODECAPI\_CHANGELISTS
description: CODECAPI\_CHANGELISTS
MS-HAID:
- 'encoderef\_33724eeb-3ba9-4c03-b217-dc09a8720f44.xml'
- 'stream.codecapi\_changelists'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c1b65350-32b9-4c94-a6d4-74cb9959d737
---

# CODECAPI\_CHANGELISTS


## <span id="ddk_codecapi_changelists_ks"></span><span id="DDK_CODECAPI_CHANGELISTS_KS"></span>


The CODECAPI\_CHANGELISTS event is used to return a list of GUIDs that have changed as a result of a property "set" call, such as [CODECAPI\_ALLSETTINGS](codecapi-allsettings.md) and [CODECAPI\_SETALLDEFAULTS](codecapi-setalldefaults.md), or an encoder setting property.

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
<th>Event descriptor type</th>
<th>Event value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes (query supported)</p></td>
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p>[<strong>KSE_NODE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561937)</p></td>
<td><p>[<strong>KSEVENTDATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561750)</p></td>
</tr>
</tbody>
</table>

 

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877).

The driver uses the AVStream [**KsGenerateEvents**](https://msdn.microsoft.com/library/windows/hardware/ff562597) to post a list of GUIDs that changed.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[**KsGenerateEvents**](https://msdn.microsoft.com/library/windows/hardware/ff562597), [CODECAPI\_ALLSETTINGS](codecapi-allsettings.md), [CODECAPI\_SETALLDEFAULTS](codecapi-setalldefaults.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20CODECAPI_CHANGELISTS%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




