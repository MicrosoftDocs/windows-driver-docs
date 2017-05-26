---
title: Initializing an Intermediate Driver
description: Initializing an Intermediate Driver
ms.assetid: cd4903f8-f522-403a-bec4-03ee7e82dcac
keywords:
- NDIS intermediate drivers WDK , initializing
- intermediate drivers WDK networking , initializing
- initializing intermediate drivers
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Initializing an Intermediate Driver


## <a href="" id="ddk-initializing-an-intermediate-driver-ng"></a>


An NDIS intermediate driver registers its *MiniportXxx* functions and its *ProtocolXxx* functions in the context of its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. To register its *MiniportXxx* functions, an intermediate driver must call the [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) function with the NDIS\_INTERMEDIATE\_DRIVER flag set. This flag is in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure that the driver passes at *MiniportDriverCharacteristics* . To register its *ProtocolXxx* functions, an intermediate driver must call the [**NdisRegisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff564520) function.

If an error occurs in **DriverEntry** after **NdisMRegisterMiniportDriver** returns successfully, the driver must call the [**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578) function before **DriverEntry** returns. If **DriverEntry** succeeds, the driver must call **NdisMDeregisterMiniportDriver** from its [*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378) function.

After a driver calls **NdisMRegisterMiniportDriver**, the driver should be prepared to be called back at its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function.

 

 





