---
title: Desktop COSA/APN database settings
description: Desktop COSA/APN database settings
ms.assetid: 860B8587-1D70-466A-A6E7-836380AA4DFA
ms.author: windowsdriverdev
ms.date: 09/22/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Desktop COSA/APN database settings

This topic describes the settings available in desktop COSA and the APN database (apndatabase.xml).

For more info about the Desktop COSA/APN database submission process, see [Planning your desktop COSA/APN database submission](planning-your-desktop-cosa-apn-database-submission.md).

For more info about COSA, see [COSA overview](cosa-overview.md).

For more info about the APN database, see [APN database overview](apn-database-overview.md).

## APN database-only settings

The following settings in the spreadsheet apply to the APN database only. These entries will be used if you are targeting Windows 8, Windows 8.1, or versions of Windows 10 before Windows 10, version 1703.

| Setting name | Description | Optional or required | Notes |
| --- | --- | --- | --- |
| CDMA ProviderID | A 5-digit number that should match the CDMA provider ID (also called SID) reported by your device. | Optional |  |
| CDMA ProviderName | A string of no more than 36 characters that should match the CDMA provider name reported by your device. This setting is case sensitive. | Optional |  |
| CertIssuerName | The Cert Issuer Name of your signing certificate used for operator XML provisioning. | Optional | If specified, you must also specify the Cert Subject Name and Carrier GUID. |
| CertSubjectName | The Cert Subject Name of your signing certificate used for operator XML provisioning. | Optional | If specified, you must also specify the Cert Issuer Name and Carrier GUID. |
| Carrier GUID | The self-assigned GUID that is used in future operator XML provisioning packages. | Optional | If specified, you must also specify the Cert Subject Name and Cert Issuer Name. |
| GSM ProviderName | A string of no more than 36 characters that should match the GSM provider name reported by your device. This setting is case sensitive. | Optional | This setting is only supported on Windows 8.1 and versions of Windows 10 before Windows 10, version 1703. |
| Purchase | A yes or no value describing if the APN is provisioning or purchase. | Required | Possible values: <ul><li>**Y** – if the APN is provisioning or purchase</li><li>**N** – if the APN is not provisioning or purchase</li></ul> <p>If **Purchase Flag** setting is **Y**, the **Connect Flag** setting must be **N**.</p> |
| Connect | A yes or no value describing if the APN is provisioning or purchase. | Required | Possible values: <ul><li>**Y** – if the APN is provisioning or purchase</li><li>**N** – if the APN is not provisioning or purchase</li></ul> <p>If **Connect Flag** setting is **Y**, the **Purchase Flag** setting must be **N**.</p> |
| AutoConnectOrder | Windows tries connections to the APNs provided by the operator and marked as “auto-connect” in the APN database until it successfully connects to the mobile network. If all auto-connect attempts fail, Windows will show a prompt allowing the user to pick an APN or enter a custom APN. | Optional | If you have more than one access string for an operator, this setting must start with 1. This is needed for Windows to try several APN entries that share either an IMSI range, ICCID range, CDMA provider ID, or CDMA provider name when the user tries to connect. |

## APN database and desktop COSA settings

The following entries apply to both APN database and desktop COSA. All entries for COSA in this table are supported in Windows 10, version 1703 and later.

| Setting name | Description | Optional or required | Notes |
| --- | --- | --- | --- |
| UpdateType | Describes whether the APN Database entry is new or modified. | Required | Possible values: <ul><li>**Add** – A new entry</li><li>**Change** – Update an existing entry</li><li>**Keep** – Do not change the entry</li><li>**Delete** – Delete the entry</li></ul> |
| Country/Region | The country or region for the APN entry. | Required | We might change this entry to match how Windows refers to a particular country or region. |
| Operator | The name of the operator. You do not need to include the country or region in this field. | Required | Ensure you use the same spelling and capitalization each time you submit an update for your APN entries. |
| MCC | A 3-digit MCC value used for GSM IMSI submissions. | Optional for ICCID ranges. |  |
| MNC | A 2- or 3-digit MNC value used for GSM IMSI submissions. | Optional for ICCID ranges. |  |
| IMSI Range - Start | A 15-digit number that includes the MCC+MNC at the start of the number. | Optional | The number should end in 00. <p>If this setting and the **IMSIRange - End** setting is left blank but the **MCC** and **MNC** entries are specified, the entire MCC+MNC range is covered.</p> |
| IMSI Range - End | A 15-digit number that includes the MCC+MNC at the start of the number. | Optional | The number should end in 99. <p>If this setting and the **IMSI Range - Start** setting is left blank but the **MCC** and **MNC** entries are specified, the entire MCC+MNC range is covered.</p> |
| ICCID Range - Start | A 19- or 20-digit number that starts with 89 (the ICCID issuer identifier number). | Optional | The number should end in 00. |
| ICCID Range - End | A 19- or 20-digit number that starts with 89 (the ICCID issuer identifier number). | Optional | The number should end in 99. |
| AccountExperienceURL | Used by Windows Connection Manager if the user does not have an active plan and tries to connect to your network. | Optional | Helps improve the plan acquisition experience. |
| FriendlyName | A name for this APN entry that is understandable and meaningful to subscribers. | Optional | Appears in the Windows Connection Manager in cases where Windows cannot automatically connect to the network. |
| AccessString | For GSM networks, this is an APN such as data.contoso.com. For CDMA networks, this is an access string that includes a special dial code such as #777 or an Network Access Identifier such as example@contoso.com. | Required |  |
| UserName | The user name used to connect to your APN. This setting is case sensitive. | Optional |  |
| Password | The password used to connect to your APN. This setting is case sensitive. | Optional |  |
| AuthProtocol | Specifies the authentication protocol to be used for activating a Packet Data Protocol (PDP) context. | Optional | Possible values: <ul><li>**NONE** – No authentication protocol is required</li><li>**PAP** – PAP authentication is required.</li><li>**CHAP** – CHAP authentication is required.</li><li>**MsCHAPV2** –MSCHAPv2 is authentication is required.</li></ul> <p>This setting is only supported on Windows 8.1 and versions of Windows 10 before Windows 10, version 1703.</p> |
| Compression | Specifies if compression will be used at the data link for header and data transfer. | Optional | Possible values: <ul><li>**ENABLE** – Compression is enabled</li><li>**DISABLE** – Compression is not enabled</li></ul> <p>This setting is only supported on Windows 8.1 and versions of Windows 10 before Windows 10, version 1703.</p> |

## Desktop COSA-only settings

The following settings apply to desktop COSA only. These entries will be used if you are targeting Windows 10, version 1703 and later.

| Setting name | Description | Optional or required | Notes | Minimum supported Windows version |
| --- | --- | --- | --- | --- |
| SupportDataMarketplace | A true/false string describing whether the profile is supported by the data marketplace. | Optional | If left blank, defaults to "false." | Windows 10, version 1703 |
| SPN | An identifier string for the Service Provider Name (SPN) | Optional | Helps to identify the MO/MVNO's network. If left blank, defaults to empty string and does nothing. | Windows 10, version 1703 |
| AlwaysOn | Describes whether the connection is always on or not. | Required | If left blank, defaults to "true." | Windows 10, version 1703 |
| PurposeGroups | A string specifying the purposes of the connection by a comma-separated list of GUIDs representing purpose values. | Required | The following purpose values are available: <ul><li>**Internet**</li><li>**MMS**</li><li>**IMS**</li><li>**SUPL**</li><li>**Purchase**</li><li>**Administrative**</li><li>**Application**</li><li>**eSIM provisioning**</li></ul> <p> If left blank, defaults to "Internet."</p> | Windows 10, version 1703 |
| IPType | A string specifying the network protocol of the connection. | Optional | Possible values: <ul><li>IPv4</li><li>IPv6</li><li>IPv4v6</li></ul> <p>If left blank, defaults to "IPv4."</p> | Windows 10, version 1703 |
| BrandingName | The mobile broadband device typically provides the operator name, which Windows shows in the Windows Connection Manager. You can override this name by specifying a custom name in metadata. | Optional | If left blank, defaults to empty string and does nothing. | Windows 10, version 1709 |
| BrandingIcon | A custom logo that appears in the Windows Connection Manager next to your network entry. | Optional | Icons must have transparent backgrounds and smooth edges. They must also meet the following format and size requirements: <ul><li>256 x 256: 32-bit + Alpha</li><li>48 x 48: 32-bit + Alpha</li><li>48 x 48: 8-bit 256 color</li><li>48 x 48: 4-bit 16 color</li><li>32 x 32: 32-bit + Alpha</li><li>32 x 32: 8-bit 256 color</li><li>32 x 32: 4-bit 16 color</li><li>24 x 24: 32-bit + Alpha</li><li>24 x 24: 8-bit 256 color</li><li>24 x 24: 4-bit 16 color</li><li>16 x 16: 32-bit + Alpha</li><li>16 x 16: 8-bit 256 color</li><li>16 x 16: 4-bit 16 color</li></ul> | Windows 10, version 1709 |
| UseBrandingNameOnRoaming | Determines if the branding should be displayed during roaming or not roaming. | Optional | Possible values: <ul><li>**0** - Use only when connected to home network</li><li>**1** - Use when connected to home network and domestic roaming</li><li>**2** - Use when connected to home network, domestic roaming, and international roaming</li></ul><p> If left blank, defaults to 0.</p> | Windows 10, version 1709 |
| Roaming | Specifies the roaming conditions under which the connection should be activated. | Optional | Possible values: <ul><li>0: Home network only</li><li>1: All roaming conditions (home and roaming)</li><li>2: Home and domestic roaming only</li><li>3: Domestic roaming only</li><li>4: Non-domestic roaming only</li><li>5: Roaming only</li></ul> If left blank, defaults to 1 (all roaming conditions). | Windows 10, version 1709 |
| DataMarketplaceRoamingUIEnabled | Indicates whether roaming UI should be shown for this DataMarketPlace SIM. | Optional | | Windows 10, version 1709 |
| UIName | If the target condition values (SPN, MCC, MNC, IMSI Range, ICCID Range, etc.) can't indicate the unique entry, then COSA will display this name to the end user to enable manual selection of which MO's connection value to use. | Optional | For example, **ContosoMVNO** is an MVNO. It doesn't have any unique values that can be used to distinguish itself from the main MO network, **Contoso**. In this case, **UIName** can be used and will be shown in the Windows Settings UI, enabling the user to manually select which MO provisioning settings to use. | Windows 10, version 1709 |
| UIOrder | The index to control the **UIName** value's dropdown list picker position. | Required if **UIName** is specified; Optional otherwise | If not specified, defaults to **0**. | Windows 10, version 1709 |
| ESIM_PROV | A true/false string describing whether the profile is to be considered as an eSIM provisioning profile. | Optional | If left blank, defaults to "false." | Windows 10, version 1709 |
| AppID | A string describing the Package Family Name (PFN) and application ID of a mobile operator's UWP companion app. | Optional | In Windows 10, version 1803 and later, **AppID** is used to identify MOs with their companion apps. **AppID** must be declared in this format: <p>**PFN!AppId**</p><p>To obtain the PFN and AppId for your app, follow these steps:<ol><li>Acquire the PFN as specified on [View App Identity Details](https://docs.microsoft.com/windows/uwp/publish/view-app-identity-details).</li><li>Locate the AppId by opening your solution's *AppManifest.XML* file and querying the AppXManifest for the application ID.</li></ol> For more info about UWP companion apps for MOs, see [UWP mobile broadband apps](https://docs.microsoft.com/windows-hardware/drivers/mobilebroadband/windows-store-mobile-broadband-apps). | Windows 10, version 1803 |
| Hotspot | Determines if you want to permit users to share their mobile broadband connection as a personal hotspot. | Optional | Possible values: <ul><li>Never</li><li>Always</li><li>EntitlementCheckRequired</li></ul> <p>If left blank, defaults to "Always."</p> <p>The *EntitlementCheckRequired* option enables users to share their hotspots with an entitlement check, which requires a handler for Windows notification events. If this option is selected, you need to develop an MO UWP companion app to handle the entitlement check requests.</p> <p>For more info about UWP companion apps for MOs, see [UWP mobile broadband apps](https://docs.microsoft.com/windows-hardware/drivers/mobilebroadband/windows-store-mobile-broadband-apps).</p> | Windows 10, version 1803 |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
