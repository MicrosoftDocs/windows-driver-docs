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

An NDIS intermediate driver registers its *MiniportXxx* functions and its *ProtocolXxx* functions in the context of its [DriverEntry](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. To register its *MiniportXxx* functions, an intermediate driver must call the [NdisMRegisterMiniportDriver](https://msdn.microsoft.com/library/windows/hardware/ff563654) function with the NDIS\_INTERMEDIATE\_DRIVER flag set. This flag is in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure that the driver passes at *MiniportDriverCharacteristics*. To register its *ProtocolXxx* functions, an intermediate driver must call the [NdisRegisterProtocolDriver](https://msdn.microsoft.com/library/windows/hardware/ff564520) function.

[DriverEntry](https://msdn.microsoft.com/library/windows/hardware/ff544113) returns STATUS_SUCCESS, or its equivalent NDIS_STATUS_SUCCESS, if the driver registered as an NDIS intermediate driver successfully. If DriverEntry fails initialization by propagating an error status that was returned by an **NdisXxx** function or by a kernel-mode support routine, the driver will not remain loaded. **DriverEntry** must execute synchronously; that is, it cannot return STATUS_PENDING or its equivalent NDIS_STATUS_PENDING.

To register the intermediate driver with NDIS, the [DriverEntry](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine must, at a minimum:

- Call the [NdisMRegisterMiniportDriver](https://msdn.microsoft.com/library/windows/hardware/ff563654) function with the NDIS_INTERMEDIATE_DRIVER flag set to register the driver's *MiniportXxx* functions.
- Call the [NdisRegisterProtocolDriver](https://msdn.microsoft.com/library/windows/hardware/ff564520) function to register the driver's *ProtocolXxx* functions if the driver subsequently binds itself to an underlying NDIS driver.
- Call the [NdisIMAssociateMiniport](https://msdn.microsoft.com/library/windows/hardware/ff562717) function to inform NDIS about the association between the driver's miniport upper edge and protocol lower edge.

If an error occurs in **DriverEntry** after **NdisMRegisterMiniportDriver** returns successfully, the driver must call the [NdisMDeregisterMiniportDriver](https://msdn.microsoft.com/library/windows/hardware/ff563578) function before **DriverEntry** returns. If **DriverEntry** succeeds, the driver must call **NdisMDeregisterMiniportDriver** from its [MiniportDriverUnload](https://msdn.microsoft.com/library/windows/hardware/ff559378) function.

Intermediate drivers share most of the **DriverEntry** requirements of protocol drivers and miniport drivers.

The initialization of an intermediate driver's virtual miniport occurs when the driver calls the [NdisIMInitializeDeviceInstanceEx](https://msdn.microsoft.com/library/windows/hardware/ff562727) function from its [ProtocolBindAdapterEx](https://msdn.microsoft.com/library/windows/hardware/ff570220) function.

NDIS calls the *ProtocolBindAdapterEx* function after all underlying miniport drivers have initialized.

In effect, the **DriverEntry** function of an NDIS intermediate driver can ignore the *RegistryPath* pointer after passing it to **NdisMRegisterMiniportDriver**. Such a driver can also ignore the *DriverObject* pointer after passing it to **NdisMRegisterMiniportDriver**. However, the driver should save the miniport driver handle value that is returned by **NdisMRegisterMiniportDriver** at *NdisMiniportDriverHandle* and the protocol handle value that is returned by **NdisRegisterProtocolDriver** at *NdisProtocolHandle* for subsequent calls to **NdisXxx** functions. The intermediate driver's *ProtocolBindAdapterEx* function binds the driver to each underlying miniport driver before its *MiniportInitializeEx* function is called to initialize the intermediate driver's virtual miniport. Still higher level protocol drivers subsequently bind themselves to the virtual miniport that it creates. This strategy enables an NDIS intermediate driver to allocate resources at the creation of the virtual miniport according to the features of the underlying miniport driver to which it is bound.