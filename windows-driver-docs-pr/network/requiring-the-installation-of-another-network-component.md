---
title: Requiring the Installation of Another Network Component
description: Requiring the Installation of Another Network Component
ms.assetid: 30e6db7f-46f4-414f-a485-051b007f0eb6
keywords:
- add-registry-sections WDK networking , component dependencies
- component IDs WDK networking
- component dependencies WDK networking
- dependencies WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Requiring the Installation of Another Network Component





A network component may require the installation of one or more other network components in order to function properly. A network INF file specifies each such dependency with a **RequiredAll** value. The **RequiredAll** value is added (through an *add-registry-section*) to the **Ndi** key of the network component that requires the installation of another network component.

The following example shows a **RequiredAll** entry in an *add-registry-section*:

```INF
[ndi.reg]
HKR, Ndi, RequiredAll, 0, "component id"
```

The *component ID* is the *hw-id* of the required network component. For more information, see [**INF Models Section**](https://msdn.microsoft.com/library/windows/hardware/ff547456). If a network component requires the installation of more than one other network component, use one **RequiredAll** entry for each network component that must be installed, as shown in the following example:

```INF
HKR, Ndi, RequiredAll, 0, "component1 id, component2 id"
```

**Note**  The **RequiredAll** value should only be used to install hidden network components that cannot be installed by the user. Such components should not support a user interface. Any network components specified by **RequiredAll** cannot be removed until the network component that required their installation through **RequiredAll** is itself removed.

 

For example, if the INF file for component A specifies, through **RequiredAll**, a dependency on component B, component B cannot be removed until component A is removed. **RequiredAll** should therefore install only network components that are absolutely required for the operation of another network component. For example, if an INF file for a Net component (an adapter) uses **RequiredAll** to specify that TCP/IP must be installed, the user will not be able to remove TCP/IP until that adapter is removed. Since the adapter does not require TCP/IP to operate, the INF for the adapter should not use **RequiredAll** to specify a dependency on TCP/IP.

The INF file that specifies a **RequiredAll** dependency must ensure that the INF file for the required network component is present in the inf directory. Typically, this is accomplished with a **CopyINF** directive. For more information about the **CopyINF** directive, see [**INF CopyINF Directive**](https://msdn.microsoft.com/library/windows/hardware/ff547317). For more information about copying INF files, see [Copying INFs](https://msdn.microsoft.com/library/windows/hardware/ff540117).

If the installation of a network component specified by a **RequiredAll** entry fails, the installation of the network component that requires the specified component fails as well.

 

 





