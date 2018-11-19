---
title: Installing a Catalog File by using SignTool
description: Installing a Catalog File by using SignTool
ms.assetid: b3d151af-d49b-468f-a34a-04e5ab875a07
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a Catalog File by using SignTool


[**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) is not a redistributable tool and therefore cannot be included with a redistributed installation application. However, SignTool can be used on a computer that has SignTool already installed in a manner that complies with the Microsoft Software License Terms for the tool. A [catalog file](catalog-files.md) can be manually installed from a command line or installed by command script by using the following SignTool command:

```cpp
SignTool catdb /v /u CatalogFileName.cat
```

Where:

-   The **catdb** command configures SignTool to add or remove a catalog file from a catalog database. By default, SignTool adds the catalog file to the system component and driver database.

-   The **/v** option configures SignTool to operate in verbose mode.

-   The **/u** option configures SignTool to generate a unique name for the catalog file being added, if necessary, to prevent replacing an already existing catalog file that has the same name as *CatalogFileName.cat*.

-   *CatalogFileName.cat* is the name of the catalog file.

 

 





