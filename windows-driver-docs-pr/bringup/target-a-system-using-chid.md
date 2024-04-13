---
title: Target a System Using CHID Targeting
description: Provides information about how to target a system using CHID targeting.
ms.date: 03/23/2023
---

# Target a system using CHID targeting

Computer Hardware IDs (CHID)s are created by the OEM/ODM running either a Windows Developer Kit(WDK) tool (ComputerHardwareIDs.exe) or the Audit tool available to OEMs through the [Microsoft OEM download site](https://www.microsoftoem.com) (login required).

The CHIDs are Computer Hardware IDs and Windows makes use of these IDs in varying levels of specificity for targeting purposes. Once the correct driver is delivered to the system, then normal PNP ranking takes over as described in [How Windows Ranks Drivers](../install/how-setup-ranks-drivers--windows-vista-and-later-.md), and the vendor can build a strategy around this that makes sense for their product line.

The OEM/ODM needs to ensure all appropriate SMBIOS fields are populated with data, based on the information provided in the [SMBIOS](smbios.md) guidance and following the [DMTF SMBIOS specification](https://www.dmtf.org/standards/smbios) to ensure CHIDs are individual and unique.

Microsoft is now requiring that a Firmware Update Package include Computer Hardware ID (CHID) Targeting in addition to the unique ID listed for **system** in the EFI System Resource Table (ESRT). The [Download Driver Publishing Workflow for Windows 10](https://download.microsoft.com/download/B/A/8/BA89DCE0-DB25-4425-9EFF-1037E0BA06F9/windows10_driver_publishing_workflow.docx) document contains a detailed description of CHIDs used in distribution targeting and installation targeting.

## Related resources

[Partner Center](../dashboard/index.yml)

[Specifying Hardware IDs for a Computer](../install/specifying-hardware-ids-for-a-computer.md)

[Download Driver Publishing Workflow for Windows 10](https://download.microsoft.com/download/B/A/8/BA89DCE0-DB25-4425-9EFF-1037E0BA06F9/windows10_driver_publishing_workflow.docx)
