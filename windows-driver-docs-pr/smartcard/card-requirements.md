---
title: Card Requirements
description: Card Requirements
ms.assetid: 3BE887F9-4B35-4A83-9E98-DD7555DF2953
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Card Requirements


To provide some context for the other requirements, this section gives some information about how the card is provisioned and used.

## <span id="What_a__Blank_Card__Is"></span><span id="what_a__blank_card__is"></span><span id="WHAT_A__BLANK_CARD__IS"></span>What a “Blank Card” Is


A “blank card,” which can be “created” and then used by the Microsoft Smart Card Base CSP/KSP, is a card that :

-   Contains the card operating system.
-   Contains or can virtualize necessary files and data to implement the file system.
-   Has default values for administrative and/or user PINs or keys.
-   Does not yet have the files that are discussed under “Card Creation” (the following section).
-   Is ready for card creation with no further preparation.
-   For future purposes, can provide an AID as defined in ISO 7816-4 part 8.

## <span id="_Card__Creation_"></span><span id="_card__creation_"></span><span id="_CARD__CREATION_"></span> Card “Creation”


For a card to be useful for cryptographic operations, it must have an identity that allows it to be recognized for purposes of deployment and management and it must be usable by the Base CSP/KSP. This requires a card ID file and certain files that the Base CSP/KSP requires to be stored on the card. The operation of creating these necessary files on the card is called “creating” the card. This is done by a deployment tool and consists of the following steps:

1.  Create the card ID file, “cardid”, in the root directory of the card with everyone having Read and the administrator having Write permissions. This file contains a unique 16-byte binary identifier for the card. It is never updated or overwritten unless the card is entirely recycled.
2.  Create the cache file, “cardcf”, in the root directory, with everyone having Read/Write permission. Initial contents are 6 bytes with values of zero.
3.  Create the application map, “cardapps”, in the root directory, with everyone having Read and users having Write permissions. Initial contents are an 8 byte record that consists of the string “mscp” followed by 4 zero bytes.
4.  Create the Base CSP/CNG KSP application by a call to [**CardCreateDirectory**](https://msdn.microsoft.com/library/windows/hardware/dn468710), referring to application “mscp”, with everyone having Read and the users having Write permissions.
5.  Create the certificate map file, “cmapfile”, in the “mscp” directory with everyone having Read and users having Write permissions. It is initially empty.

Technically, a card is “created” after step 2, but we define that all cards shall reserve the Microsoft “mscp” application, whether it is actually used. This explains the unusual facts that the “mscp” application is always created and that a file is created within the “mscp” application. As card creation is expected to be implemented by functions within the card management DLL that Microsoft supplies, this information is provided as reference information for card minidriver authors to be able to properly support these operations in that context.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[smartcrd\smartcrd]:%20Card%20Requirements%20%20RELEASE:%20%287/20/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




