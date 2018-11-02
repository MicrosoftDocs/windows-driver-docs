---
title: Updating the NDIS 6.0 Miniport Driver Characteristics Structure
description: Updating the NDIS 6.0 Miniport Driver Characteristics Structure
ms.assetid: d57f6474-e497-43e8-ae27-e989de8213ae
keywords:
- NDIS_MINIPORT_DRIVER_CHARACTERISTICS
- updating protocol driver characteristics structure
- characteristics structure WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Updating the NDIS 6.0 Miniport Driver Characteristics Structure





Many entry points in the NDIS 5.*x* NDIS\_MINIPORT\_CHARACTERISTICS structure have been removed from the NDIS 6.0 version of the structure. The NDIS 6.0 version of the structure is named [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958).

Most NDIS 6.0 data structures contain structure version information in the object header member, which is the first member of the structure. The version information is specified in the [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The object header has three members: **Type**, **Size**, and **Revision**. Calls to NDIS 6.0 functions will succeed only if the header information is correct. The following example illustrates correct header initialization:

```C++
MPChar.Header.Type     = NDIS_OBJECT_TYPE_MINIPORT_DRIVER_CHARACTERISTICS,
MPChar.Header.Size     = sizeof(NDIS_MINIPORT_DRIVER_CHARACTERISTICS);
MPChar.Header.Revision = NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_1;
```

In the following examples, *MPChar* is a structure of type [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958). The lines marked *5.x* show NDIS 5.x initialization for comparison with the unmarked lines that illustrate replacement NDIS 6.0 initialization.

```C++
5.x MPChar.MajorNdisVersion             = 5;
5.x MPChar.MinorNdisVersion             = 1;

    MPChar.MajorNdisVersion             = 6;
    MPChar.MinorNdisVersion             = 0;
```

NDIS 6.0 miniport drivers can specify a driver version. The driver version is independent of the NDIS major and minor version shown above.

```C++
    MPChar.MajorDriverVersion = NIC_MAJOR_DRIVER_VERSION;
    MPChar.MinorDriverVersion = NIC_MINOR_DRIVER_VERSION;
```

Replace the [**MiniportInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff550472) function with the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function as follows:

```C++
5.x MPChar.InitializeHandler           = MiniportInitialize;

    MPChar.InitializeHandlerEx         = MiniportInitializeEx;
```

Replace the [**MiniportHalt**](https://msdn.microsoft.com/library/windows/hardware/ff549451) function with the [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function as follows:

```C++
5.x MPChar.HaltHandler                  = MiniportHalt;

    MPChar.HaltHandlerEx                = MiniportHaltEx;
```

Replace the [**MiniportPnPEventNotify**](https://msdn.microsoft.com/library/windows/hardware/ff550487) function with the [*MiniportDevicePnPEventNotify*](https://msdn.microsoft.com/library/windows/hardware/ff559369) function as follows:

```C++
5.x MPChar.PnPEventNotifyHandler            = MiniportPnPEventNotify;

    MPChar.DevicePnPEventNotifyHandler      = MiniportDevicePnPEventNotify;
```

Replace the [**MiniportShutdown**](https://msdn.microsoft.com/library/windows/hardware/ff550533) function with the [*MiniportShutdownEx*](https://msdn.microsoft.com/library/windows/hardware/ff559449) function as follows:

```C++
5.x MPChar.AdapterShutdownHandler       = MiniportShutdown;

    MPChar.ShutdownHandlerEx            = MiniportShutdownEx;
```

Replace the [**MiniportCheckForHang**](https://msdn.microsoft.com/library/windows/hardware/ff549367) function with the [*MiniportCheckForHangEx*](https://msdn.microsoft.com/library/windows/hardware/ff559346) function as follows:

```C++
5.x MPChar.CheckForHangHandler          = MiniportCheckForHang;

    MPChar.CheckForHangHandlerEx        = MiniportCheckForHangEx;
```

Replace the [*MiniportReset*](https://msdn.microsoft.com/library/windows/hardware/ff550502) function with the [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function as follows:

```C++
5.x MPChar.ResetHandler                 = MiniportReset;

    MPChar.ResetHandlerEx               = MiniportResetEx;
```

Remove the [**MiniportQueryInformation**](https://msdn.microsoft.com/library/windows/hardware/ff550490) and [**MiniportSetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff550530) functions and replace them with the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function as follows:

```C++
5.x MPChar.QueryInformationHandler      = MiniportQueryInformation;
5.x MPChar.SetInformationHandler        = MiniportSetInformation;

    MPChar.OidRequestHandler            = MiniportOidRequest;
```

To register optional services, provide an entry point for the [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function as follows:

```C++
    MPChar.SetOptionsHandler = MiniportSetOptions;
```

Interrupt functions are not specified in the NDIS 6.0 driver characteristics structure. Remove the interrupt function entry points from the driver characteristics as follows:

```C++
5.x MPChar.HandleInterruptHandler       = MiniportHandleInterrupt;
5.x MPChar.ISRHandler                   = MiniportISR;

(Removed in NDIS 6.0)
```

To register interrupt entry points with NDIS 6.0, call the [**NdisMRegisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563649) function. The interrupt functions are specified in the [**NDIS\_MINIPORT\_INTERRUPT\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566465) structure. For more information about interrupts, see [Porting Miniport Driver Interrupt Operations to NDIS 6.0](porting-miniport-driver-interrupt-operations-to-ndis-6-0.md).

Send and receive functions that use the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) and [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures replace functions that use [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures as follows:

```C++
5.x MPChar.ReturnPacketHandler          = MiniportReturnPacket;
5.x MPChar.SendPacketsHandler           = MiniportSendPackets;
5.x MPChar.CancelSendPacketsHandler     = MiniportCancelSendPackets;

    MPChar.SendNetBufferListsHandler    = MiniportSendNetBufferLists;
    MPChar.CancelSendHandler            = MiniportCancelSendNetBufferLists;
    MPChar.ReturnNetBufferListsHandler  = MiniportReturnNetBufferLists;
```

For more information about the NET\_BUFFER and NET\_BUFFER\_LIST structures, see [NET\_BUFFER Architecture](net-buffer-architecture.md).

To support unloading, pausing, and restarting the miniport driver, add the [*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378), [*MiniportPause*](https://msdn.microsoft.com/library/windows/hardware/ff559418), and [**MiniportRestart**](https://msdn.microsoft.com/library/windows/hardware/ff559435) functions as follows:

```C++
    MPChar.UnloadHandler                = MiniportDriverUnload;
    MPChar.PauseHandler                 = MiniportPause;
    MPChar.RestartHandler               = MiniportRestart;
```

For more information about pause and restart operations, see [Driver Stack Management](driver-stack-management.md).

 

 





