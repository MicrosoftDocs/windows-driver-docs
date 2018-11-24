---
title: Querying for Bluetooth Interfaces
description: Querying for Bluetooth Interfaces
ms.assetid: 56db29cd-26ab-4262-9b9f-40d46372ffe9
keywords:
- Bluetooth WDK , interface queries
- querying Bluetooth interfaces
- interfaces WDK Bluetooth
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying for Bluetooth Interfaces


The Bluetooth driver stack exposes the following interfaces that profile drivers can use to interact with Bluetooth devices.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Interface</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>GUID_BTHDDI_SDP_NODE_INTERFACE</p></td>
<td align="left"><p>Profile drivers query for the GUID_BTHDDI_SDP_NODE_INTERFACE to obtain pointers to functions that allow them to create Service Discovery Protocol (SDP) records.</p>
<p>This interface corresponds to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536635" data-raw-source="[&lt;strong&gt;BTHDDI_SDP_NODE_INTERFACE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536635)"><strong>BTHDDI_SDP_NODE_INTERFACE</strong></a> structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>GUID_BTHDDI_SDP_PARSE_INTERFACE</p></td>
<td align="left"><p>Profile drivers query for the GUID_BTHDDI_SDP_PARSE_INTERFACE to obtain pointers to functions that allow them to parse SDP records.</p>
<p>This interface corresponds to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536636" data-raw-source="[&lt;strong&gt;BTHDDI_SDP_PARSE_INTERFACE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536636)"><strong>BTHDDI_SDP_PARSE_INTERFACE</strong></a> structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>GUID_BTHDDI_PROFILE_DRIVER_INTERFACE</p></td>
<td align="left"><p>Profile drivers query for the BTHDDI_PROFILE_DRIVER_INTERFACE to obtain pointers to functions that allow them to create, allocate, reuse, and free BRBs.</p>
<p>This interface corresponds to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536645" data-raw-source="[&lt;strong&gt;BTH_PROFILE_DRIVER_INTERFACE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536645)"><strong>BTH_PROFILE_DRIVER_INTERFACE</strong></a> structure.</p></td>
</tr>
</tbody>
</table>

 

To obtain any of these interfaces, a profile driver must first build and send an [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) IRP to the Bluetooth driver stack.

The following procedure is the general process to obtain one of these interfaces.

### <span id="to_query_for_an_interface"></span><span id="TO_QUERY_FOR_AN_INTERFACE"></span>To Query for an Interface

1.  Allocate and initialize an IRP.

2.  Allocate and initialize an instance of the interface.

3.  Specify the major and minor function codes to query for the interface.

4.  Specify the interface to query for.

5.  Pass the IRP down the driver stack to be processed.

The following pseudocode example demonstrates how to set up an IRP\_MN\_QUERY\_INTERFACE IRP to query the Bluetooth driver stack for the GUID\_BTHDDI\_PROFILE\_DRIVER\_INTERFACE.

**Note**  For readability, the following pseudocode example does not demonstrate error handling.

 

```cpp
#include <bthddi.h>

...

// Define a custom pool tag to identify your profile driver&#39;s dynamic memory allocations. You should change this tag to easily identify your driver&#39;s allocations from other drivers.
#define PROFILE_DRIVER_POOL_TAG &#39;_htB&#39;

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

 

 





