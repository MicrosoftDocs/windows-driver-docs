---
title: Improved End-User Experience
description: Improved End-User Experience
ms.assetid: d87062f2-2832-4443-b9f0-97e34f79c47f
keywords:
- Print Tickets WDK , XPSDrv
- XPSDrv printer drivers WDK , end-user improvements
- Print Capabilities WDK , XPSDrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Improved End-User Experience


Windows Vista introduces two new technologies to improve communication of device capabilities and user intent:

-   **Print Ticket**. The XML-based Print Ticket technology enables better communication of printing intent between an application and a device to improve the end-user experiences. This technology enables printing components to be more transparent and handle settings migrations more cleanly. In the new application framework that is built on managed code objects in Windows Vista, Print Ticket is the standard way to describe print job settings.

    By using a well-defined XML-based format, the Print Ticket technology enables all components and clients of the print subsystem to have transparent access to the information that is currently stored in the public and private portions of the DEVMODE structure. The Print Ticket design resolves problems that can occur after a driver upgrade or downgrade. You can avoid problems that result from driver version mismatch scenarios with print drivers that are designed to use the Print Ticket technology. By using PrintTicket to communicate settings, you can avoid negative customer experiences on migration efforts.

-   **Print Capabilities**. The XML-based Print Capabilities technology provides a way to publish configurable device capabilities, such as finishing options and page layout options. Printers can use PrintCapabilities to describe explicitly all user-configurable attributes of the device and the allowable settings for each attribute. The Print Schema framework makes it possible to precisely describe and efficiently compare device attributes. By using the keywords in the Print Schema Keywords document and the structure that is defined in the Print Schema framework, applications can use device capabilities more effectively.

 

 




