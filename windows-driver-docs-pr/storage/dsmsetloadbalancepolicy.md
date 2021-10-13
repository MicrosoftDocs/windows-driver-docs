---
title: DsmSetLoadBalancePolicy function
description: The DsmSetLoadBalancePolicy method is used to set the DSM load balance policy.
keywords: ["DsmSetLoadBalancePolicy function Storage Devices"]
topic_type:
- apiref
api_name:
- DsmSetLoadBalancePolicy
api_location:
- MPIOdisk.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DsmSetLoadBalancePolicy function


The **DsmSetLoadBalancePolicy** method is used to set the DSM load balance policy.

## Syntax

```ManagedCPlusPlus
void DsmSetLoadBalancePolicy(
   [in, Description("New Load Balance policy to be set"):amended] DSM_Load_Balance_Policy LoadBalancePolicy,
   [out, Description("Status of the operation"):amended] uint32                           Status
);
```

## Parameters

*LoadBalancePolicy*   
A [**DsmSetLoadBalancePolicy\_OUT**](/windows-hardware/drivers/ddi/mpiodisk/ns-mpiodisk-_dsmsetloadbalancepolicy_out) structure.

*Status*   
The status of the operation.

## Return value

None

## Remarks

This WMI method belongs to the [DSM\_LB\_Operations](dsm-lb-operations-wmi-class.md) WMI class.

## Requirements

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

 

