---
title: CreateVirtualPort method
description: The CreateVirtualPort method creates a virtual port with a specific world wide port name (WWPN) .
ms.assetid: B4274FB7-2850-4E17-ACDE-5592B0390E8B
keywords: ["CreateVirtualPort method Storage Devices"]
topic_type:
- apiref
api_name:
- CreateVirtualPort
api_type:
- COM
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# CreateVirtualPort method


The **CreateVirtualPort** method creates a virtual port with a specific world wide port name (WWPN) .

Syntax
------

```ManagedCPlusPlus
void CreateVirtualPort(
   [in] uint8   WWPN[8],
   [in] uint8   WWNN[8],
   [in] uint8   Tag[16],
   [in] uint16  VirtualName[64],
   [out] uint16 Status
);
```

Parameters
----------

*WWPN\[8\]*   
The world wide port name of the virtual port to create.

*WWNN\[8\]*   
The world wide node name to associate with the virtual port.

*Tag\[16\]*   
A tag identifier for the virtual port.

*VirtualName\[64\]*   
A symbolic name for the virtual port.

*Status*   
On return, contains the status of the operation.

Return value
------------

Not applicable to WMI methods.

## <span id="see_also"></span>See also


[NPIV Status Codes](https://msdn.microsoft.com/library/windows/hardware/dn386176)

 

 






