---
title: Submitting the COSA/APN database update
description: Submitting the COSA/APN database update
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1ad1be32-74c9-4f84-b680-9124135a3b66
---

# Submitting the COSA/APN database update

>[!IMPORTANT]
> The following steps to submit an APN update apply to both COSA, which is used for Windows 10 Version 1703 and later, and apndatabase.xml, which is used for Windows 8, Windows 8.1, and versions of Windows 10 before 1703. Microsoft will convert apndatabase.xml submissions to COSA if you are targeting Windows 10 Version 1703 or later.

Now that you’ve tested the APN entries, it’s now time to submit them to Microsoft by following the steps in this topic.

## Fill out the APN testing questionnaire

Once you have tested your APN values, you must fill out the following questionnaire. This will be sent to your TAM as part of your submission.

The purpose of this questionnaire is to make sure you have completed testing and to help the team at Microsoft understand how thoroughly you tested the incoming APNs.

```syntax
Please describe what testing you have done on the APNs that you are submitting.
   [describe here]

Have you tested these APN values on your network? Windows cannot test these APNs for you because we do not have access to your wireless network.
   [yes/no]

Do you understand that all the APNs that match the Operator and Country/Region combination will be wiped out and replaced by the APNs that you have attached to this request?
   [yes/no]

Have you attached an Excel sheet to this request?
   [yes/no]

Do you certify that you are entitled to submit an update on behalf of this operator?
   [yes/no]

Provide your contact information:
   [Name]
   [Company]
   [Job title]
   [E-mail from a corporate e- account for the company you are submitting for]
   [phone 1]
   [phone 2]
```

## Submit COSA/APN database updates to Microsoft

Use the following procedure to submit COSA or APN connectivity database updates to Microsoft. 

1.  **Contact your Microsoft TAM** - Using the same MS Solve case described in [Testing your COSA/APN database submission](testing-your-apn-database-submission.md), provide your TAM with a completed APN testing questionnaire to describe the level of testing that has been done.  

2.  **Microsoft triage process** -- Microsoft will review your submission and may contact you if errors are detected. Microsoft will not do any testing on your mobile network. If no errors are detected in your submission, it will proceed through the release process.

3.  **Operator validation** -- Since Microsoft cannot test the APNs you provided for your mobile network, you’ll be asked to do so after a new APN database has been generated. You’ll be provided a new copy of the APN database XML file that you’ll use to apply to your PCs and test the functionality on your actual network. You’ll go through another test pass, as described in [Testing Your COSA/APN database submission](testing-your-apn-database-submission.md). Your Microsoft TAM will provide you with an installable file that will patch the APN database on the PC with the updated database. You’ll be given a specific time period to test the new APN database. Once you have completed your testing, you’ll be asked to reply back to your Microsoft contact with your sign-off. If you find an issue or error, there may be a limited opportunity to correct it. If the issue cannot be corrected in time, your changes will be reverted from the next released update of the APN database. You’ll need to resubmit your APN connectivity database submission and wait until the next scheduled update.

> [!IMPORTANT]  
> If you do not sign-off within the allotted time period, your changes will be reverted from the next released update of the APN connectivity database. You’ll need to resubmit your APN submission and wait until the next scheduled update.     

4.  **Update is released** -- Once you have signed off on the new APN database, it will go through the update publishing process. Once it is ready, it will appear in Windows Update for users to install. You’ll be provided a more detailed release timeline after completing your APN database submission.

### Deleting an APN database entry

Deleting an APN entry is considered a special-case operation. If you are only deleting an entry, you do not have to fill out a spreadsheet. List the entries in the APN connectivity database you want to have deleted by answering the following questionnaire. Once this is done, send it to your TAM.

> [!NOTE]
> Deletions take place based on **Operator** and **Country/Region** combination. 

```syntax
Please describe which operator and region combination you wish to have removed from the APN database.
   [Describe here. For example: <Operator name="Contoso (Argentina)">]

Do you understand that all the APNs that match the Operator and Country/Region combination will be wiped out?
   [yes/no]

If you wish to add values to the APN database in addition to this deletion request, have you attached an Excel sheet and questionnaire for that add request?
   [not applicable/yes/no]

Do you certify that you are entitled to submit an update on behalf of this operator?
   [yes/no]

Provide your contact information:
   [Name]
   [Company]
   [Job title]
   [E-mail from a corporate email account for the company you are submitting for]
   [phone 1]
   [phone 2]
``` 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Submitting%20the%20APN%20database%20update%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




