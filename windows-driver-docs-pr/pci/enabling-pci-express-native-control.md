---
title: Enabling PCI Express Native Control in Windows
description: PCI Express features that can be controlled by the PCI Express Native Control feature in Windows
ms:assetid: 0E3A4408-CBF7-494F-9F25-7C78E04526B4
keywords: ACPI, ACPI \_OSC method
ms.date: 06/01/2017
ms.localizationpriority: medium
---

# Enabling PCI Express Native Control in Windows

The Advanced Configuration and Power Interface (ACPI) Operating System Capabilities (\_OSC) method is used to communicate which of the features or capabilities that are available in the platform can be controlled by the operating system. This method is defined in the ACPI Specification, Revision 4.0.

The following table lists the PCI Express features that can be controlled by the PCI Express Native Control feature in Windows Vista, Windows Server 2008 and later versions of Windows. These features are defined in the PCI Express Base Specification and are controlled by the operating system via the ACPI \_OSC method.

| PCI Express Feature                        | PCI Express Native Control |
| ------------------------------------------ | -------------------------- |
| PCI Express Native Hot Plug                | Mandatory                  |
| PCI Express Native Power Management Events | Mandatory                  |
| PCI Express Advanced Error Reporting       | Optional                   |
| PCI Express Capability Structure Control   | Mandatory                  |

If the \_OSC method grants control of these features to the operating system, Windows enables the PCI Express Native Control feature. The PCI Express Native Control feature in Windows is not dependent on PCI Express Advanced Error Reporting (AER), and therefore platform support for PCI Express AER is optional.

If the platform does not implement the \_OSC method, or if the \_OSC method communicates that operating system control of any of the PCI Express features listed in the table is not available and thus it does not grant control of the mandatory features above to the operating system, then Windows will not enable any of the advanced PCI Express features through PCI Express Native Control.

For more information, see Section 6.2.10 in the ACPI Specification, Revision 4.0, and Section 4.5 in the PCI Firmware Specification.

Those specifications are available on the ACPI and PCI SIG Web sites:

  - [ACPI Website](https://www.uefi.org/specifications)
  - [PCI SIG Website](http://www.pcisig.org/)

## See Also
[Device Specific Data (_DSD) for PCIe Root Ports](dsd-for-pcie-root-ports.md)
