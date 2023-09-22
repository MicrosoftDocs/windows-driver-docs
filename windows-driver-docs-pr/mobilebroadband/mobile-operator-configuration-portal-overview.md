---
title: Mobile operator configuration portal
description: This article introduces the mobile operator configuration portal to create a COSA database submission.
author: mhopking-msft
ms.author: mhopkins
ms.date: 09/21/2023
---

# Mobile operator configuration portal

This article introduces the mobile operator configuration portal to create a COSA database submission.

## Setting up your account

1. Go to the [mobile operator portal](https://aka.ms/moconfig).
1. Select **Sign up now**.
1. Enter your email in the first field and select **Send verification code**.
1. Check your email, enter the verification code and select **Verify**.
1. Enter a temporary password and select **Create** to send your request official to the mobile operator portal team.
1. Send email to your Microsoft representative to get your account approved for portal access.
1. After getting confirmation from your Microsoft representative, go thru and select **Sign Up** again, verify your email, then put a new password and select **Create**. This time around, this will be your permanent password for logging in.

## Introduction to COSA

COSA is made up of:

- One or more targets
- One SIM setting
- One or more connections or Access Point Name (APN) settings

Each COSA entry is also called a COSA profile. For a given COSA profile, you can specify multiple targets (different MCC, MNC pair; different IMSI or ICCID range); and a list of APNs to try to connect to (5G APNs, Internet APN, IMS APN, and so on).

However, for logo and branding, you can only specify one per COSA entry. If the desire is to create different logo and branding, you need to provide a different target for each COSA profile.

COSA profile order:

## Adding a new target

For example, the mobile operator has a new MCC, MNC pair that they want to add to the COSA profile.

1. Open the correct profile you want to modify, if you have more than 1 profile, ensure you are modifying the right profile.
    - (Optional) Check your profile APN values
        1. Open Connections -> Cellular -> Connection
        1. Make sure it's the right APN. You can have multiple connections if you have more than one APN value for this COSA profile.

    - (Optional) Check that your MCC, MNC pair does not exist in the currect target list
        1. Open **Targets**
        1. Check each target to ensure there's no duplicate of what you want to create. If you see more than one target, check each of them one by one.

1. Select **+** to add a new target to your profile, and go to the new target added to your list. This is usually the last one in the **Targets** list. If you do not see any new targets, make sure you have clicked on the drop down beside the **Targets**.

1. Select **Save draft**, add a note, then select **Save**.
 
## Modify and existing target or targets

1. Open the correct profile you want to modify. If you have more than one profile, make sure you are modifying the correct profile.

    - (Optional) Check your profiles' APN values.
    - (Optional) Check that your MCC, MNC pair does not exist in the current target list.

1. Look for the target you want to modify, then either:

    - Modify MCC / MNC
    - Add SPN, PNN, GID1, ICCID range, IMSI range
    - Modify SPN, PNN, GID1, ICCID range, IMSI range

1. Select **Save draft**, add a note, then select **Save**.

## Modify SIM branding

1. Open the correct profile you want to modify. If you have more than one profile, make sure you are modifying the correct profile.

    - (Optional) Check your profiles' APN values.
    - (Optional) Check that your MCC, MNC pair does not exist in the current target list.

1. Navigate to **Cellular** -> **PerSimSettings** -> **SettingsForSim**, then either:

    - Add or remove mobile operator logo
    - Define **AccountExperienceURL** or add a **AppID** to automatically install applications
    - Change **BrandingName** associated with your SIM card and when this will be used
    - Specify when **BrandingName** will also be used
 
    Here is the list of possible settings:

    - **AccountExperienceURL** - The Web URL for the mobile operator's MBB user account experience. If both AppID and AccountExperienceURL are specified, AppID gets higher precedence and UX will not display the AccountExperienceURL.

    - **AppID** - The package family name (PFN) and application ID of a mobile operator's UWP companion app.
    
    - **BrandingName** - The name for the mobile operator to be displayed on the UX. If no information is provided, UX will display the HomeProviderName

    - **UseBrandingNameOnRoaming** - When the **BrandingName** will be used.
    
        - Use only when connected to Home network
        - Use when connected to Home network and Domestic roaming
        - Use when connected to Home network, Domestic roaming and International roaming

    See [Desktop COSA-only settings](desktop-cosa-apn-database-settings.md#desktop-cosa-only-settings) for more information on **BrandingIcon**. 

    Branding Icon - a custom logo that appears in the Windows Connection Manager next to your network entry.

    Requirements:

    - Icons must have transparent backgrounds and smooth edges. Test the icon with both light and dark themes. Icons must also meet the following format and size requirements:

        - 256 x 256: 32-bit + Alpha
        - 48 x 48: 32-bit + Alpha
        - 48 x 48: 8-bit 256 color
        - 48 x 48: 4-bit 16 color
        - 32 x 32: 32-bit + Alpha
        - 32 x 32: 8-bit 256 color
        - 32 x 32: 4-bit 16 color
        - 24 x 24: 32-bit + Alpha
        - 24 x 24: 8-bit 256 color
        - 24 x 24: 4-bit 16 color
        - 16 x 16: 32-bit + Alpha
        - 16 x 16: 8-bit 256 color
        - 16 x 16: 4-bit 16 color

1. Select **Save draft**, add a note, then select **Save**.

## Add a new APN

1. Open the correct profile you want to modify. If you have more than one profile, make sure you are modifying the correct profile.

    - (Optional) Check your profiles' APN values.
    - (Optional) Check that your MCC, MNC pair does not exist in the current target list.

1. Select **+** beside **Cellular** and look for the new **Connection** added to your list. This is usually the last one in the **Targets** list.

    - Add the APN values. If you do not see a new **Connection**, make sure you have clicked on the drop down beside the **Cellular**.

    Common APN settings:

    - **AccessPointName** – In GSM networks, Access Point Name (APN) such as "data.contoso.com"
    - **AlwaysOn** – Automatically connect and stay connected until the user manually disconnects.
    - **AutoConnectOrder** – The order of which APN to test first. If nothing is specified, Windows picks the order randomly.
    - **FriendlyName** – An easy to understand description of this APN entry for example "Prepaid APN" or "Postpaid APN", Windows will show that instead of technical APN name to the end user. This will help to simplify the user experience.
    - **IPType** – Which IP type is supported - IPv4, IPv6, IPv4v6.
    - **PurposeGroup** – How this APN will be used.
 
        | Setting | Description |
        |--|--|
        | Internet | Used for general Internet traffic. (default) |
        | IMS | Used for IMS traffic. (LTE attach) |
        | eSIM provisioning | Used for eSIM traffic. |
 
        You can put more than one purpose in a comma delimited list.

   - **Roaming** – The roaming conditions under which the connection should be activated. 

        | Setting | Description |
        |--|--|
        | Disallowed | Home network only |
        | Allowed (default) | All roaming conditions (home and roaming) |
        | DomesticRoaming | Home and domestic roaming only |
        | UseOnlyForDomesticRoaming | Domestic roaming only |
        | UseOnlyForNonDomesticRoaming | Non-domestic roaming only |
        | UseOnlyForRoaming | Roaming only |

    (optionally, if you require username/password)
    - **AuthType** - The Auth Protocol element specifies the authentication protocol to be used for activating a Packet Data Protocol (PDP) context.

        | Setting | Description |
        |--|--|
        | None | No authentication protocol is required. (default) |
        | PAP | PAP authentication protocol is required. |
        | CHAP | Challenge Handshake Authentication Protocol(CHAP) protocol is required. |

    - **Username** – The case sensitive user name to connect to your APN.
    - **Password** – APN connection password. Can be set to blank.

     The rest of the settings can be left blank or at their default value.

1. Select **Save draft**, add a note, then select **Save**.

## Update APN, other connection settings

1. Open the correct profile you want to modify. If you have more than one profile, make sure you are modifying the correct profile.

    - (Optional) Check your profiles' APN values.
    - (Optional) Check that your MCC, MNC pair does not exist in the current target list.

1. Look for the Connection you want to modify, then modify any of the values there.
1. Select **Save draft**, add a note, then select **Save**.

## Creating a test package

Test packages are generated from the server. You must save all changes before you download a test package. If the settings were not saved as draft, your test package will not have your latest settings.

1. Choose the right Windows version.

    - Run **winver** on the PC you want to test to check your Windows version.

1. Choose the right test package to download. 
 
    - In my case, since I have 21H1, I would choose Latest Version

1. Follow the steps in [Test your submission for desktop COSA](testing-your-desktop-cosa-apn-database-submission.md#test-your-submission-for-desktop-cosa) to test your COSA package file.

    > [!NOTE]
    > Open an administrator command prompt. If you are running in S-mode, you will need to switch out of S-mode first.

## Related content

- [COSA overview](cosa-overview.md)
- [COSA database](cosa-database.md)
