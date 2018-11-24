---
title: Specifying Filter Driver Binding Relationships
description: Specifying Filter Driver Binding Relationships
ms.assetid: 0f0b81f4-2ac1-456c-aef0-73f3bbb7ce0e
keywords:
- filter drivers WDK networking , binding relationships
- NDIS filter drivers WDK , binding relationships
- binding relationships WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Filter Driver Binding Relationships





In a network driver INF file, the **UpperRange** entry lists the possible upper bindings and the **LowerRange** entry lists the possible lower bindings. These entries can contain various system-defined values.

For filter drivers, you must set the value of the **UpperRange** and **LowerRange** entries to **noupper** and **nolower**, respectively. The following example illustrates these INF file entries for a filter driver.

```INF
HKR, Ndi\Interfaces,UpperRange,,"noupper"
HKR, Ndi\Interfaces,LowerRange,,"nolower"
```

In a filter driver, the **FilterMediaTypes** entry in the filter INF file defines the driver's bindings to other drivers. **FilterMediaTypes** specifies the media types that the filter driver services. For a list of possible media types, see the list of Microsoft-supplied **LowerRange** values in [Specifying Binding Interfaces](specifying-binding-interfaces.md). The following example illustrates a **FilterMediaTypes** entry for a filter driver.

```INF
HKR, Ndi\Interfaces, FilterMediaTypes,,"ethernet"
```

When the computer loads a filter driver, the driver is inserted into all of the existing protocol-to-adapter bindings, depending on the media types that **FilterMediaTypes** lists.

 

 





