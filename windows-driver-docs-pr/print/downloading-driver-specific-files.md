---
title: Downloading Driver-Specific Files
description: Downloading Driver-Specific Files
ms.assetid: 7ac5057a-32fb-4c3a-a5c3-3fc1217dbdc6
keywords: ["Point and Print WDK , driver-specific files", "driver-specific files WDK printer", "downloading driver-specific printer files"]
---

# Downloading Driver-Specific Files


## <a href="" id="ddk-downloading-driver-specific-files-gg"></a>


A client system creates a connection to a print server by calling **AddPrinterConnection**. This call results in a call to **GetPrinterDriver** on the server, which reads the [printer's INF file](printer-inf-files.md) in order to fill in a DRIVER\_INFO\_3 structure, followed by a call to **AddPrinterDriver**, with the DRIVER\_INFO\_3 structure as input. The **AddPrinterDriver** function causes all files listed in the DRIVER\_INFO\_3 structure to be sent to the client.

These functions and the DRIVER\_INFO\_3 structure are described in the Microsoft Windows SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Downloading%20Driver-Specific%20Files%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




