---
title: Submitting a desktop COSA database update
description: Submit APN entries to Microsoft by following the steps in this topic and using the Mobile Operator Portal.
ms.date: 10/24/2023
---

# Submitting a desktop COSA database update

>[!IMPORTANT]
> The following steps to submit an APN update apply to both desktop COSA, which is used for Windows 10, version 1703 and later, and apndatabase.xml, which is used for Windows 8, Windows 8.1, and versions of Windows 10 before 1703. Microsoft will convert apndatabase.xml submissions to COSA if you are targeting Windows 10, version 1703 or later.

Now that you’ve tested the APN entries, it’s now time to submit them to Microsoft by following the steps in this topic.

## The COSA database

COSA is made up of the following:

- 1 or more targets
- 1 SIM setting
- 1 or more connections or APN settings

Each COSA entry is also called a COSA profile.

For a given COSA profile, you can specify multiple targets (different MCC, MNC pair; different IMSI or ICCID range), and a list of APNs to try to connect to (5G APNs, Internet APN, IMS APN, an so on).

For logo and branding, you can only specify one per COSA entry. If you need to create different logo and branding, provide a different target for each COSA profile.

## Adding a new target

For example, the mobile operator has a new MCC, MNC pair that they want to add to the COSA profile.

1. Open the correct profile you want to modify, if you have more than one profile, ensure you are modifying the right profile.

    :::image type="content" source="images/mobile-operator-portal-select-profile.png" alt-text="Screenshot of the Mobile Operator Portal select profile screen.":::

    - (Optional) Check your profile APN values
        1. Open **Connections > Cellular > Connection**
        1. Make sure it's the right APN. You can have multiple connections if you have more than one APN value for this COSA profile.

        :::image type="content" source="images/mobile-operator-portal-check-apn-values.png" alt-text="Screenshot of the Mobile Operator Portal connection screen.":::

    - (Optional) Check that your MCC, MNC pair does not exist in the current target list
        1. Open **Targets**
        1. Check each target to ensure there's no duplicate of what you want to create. If you see more than one target, check each of them one by one.

        :::image type="content" source="images/mobile-operator-portal-target.png" alt-text="Screenshot of the Mobile Operator Portal targets screen.":::

1. Select **+** to add a new target to your profile, and go to the new target added to your list. This is usually the last one in the **Targets** list. If you do not see any new targets, make sure you have clicked on the drop down beside the **Targets**.

    :::image type="content" source="images/mobile-operator-portal-add-new-target.png" alt-text="Screenshot of the Mobile Operator Portal add new target form.":::

1. Select **Save draft**, add a note, then select **Save**.

    :::image type="content" source="images/mobile-operator-portal-save-draft.png" alt-text="Screenshot of the Mobile Operator Portal save draft dialog box.":::

## Modify an existing target  <!-- !!! -->

This section demonstrates how to change an MCC, MNC value pair, add or change SPN, PNN, GID1, ICCID, or IMSI range.

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

1. Navigate to **Cellular > PerSimSettings > SettingsForSim**, then either:

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

## Update APN, other connection settings

1. Open the correct profile you want to modify. If you have more than one profile, make sure you are modifying the correct profile.

    - (Optional) Check your profiles' APN values.
    - (Optional) Check that your MCC, MNC pair does not exist in the current target list.

1. Look for the connection you want to modify, then modify any of the values there.
1. Select **Save draft**, add a note, then select **Save**.

## Related content

- [COSA overview](cosa-overview.md)
- [COSA database](cosa-database.md)
- [Desktop COSA database settings](desktop-cosa-database-settings.md)
- [Mobile Operator Portal](https://aka.ms/moconfig)
- [Planning your desktop COSA database submission](planning-your-desktop-cosa-database-submission.md)
- [Testing your desktop COSA database submission](testing-your-desktop-cosa-database-submission.md)
