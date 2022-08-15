---
title: XPSDrv Driver Requirements
description: The XPSDrv configuration module must meet requirements described in this topic.
keywords:
- Version 3 XPS drivers WDK XPSDrv , requirements
ms.date: 08/13/2021
---

# XPSDrv Driver Requirements

For in-box and the [Windows Hardware Certification Kit (HCK) (EXE download)](https://download.microsoft.com/download/1/8/B/18BC088A-537D-4386-9334-687747A602E6/hlk/hlksetup.exe), the XPSDrv configuration module must meet the following requirements:

- The XPSDrv printer driver must implement a Version 3 print driver configuration module.

- The configuration module must support all PrintTicket and PrintCapabilities functionality. The Windows Vista version of the Unidrv and Pscript5 printer drivers provide this support automatically. For more information about how to add this support to monolithic, GDI-based version 3 printer drivers, see [Adding Print Ticket Support to Monolithic Print Drivers](adding-print-ticket-support-to-monolithic-print-drivers.md).

For the complete list of configuration module requirements, see [Windows Hardware Certification Kit (HCK) (EXE download)](https://download.microsoft.com/download/1/8/B/18BC088A-537D-4386-9334-687747A602E6/hlk/hlksetup.exe).
