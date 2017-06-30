---
title: Planning your Onecore COSA submission
description: Planning your Onecore COSA submission
ms.assetid: 0D06718B-DC18-4E6C-8B0E-6B02D7395529
ms.author: windowsdriverdev
ms.date: 06/27/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Planning your Onecore COSA submission

Use this topic when you are planning to add a new APN to the baseline COSA database that ships with Windows Onecore platform devices, or update an existing one. Onecore COSA is available starting in Windows 10, version 1709. If you are submitting for desktop COSA, see [Planning your desktop COSA/APN database submission](planning-your-desktop-cosa-apn-database-submission.md).

Submitting a new APN or an APN update for Onecore COSA follows the same procedure as desktop COSA except that there are many more settings available in Onecore COSA than desktop COSA, which focused only on data-only settings. The tables in this topic describe all available settings for Onecore COSA.

## Calling settings

### BrandingInformation

| Setting name | Description | Optional or required | Notes |
| --- | --- | --- | --- |
| Branding Flags | A string that modifies the branding string and logo, if available, in the calling experience. | | |

### PhoneSettings

| Setting name | Description | Optional or required | Notes |
| --- | --- | --- | --- |
| Assisted Dial Setting | The default state for international assist. | | |
| Continuous DTMF Enabled | Enables DTMF tone duration for as long as the user presses a dialpad key. | | When disabled, a fixed length tone is emitted regardless of how long the user presses the dialpad key. |
| Call ID Match | Sets the global fallback for the number of digits that the OS will try to match against a contact for Caller ID. | | |
| Show Long Tones | Shows the Long Tones UI | | Default is 0 on GSM and 1 for CDMA devices. |
| Hide Call Forwarding | Hides the Call Forwarding UI. | | Default is 0, always shown. |
| Use OK For Ussd Dialogs | USSD Diaglog Button text. |  | Default behavior shows "close", 1 shows "OK". |
| VoLTE Audio Quality String | VoLTE call audio quality indicator text. | | Minimum length = 0, maximum length = 10. |
| Disable Voicemail Phone Number Display | Disables the display of the phone number below the Voicemail label in call progress dialog. | | Default is false. |

### CallIDMatchOverrides

| Setting name | Description | Optional or required | Notes |
| --- | --- | --- | --- |
| GEOID | Sets the regional override for this GEOID for the number of digits that the OS will try to match against a contact for Caller ID. | 


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")