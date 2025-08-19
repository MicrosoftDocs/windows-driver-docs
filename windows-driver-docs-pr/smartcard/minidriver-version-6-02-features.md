---
title: Minidriver Version 6.02 Features
description: Minidriver Version 6.02 Features
ms.date: 02/12/2024
ms.topic: release-notes
---

# Minidriver Version 6.02 Features

The following features are introduced in this version.

## Enhanced Support for PINs

Version 6.02 of the [Windows Smart Card Minidriver Specification](https://download.microsoft.com/download/9/c/5/9c5b2167-8017-4bae-9fde-d599bac8184a/sc-minidriver_specs_V6-final.docx) enhances support for PINs. This version introduces the concept of a logical PIN object. You can use the PIN object architecture to control PIN prompting in Windows and enable a flexible and wide set of scenarios. The PIN object may or may not correspond to an actual physical PIN on the card and should be viewed as a way for a card minidriver to control PIN-related behavior in Windows.

You can now:

- Support cards that use more than 2 PINs (up to 8 PINs in total).
- Return a session PIN to Windows to cache instead of the actual PIN.
- Control what strings appear to the user during a PIN prompt.
- Tell Windows to prompt for a PIN when a specific key is requested.
- Allow access to a card or container without a PIN prompt (empty PIN).

For more information, see the [Enhanced PIN Support](developer-guidelines.md#enhanced-pin-support) section in [Developer Guidelines](developer-guidelines.md).

For reference information, see [Card PIN Operations](card-pin-operations.md).

Device driver interfaces (DDIs) added in version 6.02 include:

- **[CardAuthenticateEx](/previous-versions/dn468703(v=vs.85))**
- **[CardGetChallengeEx](/previous-versions/dn468724(v=vs.85))**
- **[CardDeauthenticateEx](/previous-versions/dn468713(v=vs.85))**
- **[CardChangeAuthenticatorEx](/previous-versions/dn468706(v=vs.85))**

> [!IMPORTANT]
> Not all provisioning systems support multiple PINs. Care must be taken when applying PINs on keys that can be updated in the field by a card provisioning system.

## Support for Read-Only Cards

Smart cards are considered read-only when Windows can't write specific cache data to the card.

Version 6.02 of the [Windows Smart Card Minidriver Specification](https://download.microsoft.com/download/9/c/5/9c5b2167-8017-4bae-9fde-d599bac8184a/sc-minidriver_specs_V6-final.docx) adds new modes of data caching and enables a card minidriver to control those cache modes. For more information, see **[CardGetProperty](/previous-versions/dn468729(v=vs.85))**.

With these data cache modes, and proper virtualization of other system files, it's possible to develop a card minidriver that is fully compatible with a read-only smart card.

For more information on secure PIN channel, see the [Read-Only Cards](developer-guidelines.md#read-only-cards) section in [Developer Guidelines](developer-guidelines.md).

## Secure PIN Channel

Secure PIN channel is a feature that enables a secure PIN prompt followed by establishment of a secure channel between Windows and the smart card for PIN authentication. Secure PIN channel protects the card PIN against eavesdropping while traveling through operating system component and while transmitted to the card.

Secure PIN prompt means that the user is requested to press Ctrl+Alt+Del before being prompted for the PIN. The secure PIN prompt reduces the risk of PIN harvesting by a spoof PIN prompt dialog box.

Secure PIN channel is controlled and triggered by the Common Criteria group policy setting, and also by a specific attribute on the PIN object.

For more information on secure PIN channel, see the [Session PINs and Secure PIN Channel](developer-guidelines.md#-session-pins-and-secure-pin-channel) section in [Developer Guidelines](developer-guidelines.md).

The new DDI related to this feature includes **[CardAuthenticateEx](/previous-versions/dn468703(v=vs.85))**.

## External PIN Support

An external PIN support is a PIN that is collected off the PC from the user. Examples of an external PIN scenario include:

- A PIN is collected on a PIN PAD reader.
- A smart card has a fingerprint reader attached to it and performs a match on a card with a fingerprint template as an alternative to a PIN.

In an external PIN mode, whenever PIN authentication to a smart card is required, Windows doesn't prompt the user for a PIN but rather calls the minidriver's authentication DDI immediately without any notification to the user. Actual authentication and PIN collection should occur without operating system involvement.

Optionally, and subject to specific restrictions, the minidriver is allowed to display its own user interface instructing the user to perform specific actions related to PIN collection. It isn't expected that such UI is used to actually collect a PIN from the user, but rather to direct the user that Windows is waiting for a PIN to be collected externally. A minidriver isn't allowed to display UI when the context is silent mode and is expected to use a specific window handle to create UI elements. More information can be found in **[CardAuthenticateEx](/previous-versions/dn468703(v=vs.85))**, and **[CardSetProperty](/previous-versions/dn468740(v=vs.85))**.

Cards that return a temporary session PIN can return the PIN to Windows for subsequent caching. Windows presents the session PIN for any further card authentication until the card invalidates the session PIN. For more information, see **[CardAuthenticateEx](/previous-versions/dn468703(v=vs.85))**.

## Related topics

- [Windows Smart Card Minidriver Specification Version 6.02](https://download.microsoft.com/download/9/c/5/9c5b2167-8017-4bae-9fde-d599bac8184a/sc-minidriver_specs_V6-final.docx)
