---
title: Storing Device-Specific Information in the Changer's Device Extension
author: windows-driver-content
description: Storing Device-Specific Information in the Changer's Device Extension
ms.assetid: 72048d84-1c2d-4f3c-b5e8-f55a812ad567
keywords: ["changer drivers WDK storage , device-specific data storage", "storage changer drivers WDK , device-specific data storage", "device-specific data storage WDK changer"]
---

# Storing Device-Specific Information in the Changer's Device Extension


## <span id="ddk_storing_device_specific_information_in_the_changers_device_extensi"></span><span id="DDK_STORING_DEVICE_SPECIFIC_INFORMATION_IN_THE_CHANGERS_DEVICE_EXTENSI"></span>


A changer miniclass driver specifies the storage it requires for device-specific data in its [**ChangerAdditionalExtensionSize**](https://msdn.microsoft.com/library/windows/hardware/ff551400) routine. The changer class driver allocates the requested storage on behalf of the changer miniclass driver, then calls the miniclass driver's [**ChangerInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff551431) routine.

Whether the changer miniclass driver stores data in the device extension and what data it stores, is up to the driver designer. It typically includes SCSI inquiry data or the non-SCSI equivalent for changer devices.

The device extension might also include data that the miniclass driver uses to translate between device-specific element addresses and the zero-based element addresses passed in requests. In requests, elements are addressed by element type, starting with zero for the first element of a given type. Device-specific addresses typically do not follow this element addressing scheme, so the changer miniclass driver must translate the zero-based element addresses it receives into device-specific element addresses.

It does not matter how a miniclass driver translates element addresses as long as the addresses are translated. To optimize the process, a miniclass driver might store data that facilitates translation in the device extension. For example, at initialization, the driver could obtain device-specific element addresses from the SCSI element address assignment page or non-SCSI equivalent, map them to offsets that can be used to reconstruct the device-specific addresses, and store the offsets in the device extension. Then, when the changer miniclass driver receives a request that contains a zero-based element address, it could use the offset stored in the device extension to translate the zero-based address to a device-specific equivalent. The changer miniclass driver can use these device-specific addresses in the SRBs it sends to the system port driver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storing%20Device-Specific%20Information%20in%20the%20Changer's%20Device%20Extension%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


