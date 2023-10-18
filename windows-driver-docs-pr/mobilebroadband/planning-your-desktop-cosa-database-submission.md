---
title: Planning your desktop COSA database submission
description: This topic contains information on adding a new APN to the baseline COSA database that ships with Windows desktop devices, or to update an existing APN.
ms.date: 10/18/2023
---

# Planning your desktop COSA database submission

This topic contains information on adding a new APN to the baseline COSA database that ships with Windows desktop devices, or to update an existing APN.

## The COSA database

COSA is made up of the following:

- 1 or more targets
- 1 SIM setting
- 1 or more connections or APN settings

Each COSA entry is also called a COSA profile.

For a given COSA profile, you can specify multiple targets (different MCC, MNC pair; different IMSI or ICCID range), and a list of APNs to try to connect to (5G APNs, Internet APN, IMS APN, an so on).

For logo and branding, you can only specify one per COSA entry. If you need to create different logo and branding, provide a different target for each COSA profile.

## The COSA update process

To connect to a mobile broadband network, the user is typically required to provide the following information:

- On GSM networks, an Access Point Name (APN) such as "data.contoso.com" is required.
- On CDMA networks, an access string that includes a special dial code such as "\#777" or a Network Access Identifier such as <somebody@contoso.com> is required.
- A username and password for the network connection.

The COSA connectivity database is updated by using Windows Update. The figure below shows the overall submission process.

:::image type="content" source="images/COSA_and_APN_database_submission_process_diagram.png" alt-text="Flowchart that shows the COSA database submission process.":::

For more info about the settings stored in the COSA database, see [Desktop COSA database settings](desktop-cosa-database-settings.md).

## Use the Mobile Operator Portal to make COSA upates

The Microsoft Mobile Operator Portal has replaced the previous APN spreasheet for making changed to the COSA database. The Mobile Operator Portal is a web-based tool that allows mobile operators to submit APN updates to the COSA database. The Mobile Operator Portal is available to all mobile operators that have a Microsoft representative.

## Create your account

If you don't yet have a Mobile Operator Portal account, follow these steps to create one.

1. Navigate to the [Microsoft Mobile Operator Portal](https://aka.ms/moconfig) (MO portal).
1. Select **Sign up now** below the **Sign in** button.
    :::image type="content" source="images/mo-portal-sign-in.png" alt-text="Screenshot of the sign-in screen on the Microsoft Mobile Operator portal.":::
1. Enter your email address and select **Send verification code**.
    :::image type="content" source="images/mo-portal-verify.png" alt-text="Screenshot of the create email verification screen on the Microsoft Mobile Operator portal.":::
1. After you receive the verification code in your email, enter it and select **Verify**.
1. Enter a temporary password and select **Create** to send your request to the Mobile Operator Portal team.
    :::image type="content" source="images/mo-portal-create-account.png" alt-text="Screenshot of the Microsoft Mobile Operator portal account creation page.":::
1. Send an email to your Microsoft representative to get your account approved for portal access.
    :::image type="content" source="images/mo-portal-account-queue.png" alt-text="Screenshot of the Microsoft Mobile Operator portal account creation queue message.":::
1. After getting confirmation from your Microsoft representative, navigate back to the [Mobile Operator Portal](https://aka.ms/moconfig) and select **Sign Up** again.
1. Verify your email, then enter a new non-temporary password and select **Create**. This is your login password going forward.

## Considerations when updating COSA

Changes provided by the OEM will take precedence over the default COSA database included in Windows.

The **Country/Region** and the **Operator** entries are used to determine whether this is an update to an existing APN or a request for a new APN. If the **Country/Region** and the **Operator** fields match content that already exists in the COSA database, the entries will be deleted and replaced with the entries that you submit through the Mobile Operator Portal.

>[!NOTE]
>Because the previous entries will be deleted, it is important to list all APNs for the **Operator** and **Country/Region** combination, including the ones that are not changing.

For example, when the following values are entered in a row in the spreadsheet:

```syntax
Operator: Contoso
Country/Region: Argentina
```

All entries currently in the COSA connectivity database that match the following format will be deleted and replaced with the information in your draft submission for that **Operator** and **Country/Region** combination:

```syntax
<Operator name="Contoso (Argentina)">
```

If the **Operator** and **Country/Region** entries do not match content that already exists in the COSA database, a new APN is created.

For example, if the following values are entered in a row in the spreadsheet:

```syntax
Operator: Contoso
Country/Region: Argentina
```

If it does not exist in the appropriate connectivity database, a new entry is added after your submission is accepted that looks like the following:

```syntax
<Operator name="Contoso (Argentina)">
```

- On each row of the spreadsheet that is submitted, you must specify only one of the following:
  - An MCC+MNC with a blank IMSI range
  - An MCC+MNC with a specific IMSI range
  - An MCC+MNC with a specific ICCID range
  - An MCC+MNC with a specific GSM provider name

- If you have created a website for setting up Mobile Broadband service, it is important to provide the Account Experience URL and certificate data.
- Access strings used for plan purchase (**Purchase Flag**=**Y**) can be one of the following:
  - For GSM networks, an APN with a specified **User Name** and **Password** used for purchasing the subscription.
  - For CDMA networks, a Network Access Identifier (NAI) is used for purchasing the subscription.

- Access strings used for Internet connectivity (**Connect Flag**=**Y**) can be one of the following:
  - For GSM networks, an APN with a specified **User Name** and **Password** used to connect to the Internet.
  - For CDMA networks, a Network Access Identifier (NAI) is used to connect to the Internet.

Once your spreadsheet is complete, you can test the APNs you’ve entered. For the next steps in testing your APN update, see [Testing your desktop COSA database submission](testing-your-desktop-cosa-apn-database-submission.md).

## Related topics

- [Submitting the desktop COSA database update](submitting-the-desktop-cosa-database-update.md)
- [Testing your desktop COSA database submission](testing-your-desktop-cosa-apn-database-submission.md)
- [Desktop COSA database settings](desktop-cosa-database-settings.md)
- [Mobile Operator Portal](https://aka.ms/moconfig)
