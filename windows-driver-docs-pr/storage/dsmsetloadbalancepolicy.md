---
title: DsmSetLoadBalancePolicy function
description: The DsmSetLoadBalancePolicy method is used to set the DSM load balance policy.
ms.assetid: f53a776a-b350-4424-855a-49323587c57b
keywords: ["DsmSetLoadBalancePolicy function Storage Devices"]
topic_type:
- apiref
api_name:
- DsmSetLoadBalancePolicy
api_location:
- MPIOdisk.h
api_type:
- HeaderDef
---

# DsmSetLoadBalancePolicy function


The **DsmSetLoadBalancePolicy** method is used to set the DSM load balance policy.

Syntax
------

```ManagedCPlusPlus
void DsmSetLoadBalancePolicy(
   [in, Description("New Load Balance policy to be set"):amended] DSM_Load_Balance_Policy LoadBalancePolicy,
   [out, Description("Status of the operation"):amended] uint32                           Status
);
```

Parameters
----------

*LoadBalancePolicy*   
A [**DsmSetLoadBalancePolicy\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff552680) structure.

*Status*   
The status of the operation.

Return value
------------

None

Remarks
-------

This WMI method belongs to the [DSM\_LB\_Operations](dsm-lb-operations-wmi-class.md) WMI class.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">MPIOdisk.h (include MPIOdisk.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20DsmSetLoadBalancePolicy%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




