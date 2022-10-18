---
title: RescanVirtualPort method (Windows Drivers)
description: Learn more about the RescanVirtualPort method.
ms.date: 10/14/2022
---

# RescanVirtualPort method

Rescans a virtual port and all logical buses associated with that port.

## Syntax

``` c++
void RescanVirtualPort(
   [in] uint8   WWPN[8],
   [out] uint16 Status
);
```

## Parameters

- *WWPN\[8\]*  
    The world wide port name of the virtual port to rescan.

- *Status*  
    On return, contains the status of the operation.

## Return value

Not applicable to WMI methods.

## Remarks

This method causes a rescan of the virtual port and all the logical buses associated with that port. The miniport is expected to notify Storport for a bus rescan with the target path.

## See also

[NPIV Status Codes](npiv-status-codes.md)

[**StorPortNotification for BusChangeDetected**](/windows-hardware/drivers/ddi/storport/nf-storport-storportnotification)
