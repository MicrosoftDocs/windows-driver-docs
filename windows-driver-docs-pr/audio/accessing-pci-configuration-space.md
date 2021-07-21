---
title: Accessing PCI Configuration Space
description: Accessing PCI Configuration Space
keywords:
- PCI configuration space WDK audio
- audio adapter drivers WDK , PCI configuration space
- adapter drivers WDK audio , PCI configuration space
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing PCI Configuration Space


## <span id="accessing_pci_configuration_space"></span><span id="ACCESSING_PCI_CONFIGURATION_SPACE"></span>


An adapter driver can access its adapter card's PCI configuration space at IRQL PASSIVE\_LEVEL by using the [**IRP\_MN\_READ\_CONFIG**](../kernel/irp-mn-read-config.md) and [**IRP\_MN\_WRITE\_CONFIG**](../kernel/irp-mn-write-config.md) requests.

In Windows 2000 and later, PCI driver stacks export the [**BUS\_INTERFACE\_STANDARD**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_bus_interface_standard) interface, which provides access to the PCI configuration space at IRQL DISPATCH\_LEVEL.

For more information, see [Accessing Device Configuration Space](../kernel/accessing-device-configuration-space.md).

 

