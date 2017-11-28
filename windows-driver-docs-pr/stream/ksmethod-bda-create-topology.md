---
title: KSMETHOD\_BDA\_CREATE\_TOPOLOGY
description: Clients use KSMETHOD\_BDA\_CREATE\_TOPOLOGY to create a topology structure in Ring 3 that reflects the known connections in a filter.
ms.assetid: 3f34c7cc-d711-478b-a017-ad2c46545a9b
keywords: ["KSMETHOD_BDA_CREATE_TOPOLOGY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSMETHOD_BDA_CREATE_TOPOLOGY
api_location:
- Bdamedia.h
api_type:
- HeaderDef
---

# KSMETHOD\_BDA\_CREATE\_TOPOLOGY


Clients use KSMETHOD\_BDA\_CREATE\_TOPOLOGY to create a topology structure in Ring 3 that reflects the known connections in a filter.

## <span id="ddk_ksmethod_bda_create_topology_ks"></span><span id="DDK_KSMETHOD_BDA_CREATE_TOPOLOGY_KS"></span>


### <span id="Specifying_This_Method"></span><span id="specifying_this_method"></span><span id="SPECIFYING_THIS_METHOD"></span>Specifying This Method

KSMETHOD with the **Flags** member set to KSMETHOD\_TYPE\_WRITE.

### <span id="Method_Data"></span><span id="method_data"></span><span id="METHOD_DATA"></span>Method Data

A KSMULTIPLE\_ITEM structure, which is the header for a list of topology information.

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


[**BdaMethodCreateTopology**](https://msdn.microsoft.com/library/windows/hardware/ff556471)

[**KSMETHOD**](https://msdn.microsoft.com/library/windows/hardware/ff563398)

[**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563441)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSMETHOD_BDA_CREATE_TOPOLOGY%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





