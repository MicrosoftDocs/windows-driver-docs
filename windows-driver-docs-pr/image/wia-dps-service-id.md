---
title: WIA\_DPS\_SERVICE\_ID
description: The WIA\_DPS\_SERVICE\_ID property contains the service ID of a web services scanner device. The WIA minidriver creates and maintains this property.
MS-HAID:
- 'WIA\_PropTable\_c36acdc6-ae00-43d3-8074-65bfd82b8862.xml'
- 'image.wia\_dps\_service\_id'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ec77c2a6-0b9e-4c43-b189-7714257f3807
keywords: ["WIA_DPS_SERVICE_ID Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_SERVICE_ID
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPS\_SERVICE\_ID


The WIA\_DPS\_SERVICE\_ID property contains the service ID of a web services scanner device. The WIA minidriver creates and maintains this property.

Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The WIA minidriver initializes this property at run time by reading the PKEY\_PNPX\_ServiceId device property from the Function Instance object.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**WIA\_DPS\_DEVICE\_ID**](wia-dps-device-id.md)

[**WIA\_DPS\_GLOBAL\_IDENTITY**](wia-dps-global-identity.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPS_SERVICE_ID%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





