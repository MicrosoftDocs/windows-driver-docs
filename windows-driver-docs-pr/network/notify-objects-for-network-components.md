---
title: Notify Objects for Network Components
description: Notify Objects for Network Components
ms.assetid: 5b5c5da2-7163-44cf-8e8a-c736278f2535
keywords:
- notify objects WDK networking
- network notify objects WDK
- notifications WDK networking
- network component notify objects WDK
- displaying Property pages
- property pages WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Notify Objects for Network Components





A *notify object* processes notifications that are sent by the network configuration subsystem to the object on behalf of a specific network component. A notify object is served up by a dynamic-link library (DLL). A notify object is used to display Property pages for a network component and to give that component programmatic control over the network configuration.

**Note**  A network component does not generally require a notify object if both of the following conditions are true:

 

-   A network component can be installed and removed through its information (INF) file

-   Reacting to changes in network configuration is not a requirement

The following sections describe notify objects and explain how to develop them:

[About Notify Objects](about-notify-objects.md)

[Creating a Notify Object](creating-a-notify-object.md)

For reference information for the interface methods that support notify objects, see [Notify Objects](https://msdn.microsoft.com/library/windows/hardware/ff559161).

 

 





