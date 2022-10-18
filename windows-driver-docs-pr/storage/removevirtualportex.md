---
title: RemoveVirtualPortEx method (Windows Drivers)
description: Learn more about the RemoveVirtualPortEx method.
ms.date: 10/14/2022
---

# RemoveVirtualPortEx method

The **RemoveVirtualPortEx** method removes a virtual port for a specific world wide port name (WWPN) .

## Syntax

``` c++
void RemoveVirtualPortEx(
   [in] uint8   WWPN[8],
   [out] uint16 Status
);
```

## Parameters

- *WWPN\[8\]*  
    The world wide port name of the virtual port to remove.

- *Status*  
    On return, contains the status of the operation.

## Return value

Not applicable to WMI methods.

## See also

[NPIV Status Codes](npiv-status-codes.md)
