---
title: Using TDI Transports
description: Using TDI Transports
ms.assetid: 58fb5e62-e15d-4f15-8eb3-3e302ea08c4f
keywords:
- TDI transports WDK Winsock Kernel
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using TDI Transports


The Winsock Kernel (WSK) subsystem provides support for using [TDI](https://msdn.microsoft.com/library/windows/hardware/ff565094) transports. In order to use TDI transports via the WSK [Network Programming Interface (NPI)](network-programming-interface.md), a WSK application must map the combination of address family, socket type, and protocol for each of the TDI transports it uses to the associated device name of each of those TDI transports. A WSK application maps combinations of address family, socket type, and protocol to device names of TDI transports by using the [**WSK\_TDI\_DEVICENAME\_MAPPING**](https://msdn.microsoft.com/library/windows/hardware/ff571190) client control operation.

The following code example shows how a WSK application can map combinations of address family, socket type, and protocol to device names of TDI transports.

```C++
// Number of TDI mappings
#define MAPCOUNT 2

// Array of TDI mappings
const WSK_TDI_MAP TdiMap[MAPCOUNT] =
{
  {SOCK_STREAM, ..., ..., ...},
  {SOCK_DGRAM, ..., ..., ...}
};

// TDI map info structure
const WSK_TDI_MAP_INFO TdiMapInfo =
{
  MAPCOUNT,
  TdiMap
}

// Function to set the TDI map
NTSTATUS
  SetTdiMap(
    PWSK_APP_BINDING_CONTEXT BindingContext
  )
{
  NTSTATUS Status;

  // Perform client control operation
  Status =
    BindingContext->
      WskProviderDispatch->
        WskControlClient(
          BindingContext->WskClient,
          WSK_TDI_DEVICENAME_MAPPING,
          sizeof(WSK_TDI_MAP_INFO),
          &TdiMapInfo,
          0,
          NULL,
          NULL,
          NULL  // No IRP for this control operation
          );

  // Return status of client control operation
  return Status;
}
```

A WSK application must map combinations of address family, socket type, and protocol to device names of TDI transports before it creates any sockets. After the WSK application has successfully mapped the combinations of address family, socket type, and protocol to device names of TDI transports, the application can then create new sockets that use the mapped TDI transports.

**Note**  TDI will not be supported in Microsoft Windows versions after Windows Vista. Use [Windows Filtering Platform](https://msdn.microsoft.com/library/windows/hardware/ff571067) or [Winsock Kernel](https://msdn.microsoft.com/library/windows/hardware/ff571083) instead.

 

 

 





