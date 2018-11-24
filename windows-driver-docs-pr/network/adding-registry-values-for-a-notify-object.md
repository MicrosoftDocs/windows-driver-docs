---
title: Adding Registry Values for a Notify Object
description: Adding Registry Values for a Notify Object
ms.assetid: 8872a9b9-b7c5-4c10-b5d4-4fe880fc436f
keywords:
- add-registry-sections WDK networking , notify object registry values
- notify objects WDK networking , registry values
- network notify objects WDK , registry values
- registry WDK notify objects
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding Registry Values for a Notify Object





A **NetTrans**, **NetClient**, or **NetService** component can have a notify object that performs one or more of the following actions:

-   Displays a user interface for the component

-   Notifies the component of binding events so that the component can exercise some control over the binding process

-   Conditionally installs or removes software components

**Note**  **NetClient** components are deprecated in Windows 8.1, Windows Server 2012 R2, and later.

 

For more information about notify objects, see [Notify Objects for Network Components](notify-objects-for-network-components.md).

**Note**  **Net** components (adapters) do not support notify objects; therefore, these components should use a co-installer.

 

For more information about co-installers, see [Writing a Co-installer](https://msdn.microsoft.com/library/windows/hardware/ff554011).

If a component has a notify object, the INF file for that component must add (through an *add-registry-section*) the following values to the component's **Ndi** key:

<a href="" id="clsid"></a>**ClsID**  
A REG\_SZ value that specifies the GUID (globally unique identifier) for the notify object. Obtain this GUID by running the uuidgen.exe utility. For more information about this utility, see the Microsoft Windows SDK.

<a href="" id="componentdll"></a>**ComponentDll**  
A REG\_SZ value that specifies the path to the notify object DLL. The **ComponentDll** must specify the complete path to the DLL if the DLL is not in the Windows\\System32 directory.

The following is an example of an *add-registry-section* that adds **ClsID** and **ComponentDll** values to the **Ndi** key:

```INF
[MS_Protocol.ndi.reg]
HKR, Ndi, ClsID, 0, "GUID"
HKR, Ndi, ComponentDll, 0, "notifyobject.dll"
```

The *DDInstall* section for a component that has a notify object must also contain a **CopyFiles** directive which references a *file-list-section* that copies the notify object DLL to the destination directory specified by the **DestinationDirs** section. For more information about the **CopyFiles** directive and **DestinationDirs** sections, see [INF File Sections and Directives](https://msdn.microsoft.com/library/windows/hardware/ff547433).

 

 





