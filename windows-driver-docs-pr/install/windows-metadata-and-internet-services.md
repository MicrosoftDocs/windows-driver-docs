---
title: Windows Metadata and Internet Services
description: Windows Metadata and Internet Services
ms.assetid: 9e814be5-e22a-48d5-b46b-d22baa89e229
keywords: ["WMIS", "Metadata Information Server WDK", "metadata server WDK"]
---

# Windows Metadata and Internet Services


The Windows Metadata and Internet Services (WMIS) manages device metadata packages that OEMs submit to the [Windows Quality Online Services (Winqual)](http://go.microsoft.com/fwlink/p/?linkid=62651) website over the Internet. By using the Winqual site, you can certify hardware devices and software applications for Windows.

When the OEM submits a device metadata package, Winqual completes the following process:

1.  Validates the XML documents that are contained within a device metadata package, and digitally signs those packages that pass validation.

2.  Makes the package available so that WMIS can distribute and install on remote computers.

In Windows 7 and later versions of Windows, the operating system uses WMIS to discover, index, and match device metadata packages for specific devices that are connected to the computer. For more information about this process, see [Installing Device Metadata Packages from WMIS](installing-device-metadata-packages-from-wmis.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Windows%20Metadata%20and%20Internet%20Services%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




