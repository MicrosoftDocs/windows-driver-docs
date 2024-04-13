---
title: ACPI IPMI Operation Region
description: ACPI IPMI Operation Region
keywords:
- Power Metering and Budgeting WDK , ACPI IPMI operation region
- ACPI IPMI operation region WDK Power Meter
- IPMI WDK Power Meter
ms.date: 04/20/2017
---

# ACPI IPMI Operation Region

Many systems communicate with the service processor or baseboard management controller (BMC) by using the Intelligent Platform Management Interface (IPMI).

Starting with Windows 7 and Windows Server 2008 R2, the operating system provides a standardized ACPI IPMI Operation Region for IPMI access to service processors or BMCs. This enables devices to access IPMI data through ACPI Machine Language (AML), and enables a hardware platform to issue IPMI requests by using its ACPI firmware.

The operating system provides an IPMI driver that supports the ACPI IPMI Operation Region. The driver services IPMI requests, which must be made by using the Keyboard Controller Style (KCS) protocol.

For more information, refer to the [IPMI version 2.0 Specification](https://www.intel.com/content/www/us/en/products/docs/servers/ipmi/ipmi-second-gen-interface-spec-v2-rev1-1.html?wapkw=IPMI%20version%202.0%20Specification) on the Intel website.
