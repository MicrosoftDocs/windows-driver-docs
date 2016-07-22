---
title: Writing a Device Installation Application
description: Writing a Device Installation Application
ms.assetid: 9927e2e0-6c8e-437f-98ce-595bd304ec72
keywords: ["installation applications WDK , about writing installation applications", "device installation applications WDK , about writing installation applications", "Device setup WDK device installations , writing installation applications", "installing devices WDK , writing installation applications", "writing device installation applications", "installation applications WDK", "device installation applications WDK", "applications WDK device installation", "device installations WDK , applications"]
---

# Writing a Device Installation Application


## <a href="" id="ddk-writing-a-device-installation-application-dg"></a>


**Note**  Features described in this section are not supported in universal or mobile driver packages. See [Using a Universal INF File](using-a-configurable-inf-file.md).

 

If your [driver package](driver-packages.md) includes drivers and INF files that replace "inbox" drivers and INF files, or if your package includes device-specific applications, it should include a [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) that installs those components. The device installation application and distribution medium should be compatible with AutoRun, so that AutoRun starts the application automatically when a user inserts your distribution medium. For more information about AutoRun, see [Creating an AutoRun-Enabled Application](http://go.microsoft.com/fwlink/p/?linkid=133162).

For guidelines about how to write a device installation application, see [Guidelines for Writing Device Installation Applications](guidelines-for-writing-device-installation-applications.md).

Your [driver package](driver-packages.md) must handle two situations:

1.  The user plugs in your hardware before inserting your distribution medium. This is commonly referred to as a [hardware-first installation](hardware-first-installation.md).

2.  The user inserts your distribution medium before plugging in your hardware. This is commonly referred to as a [software-first installation](software-first-installation.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Writing%20a%20Device%20Installation%20Application%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




