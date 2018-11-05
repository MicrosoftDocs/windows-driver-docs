---
title: Minidriver Version 6.02 Features
description: Minidriver Version 6.02 Features
ms.assetid: 8BF4B63B-B723-4899-BCAF-7826FAFF2155
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minidriver Version 6.02 Features


The following features are introduced in this version.

## <span id="Enhanced_Support_for_PINs"></span><span id="enhanced_support_for_pins"></span><span id="ENHANCED_SUPPORT_FOR_PINS"></span>Enhanced Support for PINs


Version 6 of the smart card minidriver specification enhances the support for PINs. This version introduces a new concept of a logical PIN object. A developer can use the PIN object architecture to control PIN prompting in Windows and enable a flexible and wide set of scenarios. The PIN object may or may not correspond to an actual physical PIN on the card and should be viewed as a way for a card minidriver to control PIN-related behavior in Windows.

Through a new set of APIs, a card minidriver developer can now:

-   Support cards that use more than 2 PINs (up to 8 PINs in total).
-   Return a session PIN to Windows to cache instead of the actual PIN.
-   Control what strings appear to the user during a PIN prompt.
-   Indicate to Windows to prompt for a PIN when a specific key is requested.
-   Allow access to a card or container without a PIN prompt (empty PIN).

For more information, see the "Enhanced PIN Support" section in [Developer Guidelines](developer-guidelines.md).

For reference information, see [Card PIN Operations](card-pin-operations.md).

New APIs added in this version include:

-   [**CardAuthenticateEx**](https://msdn.microsoft.com/library/windows/hardware/dn468703)
-   [**CardGetChallengeEx**](https://msdn.microsoft.com/library/windows/hardware/dn468724)
-   [**CardDeauthenticateEx**](https://msdn.microsoft.com/library/windows/hardware/dn468713)
-   [**CardChangeAuthenticatorEx**](https://msdn.microsoft.com/library/windows/hardware/dn468706)

**Important**  Not all provisioning systems support multiple PINs; consequently, care must be taken when applying PINs on keys that can be updated in the field by a card provisioning system.

 

## <span id="Support_for_Read-Only_Cards"></span><span id="support_for_read-only_cards"></span><span id="SUPPORT_FOR_READ-ONLY_CARDS"></span>Support for Read-Only Cards


Secure PIN channel is a feature in Windows Vista with Service Pack 1 (SP1) that enables a secure PIN prompt followed by establishment of a secure channel between Windows and the smart card for PIN authentication. Secure PIN channel protects the card PIN against eavesdropping while traveling through operating system component and while transmitted to the card.

Secure PIN prompt means that the user is requested to press ALT+CTL+DEL before prompted for the PIN following a visual experience identical to Windows logon. Secure PIN prompt reduces the risk of PIN harvesting by a spoof PIN prompt dialog box.

Secure PIN channel can be controlled and triggered by Common Criteria group policy setting and also by a specific attribute on the PIN object.

For more information on secure PIN channel, see the “Session PINs" section in [Developer Guidelines](developer-guidelines.md).

The new API related to this feature includes [**CardAuthenticateEx**](https://msdn.microsoft.com/library/windows/hardware/dn468703).

## <span id="_External_PIN_Support"></span><span id="_external_pin_support"></span><span id="_EXTERNAL_PIN_SUPPORT"></span> External PIN Support


An external PIN support is a PIN that is collected off the PC from the user. Examples of an external PIN scenario include:

-   A PIN is collected on a PIN PAD reader.
-   A smart card has a fingerprint reader attached to it and performs a match on a card with a fingerprint template as an alternative to a PIN.

In an external PIN mode, whenever PIN authentication to a smart card is required, Windows does not prompt the user for a PIN but rather calls the minidriver's authentication API immediately without any notification to the user. It is expected that the actual authentication and PIN collection occur without operating system involvement.

Optionally, and subject to specific restrictions, the minidriver is allowed to display its own user interface (UI) to instruct the user to perform specific actions in relationship to PIN collection. It is not expected that such UI will be used to actually collect a PIN from the user, but rather to direct the user that Windows is waiting for a PIN to be collected externally. A minidriver is not allowed to display UI when the context is silent mode and is expected to use a specific window handle to create UI elements. More information can be found in [**CardAuthenticateEx**](https://msdn.microsoft.com/library/windows/hardware/dn468703), and [**CardSetProperty**](https://msdn.microsoft.com/library/windows/hardware/dn468740).

Cards that can return a temporary session PIN may return such a PIN to Windows for subsequent caching. In such a case, Windows presents the session PIN for any further card authentication until the card invalidates the session PIN. For more information, see [**CardAuthenticateEx**](https://msdn.microsoft.com/library/windows/hardware/dn468703).

 

 





