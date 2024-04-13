---
title: Use the HwContext Pointer to HwScsiFindAdapter Correctly
description: Use the HwContext Pointer to HwScsiFindAdapter Correctly
keywords:
- SCSI miniport drivers WDK storage , PnP
- PnP WDK SCSI
- Plug and Play WDK SCSI
- converting SCSI miniport drivers
- HwContext pointer
- HwScsiFindAdapter
ms.date: 04/20/2017
---

# Use the HwContext Pointer to HwScsiFindAdapter Correctly


## <span id="ddk_use_the_hwcontext_pointer_to_hwscsifindadapter_correctly_kg"></span><span id="DDK_USE_THE_HWCONTEXT_POINTER_TO_HWSCSIFINDADAPTER_CORRECTLY_KG"></span>


If a miniport driver's [*HwScsiFindAdapter*](/previous-versions/windows/hardware/drivers/ff557300(v=vs.85)) receives nonzero access range values from the port driver, it must not use the *HwContext* pointer. Although this restriction also applied to version 4.0 miniport drivers, nothing prevented such a miniport driver from using this pointer.

If the miniport driver can be initialized as a Plug and Play driver in Microsoft Windows 2000 and later, it must not use the *HwContext* pointer because the SCSI port driver passes in a **NULL** pointer as the *HwContext* argument.

How an existing miniport driver must be modified depends on how it currently uses *HwContext*. For example, if the miniport driver uses *HwContext* to maintain a count of HBAs (for example, to use in **DebugPrint** statements) an alternative might be to use the *HwDeviceExtension* pointer instead. *HwDeviceExtension* provides a unique number that is related to the particular HBA originating the **DebugPrint** message. (Using a global variable to store the HBA count is a bad practice, because miniport drivers should not use global variables to maintain state information.)

As another example, if the 4.0 version of the miniport driver uses *HwContext* to communicate information about the type of device being initialized (such as information about the capabilities supported by a particular model of PCI HBA), the 5.0 version of the miniport driver might use [**ScsiPortGetBusData**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportgetbusdata) to get an identifier for the HBA, then use that identifier to search through a list of such parameter blocks to find the correct information.

Another possible miniport driver modification might be to provide this information in a registry string passed in the *ArgumentString* parameter. The registry string could be set by the miniport driver's INF file during initialization to information that pertains to the model of the card detected. This provides more flexibility than hardcoding the parameters in the miniport driver because such a miniport driver could handle new models of cards using an updated INF file instead of requiring the miniport driver to be recompiled.

 

