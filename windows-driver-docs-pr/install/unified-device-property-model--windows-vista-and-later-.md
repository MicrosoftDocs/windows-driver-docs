---
title: Unified Device Property Model
description: Unified Device Property Model
ms.assetid: 51105f84-38d8-4005-a3fd-4beccc0a2a39
keywords: ["device properties WDK device installations , unified device property model"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Unified%20Device%20Property%20Model%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




