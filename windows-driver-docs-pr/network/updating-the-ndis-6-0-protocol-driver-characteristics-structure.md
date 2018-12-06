---
title: Updating the NDIS 6.0 Protocol Driver characteristics Structure
description: Updating the NDIS 6.0 Protocol Driver characteristics Structure
ms.assetid: 2f2ca525-7379-4c63-9c80-7dd24c011b4d
keywords:
- NDIS_PROTOCOL_CHARACTERISTICS
- updating protocol driver characteristics structure
- NDIS_PROTOCOL_DRIVER_CHARACTERISTICS
- characteristics structure WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Updating the NDIS 6.0 Protocol Driver characteristics Structure





Many entry points that are found in the NDIS 5.*x* NDIS\_PROTOCOL\_CHARACTERISTICS structure are removed from the NDIS 6.0 version of the structure. The NDIS 6.0 version of the structure is named [**NDIS\_PROTOCOL\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566825).

Most NDIS 6.0 data structures contain structure version information in the object header member, which is the first member of the structure. The version information is specified in the [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The object header has three members: **Type**, **Size**, and **Revision** . If the header information is incorrect, calls to NDIS 6.0 functions will fail. The following example illustrates the header initialization:

```C++
ProtocolChar.Header.Type = NDIS_OBJECT_TYPE_PROTOCOL_DRIVER_CHARACTERISTICS,
ProtocolChar.Header.Size = sizeof(NDIS_PROTOCOL_DRIVER_CHARACTERISTICS);
ProtocolChar.Header.Revision = NDIS_PROTOCOL_DRIVER_CHARACTERISTICS_REVISION_1;
```

In the following examples, **ProtocolChar** is a structure of type NDIS\_PROTOCOL\_DRIVER\_CHARACTERISTICS. Strikeouts indicate the changed NDIS 5.*x* driver equivalent.

Set the NDIS 6.0 protocol drivers' major and minor version numbers to 6 and 0, respectively.

```C++
 ProtocolChar.MajorNdisVersion             = 5;
    ProtocolChar.MajorNdisVersion             = 6;
 ProtocolChar.MinorNdisVersion             = 1;
    ProtocolChar.MinorNdisVersion             = 0;
```

NDIS 6.0 protocol drivers must specify a driver version. The driver version is independent of the NDIS major and minor version.

```C++
    ProtocolChar.MajorDriverVersion = PROTOCOL_MAJOR_DRIVER_VERSION;
    ProtocolChar.MinorDriverVersion = PROTOCOL_MINOR_DRIVER_VERSION;
```

Replace the [**ProtocolBindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff562465) function with the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function.

```C++
 ProtocolChar.BindAdapterHandler           = ProtocolBindAdapter;
    ProtocolChar.BindAdapterHandlerEx         = ProtocolBindAdapterEx;
```

Replace the [**ProtocolUnbindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff563260) function with the [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) function.

```C++
 ProtocolChar.UnbindAdapterHandler                  = ProtocolUnbindAdapter;
    ProtocolChar.UnbindAdapterHandlerEx                = ProtocolUnbindAdapterEx;
```

Replace the [**ProtocolOpenAdapterComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563238) function with the [*ProtocolOpenAdapterCompleteEx*](https://msdn.microsoft.com/library/windows/hardware/ff570265) function.

```C++
 ProtocolChar.OpenAdapterCompleteHandler           = ProtocolOpenAdapterComplete;
    ProtocolChar.OpenAdapterCompleteHandlerEx         = ProtocolOpenAdapterCompleteEx;
```

Replace the [**ProtocolCloseAdapterComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562502) function with the [*ProtocolCloseAdapterCompleteEx*](https://msdn.microsoft.com/library/windows/hardware/ff570236) function.

```C++
 ProtocolChar.CloseAdapterCompleteHandler                  = ProtocolCloseAdapterComplete;
    ProtocolChar.CloseAdapterCompleteHandlerEx                = ProtocolCloseAdapterCompleteEx;
```

Replace the [**ProtocolPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff563243) function with the [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function.

```C++
 ProtocolChar.PnPEventHandler        = ProtocolPnPEvent;
    ProtocolChar.NetPnPEventHandler      = ProtocolNetPnPEvent;
```

Replace the [**ProtocolRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563254) function with the [**ProtocolOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570264) function:

```C++
    ProtocolChar.RequestCompleteHandler        = ProtocolRequestComplete;
    ProtocolChar.OidRequestCompleteHandler        = ProtocolOidRequestComplete;
```

To register optional services, provide an entry point for the [*ProtocolSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff570269) function.

ProtocolChar.SetOptionsHandler = ProtocolSetOptions;

Send and receive functions that use the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) and [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures replace functions that use [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures:

```C++
    ProtocolChar.ReceivePacketHandler          = ProtocolReceivePacket;
    ProtocolChar.SendPacketsCompleteHandler           = ProtocolSendPacketsComplete;
    ProtocolChar.ReceiveNetBufferListsHandler    = ProtocolReceiveNetBufferLists;
    ProtocolChar.SendNetBufferListsCompleteHandler  = ProtocolSendNetBufferListsComplete;
```

For more information about the NET\_BUFFER and NET\_BUFFER\_LIST structures, see [NET\_BUFFER Architecture](net-buffer-architecture.md).

To support system uninstall of a driver, replace the [**ProtocolUnload**](https://msdn.microsoft.com/library/windows/hardware/ff563261) function, if any, with the [*ProtocolUninstall*](https://msdn.microsoft.com/library/windows/hardware/ff570279) function.

```C++
    ProtocolChar.UnloadHandler                = ProtocolUnload;
    ProtocolChar.UninstallHandler                = ProtocolUninstall;
```

 

 





