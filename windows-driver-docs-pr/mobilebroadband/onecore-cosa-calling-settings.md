---
title: Onecore COSA calling settings
description: Onecore COSA calling settings
ms.assetid: D240FF14-F9B1-45C1-B47D-067C678727D8
ms.author: windowsdriverdev
ms.date: 06/30/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Onecore COSA calling settings

The tables in this section describe the calling settings available in Onecore COSA. 

## Branding information

| Setting name | Description | Optional or required | Notes |
| --- | --- | --- | --- |
| Branding Flags | A string that modifies the branding string and logo, if available, in the calling experience. | | |

## Phone settings

| Setting name | Description | Optional or required | Notes |
| --- | --- | --- | --- |
| Assisted Dial Setting | The default state for international assist. | | |
| Continuous DTMF Enabled | Enables DTMF tone duration for as long as the user presses a dialpad key. | | When disabled, a fixed length tone is emitted regardless of how long the user presses the dialpad key. |
| Call ID Match | Sets the global fallback for the number of digits that the OS will try to match against a contact for Caller ID. | | |
| Show Long Tones | Shows the Long Tones UI | | Default is 0 on GSM and 1 for CDMA devices. |
| Hide Call Forwarding | Hides the Call Forwarding UI. | | Default is 0 (always shown). |
| Use OK For USSD Dialogs | USSD Diaglog Button text. |  | Default behavior shows "close", 1 shows "OK". |
| VoLTE Audio Quality String | VoLTE call audio quality indicator text. | | <ul><li>Minimum length: 0</li><li>Maximum length: 10</li></ul> |
| Disable Voicemail Phone Number Display | Disables the display of the phone number below the Voicemail label in call progress dialog. | | Default is false. |

## Caller ID match overrides

| Setting name | Description | Optional or required | Notes |
| --- | --- | --- | --- |
| GEOID Override | Sets the regional override for this GEOID for the number of digits that the OS will try to match against a contact for Caller ID. | 

## Per-SIM settings

### Per-SIM general settings

| Setting name | Description | Optional or required | Notes |
| --- | --- | --- | --- |
| Ignore USSD Exclusions | Ignores USSD exclusions. | | Uses exclusion list if set to 0; otherwise the list is ignored. |
| USSD Exclusion List | The USSD exclusion list. | | |
| Ignore MWI Notifications | Configures the voicemail system so the phone either ignores or responds to Message Waiting Indicator (MWI) notifications. | | |
| Default Enable Video Calling | Configures the initial value for LTE video calling. | | |
| Show Video Calling Switch | Configures the phone settings CPL to show the video calling switch. | | |
| Suppress Video Calling Charges Dialog | Configures the phone settings CPL to suppress the video calling charges dialog. | | |
| Show Caller ID Network Default Setting | Indicates whether the Network Default setting can be allowed for Outgoing Caller ID. | | |
| Default Caller ID Setting | Configures the initial value for the Caller ID setting. | | Possible values: <ul><li>1: No one</li><li>2: Only contacts</li><li>3: Everyone</li><li>4: Network default</li></ul> If set to 4 (network default), make sure that **Show Caller ID Network Default Setting** is set to **true**. |
| Allow Video Conferencing | Configures the ability to conference video calls. | | |
| Wi-Fi Calling Operator Name | The branding operator name to show when the phone is under Wi-Fi calling. | | <ul><li>Mininum length: 0</li><li>Maximum length: 200</li></ul> |
| Reset Call Forwarding | Related to call forwarding settings. | | Default is false. When set to true, provides the user with an option to retry to retry a call forwarding settings query. If the query fails, attempts to set call forwarding to off. |

### Per-SIM critical settings

| Setting name | Description | Optional or required | Notes |
| --- | --- | --- | --- |
| MO SIM Fallback Voicemail Number | The SIM fallback voicemail number for the MO. | | |
| SIM Override Voicemail Number | The SIM override voicemail number. | | |

## Voicemail registration table

### Provider registration

| Setting name | Description | Optional or required | Notes |
| --- | --- | --- | --- |
| Provider | MCC/MNC mapping. | | The value stored here will be the key for the table. |

### Settings for provider

| Setting name | Description | Optional or required | Notes |
| --- | --- | --- | --- |
| CLSID Provider | The CLSID provider. | | |
| CLSID Accessor | The CLSID accessor. | | |
| Protocol Variant | The protocol variant. | | |
| Incoming Port | The incoming port. | | |
| Client Type | The client type. | | |
| Device Type | The device type. | | |
| Initial SMS Destination Number | The initial SMS destination number. | | |
| Encrypted SMS Supported | Whether encrypted SMS is supported. | | |
| Key Data | Data for the table's key. | | |
| IMAP Port Override | The override for the IMAP port. | | |
| Token Login | Token login. | | |
| Suppress SSL | Whether to suppress SSL or not. | | |
| Ignore Legacy Notifications | Ignores legacy notifications. | | |
| Branding | The visual voicemail branding. | | <ul><li>Minimum length: 0</li><li>Maximum length: 50</li></ul> |

## Partner app support

| Setting name | Description | Optional or required | Notes |
| --- | --- | --- | --- |
| Partner Immediate Dial Strings | The partner immediate dial strings. | | |
| Partner Non-Immediate Dial Strings | The partner non-immediate dial strings. | | |

## Supplementary service code overrides

| Setting name | Description | Optional or required | Notes |
| --- | --- | --- | --- |
| Service Code Override | Enables overriding this service code and mapping to a different number. | | |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")