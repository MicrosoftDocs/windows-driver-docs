---
title: Performing Control Operations on a Client Object
description: Performing Control Operations on a Client Object
keywords:
- Winsock Kernel WDK networking , control operations
- WSK WDK networking , control operations
- control operations WDK Winsock Kernel
- client objects WDK Winsock Kernel
ms.date: 04/20/2017
---

# Performing Control Operations on a Client Object


After a Winsock Kernel (WSK) application has successfully attached to the WSK subsystem, it can perform control operations on the client object ( [**WSK\_CLIENT**](./wsk-client.md)) that was returned by the WSK subsystem during attachment. These control operations are not specific to a particular socket, but instead have a more general scope. For more information about each of the control operations that can be performed on a client object, see [WSK Client Control Operations](wsk-cache-sd.md).

A WSK application performs client control operations by calling the [**WskControlClient**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_client) function. The **WskControlClient** function is pointed to by the **WskControlClient** member of the [**WSK\_PROVIDER\_DISPATCH**](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_provider_dispatch) structure that was returned by the WSK subsystem during attachment.

The following code example shows how a WSK application can use the [**WSK\_TRANSPORT\_LIST\_QUERY**](./wsk-transport-list-query.md) client control operation to retrieve a list of available network transports that can be specified when creating a new socket.

```C++
// Function to retrieve a list of available network transports
NTSTATUS
  GetTransportList(
    PWSK_PROVIDER_NPI WskProviderNpi,
    PWSK_TRANSPORT TransportList,
    ULONG MaxTransports,
    PULONG TransportsRetrieved
    )
{
  SIZE_T BytesRetrieved;
  NTSTATUS Status;

  // Perform client control operation
  Status =
    WskProviderNpi->Dispatch->
        WskControlClient(
          WskProviderNpi->Client,
          WSK_TRANSPORT_LIST_QUERY,
          0,
          NULL,
          MaxTransports * sizeof(WSK_TRANSPORT),
          TransportList,
          &BytesRetrieved,
          NULL  // No IRP for this control operation
          );

  // Convert bytes retrieved to transports retrieved
  TransportsRetrieved = BytesRetrieved / sizeof(WSK_TRANSPORT);

  // Return status of client control operation
  return Status;
}
```

 

