---
title: CODECAPI\_ALLSETTINGS
description: CODECAPI\_ALLSETTINGS
ms.assetid: 0ae11200-af21-476a-89a8-515bd98920a0
---

# CODECAPI\_ALLSETTINGS


## <span id="ddk_codecapi_allsettings_ks"></span><span id="DDK_CODECAPI_ALLSETTINGS_KS"></span>


The CODECAPI\_ALLSETTINGS property is used to pass back and forth a minidriver-generated block of data.

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
<td><p>PVOID</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type PVOID, which is a pointer to a user-mode buffer for the minidriver-generated block of data.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

On a property get call:

If an application makes a property get call with a zero length buffer, the minidriver must return STATUS\_BUFFER\_OVERFLOW and specify the required buffer size in the **Irp-&gt;IoStatus.Information** field. If the length buffer is nonzero, the minidriver must return STATUS\_BUFFER\_TOO\_SMALL if the supplied buffer is too small for the data block, otherwise the minidriver packs its settings into a data block that can be restored later.

It is the minidriver's responsibility to add data integrity checks to the data, such as a unique GUID to indicate the minidriver generated the data, a cyclic redundancy check (CRC), and a header length.

The data returned should be lightweight and contain only information required to reconstruct the current settings.

Applications will use this property for multilevel undos, stored with their projects, etc.

On a property set call:

The minidriver must verify the data's integrity and check that the data block size is under the maximum data size (for example, reject anything over a certain size). It must also verify the CRC and the header length. The minidriver must also cache any changes to be propagated for [CODECAPI\_CURRENTCHANGELIST](codecapi-currentchangelist.md).

### <span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262), [CODECAPI\_CURRENTCHANGELIST](codecapi-currentchangelist.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20CODECAPI_ALLSETTINGS%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




