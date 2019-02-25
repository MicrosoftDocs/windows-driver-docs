---
title: DriverEntry Guidelines for PF Miniport Drivers
description: DriverEntry Guidelines for PF Miniport Drivers
ms.assetid: 6F885379-41EC-411E-8909-4DF48042849A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DriverEntry Guidelines for PF Miniport Drivers


This topic describes the guidelines for writing a [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff548818) function for the miniport driver of the PCI Express (PCIe) Physical Function (PF). The PF is a component of a network adapter that supports single root I/O virtualization (SR-IOV).

**Note**  These guidelines only apply to PF miniport drivers. For initialization guidelines for the miniport driver of a PCIe Virtual Function (VF) of the adapter, see [Initializing a VF Miniport Driver](initializing-a-vf-miniport-driver.md).

 

The SR-IOV network adapter must implement a hardware bridge that forwards network traffic over the physical port on the adapter and internal virtual ports (VPorts). This bridge is known as the *NIC switch*. For more information, see [NIC Switches](nic-switches.md).

If the PF miniport driver supports the static creation of the NIC switch on the SR-IOV network adapter, it may need to allocate switch resources when the functional device object (FDO) is created for the network adapter in the device stack. In this case, the driver must allocate those resources before NDIS calls [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389). To do this, the driver must register optional Plug-and-Play (PnP) handlers so that it can participate in the process when the adapter's FDO is added or removed from the device stack.

The miniport driver must provide a [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function to register these PnP handler functions. To do this, the driver follows these steps from the context of the call to its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff548818) function:

1.  The miniport driver initializes an [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure with the entry points of the *MiniportXxx* functions. In particular, the driver sets the **SetOptionsHandler** member to the entry point of the driver's [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function.

2.  The miniport driver calls the [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) function to register its entry points. From the context of this call, NDIS calls the driver's [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function

3.  When NDIS calls [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443), the miniport driver calls the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function and specifies an [**NDIS\_MINIPORT\_PNP\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566475) structure. This structure defines the entry points for the [*MiniportAddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559332), [*MiniportRemoveDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559427), [*MiniportStartDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559452), and [*MiniportFilterResourceRequirements*](https://msdn.microsoft.com/library/windows/hardware/ff559384) functions. NDIS calls these handler functions when it handles PnP I/O request packets (IRPs) issued by the PCI bus driver.

    If the PF miniport driver must allocate additional software resources for the NIC switch before NDIS calls the driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the driver must register a [*MiniportAddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559332) function. When NDIS calls the *MiniportAddDevice* function, the PF miniport driver can call [**NdisReadConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff564511) to read the NIC switch configuration keyword settings from the registry. For more information about these keywords, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

    For more information about guidelines for the [*MiniportAddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559332) function, see [*MiniportAddDevice* Guidelines for PF Miniport Drivers](miniportadddevice-guidelines-for-pf-miniport-drivers.md).

For more information on how NIC switches are created, see [Creating a NIC Switch](creating-a-nic-switch.md).

 

 





