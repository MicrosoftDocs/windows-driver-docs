---
title: Installing an Intermediate Driver
description: Installing an Intermediate Driver
ms.assetid: 75e299d0-b708-411d-9d37-609c8bf621f8
keywords:
- intermediate drivers WDK networking , installation
- NDIS intermediate drivers WDK , installation
- installing NDIS intermediate drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing an Intermediate Driver





Intermediate drivers require two INF files. One of the INF files defines the installation parameters for the protocol lower edge. The other INF file defines the installation parameters for the virtual miniport upper edge.

The protocol INF file is the primary INF file. After the protocol lower edge is installed, the virtual miniport upper edge is installed, based on references to the miniport driver INF file that are defined in the protocol INF file.

On Windows Vista, you can use a notify object or a custom setup application to copy the miniport driver INF file to the system INF directory. For Windows Vista and later operating system versions, you should use the [**INF CopyINF directive**](https://msdn.microsoft.com/library/windows/hardware/ff547317) in the protocol INF file to copy the miniport driver INF file. For more information about the notify object and copying INF files, see [Intermediate Driver Notify Object](intermediate-driver-notify-object.md).

The system-supplied device setup class for the protocol lower edge is **NetService** for filter intermediate drivers and **NetTrans** for MUX intermediate drivers. The driver class for the virtual miniport is always **Net**.

In addition to the INF files, you must also provide a notify object with a MUX intermediate driver. The notify object is optional for filter intermediate drivers.

The virtual miniport device is always removed from the user interface by using the **ExcludeFromSelect** directive. Therefore, the user only sees the protocol and installs the protocol from the protocol INF file.

**Note**  The **ExcludeFromSelect** directive does not remove the virtual device from the **Connections** dialog box. However, the NCF\_HIDDEN flag in the miniport driver INF file *DDInstall* section's **Characteristics** entry prevents the virtual miniport from being displayed in any part of the user interface, including the **Connections** dialog box.

 

This section provides information about intermediate INF files and notify objects. This information is described in the following topics:

[Intermediate Driver UpperRange And LowerRange INF File Entries](intermediate-driver-upperrange-and-lowerrange-inf-file-entries.md)

[MUX Intermediate Driver Installation](mux-intermediate-driver-installation.md)

[Intermediate Driver Notify Object](intermediate-driver-notify-object.md)

 

 





