---
title: Use the HwContext Pointer to HwScsiFindAdapter Correctly
description: Use the HwContext Pointer to HwScsiFindAdapter Correctly
ms.assetid: 9f287989-423b-4084-bf18-8df8676f7123
keywords: ["SCSI miniport drivers WDK storage , PnP", "PnP WDK SCSI", "Plug and Play WDK SCSI", "converting SCSI miniport drivers", "HwContext pointer", "HwScsiFindAdapter"]
---

# Use the HwContext Pointer to HwScsiFindAdapter Correctly


## <span id="ddk_use_the_hwcontext_pointer_to_hwscsifindadapter_correctly_kg"></span><span id="DDK_USE_THE_HWCONTEXT_POINTER_TO_HWSCSIFINDADAPTER_CORRECTLY_KG"></span>


If a miniport driver's [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300) receives nonzero access range values from the port driver, it must not use the *HwContext* pointer. Although this restriction also applied to version 4.0 miniport drivers, nothing prevented such a miniport driver from using this pointer.

If the miniport driver can be initialized as a Plug and Play driver in Microsoft Windows 2000 and later, it must not use the *HwContext* pointer because the SCSI port driver passes in a **NULL** pointer as the *HwContext* argument.

How an existing miniport driver must be modified depends on how it currently uses *HwContext*. For example, if the miniport driver uses *HwContext* to maintain a count of HBAs (for example, to use in **DebugPrint** statements) an alternative might be to use the *HwDeviceExtension* pointer instead. *HwDeviceExtension* provides a unique number that is related to the particular HBA originating the **DebugPrint** message. (Using a global variable to store the HBA count is a bad practice, because miniport drivers should not use global variables to maintain state information.)

As another example, if the 4.0 version of the miniport driver uses *HwContext* to communicate information about the type of device being initialized (such as information about the capabilities supported by a particular model of PCI HBA), the 5.0 version of the miniport driver might use [**ScsiPortGetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff564624) to get an identifier for the HBA, then use that identifier to search through a list of such parameter blocks to find the correct information.

Another possible miniport driver modification might be to provide this information in a registry string passed in the *ArgumentString* parameter. The registry string could be set by the miniport driver's INF file during initialization to information that pertains to the model of the card detected. This provides more flexibility than hardcoding the parameters in the miniport driver because such a miniport driver could handle new models of cards using an updated INF file instead of requiring the miniport driver to be recompiled.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Use%20the%20HwContext%20Pointer%20to%20HwScsiFindAdapter%20Correctly%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




