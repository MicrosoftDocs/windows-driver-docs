---
title: Querying for Bluetooth Interfaces
description: Querying for Bluetooth Interfaces
ms.assetid: 56db29cd-26ab-4262-9b9f-40d46372ffe9
keywords:
- Bluetooth WDK , interface queries
- querying Bluetooth interfaces
- interfaces WDK Bluetooth
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<p>This interface corresponds to the [<strong>BTHDDI_SDP_NODE_INTERFACE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff536635) structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>GUID_BTHDDI_SDP_PARSE_INTERFACE</p></td>
<td align="left"><p>Profile drivers query for the GUID_BTHDDI_SDP_PARSE_INTERFACE to obtain pointers to functions that allow them to parse SDP records.</p>
<p>This interface corresponds to the [<strong>BTHDDI_SDP_PARSE_INTERFACE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff536636) structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>GUID_BTHDDI_PROFILE_DRIVER_INTERFACE</p></td>
<td align="left"><p>Profile drivers query for the BTHDDI_PROFILE_DRIVER_INTERFACE to obtain pointers to functions that allow them to create, allocate, reuse, and free BRBs.</p>
<p>This interface corresponds to the [<strong>BTH_PROFILE_DRIVER_INTERFACE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff536645) structure.</p></td>
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

 

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[bltooth\bltooth]:%20Querying%20for%20Bluetooth%20Interfaces%20%20RELEASE:%20%283/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




