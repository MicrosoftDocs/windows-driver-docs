---
title: KSMETHOD\_BDA\_CREATE\_PIN\_FACTORY
description: Clients use KSMETHOD\_BDA\_CREATE\_PIN\_FACTORY to create a pin factory for a filter.
MS-HAID:
- 'bdaref\_9b0243ba-31a8-486a-ad54-7434d6bc6f93.xml'
- 'stream.ksmethod\_bda\_create\_pin\_factory'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ebc9dc1d-1b4b-40d3-82b5-f32d3781537c
keywords: ["KSMETHOD_BDA_CREATE_PIN_FACTORY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSMETHOD_BDA_CREATE_PIN_FACTORY
api_location:
- Bdamedia.h
api_type:
- HeaderDef
---

# KSMETHOD\_BDA\_CREATE\_PIN\_FACTORY


Clients use KSMETHOD\_BDA\_CREATE\_PIN\_FACTORY to create a pin factory for a filter.

## <span id="ddk_ksmethod_bda_create_pin_factory_ks"></span><span id="DDK_KSMETHOD_BDA_CREATE_PIN_FACTORY_KS"></span>


### <span id="Specifying_This_Method"></span><span id="specifying_this_method"></span><span id="SPECIFYING_THIS_METHOD"></span>Specifying This Method

KSM\_PIN with the **Flags** member of the **Method** member set to KSMETHOD\_TYPE\_READ.

### <span id="Method_Data"></span><span id="method_data"></span><span id="METHOD_DATA"></span>Method Data

ULONG, representing the identifier of the pin factory.

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
<td>Bdamedia.h (include Bdamedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**BdaMethodCreatePin**](https://msdn.microsoft.com/library/windows/hardware/ff556467)

[**KSM\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff563453)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSMETHOD_BDA_CREATE_PIN_FACTORY%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





