---
title: Intermediate Driver Notify Object
description: Intermediate Driver Notify Object
ms.assetid: 756e02ff-5e30-4511-af4c-b7be9830898c
keywords:
- notify objects WDK networking , intermediate drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Intermediate Driver Notify Object





An *intermediate driver notify object* is an extension of the network class installer. The network class installer loads and initializes your notify object and sends it notifications of events (such as virtual miniport removal notifications) related to your driver. If you want an overview of notify objects in general or more information about notify objects, see [Notify Objects for Network Components](notify-objects-for-network-components.md).

To include the notify object in your installation, you must reference it in your intermediate driver protocol INF. Filter intermediate drivers do not require a notify object. You can include a notify object with your filter intermediate driver if you would like to provide more flexible configuration options to your user.

On Windows Vista, you can use the notify object or a custom setup application to copy the miniport INF file to the system INF directory. For either of these, you use **SetupCopyOEMInf** (described in Microsoft Windows SDK documentation) to copy the INF. For Windows Vista and later operating system versions, you should use the [**INF CopyINF directive**](https://msdn.microsoft.com/library/windows/hardware/ff547317) in the protocol INF to copy the miniport INF. For more information about copying INF files, see [Copying INFs](https://msdn.microsoft.com/library/windows/hardware/ff540117).

A MUX intermediate driver notify object must provide services to install and remove virtual miniports. This can be done automatically or by providing a user interface. It must manage the virtual miniports' device name list in the registry. The device name list defines the bindings between virtual miniports and physical devices. For example, the n-to-one MUX intermediate driver sample notify object maintains a list of virtual miniports bound to each physical device in an **UpperBindings** registry entry. The MUX sample driver reads the **UpperBindings** list and initializes a virtual miniport for each entry.

Your MUX intermediate driver should use the **UpperRange**/**LowerRange** entries to control external bindings. However, you can control external bindings from your notify object if necessary. For more information about bindings in intermediate drivers, see [Intermediate Driver UpperRange And LowerRange INF File Entries](intermediate-driver-upperrange-and-lowerrange-inf-file-entries.md)

Your notify object can optionally provide a user interface that allows the user to change or view your driver's configuration. The MUX intermediate driver sample includes an example user interface for a notify object.

 

 





