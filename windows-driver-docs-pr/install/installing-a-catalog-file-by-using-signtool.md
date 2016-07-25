---
title: Installing a Catalog File by using SignTool
description: Installing a Catalog File by using SignTool
ms.assetid: b3d151af-d49b-468f-a34a-04e5ab875a07
---

# Installing a Catalog File by using SignTool


[**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) is not a redistributable tool and therefore cannot be included with a redistributed installation application. However, SignTool can be used on a computer that has SignTool already installed in a manner that complies with the Microsoft Software License Terms for the tool. A [catalog file](catalog-files.md) can be manually installed from a command line or installed by command script by using the following SignTool command:

```
SignTool catdb /v /u CatalogFileName.cat
```

Where:

-   The **catdb** command configures SignTool to add or remove a catalog file from a catalog database. By default, SignTool adds the catalog file to the system component and driver database.

-   The **/v** option configures SignTool to operate in verbose mode.

-   The **/u** option configures SignTool to generate a unique name for the catalog file being added, if necessary, to prevent replacing an already existing catalog file that has the same name as *CatalogFileName.cat*.

-   *CatalogFileName.cat* is the name of the catalog file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20a%20Catalog%20File%20by%20using%20SignTool%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




