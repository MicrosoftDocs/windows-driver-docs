---
title: AVC\_FUNCTION\_GET\_SUBUNIT\_INFO
description: AVC\_FUNCTION\_GET\_SUBUNIT\_INFO
MS-HAID:
- 'avcref\_70fdbc50-6701-45d3-80f4-07ce8606cfeb.xml'
- 'stream.avc\_function\_get\_subunit\_info'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1793df9d-b186-425f-a3dd-3054cb9b74bf
keywords: ["AVC_FUNCTION_GET_SUBUNIT_INFO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_GET_SUBUNIT_INFO
api_type:
- NA
---

# AVC\_FUNCTION\_GET\_SUBUNIT\_INFO


## <span id="ddk_avc_function_get_subunit_info_ks"></span><span id="DDK_AVC_FUNCTION_GET_SUBUNIT_INFO_KS"></span>


The **AVC\_FUNCTION\_GET\_SUBUNIT\_INFO** function code obtains the subunit information of the target device.

### <span id="i_o_status_block"></span><span id="I_O_STATUS_BLOCK"></span>I/O Status Block

This function always sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

This function uses the **Subunits** member of the AVC\_MULTIFUNC\_IRB structure as shown below.

```
typedef struct _AVC_MULTIFUNC_IRB {
  AVC_IRB  Common;
  union {
    .
    .
    .
    AVC_SUBUNIT_INFO_BLOCK Subunits;
 };
} AVC_MULTIFUNC_IRB, *PAVC_MULTIFUNC_IRB;
```

### <span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### <span id="avc_multifunc_irb_input"></span><span id="AVC_MULTIFUNC_IRB_INPUT"></span>AVC\_MULTIFUNC\_IRB Input

<span id="Common"></span><span id="common"></span><span id="COMMON"></span>**Common**  
The **Function** submember of this member must be set to **AVC\_FUNCTION\_GET\_SUBUNIT\_INFO** from the AVC\_FUNCTION enumeration.

<span id="Subunits"></span><span id="subunits"></span><span id="SUBUNITS"></span>**Subunits**  
Specifies a description of an AV/C subunit's information.

This function is satisfied locally, so no commands are sent to the target.

This function code may be called at IRQL &lt;= DISPATCH\_LEVEL.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[**AVC\_MULTIFUNC\_IRB**](https://msdn.microsoft.com/library/windows/hardware/ff554177), [**AVC\_SUBUNIT\_INFO\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff554199), [**AVC\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554145)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AVC_FUNCTION_GET_SUBUNIT_INFO%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




