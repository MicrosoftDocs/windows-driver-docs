---
title: Minidriver Version 7.06 Features
description: Minidriver Version 7.06 Features
ms.assetid: 6066C6F9-DF03-4886-A5AE-FFE50B2B34D8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minidriver Version 7.06 Features


The following features are introduced in this version.

## <span id="Secure_Key_Injection"></span><span id="secure_key_injection"></span><span id="SECURE_KEY_INJECTION"></span>Secure Key Injection


This feature is useful if applications, which are running on a computer that is disconnected from a smart card, must import sensitive data to the smart card that is connected to other computers.

One typical scenario for secure key injection is when a certification authority (CA), which is running on a server, must perform the following actions:

-   Generate a key pair on the server.
-   Archive the user key.
-   Import the key pair to the smart card inserted in the user’s computer.

Developers can use the new APIs and data structures that were introduced for secure key injection to provide the following:

-   Support for the properties that allow the smart card framework to determine whether the card supports secure key injection.
-   Establish symmetric keys for encryption of data such as PINs, administrator keys and asymmetric key pairs. The session keys can then be imported to the smart card.
-   Encrypt and encapsulate data into a format that can be imported to and processed on the smart card.
-   Decrypt the encrypted data with the session key on the smart card.

The following structures for passing encrypted data are defined in this version of the specification:

-   [**CARD\_AUTHENTICATE**](https://msdn.microsoft.com/library/windows/hardware/dn468744)
-   [**CARD\_AUTHENTICATE\_RESPONSE**](https://msdn.microsoft.com/library/windows/hardware/dn468745)
-   [**CARD\_CHANGE\_AUTHENTICATOR**](https://msdn.microsoft.com/library/windows/hardware/dn468746)
-   [**CARD\_CHANGE\_AUTHENTICATOR\_RESPONSE**](https://msdn.microsoft.com/library/windows/hardware/dn468747)
-   [**CARD\_ENCRYPTED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/dn468749)
-   [**CARD\_IMPORT\_KEYPAIR**](https://msdn.microsoft.com/library/windows/hardware/dn468750)

The following card properties for secure key injection are defined in version 7 of this specification. For more information about these properties, see [**CardGetProperty**](https://msdn.microsoft.com/library/windows/hardware/dn468729).

-   CP\_KEY\_IMPORT\_SUPPORT
-   CP\_ENUM\_ALGORITHMS
-   CP\_PADDING\_SCHEMES
-   CP\_CHAINING\_MODES

The following APIs have been added for secure key injection in version 7 of this specification. For more information, see [Secure Key Injection](secure-key-injection.md).

Server functions:

-   [**MDEncryptData**](https://msdn.microsoft.com/library/windows/hardware/dn468756)
-   [**MDImportSessionKey**](https://msdn.microsoft.com/library/windows/hardware/dn468757)

Shared functions:

-   [**CardDestroyKey**](https://msdn.microsoft.com/library/windows/hardware/dn468720)
-   [**CardGetAlgorithmProperty**](https://msdn.microsoft.com/library/windows/hardware/dn468722)
-   [**CardGetKeyProperty**](https://msdn.microsoft.com/library/windows/hardware/dn468728)
-   [**CardGetSharedKeyHandle**](https://msdn.microsoft.com/library/windows/hardware/dn468730)
-   [**CardProcessEncryptedData**](https://msdn.microsoft.com/library/windows/hardware/dn468732)
-   [**CardSetKeyProperty**](https://msdn.microsoft.com/library/windows/hardware/dn468739)

Client functions:

-   [**CardImportSessionKey**](https://msdn.microsoft.com/library/windows/hardware/dn468731)

## <span id="Support_for_RSA_Padding_Removal_Operations_in_the_Smart_Card"></span><span id="support_for_rsa_padding_removal_operations_in_the_smart_card"></span><span id="SUPPORT_FOR_RSA_PADDING_REMOVAL_OPERATIONS_IN_THE_SMART_CARD"></span>Support for RSA Padding Removal Operations in the Smart Card


Version 7 of the smart card minidriver interface lets smart card vendors provide support for RSA padding removal operations in the smart card itself. This prevents exposure to a ciphertext attack when the Base CSP/KSP removes the padding. This enhancement also removes the requirement for raw RSA decryption operations by the minidriver.

Version 7 also provides support for older cards that do not support internal (or OnCard) padding removal. This allows these cards to continue to use the padding removal capabilities that the Base CSP/KSP provides.

For more information, see [**PFN\_CSP\_UNPAD\_DATA**](https://msdn.microsoft.com/library/windows/hardware/dn468771) and [**CardRSADecrypt**](https://msdn.microsoft.com/library/windows/hardware/dn468737) later in this specification.

## <span id="Smart_Card_Plug_and_Play"></span><span id="smart_card_plug_and_play"></span><span id="SMART_CARD_PLUG_AND_PLAY"></span>Smart Card Plug and Play


When a logo-certified smart card is first inserted into a card reader that is connected to a Windows 7 computer, the Plug and Play framework searches for a compatible minidriver that is published in Windows Update. If it finds a minidriver, Plug and Play automatically downloads the minidriver from Windows Update and installs it in the computer.

For more information, see [Smart Card Plug and Play](smart-card-plug-and-play.md).

## <span id="_CardCreateContainerEx"></span><span id="_cardcreatecontainerex"></span><span id="_CARDCREATECONTAINEREX"></span> CardCreateContainerEx


This new API is extends the functionality of the [**CardCreateContainer**](https://msdn.microsoft.com/library/windows/hardware/dn468708) API. In addition to creating the key container, this function establishes the PIN association when the container is created.

For more information, see [**CardCreateContainerEx**](https://msdn.microsoft.com/library/windows/hardware/dn468709) later in this specification.

## <span id="New_Card_Container_Property_for_ECDSA_ECDH_Key_Association"></span><span id="new_card_container_property_for_ecdsa_ecdh_key_association"></span><span id="NEW_CARD_CONTAINER_PROPERTY_FOR_ECDSA_ECDH_KEY_ASSOCIATION"></span>New Card Container Property for ECDSA/ECDH Key Association


This new container property associates an Elliptic Curve Digital Signature Algorithm (ECDSA) key with an Elliptic Curve Diffie-Hellman (ECDH) key. Each ECDSA key is paired with an ECDH key, which is used for data encryption and decryption. This association supports scenarios that require encryption when ECDSA keys are used.

When the logon certificate is an ECDSA certificate, the cached logon credentials are encrypted by using the associated ECDH key. During cached logon operations, data from the domain controller is decrypted by using the ECDH key that is associated with the ECDSA key that was used for user logon. In this situation, the smart card can be used for logon operations when the computer is offline or the domain controller is inaccessible.

For more information, see the description of the CCP\_ASSOCIATED\_ECDH\_KEY property in “Card and Container Properties” later in this specification.

## <span id="Generic_Inbox_Minidriver_that_Supports_PIV"></span><span id="generic_inbox_minidriver_that_supports_piv"></span><span id="GENERIC_INBOX_MINIDRIVER_THAT_SUPPORTS_PIV"></span>Generic Inbox Minidriver that Supports PIV


Beginning with Windows 7, the operating system includes an inbox generic minidriver that can be used with smart cards that support the Personal Identity Verification (PIV) card edge and data model.

For more information about PIV, see the “About Personal Identity Verification (PIV) of Federal Employees and Contractors” Web page.

For more information about the process that Windows follows to identify and pair a PIV card with the inbox driver, see [Windows Inbox Smart Card Minidriver](windows-inbox-smart-card-minidriver.md).

 

 





