---
title: Including a PrintProvider Section
description: Including a PrintProvider Section
ms.assetid: 2cbf1b56-e603-4a21-a1d7-d51634c91456
keywords:
- INF files WDK network , PrintProvider section
- network INF files WDK , PrintProvider section
- PrintProvider section WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Including a PrintProvider Section





An INF file that installs a **NetClient** component that is a print provider must contain a **PrintProvider** section for that component.

**Note**  **NetClient** components are deprecated in Windows 8.1, Windows Server 2012 R2, and later.

 

To create a **PrintProvider** section, add the **PrintProvider** extension to the *DDInstall* section for the component, as shown in the following example:
```cpp
[DDInstall-section] ; Install section
[DDInstall-section.PrintProvider] ; PrintProvider section
```

The **PrintProvider** section must include the following entries:

<a href="" id="printprovidername"></a>**PrintProviderName**  
A nonlocalized string that specifies the name of the print provider.

<a href="" id="printproviderdll"></a>**PrintProviderDll**  
The file name of the print provider DLL.

<a href="" id="displayname"></a>**DisplayName**  
A localizable string that specifies the name of the print provider. The **DisplayName** can differ from the **PrintProviderName**.

The **PrintProviderName** and **PrintProviderDll** entries supply information that is used as input (in a PROVIDOR\_INFO\_1 structure) to the **AddPrintProvidor** function. The **AddPrintProvidor** function adds the print provider component as a print provider. For more information about the **AddPrintProvidor** function, see the Microsoft Windows SDK.

The following is an example of a **PrintProvider** section:

```cpp
[DDnstall-section.PrintProvider]
PrintProviderName = "NetWare or Compatible Network"
PrintProviderDll  = "nwprovau.dll"
DisplayName       = "%NWC_Network_Display_Name%"
```

 

 





