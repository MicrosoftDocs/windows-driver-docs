---
title: Querying for Bluetooth Interfaces
description: Querying for Bluetooth interfaces
keywords:
- Bluetooth WDK , interface queries
- querying Bluetooth interfaces
- interfaces WDK Bluetooth
ms.date: 01/10/2024
---

# Querying for Bluetooth interfaces

The Bluetooth driver stack exposes the following interfaces that profile drivers can use to interact with Bluetooth devices.

| Interface | Description |
|--|--|
| GUID_BTHDDI_SDP_NODE_INTERFACE | Profile drivers query for the GUID_BTHDDI_SDP_NODE_INTERFACE to obtain pointers to functions that allow them to create Service Discovery Protocol (SDP) records.</br></br>This interface corresponds to the **[BTHDDI_SDP_NODE_INTERFACE](/windows-hardware/drivers/ddi/bthsdpddi/ns-bthsdpddi-_bthddi_sdp_node_interface)** structure. |
| GUID_BTHDDI_SDP_PARSE_INTERFACE | Profile drivers query for the GUID_BTHDDI_SDP_PARSE_INTERFACE to obtain pointers to functions that allow them to parse SDP records.</br></br>This interface corresponds to the **[BTHDDI_SDP_PARSE_INTERFACE](/windows-hardware/drivers/ddi/bthsdpddi/ns-bthsdpddi-_bthddi_sdp_parse_interface)** structure. |
| GUID_BTHDDI_PROFILE_DRIVER_INTERFACE | Profile drivers query for the BTHDDI_PROFILE_DRIVER_INTERFACE to obtain pointers to functions that allow them to create, allocate, reuse, and free BRBs.</br></br>This interface corresponds to the **[BTH_PROFILE_DRIVER_INTERFACE](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_bth_profile_driver_interface)** structure. |

To obtain any of these interfaces, a profile driver must first build and send an [**IRP\_MN\_QUERY\_INTERFACE**](../kernel/irp-mn-query-interface.md) IRP to the Bluetooth driver stack.

The following procedure is the general process to obtain one of these interfaces.

## To query for an interface

1. Allocate and initialize an IRP.
1. Allocate and initialize an instance of the interface.
1. Specify the major and minor function codes to query for the interface.
1. Specify the interface to query for.
1. Pass the IRP down the driver stack to be processed.

The following pseudocode example demonstrates how to set up an IRP\_MN\_QUERY\_INTERFACE IRP to query the Bluetooth driver stack for the GUID\_BTHDDI\_PROFILE\_DRIVER\_INTERFACE. For readability, the example does not demonstrate error handling.

```cpp
#include <bthddi.h>

...

// Define a custom pool tag to identify your profile driver's dynamic memory allocations. You should change this tag to easily identify your driver's allocations from other drivers.
#define PROFILE_DRIVER_POOL_TAG '_htB'

PIRP Irp;
Irp = IoAllocateIrp( DeviceExtension->ParentDeviceObject->StackSize, FALSE );

PBTH_PROFILE_DRIVER_INTERFACE BthInterface; // Define storage for an instance of the BTH_PROFILE_DRIVER_INTERFACE structure
BthInterface = ExAllocatePoolWithTag( NonPagedPool, sizeof( BTH_PROFILE_DRIVER_INTERFACE ), PROFILE_DRIVER_POOL_TAG );

// Zero the memory associated with the structure
RtlZeroMemory( BthInterface, sizeof( BTH_PROFILE_DRIVER_INTERFACE ) );

// Set up the next IRP stack location
PIO_STACK_LOCATION NextIrpStack;
NextIrpStack = IoGetNextIrpStackLocation( Irp );
NextIrpStack->MajorFunction = IRP_MJ_PNP;
NextIrpStack->MinorFunction = IRP_MN_QUERY_INTERFACE;
NextIrpStack->Parameters.QueryInterface.InterfaceType = (LPGUID) &GUID_BTHDDI_PROFILE_DRIVER_INTERFACE;
NextIrpStack->Parameters.QueryInterface.Size = sizeof( BTH_PROFILE_DRIVER_INTERFACE );
NextIrpStack->Parameters.QueryInterface.Version = BTHDDI_PROFILE_DRIVER_INTERFACE_VERSION_FOR_QI;
NextIrpStack->Parameters.QueryInterface.Interface = (PINTERFACE) BthInterface;
NextIrpStack->Parameters.QueryInterface.InterfaceSpecificData = NULL;

// Pass the IRP down the driver stack
NTSTATUS Status;
Status = IoCallDriver( DeviceExtension->NextLowerDriver, Irp );
```

If the IRP returns successfully, the profile driver can then access and use the function pointers that are contained in the interface.
