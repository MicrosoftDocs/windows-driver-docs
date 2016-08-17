---
title: Overview of Microsoft STI and Microsoft WIA
description: Overview of Microsoft STI and Microsoft WIA
MS-HAID:
- 'stillimg\_c201559a-cc95-4e7f-bf16-e39322ea3e2e.xml'
- 'image.overview\_of\_microsoft\_sti\_and\_microsoft\_wia'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c973f9a2-48a5-420f-b317-0797171cf714
---

# Overview of Microsoft STI and Microsoft WIA


## <a href="" id="ddk-overview-of-microsoft-sti-and-microsoft-wia-si"></a>


The imaging architecture in Microsoft Windows 2000 and Windows 95/98 consists of a low-level hardware abstraction, STI, and a high-level set of APIs known as TWAIN. In the Windows XP and Windows Me operating system versions, Microsoft introduces Windows Imaging Architecture (WIA), an imaging architecture that builds on STI. The following diagram illustrates these two imaging architectures.

![diagram illustrating the twain/sti and the microsoft wia imaging architectures](images/sti-wia.png)

As shown in the preceding figure, the TWAIN/STI architecture includes TWAIN, a high-level set of image acquisition APIs, together with STI, a low-level hardware abstraction. The WIA architecture incorporates STI as a foundation to provide a complete solution to imaging device IHVs.

### Differences Between STI and WIA

A WIA driver builds on the foundation provided by STI and so exposes STI interfaces in addition to its own. At a minimum, a WIA driver must expose the **IStiUSD** interface. STI has no corresponding dependency on any WIA interface. Because a WIA minidriver must be compliant with an STI minidriver, it is possible to write just an STI minidriver that makes a WIA-capable camera or scanner an STI image device. However, WIA is recommended for a better user experience. For example, an STI driver for a camera does not show thumbnails in Explorer.

Some differences between STI and WIA include the following:

-   STI runs in both the client application process and the system service process; WIA runs in the system service process only.

-   STI, being a low-level hardware abstraction, must have detailed information about the device in order to operate; WIA can operate without such detailed device information.

-   STI is not a complete imaging interface; WIA, which is built on top of STI, is a full solution for imaging IHVs. An IHV-supplied UI module (for example, Twain,) is required in an STI architecture because it has only a device communication mechanism, and does not have a UI front end. A WIA minidriver does not require its own UI module, because there is a default UI (the Scanner and Camera Wizard). Additionally, a Twain interface is supported through the TWAIN compatibility layer in the WIA architecture. IHVs can extend or replace these default UIs in WIA.

For more information about the WIA architecture, see [WIA Architecture Overview](wia-architecture-overview.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Overview%20of%20Microsoft%20STI%20and%20Microsoft%20WIA%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




