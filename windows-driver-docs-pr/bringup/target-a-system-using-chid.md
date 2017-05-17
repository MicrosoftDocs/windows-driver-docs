---
title: Target a system using CHID targeting
description: Target a system using CHID targeting
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 05/15/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---


# Target a system using CHID targeting


Computer Hardware IDs (CHID)s are created by the OEM/ODM running either a Windows Developer Kit(WDK) tool (ComputerHardwareIDs.exe) or the Audit tool available to OEMs through the [Microsoft OEM download site](https://www.microsoftoem.com/Login.aspx) (login required).

The CHIDs are Computer Hardware IDs and Windows makes use of these IDs in varying levels of specificity for targeting purposes. Once the correct driver is delivered to the system, then normal PNP ranking takes over as described in [How Windows Ranks Drivers](https://msdn.microsoft.com/en-us/windows/hardware/drivers/install/how-setup-ranks-drivers--windows-vista-and-later-), and the vendor can build a strategy around this that makes sense for their product line.

The OEM/ODM needs to ensure all appropriate SMBIOS fields are populated with data, based on the information provided in the [SMBIOS](smbios.md) guidance and following the [DMTF SMBIOS specification](http://www.dmtf.org/standards/smbios) to ensure CHIDs are individual and unique.

Microsoft is now requiring that a Firmware Update Package include Computer Hardware ID (CHID) Targeting in addition to the unique ID listed for **system** in the EFI System Resource Table (ESRT). The [Download Driver Publishing Workflow for Windows 10](http://download.microsoft.com/download/B/A/8/BA89DCE0-DB25-4425-9EFF-1037E0BA06F9/windows10_driver_publishing_workflow.docx) document contains a detailed description of CHIDs used in distribution targeting and installation targeting.

## Related resources

[Manage Driver Distribution by submissions](https://msdn.microsoft.com/library/windows/hardware/mt181351)                                                                    

[Specifying Hardware IDs for a Computer](https://msdn.microsoft.com/en-us/library/windows/hardware/ff552325)                                                       

[Download Driver Publishing Workflow for Windows 10](http://download.microsoft.com/download/B/A/8/BA89DCE0-DB25-4425-9EFF-1037E0BA06F9/windows10_driver_publishing_workflow.docx) 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


