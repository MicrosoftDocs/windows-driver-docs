---
title: Updating Bus-Specific Configuration Space Access for NDIS 6.0
description: Updating Bus-Specific Configuration Space Access for NDIS 6.0
ms.assetid: 1b2c590a-c5b4-43cd-93ee-6c6fd3798761
keywords:
- bus configuration space WDK networking
- miniport adapters WDK networking , bus configuration space
- adapters WDK networking , bus configuration space
- porting miniport drivers WDK networking , adapters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Updating Bus-Specific Configuration Space Access for NDIS 6.0





To read or write to the bus configuration space, a miniport driver calls the [**NdisMGetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff563591) or [**NdisMSetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff563670) function, respectively. These functions replace the [**NdisReadPciSlotInformation**](https://msdn.microsoft.com/library/windows/hardware/ff554554) and [**NdisWritePciSlotInformation**](https://msdn.microsoft.com/library/windows/hardware/ff554871) functions.

The following code samples show how both NDIS 5.*x* miniport drivers and NDIS 6.0 miniport drivers read and write to the PCI configuration space.

### NDIS 5.x Miniport Drivers

Reading

```C++
            ulResult = NdisReadPciSlotInformation(
                           Adapter->AdapterHandle,
                           0,
                           FIELD_OFFSET(PCI_COMMON_CONFIG, Command),
                           &usPciCommand,
                           sizeof(USHORT));
```

Writing

```C++
            ulResult = NdisWritePciSlotInformation(
                           Adapter->AdapterHandle,
                           0,
                           FIELD_OFFSET(PCI_COMMON_CONFIG, Command),
                           &usPciCommand,
                           sizeof(USHORT));
```

### NDIS 6.0 Miniport Drivers

Reading

```C++
            ulResult = NdisMGetBusData(
                           Adapter->AdapterHandle,
                           PCI_WHICHSPACE_CONFIG,
                           FIELD_OFFSET(PCI_COMMON_CONFIG, Command),
                           &usPciCommand,
                           sizeof(USHORT) );
```

Writing

```C++
            ulResult = NdisMSetBusData(
                           Adapter->AdapterHandle,
                           PCI_WHICHSPACE_CONFIG,
                           FIELD_OFFSET(PCI_COMMON_CONFIG, Command),
                           &usPciCommand,
                           sizeof(USHORT) );
```

 

 





