---
title: rpcexts.rpcreadstack
description: The rpcexts.rpcreadstack extension reads an RPC client-side stack and retrieves the call information.
ms.assetid: e0988ac9-dc6e-4a4f-9096-6af2e70dcd42
keywords: ["rpcexts.rpcreadstack Windows Debugging"]
topic_type:
- apiref
api_name:
- rpcexts.rpcreadstack
api_type:
- NA
---

# !rpcexts.rpcreadstack


The **!rpcexts.rpcreadstack** extension reads an RPC client-side stack and retrieves the call information.

``` syntax
!rpcexts.rpcreadstack ThreadStackPointer
```

## <span id="ddk__rpcexts_rpcreadstack_dbg"></span><span id="DDK__RPCEXTS_RPCREADSTACK_DBG"></span>Parameters


<span id="_______ThreadStackPointer______"></span><span id="_______threadstackpointer______"></span><span id="_______THREADSTACKPOINTER______"></span> *ThreadStackPointer*   
Specifies the pointer to the thread stack.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Rpcexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about debugging Microsoft Remote Procedure Call (RPC), see [RPC Debugging](rpc-debugging.md).

Remarks
-------

For a common use of this extension, see [Analyzing a Stuck Call Problem](analyzing-a-stuck-call-problem.md).

Here is an example:

``` syntax
0:001> !rpcexts.rpcreadstack 68fba4
CallID: 1
IfStart: 19bb5061
ProcNum: 0
        Protocol Sequence:      "ncacn_ip_tcp"  (Address: 00692ED8)
        NetworkAddress: ""      (Address: 00692F38)
        Endpoint:       "1120"  (Address: 00693988)
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!rpcexts.rpcreadstack%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




