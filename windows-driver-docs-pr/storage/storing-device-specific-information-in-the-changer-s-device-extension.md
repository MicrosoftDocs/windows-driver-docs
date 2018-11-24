---
title: Storing Device-Specific Information in the Changer's Device Extension
description: Storing Device-Specific Information in the Changer's Device Extension
ms.assetid: 72048d84-1c2d-4f3c-b5e8-f55a812ad567
keywords:
- changer drivers WDK storage , device-specific data storage
- storage changer drivers WDK , device-specific data storage
- device-specific data storage WDK changer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storing Device-Specific Information in the Changer's Device Extension


## <span id="ddk_storing_device_specific_information_in_the_changers_device_extensi"></span><span id="DDK_STORING_DEVICE_SPECIFIC_INFORMATION_IN_THE_CHANGERS_DEVICE_EXTENSI"></span>


A changer miniclass driver specifies the storage it requires for device-specific data in its [**ChangerAdditionalExtensionSize**](https://msdn.microsoft.com/library/windows/hardware/ff551400) routine. The changer class driver allocates the requested storage on behalf of the changer miniclass driver, then calls the miniclass driver's [**ChangerInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff551431) routine.

Whether the changer miniclass driver stores data in the device extension and what data it stores, is up to the driver designer. It typically includes SCSI inquiry data or the non-SCSI equivalent for changer devices.

The device extension might also include data that the miniclass driver uses to translate between device-specific element addresses and the zero-based element addresses passed in requests. In requests, elements are addressed by element type, starting with zero for the first element of a given type. Device-specific addresses typically do not follow this element addressing scheme, so the changer miniclass driver must translate the zero-based element addresses it receives into device-specific element addresses.

It does not matter how a miniclass driver translates element addresses as long as the addresses are translated. To optimize the process, a miniclass driver might store data that facilitates translation in the device extension. For example, at initialization, the driver could obtain device-specific element addresses from the SCSI element address assignment page or non-SCSI equivalent, map them to offsets that can be used to reconstruct the device-specific addresses, and store the offsets in the device extension. Then, when the changer miniclass driver receives a request that contains a zero-based element address, it could use the offset stored in the device extension to translate the zero-based address to a device-specific equivalent. The changer miniclass driver can use these device-specific addresses in the SRBs it sends to the system port driver.

 

 




