---
title: Initializing an Intermediate Driver
description: Initializing an Intermediate Driver
keywords:
- NDIS intermediate drivers WDK , initializing
- intermediate drivers WDK networking , initializing
- initializing intermediate drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing an Intermediate Driver



An NDIS intermediate driver registers its *MiniportXxx* functions and its *ProtocolXxx* functions in the context of its [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine. To register its *MiniportXxx* functions, an intermediate driver must call the [NdisMRegisterMiniportDriver](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) function with the NDIS\_INTERMEDIATE\_DRIVER flag set. This flag is in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics) structure that the driver passes at *MiniportDriverCharacteristics*. To register its *ProtocolXxx* functions, an intermediate driver must call the [NdisRegisterProtocolDriver](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisregisterprotocoldriver) function.

[DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) returns STATUS_SUCCESS, or its equivalent NDIS_STATUS_SUCCESS, if the driver registered as an NDIS intermediate driver successfully. If DriverEntry fails initialization by propagating an error status that was returned by an **NdisXxx** function or by a kernel-mode support routine, the driver will not remain loaded. **DriverEntry** must execute synchronously; that is, it cannot return STATUS_PENDING or its equivalent NDIS_STATUS_PENDING.

To register the intermediate driver with NDIS, the [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine must, at a minimum:

- Call the [NdisMRegisterMiniportDriver](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) function with the NDIS_INTERMEDIATE_DRIVER flag set to register the driver's *MiniportXxx* functions.
- Call the [NdisRegisterProtocolDriver](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisregisterprotocoldriver) function to register the driver's *ProtocolXxx* functions if the driver subsequently binds itself to an underlying NDIS driver.
- Call the [NdisIMAssociateMiniport](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisimassociateminiport) function to inform NDIS about the association between the driver's miniport upper edge and protocol lower edge.

If an error occurs in **DriverEntry** after **NdisMRegisterMiniportDriver** returns successfully, the driver must call the [NdisMDeregisterMiniportDriver](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterminiportdriver) function before **DriverEntry** returns. If **DriverEntry** succeeds, the driver must call **NdisMDeregisterMiniportDriver** from its [MiniportDriverUnload](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_unload) function.

Intermediate drivers share most of the **DriverEntry** requirements of protocol drivers and miniport drivers.

The initialization of an intermediate driver's virtual miniport occurs when the driver calls the [NdisIMInitializeDeviceInstanceEx](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisiminitializedeviceinstanceex) function from its [ProtocolBindAdapterEx](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) function.

NDIS calls the *ProtocolBindAdapterEx* function after all underlying miniport drivers have initialized.

In effect, the **DriverEntry** function of an NDIS intermediate driver can ignore the *RegistryPath* pointer after passing it to **NdisMRegisterMiniportDriver**. Such a driver can also ignore the *DriverObject* pointer after passing it to **NdisMRegisterMiniportDriver**. However, the driver should save the miniport driver handle value that is returned by **NdisMRegisterMiniportDriver** at *NdisMiniportDriverHandle* and the protocol handle value that is returned by **NdisRegisterProtocolDriver** at *NdisProtocolHandle* for subsequent calls to **NdisXxx** functions. The intermediate driver's *ProtocolBindAdapterEx* function binds the driver to each underlying miniport driver before its *MiniportInitializeEx* function is called to initialize the intermediate driver's virtual miniport. Still higher level protocol drivers subsequently bind themselves to the virtual miniport that it creates. This strategy enables an NDIS intermediate driver to allocate resources at the creation of the virtual miniport according to the features of the underlying miniport driver to which it is bound.
