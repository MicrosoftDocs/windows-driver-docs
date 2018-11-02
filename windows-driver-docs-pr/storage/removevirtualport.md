---
title: RemoveVirtualPort method
description: The RemoveVirtualPort method removes a virtual port for a specific world wide port name (WWPN) .
ms.assetid: 47A85B72-821C-4552-BA6E-1742D58B54A4
keywords: ["RemoveVirtualPort method Storage Devices"]
topic_type:
- apiref
api_name:
- RemoveVirtualPort
api_type:
- COM
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# RemoveVirtualPort method


The **RemoveVirtualPort** method removes a virtual port for a specific world wide port name (WWPN) .

Syntax
------

```ManagedCPlusPlus
void RemoveVirtualPort(
   [in] uint8   WWPN[8],
   [out] uint16 Status
);
```

Parameters
----------

*WWPN\[8\]*   
The world wide port name of the virtual port to remove.

*Status*   
On return, contains the status of the operation.

Return value
------------

Not applicable to WMI methods.

## <span id="see_also"></span>See also


[NPIV Status Codes](https://msdn.microsoft.com/library/windows/hardware/dn386176)

 

 






