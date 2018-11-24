---
title: Discovery Process
description: Discovery Process
ms.assetid: 6B94CAF1-D998-4EAF-8ABB-80A21193B50F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Discovery Process


Beginning with Windows 7, smart card minidrivers that are logo-certified through the Windows Logo Program (WLP) are automatically downloaded and installed by the Windows Plug and Play components. Windows 7 also introduces a class minidriver for PIV-compatible cards and cards that support the GIDS card edge.

When a smart card is inserted into the reader, Windows performs the following discovery processes:

-   Smart Card Plug and Play Process:

    This process requests and download a logo-certified minidriver from Windows Update through Plug and Play.

-   Winscard Discovery Process:

    This process associates a compatible smart card with a PIV- or GIDS-compatible class minidriver.

-   Windows Smart Card Class Minidriver Discovery Process:

    This process associates an installed minidriver with a smart card.

The following table lists the AID values that the different discovery processes use.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">AID name</th>
<th align="left">AID value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">PIV AID</td>
<td align="left">A0 00 00 03 08 00 00 10 00 xx yy</td>
<td align="left">PIV AID, which does not include version information. The Microsoft smart card framework ignores the least-significant 2 bytes.</td>
</tr>
<tr class="even">
<td align="left">MS GIDS AID</td>
<td align="left">A0 00 00 03 97 42 54 46 59 xx yy</td>
<td align="left"><p>Microsoft (MS) GIDS AID, which does not include version information.</p>
<p>The least-significant 2 bytes are not sent to the card, but are reserved by the host as follows:</p>
<ul>
<li>The first of these bytes (xx) is used by the Windows smart card framework for the GIDS version number. This byte must be set to the GIDS specification revision number which is either 0x01 or 0x02.</li>
<li>The second byte (yy) is reserved for use by the card application.</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left">SC PNP AID</td>
<td align="left">A0 00 00 03 97 43 49 44 5F 01 00</td>
<td align="left">Smart card Plug and Play AID.</td>
</tr>
</tbody>
</table>

 

The following table lists the files used by the discovery process.

| Command | Instruction (INS) value |
|---------|-------------------------|
| MF      | 0x3F00                  |
| EF.ATR  | 0x2F01                  |

 

The following table lists the commands that the different discovery processes use.

| Command      | Instruction (INS) value |
|--------------|-------------------------|
| SELECT       | 0xA4                    |
| GET DATA     | 0xCA                    |
| GET RESPONSE | 0xC0                    |

 

## <span id="Smart_Card_Plug_and_Play_Process"></span><span id="smart_card_plug_and_play_process"></span><span id="SMART_CARD_PLUG_AND_PLAY_PROCESS"></span>Smart Card Plug and Play Process


Plug and Play installs a smart card minidriver if no compatible inbox minidriver is available. Plug and Play also updates the installed smart card minidrivers though Windows Update.

To do either of these tasks, Plug and Play must be able to derive a unique ID for the smart card. Beginning with Windows 7, the following describes the smart card discovery process that Plug and Play uses to derive a unique ID for the card:

1.  Plug and Play gets the historical bytes from the ATR. These bytes are used later in this discovery process.
2.  Plug and Play issues a SELECT command to locate the SC PNP AID.Plug and Play issues a GET DATA command to locate the Windows proprietary tag 0x7F68 (ASN.1 DER encoded). For more information, see the following subsection “Windows Smart Card Framework Card Identifier”. If this command is successful, a list of unique identifiers is returned. Plug and Play uses the first identifier in the list as the smart card’s device ID and uses that value for the card’s unique ID. For more information, see [Device IDs](https://msdn.microsoft.com/library/windows/hardware/ff541237).
3.  If Plug and Play derives a unique ID for the smart card, it proceeds to step 12.
4.  If Windows fails to obtain a device ID in the step above it will issue a SELECT of the MF and EF.ATR followed by a READ BINARY command, if Windows succeeds in obtaining a unique identifier that it can use as a device ID for WU go to step 12.
5.  If Plug and Play fails to obtain a unique identifier in the step above, it issues a SELECT command for the PIV AID. If Plug and Play succeeds, it considers the smart card to be a PIV-compatible device. Plug and Play uses the following as the card’s unique ID:

    1.  The PIV-compatible device ID as the device’s compatible ID. For more information, see [Compatible IDs](https://msdn.microsoft.com/library/windows/hardware/ff539950).
    2.  The card’s ATR historical bytes as the device ID. If there are no historical ATR bytes, Windows uses the PIV-compatible device id as the device ID.

6.  If Plug and Play derives a unique ID for the smart card, it proceeds to step 12.
7.  If the SELECT command in step 4 is unsuccessful, Windows issues a SELECT command for the MS GIDS AID.If Plug and Play succeeds in selecting the MS GIDS AID, it considers the smart card to be a GIDS-compatible device. Plug and Play uses the following as the card’s unique ID:

    1.  The GIDS-compatible device ID as the compatible ID.
    2.  The card’s ATR historical bytes as the device ID. If there are no historical ATR bytes, Plug and Play uses the GIDS-compatible device ID as the device ID.

8.  If Plug and Play derives a unique ID for the smart card, it proceeds to step 12.
9.  If Plug and Play fails to select the PIV AID or the MS GIDS AID, it uses the card’s ATR historical bytes (if any) as the device ID for the smart card’s unique ID.
10. If Plug and Play does not have the ATR historical bytes, it does not have enough information for Windows Update. Plug and Play fails the discovery process with SCARD\_E\_UNEXPECTED.
11. If Plug and Play derives a unique ID for the smart card, it proceeds to step 12.
12. Plug and Play stops the discovery process and uses the unique identifier.

Starting fromWindows 8, if Plug and Play is unable to find a driver for the card, the card is paired with an inbox NULL driver. Additional software specific to the card is then required for the card to function when connected to a smart card reader connected to the PC.

## <span id="Winscard_Discovery_Process"></span><span id="winscard_discovery_process"></span><span id="WINSCARD_DISCOVERY_PROCESS"></span>Winscard Discovery Process


The Winscard (Winscard.dll) discovery process is used to associate a card in the system with an installed minidriver. The process is started when [**SCardListCards**](https://msdn.microsoft.com/library/windows/desktop/aa379789) or [**SCardLocateCards**](https://msdn.microsoft.com/library/windows/desktop/aa379794) is called.

Beginning with Windows 7, the following describes the Winscard discovery process:

1.  Winscard looks in the registry under the Calais key for various subkeys that represent smart cards that are installed in the computer. These subkeys are located at:

    HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\Calais\\SmartCards

2.  Winscard searches each subkey under the SmartCards subkey for a match between the subkey’s ATR value and an ATR value that is obtained from the smart card. If a match is found, go to step 6.
3.  Winscard looks for a match between a SmartCards subkey value for a minidriver and a value within either the PIV Device ATR Cache (for PIV cards) or IDMP ATR Cache (for Microsoft GIDS-compatible cards) subkeys. If a match is found go to step 6.
4.  Winscard issues a SELECT command for the MS GIDS AID. If this command is successful, go to step 6.
5.  If step 4 fails, Winscard issues a SELECT command for the PIV AID. If this command is successful, go to step 6.
6.  Winscard returns the name of the card, which corresponds to the minidriver registry key that matches the card.

**Note**  The following table describes the various registry keys that the Winscard discovery process uses.

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Registry key</th>
<th align="left">Use</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft \Cryptography\Calais\SmartCards</td>
<td align="left">Winscard uses this key as the Calais\SmartCards key in step 1.</td>
</tr>
<tr class="even">
<td align="left">HKEY_LOCAL_MACHINE\ SOFTWARE\Microsoft \Cryptography\Calais\PIV Device ATR Cache</td>
<td align="left"><p>If a match is found in step 4, the full ATR of the matched card is stored in this registry key as a binary value. The name of the entry is randomly selected.</p>
<p>After this entry is cached, it is used in step 3 to improve performance.</p></td>
</tr>
<tr class="odd">
<td align="left">HKEY_LOCAL_MACHINE\ SOFTWARE\Microsoft \Cryptography\Calais\IDMP ATR Cache</td>
<td align="left"><p>If a match is found in step 5, the full ATR of the matched card is stored in under this registry key as a binary value. The name of the entry is randomly selected.</p>
<p>After this entry is cached, it is used in step 3 to improve performance.</p></td>
</tr>
</tbody>
</table>

 

## <span id="_Windows_Smart_Card_Class_Minidriver_Discovery_Process"></span><span id="_windows_smart_card_class_minidriver_discovery_process"></span><span id="_WINDOWS_SMART_CARD_CLASS_MINIDRIVER_DISCOVERY_PROCESS"></span> Windows Smart Card Class Minidriver Discovery Process


The Windows smart card class minidriver performs the following discovery process when [**CardAcquireContext**](https://msdn.microsoft.com/library/windows/hardware/dn468701) is called. The minidriver performs this discovery process to mark the associated card as PIV- or Microsoft GIDS-compatible:

1.  The minidriver issues a SELECT command for the PIV AID. If the command succeeds, the card is marked as PIV-compatible and the discovery process stops.
2.  Otherwise, the minidriver issues a SELECT command for the MS GIDS AID. If the command succeeds or fails to locate the AID, the minidriver marks the card as MS GIDS.

**Note**  
-   If the smart card was previously discovered through the Winscard discovery process with the class minidriver, it might not respond to the SELECT command for either the PIV or GIDS AID. In this situation, it must be a card from a vendor that implements the GIDS card-edge with a custom AID. Such cards could extend the Microsoft smart card data model with additional data objects.
-   PIV and GIDS smart card vendors can use the Windows smart card class minidriver and add branding by providing an INF-only installation package. For more information about using the class minidriver for compatible cards, see the INF sample in [Smart Card Plug and Play](smart-card-plug-and-play.md). Only historical bytes are used for Plug and Play matching in the INF.

    The INF file that the vendor provides creates entries under the Calais\\SmartCards registry subkey with the following information.

    | Entry name                      | Type   | Value                                     |
    |---------------------------------|--------|-------------------------------------------|
    | 80000001                        | String | Msclmd.dll                                |
    | ATR                             | Binary | Card’s ATR                                |
    | ATRMask                         | Binary | Card’s ATR Mask                           |
    | Crypto Provider                 | String | Microsoft Base Smart Card Crypto Provider |
    | Smart Card Key Storage Provider | String | Microsoft Smart Card Key Storage Provider |

     

 

## <span id="Selection_Mechanisms"></span><span id="selection_mechanisms"></span><span id="SELECTION_MECHANISMS"></span>Selection Mechanisms


### <span id="Applications_that_Contain_Microsoft_identifiers"></span><span id="applications_that_contain_microsoft_identifiers"></span><span id="APPLICATIONS_THAT_CONTAIN_MICROSOFT_IDENTIFIERS"></span>Applications that Contain Microsoft identifiers

The Windows smart card framework tries to select an application by using the Microsoft Plug and Play AID. If the card does not support the specified AID, it should return an error after the SELECT command. If the SELECT command completes successfully, the framework attempts to identify the card and corresponding smart card minidriver by issuing a GET DATA command.

The GET DATA commands take place regardless of whether the SC Plug and Play AID is supported. This allows applications, which are either associated with other AIDs or are not associated with any AIDs, to implement the card selection mechanisms in this specification.

### <span id="_GET_DATA"></span><span id="_get_data"></span> GET DATA

After it selects the Plug and Play MS AID on the card, the smart card framework issues a GET DATA command with the Windows proprietary tag of 0x7F68. If the card supports the GET DATA command and the proprietary tag, it responds by returning a list of one or more unique identifiers. The unique identifiers must be structured as defined in the following “Windows Smart Card Framework Card Identifier” section.

The Windows smart card framework uses only the first unique identifier in the list to locate and install the appropriate smart card minidriver. The other identifiers may be used in the future.

### <span id="_SELECT_PIV_AID_Command"></span><span id="_select_piv_aid_command"></span><span id="_SELECT_PIV_AID_COMMAND"></span> SELECT PIV AID Command

To identify a PIV application, Windows issues the SELECT PIV AID command. If this command succeeds, a PIV application is present on the card and is now selected. In this situation, the Windows smart card framework can now associate a PIV-compliant minidriver with the card.

### <span id="_SELECT_MS_GIDS_AID_Command"></span><span id="_select_ms_gids_aid_command"></span><span id="_SELECT_MS_GIDS_AID_COMMAND"></span> SELECT MS GIDS AID Command

To identify an MS GIDS application, a SELECT MS GIDS AID command is used. If this command succeeds, an MS GIDS application is present on the card and is now selected. The Windows smart card framework can now associate an MS GIDS–compliant minidriver with the card.

### <span id="Use_of_the_ATR_Historical_Bytes"></span><span id="use_of_the_atr_historical_bytes"></span><span id="USE_OF_THE_ATR_HISTORICAL_BYTES"></span>Use of the ATR Historical Bytes

Under the following conditions, the Windows smart card framework reverts to using the ATR historical bytes ATR to determine the minidriver to load:

-   The smart card does not support the GET DATA command.
-   The smart card does not support the AID selection methods in this specification.

The use of the ATR historical bytes is the legacy method that is used to identify the inserted card. The framework uses all historical bytes in its search for a minidriver.

### <span id="_Windows_Smart_Card_Framework_Card_Identifier"></span><span id="_windows_smart_card_framework_card_identifier"></span><span id="_WINDOWS_SMART_CARD_FRAMEWORK_CARD_IDENTIFIER"></span> Windows Smart Card Framework Card Identifier

If the smart card supports the GET DATA command, the Windows smart card framework expects the card to return a DER-TLV encoded byte array that is formatted in the following ASN.1 Structure.

``` syntax
CardID ::= SEQUENCE {
                   version Version DEFAULT v1,
                   vendor VENDOR,
                   guids GUIDS }

Version ::= INTEGER {v1(0), v2(1), v3(2)}
VENDOR ::= IA5STRING(SIZE(0..8))
GUID ::= OCTET STRING(SIZE(16))
GUIDS ::= SEQUENCE OF GUID
```

The Version member must be set to 0 (v1).

The VENDOR member must be set to “MSFT”.

The GUID member is a 16-byte GUID that uniquely identifies the card/application combination. This value is used to detect and load the appropriate smart card minidriver.

**Note**  The IHV or ISV that issues the application must create a unique GUID for its card/application combination.

 

 

 





