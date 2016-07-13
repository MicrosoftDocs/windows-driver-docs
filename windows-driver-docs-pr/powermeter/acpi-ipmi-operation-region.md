---
title: ACPI IPMI Operation Region
description: ACPI IPMI Operation Region
ms.assetid: fb953ee1-2628-4cd1-a2d3-a725cf59cc9f
keywords: ["Power Metering and Budgeting WDK , ACPI IPMI operation region", "ACPI IPMI operation region WDK Power Meter", "IPMI WDK Power Meter"]
---

# ACPI IPMI Operation Region


Many systems communicate with the service processor or baseboard management controller (BMC) by using the Intelligent Platform Management Interface (IPMI).

Starting with Windows 7 and Windows Server 2008 R2, the operating system provides a standardized ACPI IPMI Operation Region for IPMI access to service processors or BMCs. This enables devices to access IPMI data through ACPI Machine Language (AML), and enables a hardware platform to issue IPMI requests by using its ACPI firmware.

The operating system provides an IPMI driver that supports the ACPI IPMI Operation Region. The driver services IPMI requests, which must be made by using the Keyboard Controller Style (KCS) protocol.

For more information, refer to the [IPMI version 2.0 Specification](http://go.microsoft.com/fwlink/p/?linkid=69485).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[powermeter\powermeter]:%20ACPI%20IPMI%20Operation%20Region%20%20RELEASE:%20%286/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


