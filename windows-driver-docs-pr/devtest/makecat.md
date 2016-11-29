---
title: MakeCat
description: MakeCat
ms.assetid: 348c5069-0360-4ff9-897e-9a8832ac196c
---

# MakeCat


MakeCat (Makecat.exe) is a command-line [CryptoAPI](http://go.microsoft.com/fwlink/p/?linkid=136391) tool that creates a [catalog file](https://msdn.microsoft.com/library/windows/hardware/ff537872) for a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840).

For more information about the MakeCat tool and its command-line arguments, see the [Using MakeCat](http://go.microsoft.com/fwlink/p/?linkid=70086) website.

For more information about how to use the MakeCat tool, see [Creating a Catalog File for Release-Signing a Driver Package](https://msdn.microsoft.com/library/windows/hardware/ff540172).

**Note**   You must use the MakeCat tool only to create catalog files for driver packages that are not installed by using an INF file. If the driver package is installed by using an INF file, use the [**Inf2Cat**](inf2cat.md) tool to create the catalog file. Inf2Cat automatically includes all the files in the driver package that are referenced within the package's INF file. For more information about how to use the Inf2Cat tool, see [Using Inf2Cat to Create a Catalog File](https://msdn.microsoft.com/library/windows/hardware/ff553618).

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20MakeCat%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




