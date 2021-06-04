---
title: DEVPKEY_Device_DmaRemappingPolicy
description: DEVPKEY_Device_DmaRemappingPolicy
keywords: ["DEVPKEY_Device_DmaRemappingPolicy Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_DmaRemappingPolicy
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 07/15/2020
---

# DEVPKEY_Device_DmaRemappingPolicy

The value of the DEVPKEY_Device_DmaRemappingPolicy device property indicates the DMA remapping capability of the device.

**Property key**: DEVPKEY_Device_DmaRemappingPolicy  
**Property-data-type identifier**: [**DEVPROP_TYPE_INT32**](devprop-type-int32.md)  
**Property access**: Read-only access by applications and services.  
**Localized?**: No  

 
## Remarks

| Value | Meaning |
| ----- | ------- |
| 2     | Drivers on this device are capable of using DMA remapping. |
| 1     | At least one driver on this device opted out of DMA remapping. |
| 0 or the DMA Remapping Policy property is not visible | A DMA remapping INF directive is not specified in the INF file. DMA remapping is not enforced for this device. |


You can access the DEVPKEY_Device_DmaRemappingPolicy property by calling [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) and [**SetupDiSetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw).

## Requirements

**Version**: Available in Windows 10, version 1803 (Redstone 4)  
**Header**: Devpkey.h (include Devpkey.h)  


## See also

[Enabling DMA remapping for device drivers](../pci/enabling-dma-remapping-for-device-drivers.md)

[Kernel DMA Protection](/windows/security/information-protection/kernel-dma-protection-for-thunderbolt)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

[**SetupDiSetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw)
