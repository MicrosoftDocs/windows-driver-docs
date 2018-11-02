---
title: DsmSetLoadBalancePolicyALUA function
description: The DsmSetLoadBalancePolicyALUA method is used to set the DSM ALUA load balance policy.
ms.assetid: f63bdf0a-5b78-475d-b7c5-2af587b6356f
keywords: ["DsmSetLoadBalancePolicyALUA function Storage Devices"]
topic_type:
- apiref
api_name:
- DsmSetLoadBalancePolicyALUA
api_location:
- MPIOdisk.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DsmSetLoadBalancePolicyALUA function


The **DsmSetLoadBalancePolicyALUA** method is used to set the DSM ALUA load balance policy.

Syntax
------

```ManagedCPlusPlus
void DsmSetLoadBalancePolicyALUA(
   [in, Description("New Load Balance policy to be set"):amended] DSM_Load_Balance_Policy_V2 LoadBalancePolicy,
   [out, Description("Status of the operation"):amended] uint32                              Status
);
```

Parameters
----------

*LoadBalancePolicy*   
A [**DsmSetLoadBalancePolicyALUA\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff552675) structure.

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

 

 





