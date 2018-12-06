---
title: Including a NetworkProvider Section
description: Including a NetworkProvider Section
ms.assetid: 8972f926-c4f5-4a2f-8f2d-f9353fdbd83f
keywords:
- INF files WDK network , NetworkProvider section
- network INF files WDK , NetworkProvider section
- NetworkProvider section WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Including a NetworkProvider Section





A **NetworkProvider** section specifies either a substitute device name for a **NetClient** component or a short name for use with the NetWare **net view** command, or both.

**Note**  **NetClient** components are deprecated in Windows 8.1, Windows Server 2012 R2, and later.

 

To create a **NetworkProvider** section, add the **NetworkProvider** extension to the *DDInstall* section for the component, as shown in the following example:
```INF
[DDInstall] ; Install section
[DDInstall.NetworkProvider] ; NetworkProvider section
```

### Specifying a Device Name

The network class installer usually creates the device name for a network provider by copying the **Ndi\\Service** value for the component to the NetworkProvider key under the component's **Service** key. For more information, see [Adding Service-Related Values to the Ndi Key](adding-service-related-values-to-the-ndi-key.md). To specify a different device name for the component, include a **DeviceName** entry in the **NetworkProvider** section for the component, as shown in the following example:

```INF
[DDInstall-section.NetworkProvider]
DeviceName = "nwrdr"
```

The **DeviceName** is optional and should be specified only if the **Ndi\\Service** value for the component is inadequate as a device name for the network provider.

### Specifying a Short Name

To specify a short name for a network provider for use with the NetWare **net view** command, include a **ShortName** entry in the **NetworkProvider** section for the component, as shown in the following example:

```INF
[DDInstall-section.NetworkProvider]
ShortName = "nw"
```

The following is an example of a short name used with the **net view** command:

```INF
net view /n:nw
```

The **ShortName** is easier to remember and type than the entire name of the network provider.

The **ShortName** is optional and should only be specified if needed.

 

 





