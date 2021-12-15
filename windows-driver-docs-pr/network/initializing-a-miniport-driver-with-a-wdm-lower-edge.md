---
title: Initializing a Miniport Driver with a WDM Lower Edge
description: Initializing a Miniport Driver with a WDM Lower Edge
keywords:
- NDIS-WDM miniport drivers WDK networking , initializing
- NDIS-WDM miniport drivers WDK networking , upper edge of
- miniport drivers WDK networking , initializing
- NDIS miniport drivers WDK , initializing
- deserialized NDIS miniport drivers WDK networking
- lower edge of NDIS miniport drivers WDK networking , driver initialization
- WDM lower edge WDK networking , driver initialization
- initializing miniport drivers
ms.date: 04/20/2017
---

# Initializing a Miniport Driver with a WDM Lower Edge





After a miniport driver has been loaded by the operating system, NDIS calls the miniport driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function to initialize a miniport instance that the miniport driver manages. To communicate through a miniport instance that has a WDM lower edge, the miniport driver must retrieve specific information to set up its communications.

During initialization of this miniport instance, the miniport driver must call the [**NdisMGetDeviceProperty**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismgetdeviceproperty) function to retrieve device objects that are required to set up communication with the miniport instance through a WDM interface. In this call, the miniport driver passes the handle to the miniport instance in the *MiniportAdapterHandle* parameter and buffers that receive pointers to [**DEVICE\_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object) structures. The miniport driver uses the retrieved pointer to the next-device object ( *NextDeviceObject* parameter) to create and submit IRPs. For more information, see [Handling IRPs](../kernel/handling-irps.md).

A miniport driver with a WDM lower edge must be a deserialized miniport driver. A deserialized miniport driver manages its own queue of send and receive requests internally whenever it has insufficient resources to handle these requests immediately; if a miniport driver is not deserialized, NDIS manages this queue. An NDIS-WDM miniport driver must be deserialized because it sends and receives packets outside of the context of NDIS calls. During initialization of a miniport instance, an NDIS-WDM miniport driver must specify the deserialized feature. All NDIS 6.0 and later miniport drivers are deserialized.

Note that an NDIS-WDM miniport driver cannot be an intermediate driver (a driver that exposes a miniport driver interface at the top and a protocol driver interface at the bottom).

 

