---
title: SetChapForPhysicalPort method (Windows Drivers)
description: Learn more about the SetChapForPhysicalPort method.
ms.date: 10/14/2022
---

# SetChapForPhysicalPort method

Sets DH-CHAP as the unidirectional authentication method for the physical port of a Fibre Channel HBA.

## Syntax

``` c++
void SetChapForPhysicalPort(
   [in] MSFC_DH_Chap_Parameters CHAP,
   [out] uint32                 Status
);
```

## Parameters

- *CHAP*  
    Response parameters for a DH-CHAP challenge.

- *Status*  
    On return, contains the status of the operation.

## Return value

Not applicable to WMI methods.

## See also

[NPIV Status Codes](npiv-status-codes.md)
