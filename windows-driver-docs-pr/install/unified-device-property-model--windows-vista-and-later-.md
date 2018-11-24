---
title: Unified Device Property Model
description: Unified Device Property Model
ms.assetid: 51105f84-38d8-4005-a3fd-4beccc0a2a39
keywords:
- device properties WDK device installations , unified device property model
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unified Device Property Model


Windows Vista and later versions of Windows support a unified device property model that characterizes the system configuration of [*device instances*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance), [device setup classes](device-setup-classes.md), [device interface classes](device-interface-classes.md), and [*device interfaces*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-interface). For information about the unified device property model, see the following topics:

-   [System-Defined Device Properties](system-defined-device-properties2.md)

-   [Creating Custom Device Properties](creating-custom-device-properties.md)

-   [Property Keys](property-keys.md)

-   [Property-Data-Type Identifiers](property-data-type-identifiers.md)

-   [Property Value Requirements](property-value-requirements.md)

-   [Properties and Related System-Defined Items](properties-and-related-system-defined-items.md)

-   [INF File Entry Values That Modify Device Properties](inf-file-entry-values-that-modify-device-properties--windows-vista-and.md)

-   [Using SetupAPI to Access Device Properties](using-setupapi-to-access-device-properties--windows-vista-and-later-.md)

-   [Using the INF AddProperty Directive and the INF DelProperty Directive](using-the-inf-addproperty-directive-and-the-inf-delproperty-directive.md)

Many of the system-defined device properties in the unified device property model have corresponding representations that can be used to access the same information on Microsoft Windows Server 2003, Windows XP, and Windows 2000. To maintain compatibility with these earlier Windows versions, Windows Vista and later versions of Windows also support these representations. However, you should use the unified device property model of Windows Vista and later to access device properties.

 

 





