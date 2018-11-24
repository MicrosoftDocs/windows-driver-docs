---
title: Handling WMI SRBs in Storage Miniport Drivers
description: Handling WMI SRBs in Storage Miniport Drivers
ms.assetid: 92b78611-7e6f-4d77-9133-635df96584f0
keywords:
- storage miniport drivers WDK , WMI SRBs
- miniport drivers WDK storage , WMI SRBs
- WMI SRBs WDK storage , about WMI SRBs
- WMI SRBs WDK storage
- SRB WMI support WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling WMI SRBs in Storage Miniport Drivers


## <span id="ddk_handling_wmi_srbs_in_storage_miniport_drivers_kg"></span><span id="DDK_HANDLING_WMI_SRBS_IN_STORAGE_MINIPORT_DRIVERS_KG"></span>


WMI interfaces that report information about a host bus adapter (HBA), or that allow WMI clients to interact with the HBA's storage miniport driver, usually require the miniport driver to function as a WMI provider. After a storage miniport driver registers as a WMI provider, it must be prepared to handle a special kind of SCSI request block (SRB) called a Windows Management Instrumentation (WMI) SCSI request block ([**SCSI\_WMI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565397)).

To prepare your storage miniport driver to handle WMI SRBs, complete the following steps:

1.  Design and compile a Managed Object Format (MOF) file that describes those parts of the WMI schema that are not defined by system-supplied MOF files.

    For a description of MOF syntax, see [MOF Syntax for WMI Data and Event Blocks](https://msdn.microsoft.com/library/windows/hardware/ff556400).

2.  Implement miniport driver callback routines.

    The SCSI Port WMI library simplifies the processing of WMI SRBs for miniport drivers. To use the SCSI Port WMI library, implement the *HwScsiWmiXxx* callback routines described in [SCSI Miniport Driver Routines](https://msdn.microsoft.com/library/windows/hardware/ff565312).

3.  Add required code to the miniport driver's [**DriverEntry of SCSI Miniport Driver**](https://msdn.microsoft.com/library/windows/hardware/ff552654) routine.

4.  Add required code to the miniport driver's [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300) routine.

5.  Add required code to the miniport driver's [**HwScsiStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557323) routine.

For information about implementing the previous steps, see the following topics included in this section:

[How the Port Driver Processes WMI Requests](how-the-port-driver-processes-wmi-requests.md)

[Using the SCSI Port WMI Library](using-the-scsi-port-wmi-library.md)

[Designing WMI Miniport Driver Callback Routines](designing-wmi-miniport-driver-callback-routines.md)

[Modifying Storage Miniport Driver Routines to Support WMI SRBs](modifying-storage-miniport-driver-routines-to-support-wmi-srbs.md)

 

 




