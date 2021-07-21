---
title: DriverEntry of SCSI Miniport Driver routine
description: Each miniport driver must have a routine explicitly named DriverEntry in order to be loaded.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
keywords: ["DriverEntry routine Storage Devices"]
topic_type:
- apiref
api_name:
- DriverEntry
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DriverEntry of SCSI Miniport Driver routine


Each miniport driver must have a routine explicitly named **DriverEntry** in order to be loaded.

> [!NOTE]
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](./storport-driver-overview.md) and [Storport miniport](./storport-miniport-drivers.md) driver models.

 

## Syntax

```ManagedCPlusPlus
ULONG DriverEntry(
  _In_ PVOID Argument1,
  _In_ PVOID Argument2
);
```

## Parameters

*Argument1* \[in\]  
Is a pointer with which the miniport driver must call **ScsiPortInitialize**.

*Argument2* \[in\]  
Is a pointer with which the miniport driver must call **ScsiPortInitialize**.

## Return value

**DriverEntry** returns the value returned by **ScsiPortInitialize**. If it calls **ScsiPortInitialize** more than once, **DriverEntry** returns the lowest value returned by **ScsiPortInitialize**.

## Remarks

A miniport driver's **DriverEntry** routine allocates memory on the stack and initializes a HW\_INITIALIZATION\_DATA structure with zeros. **DriverEntry** must zero all members in the HW\_INITIALIZATION\_DATA structure before initializing it with values appropriate to the HBA(s) the miniport driver supports.

**DriverEntry** should set the **HwInitializationDataSize** member to **sizeof**(HW\_INITIALIZATION\_DATA) to indicate which version of this structure it is using, as well as initializing all members appropriately for its HBA(s).

Next, **DriverEntry** calls **ScsiPortInitialize**. If a miniport driver supports HBA(s) that can be connected on more than one type of I/O bus, such as both **MicroChannel** and **Isa** type buses, it should call **ScsiPortInitialize** once for each type of I/O bus. Such a miniport driver must return the lowest value returned by its calls to **ScsiPortInitialize** from the **DriverEntry** routine. A miniport driver writer can make no assumptions about the values returned by **ScsiPortInitialize**.

## <span id="see_also"></span>See also


[**HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/srb/ns-srb-_hw_initialization_data)

[*HwScsiFindAdapter*](/previous-versions/windows/hardware/drivers/ff557300(v=vs.85))

[**ScsiPortInitialize**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportinitialize)

