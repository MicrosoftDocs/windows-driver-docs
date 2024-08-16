---
title: Microsoft Mobile Operator Configuration Portal Guide
description: This article introduces the mobile operator configuration portal to create a COSA database submission.
ms.date: 08/16/2024
author: mhopkins-msft
ms.author: mhopkins
---
# Microsoft mobile operator configuration portal guide

This article introduces the Microsoft mobile operator configuration portal to create COSA database submissions.

The mobile operator configuration portal has replaced the previous APN spreadsheet for making changes to the COSA database. The mobile operator configuration portal is a web-based tool that allows mobile operators to submit APN updates to the COSA database. The mobile operator configuration portal is available to all mobile operators that have a Microsoft representative.

## Create your account

If you don't yet have a mobile operator configuration portal account, follow these steps to create one.

1. Start by reaching out to your Microsoft representative (Premier Support, Windows Ecosystem Enablement PM, Surface, etc.) and inform them you intend to onboard to the MO Configuration portal. You'll need to work with them to complete your MOCP onboarding.
   If you do not have a Microsoft representative, contact Microsoft Support by calling (800) MICROSOFT (642-7676).
2. Navigate to the [Microsoft mobile operator configuration portal](https://aka.ms/moconfig) (MO portal).
3. Select **Sign up now** below the **Sign in** button.
4. Enter your email address and select **Send verification code**.
5. After you receive the verification code in your email, enter it and select **Verify**.
6. Enter a temporary password and select **Create** to send your request to the mobile operator configuration portal team.
7. Send an email to your Microsoft representative to get your account approved for portal access.
8. After getting confirmation from your Microsoft representative, navigate back to the [mobile operator configuration portal](https://aka.ms/moconfig) and select **Sign Up** again.
9. Verify your email, then enter a new non-temporary password and select **Create**. This is your sign-in password going forward.

## Introduction to COSA

COSA is made up of the following:

- Targets: These are the network / SIM identifiers Windows uses to match COSA
  settings to a device.
- One SIM setting: These are settings Windows uses to change the experience such as branding, icons, and
  account management.
- One or more connections: These are settings that specify how the device connects to the network. This
  includes the APN, and APN related settings

Each COSA entry is also called a COSA profile.

For a given COSA profile, you can specify multiple targets (different *MCC, MNC* pair; different IMSI or ICCID range), and a list of APNs to try to connect to (5G APNs, Internet APN, IMS APN, and so on).

For logo and branding, you can only specify one per COSA entry. If you need to add a second logo or branding, you'll need to create a new COSA entry with a different target. For instance, if you'd like a specific range of ICCIDs to have a different logo and branding, please create a second COSA profile specifying the new target and updated logo and branding. Don't forget to fill out the connection settings as well, even if the same APN is used.

## Creating a new draft

The MO Config Portal uses drafts to handle changes to COSA.
After logging into the MOCP, you'll find yourself on the draft management page.
Here, you can create a new draft to start reviewing and modifying  COSA settings.

1. Sign into the [Microsoft mobile operator configuration portal](https://aka.ms/moconfig).
2. Select **New draft**.
3. Fill out the fields labeled **Title**, **Description**, and **Background**. To the best of your knowledge at this time. You'll have an opportunity to update these fields again before submitting.

## Modifying a draft

Once a draft has been created, you can start editing. Select the draft you'd like to modify. On the right side of the page, the draft metadata is populated. Here, you can modify the drafts **Description** and **Background** fields. When you're ready to make changes to COSA, select **Open draft** . This brings you to the COSA editing page.

On the left side of the COSA editing page is the COSA profile menu. This menu should list the COSA profiles tied to your MO.  You can also create a new profile by selecting **New profile.** If you believe you should see a profile not currently listed, please reach out to [MOPortalSupport@microsoft.com](mailto:MOPortalSupport@microsoft.com).

Selecting a profile from the left menu opens that profile for editing. The menu on the left shows the different types of settings available to be edited.

To change the name of the profile, you can select the three dots to the right of the profile's name.

Remember to select **Save draft** periodically to save your changes. From this page, you can also Create a test package, to test your changes. When you're ready to submit, you can submit your changes.

## Add a new target

This section demonstrates how to add a new *MCC, MNC* pair to your COSA profile.

1. Open the correct profile you want to modify. If you have more than one profile, ensure you're modifying the right profile.

   - Check your profile APN values (optional)

     1. Open **Connections > Cellular > Connection**
     2. Make sure it's the right APN. You can have multiple connections if you have more than one APN value for this COSA profile.
   - Check that your *MCC, MNC* pair doesn't exist in the current target list (optional)

     1. Open **Targets**
     2. Check each target to ensure there's no duplicate of what you want to create. If you see more than one target, check each of them one by one.
2. Select **+** to add a new target to your profile, and go to the new target added to your list. This is usually the last one in the **Targets** list. If you don't see any new targets, make sure you click on the drop-down beside the **Targets**.
3. Select **Save draft**, add a note, then select **Save**.

## Modify an existing target

This section demonstrates how to change an *MCC, MNC* value pair, add or change SPN, PNN, GID1, ICCID, or IMSI range.

1. Open the correct profile you want to modify. If you have more than one profile, make sure you're modifying the correct profile.

   - Check your profile APN values. (optional)
   - Check that your *MCC, MNC* pair doesn't exist in the current target list. (optional)
2. Look for the target you want to modify, then either:

   - Modify the *MCC, MNC*.
   - Add SPN, PNN, GID1, ICCID range, IMSI range.
   - Modify SPN, PNN, GID1, ICCID range, IMSI range.
3. Select **Save draft**, add a note, then select **Save**.

## Modify SIM branding

1. Open the correct profile you want to modify. If you have more than one profile, make sure you're modifying the correct profile.

   - Check your profiles' APN values. (optional)
   - Check that your *MCC, MNC* pair doesn't exist in the current target list. (optional)
2. Navigate to **Cellular > PerSimSettings > SettingsForSim**, then either:

   - Add or remove a mobile operator logo.
   - Define the **AccountExperienceURL** or add an **AppID** to automatically install applications.
   - Change the **BrandingName** associated with your SIM card and when this will be used.
   - Specify when **BrandingName** will also be used.

   Here's the list of possible settings:

   - **AccountExperienceURL** - The Web URL for the mobile operator's MBB user account experience. If both **AppID** and **AccountExperienceURL** are specified, **AppID** gets higher precedent and the **AccountExperienceURL** won't display.
   - **AppID** - The package family name (PFN) and application ID of a mobile operator's companion app.
   - **BrandingName** - The name for the mobile operator to be displayed on the UX. If no information is provided, the **HomeProviderName** is displayed.
   - **UseBrandingNameOnRoaming** - When the **BrandingName** will be used.

     - Use only when connected to the home network.
     - Use when connected to the home network and domestic roaming.
     - Use when connected to the home network, domestic roaming, and international roaming.
   - **BrandingIcon** - A custom logo that appears in the Windows Connection Manager next to your network entry. See [Desktop COSA database settings](desktop-cosa-database-settings.md) for more information on **BrandingIcon**.

   Requirements:

   - Icons must have a transparent background and smooth edges.
   - Test the icon with both light and dark themes.
   - Icons must meet the following format and size requirements:

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
3. Select **Save draft**, add a note, then select **Save**.

## Add a new APN

1. Open the correct profile you want to modify. If you have more than one profile, make sure you're modifying the correct profile.

   - Check your profiles' APN values. (optional)
   - Check that your *MCC, MNC* pair doesn't exist in the current target list. (optional)
2. Select **+** beside **Cellular** and look for the new **Connection** added to your list. This is usually the last one in the **Targets** list.

   - Add the APN values. If you don't see a new **Connection**, make sure you have clicked on the drop-down next to **Cellular**.

   Common APN settings:

   - **AccessPointName** – In GSM networks, Access Point Name (APN) such as "data.contoso.com"
   - **AlwaysOn** – Automatically connect and stay connected until the user manually disconnects.
   - **AutoConnectOrder** – The order of which APN to test first. If nothing is specified, Windows picks the order randomly.
   - **FriendlyName** – An easy to understand description of this APN entry for example "Prepaid APN" or "Postpaid APN". Windows shows the **FriendlyName** instead of the APN name to simplify the end user experience.
   - **IPType** – Which IP type is supported - IPv4, IPv6, IPv4v6.
   - **PurposeGroup** – How this APN is used.


     | Setting           | Description                                  | GUID                                 |
     | ------------------- | ---------------------------------------------- | -------------------------------------- |
     | Internet          | Used for general Internet traffic. (default) | 3E5545D2-1137-4DC8-A198-33F1C657515F |
     | MMS               |                                              | 53E2C5D3-D13C-4068-AA38-9C48FF2E55A8 |
     | IMS               | Used for IMS traffic. (LTE attach)           | 474D66ED-0E4B-476B-A455-19BB1239ED13 |
     | SUPL              |                                              | 6D42669F-52A9-408E-9493-1071DCC437BD |
     | eSIM Provisioning | Used for eSIM bootstrap connectivity.        | a36e171f-2377-4965-88fe-1f53eb4b47c0 |

     You can put more than one purpose in a comma delimited list.
   - **Roaming** – The roaming conditions under which the connection should be activated.


     | Setting                      | Description                               |
     | ------------------------------ | ------------------------------------------- |
     | Disallowed                   | Home network only                         |
     | Allowed (default)            | All roaming conditions (home and roaming) |
     | DomesticRoaming              | Home and domestic roaming only            |
     | UseOnlyForDomesticRoaming    | Domestic roaming only                     |
     | UseOnlyForNonDomesticRoaming | Non-domestic roaming only                 |
     | UseOnlyForRoaming            | Roaming only                              |

   Optionally, if you require a username and password:

   - **AuthType** - The Auth Protocol element specifies the authentication protocol to be used for activating a Packet Data Protocol (PDP) context.


     | Setting | Description                                                             |
     | --------- | ------------------------------------------------------------------------- |
     | None    | No authentication protocol is required. (default)                       |
     | PAP     | PAP authentication protocol is required.                                |
     | CHAP    | Challenge Handshake Authentication Protocol(CHAP) protocol is required. |
   - **Username** – The case sensitive user name to connect to your APN.
   - **Password** – APN connection password. Can be set to blank.

   The rest of the settings can be left blank or at their default value.
3. Select **Save draft**, add a note, then select **Save**.

## Update APN, other connection settings

1. Open the correct profile you want to modify. If you have more than one profile, make sure you're modifying the correct profile.

   - Check your profiles' APN values. (optional)
   - Check that your *MCC, MNC* pair doesn't exist in the current target list. (optional)
2. Look for the Connection you want to modify, then modify any of the values there.
3. Select **Save draft**, add a note, then select **Save**.

## Specify an APN to be used for a hotspot connection

1. Add a new connection and set its APN.
2. Set the Purpose Group to the Internet GUID listed above.
3. Set **AlwaysOn** to disabled.
4. Fill in the **FriendlyName**, **IPType**, and any other relevant settings.
5. Navigate to **HotSpot** on the left menu.
6. Set **Enabled** to **True**.
7. Set **DedicatedConnections** to the name of your APN's connection. You can find this by clicking on **Connections** and then **Cellular** on the left menu. Find the connection that contains the APN you'd like to set for your hotspot. The name of the connection is the text in **bold** following the string "Connection - ". For example, an MO in the United States may have a connection name that looks like "Contoso (United States)_i0$(_MVID)@WAP"
8. Fill out any other relevant fields under **HotSpot**.
9. Select **Save draft**, add a note, then select **Save**.

## Create a test package

Test packages are generated from the server. You must save all changes before you download a test package. If the settings aren't saved as a draft, your test package won't have your latest settings.

1. Choose the Windows version.

   - Run **winver** on the PC you want to test to check your Windows version.
2. Choose the test package to download.
3. Follow the steps in [Test your submission for desktop COSA](testing-your-desktop-cosa-database-submission.md#test-your-submission-for-desktop-cosa) to test your COSA package file.

   > [!NOTE]
   > Open an administrator command prompt. If you are running in S-mode, you will need to switch out of S-mode first.
   >

## Making a submission

Once you've made your changes and tested your submission using the instructions above, you're ready to submit your change.

Start by clicking on the **submit** button at the bottom of your draft. Remember, Microsoft won't test your
changes with your network. The MO *must* confirm that the settings are accurate and work as expected.

Update the fields on the submission box to the latest information. Provide as much detail as possible to reduce any friction during reviewal. In the **Background** field, confirm that the submission has been
tested. If you aren't* an MO, confirm that you have written approval from the MO to make changes to their COSA settings and approval of the specific changes.

For non-MOs (OEMs, IHVs, vendors, etc.) please work with your Microsoft representative to provide written verification from the MO that you have approval to make COSA changes on their behalf.

## Viewing submission status

Once a submission has been made, you can view the status of your submissions from the **Submissions** page. From this page you can see a table of both your active submissions and all previous submissions.

Active submissions are in the **Pending** state. Once a submission is reviewed, its state is updated to either **Accepted** or **Rejected** and will be moved to the previous submissions table.

Selecting an active submission shows the submission metadata on the right side of the page. Active submissions can be modified or discarded before being reviewed. You can modify an active submission by
selecting the submission and selecting **Open submission** at the bottom of the page. Active submissions can be discarded by selecting the submission and selecting **Discard submission**.

During review, the COSA review team might choose to send a message back to the submitter through the MOCP. Submissions with comments from the review team will have a red exclamation mark next to them. Selecting a
submission with comments from the review team will display the comments with the submission metadata on the right side of the page.

## Related content

- [COSA overview](cosa-overview.md)
- [COSA database](cosa-database.md)
- [Desktop COSA database settings](desktop-cosa-database-settings.md)
- [Mobile operator portal](https://aka.ms/moconfig)
- [Planning your desktop COSA database submission](planning-your-desktop-cosa-database-submission.md)
- [Testing your desktop COSA database submission](testing-your-desktop-cosa-database-submission.md)
