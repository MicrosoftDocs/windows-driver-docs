---
title: Updating the DriverEntry Routine for an NDIS 6.0 Protocol Driver
description: Updating the DriverEntry Routine for an NDIS 6.0 Protocol Driver
ms.assetid: b856816e-1c3b-4397-bda3-87d51e8665f3
keywords:
- NdisRegisterProtocol
- updating DriverEntry
- DriverEntry WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Updating the DriverEntry Routine for an NDIS 6.0 Protocol Driver





Like NDIS 5.*x*, NDIS 6.0 protocol drivers register with NDIS in the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. In NDIS 6.0, the [**NdisRegisterProtocol**](https://msdn.microsoft.com/library/windows/hardware/ff554653) function is eliminated. To register the protocol driver with NDIS 6.0, call the [**NdisRegisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff564520) function.

Like **NdisRegisterProtocol**, the input parameters to **NdisRegisterProtocolDriver** include the [**NDIS\_PROTOCOL\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566825) structure (formerly NDIS\_PROTOCOL\_CHARACTERISTICS) and a pointer to an NDIS\_HANDLE at *NdisProtocolHandle* . NDIS provides the handle to identify the driver. In addition, **NdisRegisterProtocolDriver** includes the *ProtocolDriverContext* parameter that specifies a handle to a driver-allocated context area where the driver maintains state and configuration information. NDIS later passes the value at *ProtocolDriverContext* to the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function.

If the call to **NdisRegisterProtocolDriver** succeeds, the protocol driver must later call the [**NdisDeregisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff561743) function. Call **NdisDeregisterProtocolDriver** in the context of the protocol driver's [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine.

If an error occurs after a successful call to **NdisRegisterProtocolDriver**, the driver must call the **NdisDeregisterProtocolDriver** function before **DriverEntry** returns.

For more information about NDIS 6.0 driver initialization, see [Initializing a Protocol Driver](initializing-a-protocol-driver.md).

 

 





