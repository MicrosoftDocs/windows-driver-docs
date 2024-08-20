---
title: Planning your Desktop COSA Database Submission
description: Use this article plan for adding a new APN to the baseline COSA database that ships with Windows desktop devices, or to update an existing APN.
ms.date: 08/16/2024
author: mhopkins-msft
ms.author: mhopkins
---

# Planning your desktop COSA database submission

> [!IMPORTANT]
> Starting in Windows 10, version 1703, the APN spreadsheet (apndatabase.xml) is replaced by the Country and Operator Settings Asset (COSA) database. Windows 8, Windows 8.1, and versions of Windows 10 before version 1703 will continue to use the APN database while Windows 10, version 1703 and later use COSA. For more information about COSA, see [COSA overview](cosa-overview.md).

Use this article plan for adding a new APN to the baseline COSA database that ships with Windows desktop devices, or to update an existing APN.

## The COSA update process

:::image type="content" source="images/cosa_submission_process.png" alt-text="COSA update process":::

## Use the Microsoft mobile operator portal

The Microsoft mobile operator configuration portal (MOCP) is a web-based tool that allows mobile operators (MOs) to submit APN updates to Microsoft. The MOCP is used to submit APN updates for the COSA database. For more information about the MOCP, see the [Microsoft mobile operator configuration portal](https://aka.ms/moconfig).

For more information about the mobile operator portal, see the [Mobile operator configuration portal guide](mobile-operator-configuration-portal-guide.md).

## Mobile operators make changes to their own COSA profile

COSA is a database of mobile network device provisioning settings. These settings are properties of the Mobile Network Operators. As such, Windows views these settings as properties of the Mobile Network Operators and only permits the changing of COSA settings by or with expressed written permission from the Mobile network operator (or Mobile virtual network operator). OEMs, IHVs, or other entities looking to make changes to COSA must provide written verification from the MO that they approve of the changes made by the entity making them.

## Mobile operators are responsible for validating their changes

As part of the COSA update process, Microsoft does not test or validate the changes to COSA with the respective mobile network. Mobile operators must test and confirm the functionality of each change before submitting.

## COSA submission reviewal process

Microsoft performs a review of every COSA change submitted through the MO Config Portal. At that time, Microsoft will evaluate the submission based on:

- A visual inspection of the changes
- Confirmation from the submitter that the changes have been tested and confirmed to work as expected
- In cases where a non-MO has submitted a COSA change, Microsoft will look for written verification from the MO that the change is approved to be submitted by the submitter. Please work with your Microsoft contact (CSS, WE2, Surface, etc.) to provide this information.

If Microsoft determines that the requested change is in good standing condition and ready to be serviced into Windows. Microsoft will approve the change and submit it to be serviced in the next possible "D" release. A Windows "D" release, is the release of windows on the 4th week of the month. COSA submissions are reviewed ~6 weeks before a release. For example, if an MO is targetting a COSA change to be serviced to Windows in October. The COSA change should be submitted by the second week of September. The submitter will see the submission in their MOCP account updated to show a status of "Approved".

If the requested change is not found to meet the above criteria, Microsoft will reject the submission. If rejected, the submitter will see the submission in their MOCP account updated to show a status of "Rejected". The submission may also contain a message from the COSA review team containing an explanation for the rejection and recommended next steps. Microsoft will NOT send e-mail notifications to the submitter. Submitter must view status updates form the MOCP.

### COSA database considerations

- The operator identification data is stored in the COSA database as encoded Hardware IDs.
  - For GSM networks, you can have a separate database entry for each unique combination of MCC/MNC pair. If you are a Mobile Virtual Network Operator (MVNO) and do not have a unique MCC/MNC pair, you can specify one or more ranges of IMSIs or SIM ICC IDs currently leased from a Mobile Network Operator (MNO).

- The auto-connect order must be unique for the **Operator** and **Country/Region** combination with the same IMSI, ICCID range, CDMA provider name, or CDMA provider ID value.

  For example, if Contoso had four APNs for MCC+MNC value 100 101, it would list each APN entry in a new row in the spreadsheet and number the auto-connect order starting with 1 up to 4 for each of those four entries because they share the same IMSI range. If Contoso had another set of APNs for MCC+MNC value 100 102, it should start the auto-connect ordering at 1 for that set of APNs.

  If you don't provide an auto-connect order, Windows will ask the user to choose an APN, which could introduce user error. We recommend that the auto-connect order be specified. In this case, the user sees the **Friendly Name** of the APN in Windows Connection Manager.

- Changes provided by OEM extension will take precedence over the default COSA database included in Windows.

- In the mobile operator configuration portal, you must specify only one of the following:

  - An MCC+MNC with a blank IMSI range
  - An MCC+MNC with a specific IMSI range
  - An MCC+MNC with a specific ICCID range
  - An MCC+MNC with a specific GSM provider name

- If you have created a website for setting up Mobile Broadband service, it is important to provide the Account Experience URL and certificate data.

- Access strings used for plan purchase (**Purchase Flag**=**Y**) can be one of the following:
  - For GSM networks, an APN with a specified **User Name** and **Password** used for purchasing the subscription.

- Access strings used for Internet connectivity (**Connect Flag**=**Y**) can be one of the following:
  - For GSM networks, an APN with a specified **User Name** and **Password** used to connect to the Internet.

For the next steps in testing your APN update, see [Mobile operator configuration portal guide](mobile-operator-configuration-portal-guide.md).

## Related articles

- [Microsoft mobile operator configuration portal](https://aka.ms/moconfig)
- [Testing your desktop COSA database submission](testing-your-desktop-cosa-database-submission.md)
