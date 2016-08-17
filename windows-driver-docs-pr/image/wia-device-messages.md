---
title: WIA Device Messages
description: WIA Device Messages
MS-HAID:
- 'WIA\_error\_2ad4285b-061a-4167-90a0-223128872fff.xml'
- 'image.wia\_device\_messages'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b498a75d-1252-4f13-ae62-9a53491c2bde
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Device%20Messages%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




