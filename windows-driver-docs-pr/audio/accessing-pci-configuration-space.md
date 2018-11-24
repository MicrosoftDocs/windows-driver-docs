---
title: Accessing PCI Configuration Space
description: Accessing PCI Configuration Space
ms.assetid: 4ec520db-7976-40e8-8336-f9056dc024b1
keywords:
- PCI configuration space WDK audio
- audio adapter drivers WDK , PCI configuration space
- adapter drivers WDK audio , PCI configuration space
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing PCI Configuration Space


## <span id="accessing_pci_configuration_space"></span><span id="ACCESSING_PCI_CONFIGURATION_SPACE"></span>


In Windows Me/98, and Windows 2000 and later, an adapter driver can access its adapter card's PCI configuration space at IRQL PASSIVE\_LEVEL by using the [**IRP\_MN\_READ\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551727) and [**IRP\_MN\_WRITE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551769) requests.

In Windows 2000 and later, PCI driver stacks export the [**BUS\_INTERFACE\_STANDARD**](https://msdn.microsoft.com/library/windows/hardware/ff540707) interface, which provides access to the PCI configuration space at IRQL DISPATCH\_LEVEL.

For more information, see [Accessing Device Configuration Space](https://msdn.microsoft.com/library/windows/hardware/ff540450).

 

 




