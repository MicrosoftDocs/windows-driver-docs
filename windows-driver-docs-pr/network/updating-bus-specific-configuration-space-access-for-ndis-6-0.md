---
title: Updating Bus-Specific Configuration Space Access for NDIS 6.0
description: Updating Bus-Specific Configuration Space Access for NDIS 6.0
ms.assetid: 1b2c590a-c5b4-43cd-93ee-6c6fd3798761
keywords: ["bus configuration space WDK networking", "miniport adapters WDK networking , bus configuration space", "adapters WDK networking , bus configuration space", "porting miniport drivers WDK networking , adapters"]
---

# Updating Bus-Specific Configuration Space Access for NDIS 6.0


## <a href="" id="ddk-updating-bus-specific-configuration-space-access-for-ndis-6-0-ng"></a>


To read or write to the bus configuration space, a miniport driver calls the [**NdisMGetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff563591) or [**NdisMSetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff563670) function, respectively. These functions replace the [**NdisReadPciSlotInformation**](https://msdn.microsoft.com/library/windows/hardware/ff554554) and [**NdisWritePciSlotInformation**](https://msdn.microsoft.com/library/windows/hardware/ff554871) functions.

The following code samples show how both NDIS 5.*x* miniport drivers and NDIS 6.0 miniport drivers read and write to the PCI configuration space.

### NDIS 5.x Miniport Drivers

Reading

```
            ulResult = NdisReadPciSlotInformation(
                           Adapter->AdapterHandle,
                           0,
                           FIELD_OFFSET(PCI_COMMON_CONFIG, Command),
                           &usPciCommand,
                           sizeof(USHORT));
```

Writing

```
            ulResult = NdisWritePciSlotInformation(
                           Adapter->AdapterHandle,
                           0,
                           FIELD_OFFSET(PCI_COMMON_CONFIG, Command),
                           &usPciCommand,
                           sizeof(USHORT));
```

### NDIS 6.0 Miniport Drivers

Reading

```
            ulResult = NdisMGetBusData(
                           Adapter->AdapterHandle,
                           PCI_WHICHSPACE_CONFIG,
                           FIELD_OFFSET(PCI_COMMON_CONFIG, Command),
                           &usPciCommand,
                           sizeof(USHORT) );
```

Writing

```
            ulResult = NdisMSetBusData(
                           Adapter->AdapterHandle,
                           PCI_WHICHSPACE_CONFIG,
                           FIELD_OFFSET(PCI_COMMON_CONFIG, Command),
                           &usPciCommand,
                           sizeof(USHORT) );
```

 

 





