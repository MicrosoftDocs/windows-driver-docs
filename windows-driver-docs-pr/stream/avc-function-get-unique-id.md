---
title: AVC\_FUNCTION\_GET\_UNIQUE\_ID
description: AVC\_FUNCTION\_GET\_UNIQUE\_ID
MS-HAID:
- 'avcref\_04c4784f-1902-4c1d-a1b0-3f22ae15894b.xml'
- 'stream.avc\_function\_get\_unique\_id'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 51b35686-03a9-45b3-8bdc-14cbd24714dc
keywords: ["AVC_FUNCTION_GET_UNIQUE_ID Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_GET_UNIQUE_ID
api_type:
- NA
---

# AVC\_FUNCTION\_GET\_UNIQUE\_ID


## <span id="ddk_avc_function_get_unique_id_ks"></span><span id="DDK_AVC_FUNCTION_GET_UNIQUE_ID_KS"></span>


The **AVC\_FUNCTION\_GET\_UNIQUE\_ID** function code obtains the unique ID of the AV/C unit.

### <span id="i_o_status_block"></span><span id="I_O_STATUS_BLOCK"></span>I/O Status Block

If successful, the AV/C protocol driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

Possible other return values include:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>STATUS_TIMEOUT</p></td>
<td><p>The request was made, but no response was received before all time-out and retry processing was complete.</p></td>
</tr>
<tr class="even">
<td><p>STATUS_REQUEST_ABORTED</p></td>
<td><p>Immediately abort when the IRP completion status is STATUS_REQUEST_ABORTED. This indicates that the device has been removed or is no longer available on the 1394 bus.</p></td>
</tr>
<tr class="odd">
<td><p>STATUS_*</p></td>
<td><p>Any other return code indicates that an error or warning occurred that was beyond the scope of the AV/C protocol.</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

This function uses the **UniqueID** member of the AVC\_MULTIFUNC\_IRB structure as shown below.

```
typedef struct _AVC_MULTIFUNC_IRB {
  AVC_IRB  Common;
  union {
    .
    .
    .
    AVC_UNIQUE_ID UniqueID;
 .
    .
    .
  };
} AVC_MULTIFUNC_IRB, *PAVC_MULTIFUNC_IRB;
```

The members of the AVC\_UNIQUE\_ID structure are shown below:

```
typedef struct _AVC_UNIQUE_ID {
    OUT GUID DeviceID;
} AVC_UNIQUE_ID, *PAVC_UNIQUE_ID;
```

### <span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### <span id="avc_multifunc_irb_input"></span><span id="AVC_MULTIFUNC_IRB_INPUT"></span>AVC\_MULTIFUNC\_IRB Input

<span id="Common"></span><span id="common"></span><span id="COMMON"></span>**Common**  
The **Function** submember of this member must be set to **AVC\_FUNCTION\_GET\_UNIQUE\_ID** from the AVC\_FUNCTION enumeration.

<span id="UniqueID"></span><span id="uniqueid"></span><span id="UNIQUEID"></span>**UniqueID**  
Specifies a GUID representing the unit as a whole. All subunits within the same unit share the same GUID. No two units share the same GUID.

This function code is not supported by virtual instances of *avc.sys*.

The subunit driver uses this function if it must report the device GUID to a controlling application (an application that must know which of the many subunit driver instances belong in the same unit), or if it is building its own AVCPRECONNECTINFO structures for external plugs.

This must be called at IRQL = PASSIVE\_LEVEL.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[**AVC\_MULTIFUNC\_IRB**](https://msdn.microsoft.com/library/windows/hardware/ff554177), [**AVC\_UNIQUE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff554200), [**AVCPRECONNECTINFO**](https://msdn.microsoft.com/library/windows/hardware/ff554103), [**AVC\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554145)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AVC_FUNCTION_GET_UNIQUE_ID%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




