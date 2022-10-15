---
title: RemoveChapForPhysicalPort method (Windows Drivers)
description: Learn more about the RemoveChapForPhysicalPort method.
ms.date: 10/14/2022
---

# RemoveChapForPhysicalPort method

Removes DH-CHAP as the authentication method for the physical port of a Fibre Channel HBA.

## Syntax

``` c++
void RemoveChapForPhysicalPort(
   [out] uint32 Status
);
```

## Parameters

- *Status*  
    On return, contains the status of the operation.

## Return value

Not applicable to WMI methods.

## See also

[NPIV Status Codes](npiv-status-codes.md)
