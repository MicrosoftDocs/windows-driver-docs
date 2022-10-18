---
title: CreateVirtualPortEx method (Windows Drivers)
description: Learn more about the CreateVirtualPortEx method.
ms.date: 10/14/2022
---

# CreateVirtualPortEx method

Creates a virtual port for a guest virtual machine with a specific WWPN. An authentication method is not set during the create.

## Syntax

``` c++
void CreateVirtualPortEx(
   [in] uint8   WWPN[8],
   [in] uint8   WWNN[8],
   [in] uint8   Tag[16],
   [in] uint16  VirtualName[64],
   [out] uint16 Status
);
```

## Parameters

- *WWPN\[8\]*  
    The world wide port name of the virtual port to create.

- *WWNN\[8\]*  
    The world wide node name to associate with the virtual port.

- *Tag\[16\]*  
    A tag identifier for the virtual port.

- *VirtualName\[64\]*  
    A symbolic name for the virtual port.

- *Status*  
    On return, contains the status of the operation.

## Return value

Not applicable to WMI methods.

## See also

[NPIV Status Codes](npiv-status-codes.md)
