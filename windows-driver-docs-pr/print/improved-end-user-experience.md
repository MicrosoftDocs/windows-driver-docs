---
title: Improved End-User Experience
description: Improved End-User Experience
ms.assetid: d87062f2-2832-4443-b9f0-97e34f79c47f
keywords: ["Print Tickets WDK , XPSDrv", "XPSDrv printer drivers WDK , end-user improvements", "Print Capabilities WDK , XPSDrv"]
---

# Improved End-User Experience


Windows Vista introduces two new technologies to improve communication of device capabilities and user intent:

-   **Print Ticket**. The XML-based Print Ticket technology enables better communication of printing intent between an application and a device to improve the end-user experiences. This technology enables printing components to be more transparent and handle settings migrations more cleanly. In the new application framework that is built on managed code objects in Windows Vista, Print Ticket is the standard way to describe print job settings.

    By using a well-defined XML-based format, the Print Ticket technology enables all components and clients of the print subsystem to have transparent access to the information that is currently stored in the public and private portions of the DEVMODE structure. The Print Ticket design resolves problems that can occur after a driver upgrade or downgrade. You can avoid problems that result from driver version mismatch scenarios with print drivers that are designed to use the Print Ticket technology. By using PrintTicket to communicate settings, you can avoid negative customer experiences on migration efforts.

-   **Print Capabilities**. The XML-based Print Capabilities technology provides a way to publish configurable device capabilities, such as finishing options and page layout options. Printers can use PrintCapabilities to describe explicitly all user-configurable attributes of the device and the allowable settings for each attribute. The Print Schema framework makes it possible to precisely describe and efficiently compare device attributes. By using the keywords in the Print Schema Keywords document and the structure that is defined in the Print Schema framework, applications can use device capabilities more effectively.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Improved%20End-User%20Experience%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




