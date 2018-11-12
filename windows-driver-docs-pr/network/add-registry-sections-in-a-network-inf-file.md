---
title: Add-registry-sections in a Network INF File
description: Add-registry-sections in a Network INF File
ms.assetid: 43c39389-5d01-49e9-a792-e853136068b4
keywords:
- INF files WDK network , add-registry-sections
- network INF files WDK , add-registry-sections
- add-registry-sections WDK networking
- add-registry-sections WDK networking , about add-registry-sections
- keys WDK network INF files
- Ndi key WDK networking
- values WDK network INF files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Add-registry-sections in a Network INF File





An INF file contains one or more *add-registry-sections* for each component that it installs. An *add-registry-section* adds keys and values to the registry. The **DDInstall** section of an INF file contains an **AddReg** directive that references one or more *add-registry-sections*. For more information about the *add-registry-section* and the **AddReg** directive, see [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320).

### Adding Keys and Values to Instance Keys

One or more *add-registry-sections* can add keys and values to the instance key for a component to accomplish any of the following:

-   Set static parameters for a component -- that is, configuration parameters that cannot be modified through a user interface. For more information, see [Setting Static Parameters](setting-static-parameters.md).

-   Specify the number of endpoints (also known as channels, circuits or bearer channels) for a WAN adapter. For more information, see [Specifying WAN Endpoints for a WAN Adapter](specifying-wan-endpoints-for-a-wan-adapter.md).

-   Specify keys and values for an ISDN adapter. For more information, see [Specifying ISDN Keys and Values for an ISDN Adapter](specifying-isdn-keys-and-values-for-an-isdn-adapter.md).

-   Require the installation of another network component. For more information, see [Requiring the Installation of Another Network Component](requiring-the-installation-of-another-network-component.md).

-   Specify values that support a custom properties sheet for a network adapter. For more information, see [Specifying Custom Property Pages for Network Adapters](specifying-custom-property-pages-for-network-adapters.md).

### Adding Keys and Values to a NetClient Component

An *add-registry-section* in an INF file for a **NetClient** component must add a **NetworkProvider** key to the *service* key for that component. The **NetworkProvider** key has two values: a **Name** that specifies the name of the network provider, and a **ProviderPath** that specifies the full path to the network provider DLL. For more information, see [Specifying the Name and Provider Path for a NetClient Component](specifying-the-name-and-provider-path-for-a-netclient-component.md).

**Note**  **NetClient** components are deprecated in Windows 8.1, Windows Server 2012 R2, and later.

 

### <a href="" id="ddk-creating-the-ndi-key-ng"></a>Creating the Ndi Key

Each network INF file must contain at least one *add-registry-section* that adds an **Ndi** key for the component installed by the file. The **Ndi** key is a network-specific key that is added to the instance key for the component. The keys and values that are added to the **Ndi** key vary according to the type of network component being installed and its capabilities. The **Ndi** key specifies the following:

-   **HelpText** value for a **NetTrans**, **NetClient**, or **NetService** component. For more information, see [Adding a HelpText Value](adding-a-helptext-value.md).

-   Values for a notify object. For more information, see [Adding Registry Values for a Notify Object](adding-registry-values-for-a-notify-object.md).

-   Service-related values. For more information, see [Adding Service-Related Values to the Ndi Key](adding-service-related-values-to-the-ndi-key.md).

-   Binding interfaces. For more information, see [Specifying Binding Interfaces](specifying-binding-interfaces.md).

-   Adapter configuration parameters for the **Advanced** page. For more information, see [Specifying Configuration Parameters for the Advanced Properties Page](specifying-configuration-parameters-for-the-advanced-properties-page.md).

-   Bundle membership. For more information, see [Specifying Bundle Membership](specifying-bundle-membership.md).

For a list of **Ndi** registry keys and values that are available in Windows 95/98/Me but not used in Windows 2000 and later versions, see [Ndi Values and Keys Not Used in Windows 2000 and Later Versions](ndi-values-and-keys-not-used-in-windows-2000-and-later-versions.md).

 

 





