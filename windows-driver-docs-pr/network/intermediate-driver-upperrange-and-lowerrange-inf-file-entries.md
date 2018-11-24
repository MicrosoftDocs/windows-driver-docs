---
title: Intermediate Driver UpperRange And LowerRange INF File Entries
description: Intermediate Driver UpperRange And LowerRange INF File Entries
ms.assetid: 12a8561c-d410-45d0-8e96-898af6343f89
keywords:
- INF files WDK network , intermediate drivers
- UpperRange INF file entries
- LowerRange INF file entries
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Intermediate Driver UpperRange And LowerRange INF File Entries





This topic describes how to use the **UpperRange** and **LowerRange** INF file entries to define NDIS intermediate driver binding relationships.

In a network driver INF file, the **UpperRange** entry lists the possible upper bindings and the **LowerRange** entry lists the possible lower bindings. There are various system-defined values for these lists.

For filter intermediate drivers, you must set the value of the **UpperRange** and **LowerRange** entries to **noupper** and **nolower**, respectively. You should define these entries only in the protocol INF file; they are not required in the miniport driver INF file. The following code example illustrates these entries for a filter intermediate driver.

```INF
HKR, Ndi\Interfaces, UpperRange, , noupper
HKR, Ndi\Interfaces, LowerRange, , nolower
```

In a filter intermediate driver, the **FilterMediaTypes** entry in the protocol INF file defines the driver's bindings to other drivers. **FilterMediaTypes** specifies the media types serviced by the filter intermediate driver. For a list of possible media types, see the list of Microsoft-supplied **LowerRange** values in [Specifying Binding Interfaces](specifying-binding-interfaces.md). The following code example illustrates this entry for a filter intermediate driver.

```INF
HKR, Ndi\Interfaces, FilterMediaTypes, , "ethernet, tokenring, fddi, wan"
```

When a filter intermediate driver is initialized, it inserts itself into all existing protocol-to-miniport bindings, as appropriate to the media types listed in **FilterMediaTypes**.

For MUX intermediate drivers, you should always set **UpperRange** in the protocol INF file to **noupper**. Set **LowerRange** to a list of values taken from those values allowed for **LowerRange,** as specified in [Specifying Binding Interfaces](specifying-binding-interfaces.md). The following code example illustrates these entries for a MUX intermediate driver's lower edge.

```INF
HKR, Ndi\Interfaces, UpperRange, 0, "noupper"
HKR, Ndi\Interfaces, LowerRange, 0, "ndis5"
```

For MUX intermediate drivers, you should always set **LowerRange** in the miniport driver INF file to **nolower**. Set the **UpperRange** to a list of values taken from those values allowed for the **UpperRange,** as specified in [Specifying Binding Interfaces](specifying-binding-interfaces.md). The following code example illustrates these entries for a MUX intermediate driver virtual miniport.

```INF
HKR, Ndi\Interfaces, UpperRange, 0, "ndis5"
HKR, Ndi\Interfaces, LowerRange, 0, "nolower"
```

 

 





