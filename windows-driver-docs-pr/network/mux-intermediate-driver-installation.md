---
title: MUX Intermediate Driver Installation
description: MUX Intermediate Driver Installation
ms.assetid: 9d0c6d6f-c12f-4921-b08a-b23b7d96ccd9
keywords:
- MUX intermediate drivers WDK
- NDIS MUX intermediate drivers WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MUX Intermediate Driver Installation





This topic provides an overview of MUX intermediate driver installation issues. For additional information about the structure of intermediate driver INF files, see [Installation Requirements for Network MUX Intermediate Drivers](installation-requirements-for-network-mux-intermediate-drivers.md).

A MUX intermediate driver requires two INF files. The protocol INF file defines the installation parameters for the protocol lower edge. The miniport INF file defines the installation parameters for the virtual miniport upper edge. Set the **Class** INF file entry to **Net** in the virtual miniport INF file and **NetTrans** in the protocol INF file. The following code example shows a **Class** entry for the protocol INF file.

```INF
Class = NetTrans
```

The *DDInstall* section in a MUX intermediate driver INF file must have a **Characteristics** entry. Define the **Characteristics** entry in your protocol INF file as demonstrated in the following code example.

```INF
Characteristics = 0x80
```

NCF\_HAS\_UI (0x80) is required to enable custom property pages, which in this case is the notify object

Define the **Characteristics** entry in your miniport INF file as demonstrated in the following code example.

```INF
Characteristics = 0x21
```

The **Characteristics** value 0x21 indicates the NCF\_VIRTUAL (0x1) and NCF\_NOT\_USER\_REMOVABLE (0x20) flags are set. NCF\_VIRTUAL specifies that the device is a virtual adapter. NCF\_NOT\_USER\_REMOVABLE is optional and specifies that the user cannot remove the intermediate driver. If you want to hide the virtual miniport from the user (you should not do this if your user must install devices manually) you can define the NCF\_HIDDEN (0x8) flag. The NCF\_*Xxx* flags are defined in Netcfgx.h. For more information about the **Characteristics** entry and NCF\_*Xxx* flags, see [DDInstall Section](ddinstall-section-in-a-network-inf-file.md).

The *DDInstall* section of the protocol INF file for a MUX intermediate driver must include an **Addreg** directive for an **Ndi** key. For more information, see [Adding Service-Related Values to the Ndi Key](adding-service-related-values-to-the-ndi-key.md) and [DDInstall.Services Section](ddinstall-services-section-in-a-network-inf-file.md).

In addition to the INF files, you must also provide a notify object with a MUX Intermediate driver. The notify object is responsible for installation of virtual miniports. Reference the notify object with the **ComponentDll** entry in the protocol INF as follows:

```INF
HKR, Ndi,            ComponentDll,   , mux.dll
```

The user installs the protocol INF file which defines configuration parameters, copies installation files and also installs the notify object DLL. The user adds virtual miniports through the user interface provided by the notify object. The miniport INF file should define the **ExcludeFromSelect** entry to prevent the user from installing the miniport INF file instead of the protocol INF file.

The protocol name that the driver registers must match the service name.

```INF
HKR, Ndi, Service, 0, MUXP
```

The **UpperRange** and **LowerRange** INF file entries determine the bindings for a MUX intermediate driver. The protocol INF file must define the protocol edge bindings, as the following code example shows.

```INF
HKR, Ndi\Interfaces, UpperRange,    0,          "noupper"
HKR, Ndi\Interfaces, LowerRange,    0,          "ndis5"
```

The miniport INF file must define the upper edge bindings, as the following code example shows.

```INF
HKR, Ndi\Interfaces,    UpperRange, 0,  "ndis5"
HKR, Ndi\Interfaces,    LowerRange, 0,  "nolower"
```

You should replace "ndis5" in the preceding code examples with the protocol bindings required by your driver. For more information about intermediate driver bindings and the **UpperRange**/**LowerRange** entries, see [Intermediate Driver UpperRange And LowerRange INF File Entries](intermediate-driver-upperrange-and-lowerrange-inf-file-entries.md).

 

 





