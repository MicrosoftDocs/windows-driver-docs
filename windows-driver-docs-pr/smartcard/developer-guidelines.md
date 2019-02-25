---
title: Developer Guidelines
description: This topic discusses general guidelines for working with and developing smart card minidrivers. 
ms.assetid: 48999DF6-3AC2-4DEA-8ABC-C427237B31E8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Developer Guidelines


This topic discusses general guidelines for developers who work with, and/or develop smart card minidrivers - to let you know the expected behavior of the smart card and its associated applications.

## <span id="General_Design_Guidelines"></span><span id="general_design_guidelines"></span><span id="GENERAL_DESIGN_GUIDELINES"></span>General Design Guidelines


For information about how to distribute card minidrivers, how to map logical card file-systems and other minidriver design guidelines, see the **General Design Guidelines** section under [Smart Card Minidriver Overview](smart-card-minidriver-overview.md).

## <span id="Challenge_Response_Method_of_Unblocking_Smart_Card_PIN"></span><span id="challenge_response_method_of_unblocking_smart_card_pin"></span><span id="CHALLENGE_RESPONSE_METHOD_OF_UNBLOCKING_SMART_CARD_PIN"></span>Challenge/Response Method of Unblocking Smart Card PIN


For an administrator to successfully use this mechanism to unblock a user’s card, administrators must be able to identify and use the administrator key that is stored on the card so that they can correctly generate the response data to the challenge that was issued.

One way to do this is to use the card identifier to uniquely identify the card. (The card identifier is a unique identifier for a card.) This can be represented in some form to users in the UI, but otherwise a program could be written to send appropriate APDU commands to the card to read this information.

This information can then allow the administrator to identify the secret key on the card and calculate the appropriate response to the challenge data that is issued to users.

It is assumed that the administrator secret key stored on a card is held by using some secure mechanism that is accessible only to valid and trusted administrators (preferably as few as possible). However, this is beyond the scope of this specification.

For more information, see the following “Challenge/Response Mechanism” section.

## <span id="Enhanced_PIN_Support"></span><span id="enhanced_pin_support"></span><span id="ENHANCED_PIN_SUPPORT"></span>Enhanced PIN Support


Version 6.0 supported a flexible architecture for multiple PIN support. This architecture introduced a new concept of roles in which each role corresponds to a PIN identifier. The PIN identifiers are used to extract PIN information from the card, as well as to associate a PIN with a key container.

The identifier consists of a number, currently limited to 0 through7. We also introduced the notion of a PIN\_SET, which is a bitmask that can be generated from the PIN identifier. Currently only the lower 8 bits are used for the PIN set. We can also choose to use the remaining bits to indicate conditions such as ‘and’, ‘or’, or other information that we might find useful in the future. We chose this approach so that the bit mask is easy for the card to enforce.

Assume that the user authenticates with role 3, corresponding to PIN \#3. This translates to the bit mask 0000 0100 (base 2). The card can record this as the currently authenticated ID and can easily verify access control rules on keys and PINs by doing a bit-wise AND operation. The design allows having multiple authenticated identities on the card simultaneously, and this is a requirement for cards that support v6 card minidrivers. As an example, if PIN \#1 is authenticated and then subsequently PIN \#2 is authenticated, operations that any of these PINs control should be allowed.

## <span id="_Session_PINs_and_Secure_PIN_Channel"></span><span id="_session_pins_and_secure_pin_channel"></span><span id="_SESSION_PINS_AND_SECURE_PIN_CHANNEL"></span> Session PINs and Secure PIN Channel


When Windows must establish a secure PIN channel for PIN authentication, the following sequence of operations is performed with the minidriver. To comply, a minidriver and the card must be compatible with the following sequence. In particular, session PINs should be transferable between processes and last for only a certain length of time. (We recommend that any session PIN be valid until the cold reset of the card by using the CARD\_AUTHENTICATE\_ SESSION\_PIN flag even if [**CardAuthenticateEx**](https://msdn.microsoft.com/library/windows/hardware/dn468703) is called with the GENERATE\_SESSION\_PIN flag set.)

The following behavior should be supported:

1.  Application A, a trusted system process, acquires a handle to the smart card and collects a PIN.
2.  Application A then calls the card [**CardAuthenticateEx**](https://msdn.microsoft.com/library/windows/hardware/dn468703) minidriver function, and passes the PIN that was collected and sets the CARD\_AUTHENTICATE\_GENERATE\_SESSION\_PIN flag. This does not cause the card to be unlocked.
3.  Application A stores the session PIN that was generated and releases the handle to the card and card minidriver. The card is not cold reset.
4.  Application A sends the session PIN and the name of the reader that has the card that was acquired in step 1 to Application B.
5.  Application B acquires the same card as in 1.
6.  Application B calls [**CardAuthenticateEx**](https://msdn.microsoft.com/library/windows/hardware/dn468703) and passes in the session PIN and sets the CARD\_AUTHENTICATE\_SESSION\_PIN flag. If the session PIN is still valid, the card should be authenticated and valid for use.
7.  When Application B is finished using the card, it calls [**CardDeauthenticateEx**](https://msdn.microsoft.com/library/windows/hardware/dn468713) to deauthorize the card.

This behavior has the following practical limitations:

-   Cards must declare their ability to work with session PINs by returning the appropriate value for CP\_CARD\_PIN\_STRENGTH\_VERIFY.
-   Cards that rely on having the PIN for each verification are not compatible with this system.
-   Several applications can have what they determine to be valid session PINs at any one time. If only one session PIN is possible for each PIN, the following implementation is advised:

    -   The card should remember the most recent session PIN that was generated.
    -   If an invalid session PIN is presented, the card should fail the authentication and, if supported, decrement the retry counter for the session PIN. If the retry count reaches 0 and the next authentication attempt is invalid, the session PIN should be invalidated.
    -   Subsequent session PIN presentations should fail until a new session PIN is negotiated.
-   The session PIN must be able to be used from different applications on the system.
-   The session PIN must not simply be an encoding of the PIN.
-   The security of this system is limited to the strength of the session PIN and the negotiation protocol that is used to generate it. The actual session PIN negotiation is outside the scope of this specification. We make no requirements on the design except that it works as described in this section.
-   The session PIN is still considered valuable and should be treated as a secret.
-   The card should be able to detect an invalid session PIN.

## <span id="Read-Only_Cards"></span><span id="read-only_cards"></span><span id="READ-ONLY_CARDS"></span>Read-Only Cards


To address cards that are personalized outside the Base CSP/KSP environment and are inherently read-only, we have introduced a new concept of read-only cards. If a card is read-only, it must advertise this through the [**CardGetProperty**](https://msdn.microsoft.com/library/windows/hardware/dn468729) function (see this section earlier in this specification).

Read-only cards must support only a subset of the Version 7 card minidriver interface and are not required to support an administrator PIN.

The following table lists the functions that a read-only card must support.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function name</th>
<th align="left">Required</th>
<th align="left">Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468701" data-raw-source="[&lt;strong&gt;CardAcquireContext&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468701)"><strong>CardAcquireContext</strong></a></td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468715" data-raw-source="[&lt;strong&gt;CardDeleteContext&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468715)"><strong>CardDeleteContext</strong></a></td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468704" data-raw-source="[&lt;strong&gt;CardAuthenticatePin&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468704)"><strong>CardAuthenticatePin</strong></a></td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468723" data-raw-source="[&lt;strong&gt;CardGetChallenge&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468723)"><strong>CardGetChallenge</strong></a></td>
<td align="left">No (Optional)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468702" data-raw-source="[&lt;strong&gt;CardAuthenticateChallenge&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468702)"><strong>CardAuthenticateChallenge</strong></a></td>
<td align="left">No (Optional)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468712" data-raw-source="[&lt;strong&gt;CardDeauthenticate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468712)"><strong>CardDeauthenticate</strong></a></td>
<td align="left">Yes (Optional)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468742" data-raw-source="[&lt;strong&gt;CardUnblockPin&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468742)"><strong>CardUnblockPin</strong></a></td>
<td align="left">No (Optional)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468705" data-raw-source="[&lt;strong&gt;CardChangeAuthenticator&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468705)"><strong>CardChangeAuthenticator</strong></a></td>
<td align="left">No (Optional)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468710" data-raw-source="[&lt;strong&gt;CardCreateDirectory&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468710)"><strong>CardCreateDirectory</strong></a></td>
<td align="left">No</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468716" data-raw-source="[&lt;strong&gt;CardDeleteDirectory&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468716)"><strong>CardDeleteDirectory</strong></a></td>
<td align="left">No</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468736" data-raw-source="[&lt;strong&gt;CardReadFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468736)"><strong>CardReadFile</strong></a></td>
<td align="left">Yes</td>
<td align="left">Card minidriver must emulate a file system.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468711" data-raw-source="[&lt;strong&gt;CardCreateFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468711)"><strong>CardCreateFile</strong></a></td>
<td align="left">No</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468727" data-raw-source="[&lt;strong&gt;CardGetFileInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468727)"><strong>CardGetFileInfo</strong></a></td>
<td align="left">Yes</td>
<td align="left">Card minidriver must emulate a file system.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468743" data-raw-source="[&lt;strong&gt;CardWriteFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468743)"><strong>CardWriteFile</strong></a></td>
<td align="left">No</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468711" data-raw-source="[&lt;strong&gt;CardDeleteFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468711)"><strong>CardDeleteFile</strong></a></td>
<td align="left">No</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468721" data-raw-source="[&lt;strong&gt;CardEnumFiles&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468721)"><strong>CardEnumFiles</strong></a></td>
<td align="left">Yes</td>
<td align="left">Card minidriver must emulate a file system.</td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468734" data-raw-source="[&lt;strong&gt;CardQueryFreeSpace&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468734)"><strong>CardQueryFreeSpace</strong></a></td>
<td align="left">Yes</td>
<td align="left">Card minidriver must emulate a file system.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468733" data-raw-source="[&lt;strong&gt;CardQueryCapabilities&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468733)"><strong>CardQueryCapabilities</strong></a></td>
<td align="left">Yes</td>
<td align="left">Card minidriver must emulate a file system.</td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468708" data-raw-source="[&lt;strong&gt;CardCreateContainer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468708)"><strong>CardCreateContainer</strong></a></td>
<td align="left">No</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468709" data-raw-source="[&lt;strong&gt;CardCreateContainerEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468709)"><strong>CardCreateContainerEx</strong></a></td>
<td align="left">No (Optional)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468714" data-raw-source="[&lt;strong&gt;CardDeleteContainer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468714)"><strong>CardDeleteContainer</strong></a></td>
<td align="left">No</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468725" data-raw-source="[&lt;strong&gt;CardGetContainerInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468725)"><strong>CardGetContainerInfo</strong></a></td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468737" data-raw-source="[&lt;strong&gt;CardRSADecrypt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468737)"><strong>CardRSADecrypt</strong></a></td>
<td align="left">Yes (Optional)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468707" data-raw-source="[&lt;strong&gt;CardConstructDHAgreement&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468707)"><strong>CardConstructDHAgreement</strong></a></td>
<td align="left">Yes (Optional)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468718" data-raw-source="[&lt;strong&gt;CardDeriveKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468718)"><strong>CardDeriveKey</strong></a></td>
<td align="left">Yes (Optional)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468719" data-raw-source="[&lt;strong&gt;CardDestroyDHAgreement&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468719)"><strong>CardDestroyDHAgreement</strong></a></td>
<td align="left">Yes (Optional)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468741" data-raw-source="[&lt;strong&gt;CardSignData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468741)"><strong>CardSignData</strong></a></td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468735" data-raw-source="[&lt;strong&gt;CardQueryKeySizes&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468735)"><strong>CardQueryKeySizes</strong></a></td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468703" data-raw-source="[&lt;strong&gt;CardAuthenticateEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468703)"><strong>CardAuthenticateEx</strong></a></td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468706" data-raw-source="[&lt;strong&gt;CardChangeAuthenticatorEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468706)"><strong>CardChangeAuthenticatorEx</strong></a></td>
<td align="left">No (Optional)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468713" data-raw-source="[&lt;strong&gt;CardDeauthenticateEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468713)"><strong>CardDeauthenticateEx</strong></a></td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468724" data-raw-source="[&lt;strong&gt;CardGetChallengeEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468724)"><strong>CardGetChallengeEx</strong></a></td>
<td align="left">No (Optional)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468726" data-raw-source="[&lt;strong&gt;CardGetContainerProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468726)"><strong>CardGetContainerProperty</strong></a></td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468738" data-raw-source="[&lt;strong&gt;CardSetContainerProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468738)"><strong>CardSetContainerProperty</strong></a></td>
<td align="left">No</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468729" data-raw-source="[&lt;strong&gt;CardGetProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468729)"><strong>CardGetProperty</strong></a></td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468740" data-raw-source="[&lt;strong&gt;CardSetProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468740)"><strong>CardSetProperty</strong></a></td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468757" data-raw-source="[&lt;strong&gt;MDImportSessionKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468757)"><strong>MDImportSessionKey</strong></a></td>
<td align="left">No (Optional)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468756" data-raw-source="[&lt;strong&gt;MDEncryptData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468756)"><strong>MDEncryptData</strong></a></td>
<td align="left">No (Optional)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468731" data-raw-source="[&lt;strong&gt;CardImportSessionKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468731)"><strong>CardImportSessionKey</strong></a></td>
<td align="left">No (Optional)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468730" data-raw-source="[&lt;strong&gt;CardGetSharedKeyHandle&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468730)"><strong>CardGetSharedKeyHandle</strong></a></td>
<td align="left">No (Optional)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468722" data-raw-source="[&lt;strong&gt;CardGetAlgorithmProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468722)"><strong>CardGetAlgorithmProperty</strong></a></td>
<td align="left">No (Optional)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468728" data-raw-source="[&lt;strong&gt;CardGetKeyProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468728)"><strong>CardGetKeyProperty</strong></a></td>
<td align="left">No (Optional)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468739" data-raw-source="[&lt;strong&gt;CardSetKeyProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468739)"><strong>CardSetKeyProperty</strong></a></td>
<td align="left">No (Optional)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468720" data-raw-source="[&lt;strong&gt;CardDestroyKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468720)"><strong>CardDestroyKey</strong></a></td>
<td align="left">No (Optional)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/dn468732" data-raw-source="[&lt;strong&gt;CardProcessEncryptedData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468732)"><strong>CardProcessEncryptedData</strong></a></td>
<td align="left">No (Optional)</td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Legend</th>
<th align="left"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Yes</td>
<td align="left">This function must be implemented.</td>
</tr>
<tr class="even">
<td align="left">No</td>
<td align="left">Entry point must exist and must return SCARD_E_UNSUPPORTED_FEATURE.</td>
</tr>
<tr class="odd">
<td align="left">No (Optional)</td>
<td align="left">The operation is not required to be supported for a read-only card, but may be implemented if the card supports the operation. If not supported, the entry point must return SCARD_E_UNSUPPORTED_FEATURE.</td>
</tr>
<tr class="even">
<td align="left">Yes (Optional)</td>
<td align="left">This function should be implemented according to its definition in this specification, regardless of whether the card is read-only.</td>
</tr>
</tbody>
</table>

 

The following requirements should be considered when developing a minidriver for a read-only card:

-   All expected Base CSP/KSP files, with the exception of the ‘msroots’ file (such as ‘cardcf’ and ‘cardid’) must exist on the read-only card (or must be virtualized through the minidriver interface).
-   A read-only card must contain at least one key on the card that is protected by the primary card (that is, ROLE\_USER) PIN.
-   A read-only card is allowed to not contain an admin key. If this is the situation, it is expected that the minidriver will not support [**CardGetChallenge**](https://msdn.microsoft.com/library/windows/hardware/dn468723), [**CardAuthenticateChallenge**](https://msdn.microsoft.com/library/windows/hardware/dn468702), and [**CardUnblockPin**](https://msdn.microsoft.com/library/windows/hardware/dn468742).
-   When queried, a read-only card should return 0 bytes available and 0 containers available.
-   Only the CP\_PARENT\_WINDOW and CP\_PIN\_CONTEXT\_STRING properties should be allowed to be set on a read-only card.
-   For a read-only card, the CP\_SUPPORTS\_WIN\_X509\_ENROLLMENT property should be false.

## <span id="Cache_Modes"></span><span id="cache_modes"></span><span id="CACHE_MODES"></span>Cache Modes


The Base CSP/KSP supports three different modes of caching depending on the cache mode that was returned by the [**CardGetProperty**](https://msdn.microsoft.com/library/windows/hardware/dn468729) called with the parameter CP\_CARD\_CACHE\_MODE:

-   If the returned flag is CP\_CACHE\_MODE\_GLOBAL\_CACHE and the card reported the CP\_READ\_ONLY\_CARD property as TRUE, the Base CSP/KSP data cache is a global cache. If the card is read-only, the Base CSP/KSP does not write to the cardcf file. If the card can be written to the Base CSP/KSP, it will operate as today.
-   For more information about CP\_CARD\_CACHE\_MODE and CP\_CACHE\_MODE\_GLOBAL\_CACHE, see [**CardGetProperty**](https://msdn.microsoft.com/library/windows/hardware/dn468729).
-   When the returned flag is CP\_CACHE\_MODE\_SESSION\_ONLY, the Base CSP/KSP operates so that the data cache is cleared when it detects that the card has been removed or reinserted. In other words, we have defined a session to be the span between card insertion and removal.
-   The cache is also implemented for each process and is not global. This mode is designed for read-only cards that do not change on a user’s PC, but rather at some government station or other external site. (This mode is supported for read/write cards, but we recommend the global cache for these cards.)
-   If the card is read-only and there is a chance that the card will change on the user’s PC (by means other than Base CSP/KSP), the application should use the no cache mode that is described later in this specification to avoid the situation in which the cache could contain stale data.
-   When the flag is CP\_CACHE\_MODE\_NO\_CACHE, the Base CSP/KSP does not implement any data caching. This mode is designed for card minidrivers that do not support writing the cardcf file, but where the card state can change. The card minidriver decides whether it wants to do any caching in its layer.

## <span id="_Challenge_Response_Mechanism"></span><span id="_challenge_response_mechanism"></span><span id="_CHALLENGE_RESPONSE_MECHANISM"></span> Challenge/Response Mechanism


The card minidriver interface supports a challenge/response authentication mechanism. The card must generate a challenge of one or more 8 byte blocks. The authenticating entity calculates the response by encrypting the challenge by using Triple DES (3DES) that operates operating in CBC mode with a 168-bit key (and ignoring the parity bits).

The card verifies the response by using one of the following methods:

-   Repeating the encryption operation on the previously issued challenge and comparing the results.
-   Decrypting the response and comparing the result to the challenge.

If the resulting values are the same, the authentication is successful.

Both the card and the authenticating entity must use the same symmetric key.

The following sample code details how the authenticating entity could calculate the response. This code does not cover any associated warranties and is provided merely as an example and guidance.

```ManagedCPlusPlus
#include <windows.h>
#include <wincrypt.h>
#include <winscard.h>
#include <stdlib.h>
#include <stdio.h>
#include <memory.h>


int __cdecl wmain(int argc, __in_ecount(argc) WCHAR **wargv)
{
    //Acquire the context Use CryptAcquireContext

    HCRYPTPROV hProv= 0;
    DWORD dwMode=CRYPT_MODE_ECB;
    BYTE *pbLocData = NULL,tempbyte;
    DWORD cbLocData = 8, count = 0;
    HCRYPTKEY hKey = 0;
    BYTE rgEncByte [] = {0xA8,0x92,0xD7,0x56,0x01,0x61,0x7C,0x5D };

    BYTE DesKeyBlob [] = {
        0x08, 0x02, 0x00, 0x00, 0x03, 0x66, 0x00, 0x00,
        0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00
    };

    pbLocData = (BYTE *) malloc (sizeof(BYTE)*cbLocData);
    memcpy(pbLocData,rgEncByte,cbLocData);

    if (!CryptAcquireContext(
            &hProv,
            NULL,
            L"Microsoft Enhanced Cryptographic Provider V1.0",
            PROV_RSA_FULL,
            CRYPT_VERIFYCONTEXT))
    {
        printf("Acquire context failed with 0x%08x \n", GetLastError());
        goto Cleanup;
    }
    if (!CryptImportKey(
            hProv,
            DesKeyBlob,
            sizeof(DesKeyBlob),
            0,
            0,
            &hKey ) )
    {
        printf("Error 0x%08x in importing the 3Des key \n", GetLastError());
        goto Cleanup;
    }
    if (!CryptSetKeyParam(
            hKey,
            KP_MODE,
            (BYTE *)&dwMode,
            0))
    {
        printf("Error 0x%08x in CryptSetKeyParam \n", GetLastError());
        goto Cleanup;
    }
    if (!CryptEncrypt(
            hKey,
            0,
            FALSE,
            0,
            pbLocData,
            &cbLocData,
            cbLocData))
    {
        printf("Error 0x%08x in CryptEncrypt call \n", GetLastError());
        goto Cleanup;
    }

    for (count=0; count < cbLocData; ++count)
    {
        printf("0x%02x",pbLocData[count]);
    }
    printf("\n");

Cleanup:    
    if (hKey)
    {
        CryptDestroyKey(hKey);
        hKey = 0;
    }
    if (pbLocData)
    {
        free(pbLocData);
        pbLocData = NULL;
    }
    if (hProv)
    {
        CryptReleaseContext(hProv,0);
    }

    return 0;
}
```

## <span id="_Interoperability_with_msroots"></span><span id="_interoperability_with_msroots"></span><span id="_INTEROPERABILITY_WITH_MSROOTS"></span> Interoperability with msroots


The msroots file is a PKCS \#7 formatted certificate store for enterprise trusted roots. (The file is a bag of certificates with empty content and an empty signature and is written and read by the Base CSP.) Card minidriver developers are not required to write any special code in the card minidriver to handle this file. When storing certificates in msroots file, properties such as CODE\_SIGNING EKU are not propagated to the smart card because the msroots file stores certificates in a format different from the machine stores. Developers who want to read or write this file from other applications can use the following sample code snippets to access the data.

### <span id="Read_operations"></span><span id="read_operations"></span><span id="READ_OPERATIONS"></span>Read operations

```ManagedCPlusPlus
if (FALSE == CryptQueryObject(CERT_QUERY_OBJECT_BLOB,
                                &dbStore,
                                CERT_QUERY_CONTENT_FLAG_PKCS7_SIGNED,
                                CERT_QUERY_FORMAT_FLAG_BINARY,
                                0,
                                NULL,
                                NULL,
                                NULL,
                                phCertStore,
                                NULL,
                                NULL))
{
    dwSts = GetLastError();
}
```

### <span id="Write_operations"></span><span id="write_operations"></span><span id="WRITE_OPERATIONS"></span>Write operations

```ManagedCPlusPlus
// Serialize the store

if (FALSE == CertSaveStore( hCertStore,
                            PKCS_7_ASN_ENCODING | X509_ASN_ENCODING,
                            CERT_STORE_SAVE_AS_PKCS7,
                            CERT_STORE_SAVE_TO_MEMORY,
                            &dbStore,
                            0))
{
    dwSts = GetLastError();
    goto Ret;
}

dbStore.pbData = CspAllocH(dbStore.cbData);

if (NULL == dbStore.pbData)
{
    dwSts = ERROR_NOT_ENOUGH_MEMORY;
    goto Ret;
}

if (FALSE == CertSaveStore( hCertStore,
                            PKCS_7_ASN_ENCODING | X509_ASN_ENCODING,
                            CERT_STORE_SAVE_AS_PKCS7,
                            CERT_STORE_SAVE_TO_MEMORY,
                            &dbStore,
                            0))
{
    dwSts = GetLastError();
    goto Ret;
}
```

## <span id="Group_Policy_Settings_for_Microsoft_Base_Smart_Card_CSP"></span><span id="group_policy_settings_for_microsoft_base_smart_card_csp"></span><span id="GROUP_POLICY_SETTINGS_FOR_MICROSOFT_BASE_SMART_CARD_CSP"></span>Group Policy Settings for Microsoft Base Smart Card CSP


Group Policy settings for the Microsoft Base Smart Card Crypto Service Provider are located in \[HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\Defaults \\Provider\\Microsoft Base Smart Card Crypto Provider\].

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Key</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">DefaultPrivateKeyLenBits</td>
<td align="left"><p>dword:00000400</p>
<p>Default key generation parameter—1024-bit key.</p></td>
</tr>
<tr class="even">
<td align="left">RequireOnCardPrivateKeyGen</td>
<td align="left"><p>dword:00000000</p>
<p>This sets the flag for requiring on-card private key generation (default). If this value is set, the key that is generated on a host can be imported into the card. This is used for cards that do not support on-card key generation or where key escrow is required.</p></td>
</tr>
<tr class="odd">
<td align="left">TransactionTimeoutMilliseconds</td>
<td align="left"><p>dword:000005dc</p>
<p>1500, 1.5 seconds is the default time-out for holding transactions to the card.</p></td>
</tr>
<tr class="even">
<td align="left">AllowPrivateSignatureKeyImport</td>
<td align="left"><p>dword:00000000</p>
<p>Allows importing signature keys, that is, key archival scenarios.</p></td>
</tr>
<tr class="odd">
<td align="left">AllowPrivateExchangeKeyImport</td>
<td align="left"><p>dword:00000000</p>
<p>Allows importing exchange keys, that is, key archival scenarios.</p></td>
</tr>
</tbody>
</table>

 

## <span id="_Group_Policy_Settings_for_Microsoft_CNG_Smart_Card_KSP"></span><span id="_group_policy_settings_for_microsoft_cng_smart_card_ksp"></span><span id="_GROUP_POLICY_SETTINGS_FOR_MICROSOFT_CNG_SMART_CARD_KSP"></span> Group Policy Settings for Microsoft CNG Smart Card KSP


Group Policy Settings for Microsoft CNG Smart Card Key Storage Provider are located in \[HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Cryptography \\Providers\\Microsoft Smart Card Key Storage Provider\].

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Key</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">DefaultPrivateKeyLenBits</td>
<td align="left"><p>dword:00000400</p>
<p>Default key generation parameter—1024-bit key.</p></td>
</tr>
<tr class="even">
<td align="left">RequireOnCardPrivateKeyGen</td>
<td align="left"><p>dword:00000000</p>
<p>This sets the flag for requiring on-card private key generation (default). If this value is set, the key that is generated on a host can be imported into the card. This is used for cards that do not support on-card key generation or where key escrow is required.</p></td>
</tr>
<tr class="odd">
<td align="left">TransactionTimeoutMilliseconds</td>
<td align="left"><p>dword:000005dc</p>
<p>1500, 1.5 seconds is the default time-out for holding transactions to the card.</p></td>
</tr>
<tr class="even">
<td align="left">AllowPrivateSignatureKeyImport</td>
<td align="left"><p>dword:00000000</p>
<p>Allows importing signature keys, that is, key archival scenarios.</p></td>
</tr>
<tr class="odd">
<td align="left">AllowPrivateExchangeKeyImport</td>
<td align="left"><p>dword:00000000</p>
<p>Allows importing exchange keys, that is, key archival scenarios.</p></td>
</tr>
<tr class="even">
<td align="left">AllocPrivateECDHEKeyImport</td>
<td align="left"><p>dword:00000000</p>
<p>Allows importing ECDH keys, that is, key archival scenarios</p></td>
</tr>
<tr class="odd">
<td align="left">AllowPrivateECDSAKeyImport</td>
<td align="left"><p>dword:00000000</p>
<p>Allows importing ECDSA keys, that is, key archival scenarios</p></td>
</tr>
</tbody>
</table>

 

## <span id="Special_Considerations"></span><span id="special_considerations"></span><span id="SPECIAL_CONSIDERATIONS"></span>Special Considerations


-   In Windows Vista with Service Pack 1 (SP1), while the operating system is running in safe mode, no PIN-required smart card operations are possible, other than Windows logon.
-   Calling CryptAcquireContext with one of the following flags prompts for PIN authentication with USER\_PIN regardless of the actual PIN that is assigned to the container:

    -   CRYPT\_NEWKEYSET
    -   CRYPT\_DEFAULT\_CONTAINER\_OPTIONAL
    -   CRYPT\_DELETEKEYSET
    -   CRYPT\_VERIFYCONTEXT
-   [**CardDeleteContext**](https://msdn.microsoft.com/library/windows/hardware/dn468715) can be called even after *DllMain* was called with DLL\_PROCESS\_DETACH.

 

 

