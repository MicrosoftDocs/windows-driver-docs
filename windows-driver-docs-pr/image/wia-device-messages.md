---
title: WIA Device Messages
description: WIA Device Messages
ms.assetid: b498a75d-1252-4f13-ae62-9a53491c2bde
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Device Messages


The following list shows all currently defined WIA device messages. These messages can be sent during **IWiaTransfer::Download** and **IWiaTransfer::Upload**. The **IWiaTransfer** interface is described in the Microsoft Windows SDK documentation.

### Device Status Messages:

-   WIA\_STATUS\_WARMING\_UP

-   WIA\_STATUS\_CALIBRATING

-   WIA\_STATUS\_RESERVING\_NETWORK\_DEVICE

-   WIA\_STATUS\_NETWORK\_DEVICE\_RESERVED

-   WIA\_STATUS\_CLEAR

### Device Error Messages:

-   WIA\_ERROR\_GENERAL\_ERROR

-   WIA\_ERROR\_PAPER\_JAM

-   WIA\_ERROR\_PAPER\_EMPTY

-   WIA\_ERROR\_PAPER\_PROBLEM

-   WIA\_ERROR\_OFFLINE

-   WIA\_ERROR\_BUSY

-   WIA\_ERROR\_WARMING\_UP

-   WIA\_ERROR\_USER\_INTERVENTION

-   WIA\_ERROR\_ITEM\_DELETED

-   WIA\_ERROR\_DEVICE\_COMMUNICATION

-   WIA\_ERROR\_INVALID\_COMMAND

-   WIA\_ERROR\_INCORRECT\_HARDWARE\_SETTING

-   WIA\_ERROR\_DEVICE\_LOCKED

-   WIA\_ERROR\_EXCEPTION\_IN\_DRIVER

-   WIA\_ERROR\_INVALID\_DRIVER\_RESPONSE

-   WIA\_ERROR\_COVER\_OPEN

-   WIA\_ERROR\_LAMP\_OFF

-   WIA\_ERROR\_DESTINATION

-   WIA\_ERROR\_NETWORK\_RESERVATION\_FAILED

WIA Default Error Handler

Currently, the WIA default error handler supports the following device messages:

-   WIA\_STATUS\_WARMING\_UP

-   WIA\_STATUS\_CALIBRATING

-   WIA\_STATUS\_RESERVING\_NETWORK\_DEVICE

-   WIA\_STATUS\_NETWORK\_DEVICE\_RESERVED

-   WIA\_ERROR\_PAPER\_JAM

-   WIA\_ERROR\_DEVICE\_LOCKED

-   WIA\_ERROR\_NETWORK\_RESERVATION\_FAILED

-   WIA\_ERROR\_COVER\_OPEN

-   WIA\_ERROR\_LAMP\_OFF

-   WIA\_ERROR\_DESTINATION

-   WIA\_ERROR\_PAPER\_EMPTY

 

 




