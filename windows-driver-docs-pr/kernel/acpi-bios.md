---
title: ACPI BIOS
author: windows-driver-content
description: ACPI BIOS
ms.assetid: 787e82ed-e58c-461f-abb6-71ed6cba411c
keywords: ["ACPI BIOS WDK power management"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ACPI BIOS


## <a href="" id="ddk-acpi-bios-kg"></a>


The integrated power management features supported by Microsoft Windows operating systems are available only on computers that have an Advanced Configuration and Power Interface (ACPI) BIOS.

Windows Server 2003, Windows XP, and Windows 2000 require that an ACPI BIOS be dated January 1, 1999 or later. However, if one of these Windows versions determines that such a BIOS is known to exhibit ACPI problems, the loader disables ACPI and instead uses Advanced Power Management (APM). Beginning with Windows Vista, the operating system supports only a computer with an ACPI-compliant BIOS that is dated January 1, 1999 or later.

Device Manager shows whether an individual computer supports ACPI. Check the driver information for the **Computer** device category.

For more information about ACPI, see the Advanced Configuration and Power Interface Specification at the [ACPI website](http://www.acpi.info).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20ACPI%20BIOS%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


