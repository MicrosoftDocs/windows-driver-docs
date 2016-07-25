---
title: Copying INF Files
description: Copying INF Files
ms.assetid: 3ef92943-6462-4fe7-bd9b-8235083e8e16
keywords: ["INF files WDK device installations , copying", "copying INF files"]
---

# Copying INF Files


## <a href="" id="ddk-copying-infs-dg"></a>


It is sometimes necessary to copy INF files during device installation so that Windows can find them without repetitively displaying user prompts. For example, the base INF file for a multifunction device might copy the INF files for the device's individual functions so that Windows can find these INF files without prompting the user each time it installs one of the device's functions.

To copy INF files, an INF file can use the [**INF CopyINF directive**](inf-copyinf-directive.md).

Doing so will:

-   Install the appropriate catalog file, if it exists, along with the INF file.

-   Give the INF file a unique name so that it does not overwrite any other INF files, and will not be overwritten by other INF files.

-   Retain the path of the source medium from which device files are to be copied.

-   Ensure compatibility with future versions of Windows.

Installation software must never copy INF files directly into a system's *%SystemRoot%/inf* directory. Copying INF files by using techniques not described in this section will invalidate a driver's digital signature.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Copying%20INF%20Files%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




