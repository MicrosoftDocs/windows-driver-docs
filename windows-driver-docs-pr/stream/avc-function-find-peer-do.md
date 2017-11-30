---
title: AVC\_FUNCTION\_FIND\_PEER\_DO
description: AVC\_FUNCTION\_FIND\_PEER\_DO
ms.assetid: a21dde69-f005-4782-97d9-095a57b2b1a5
keywords: ["AVC_FUNCTION_FIND_PEER_DO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_FIND_PEER_DO
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# AVC\_FUNCTION\_FIND\_PEER\_DO


## <span id="ddk_avc_function_find_peer_do_ks"></span><span id="DDK_AVC_FUNCTION_FIND_PEER_DO_KS"></span>


The **AVC\_FUNCTION\_FIND\_PEER\_DO** function code locates a nonvirtual *avc.sys* instance.

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
<td><p>STATUS_UNSUCCESSFUL</p></td>
<td><p>A nonvirtual instance of <em>avc.sys</em> was not found</p></td>
</tr>
<tr class="even">
<td><p>STATUS_INVALID_GENERATION</p></td>
<td><p>A bus reset occurred before the Device Object reference could be found. Obtain a new NodeAddress and try again.</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

This function uses the **PeerLocator** member of the AVC\_MULTIFUNC\_IRB structure as shown below.

```
typedef struct _AVC_MULTIFUNC_IRB {
  AVC_IRB  Common;
  union {
    .
    .
    .
    AVC_PEER_DO_LOCATOR PeerLocator;
 .
    .
    .
  };
} AVC_MULTIFUNC_IRB, *PAVC_MULTIFUNC_IRB;
```

### <span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### <span id="avc_multifunc_irb_input"></span><span id="AVC_MULTIFUNC_IRB_INPUT"></span>AVC\_MULTIFUNC\_IRB Input

<span id="Common"></span><span id="common"></span><span id="COMMON"></span>**Common**  
The **Function** submember of this member must be set to **AVC\_FUNCTION\_FIND\_PEER\_DO** from the AVC\_FUNCTION enumeration.

<span id="PeerLocator"></span><span id="peerlocator"></span><span id="PEERLOCATOR"></span>**PeerLocator**  
Specifies the nonvirtual (peer) instances of *avc.sys*.

This function locates a nonvirtual *avc.sys* instance according to the node address of the device it represents. If an instance is not found, the IRP completes with a status of STATUS\_UNSUCCESSFUL. Once an instance is located, the caller may submit any GUID\_AVC\_CLASS Device Interface requests through the object. The caller must release the reference to this object (through **ObDereferenceObject**) when finished with it.

This function code may be called at IRQL &lt;= DISPATCH\_LEVEL.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[**AVC\_MULTIFUNC\_IRB**](https://msdn.microsoft.com/library/windows/hardware/ff554177), [**AVC\_PEER\_DO\_LOCATOR**](https://msdn.microsoft.com/library/windows/hardware/ff554180), [**AVC\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554145), [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AVC_FUNCTION_FIND_PEER_DO%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




