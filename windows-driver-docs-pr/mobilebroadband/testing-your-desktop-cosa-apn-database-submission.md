---
title: Testing your desktop COSA/APN database submission
description: Testing your desktop COSA/APN database submission
ms.assetid: 8f45dbf0-4f96-4d11-b2a2-41b9e75b5e9b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Testing your desktop COSA/APN database submission

Before submitting an APN update request to Microsoft, it is important for the MNO or MVNO to validate the APN entries that they are about to submit. Microsoft does not have access to your network, so it is your responsibility to ensure the values that are being submitted are valid and work correctly.

## Contact your Microsoft TAM

The first step in testing and submitting your APN update is to work with your TAM to open a MS Solve case with Microsoft Customer Services and Support. This case is for tracking purposes. After a MS Solve case is opened, provide the following information to the support engineer:

-   A completed spreadsheet that contains your APN information.

If you do not have a TAM:
-   Contact Microsoft Customer Services and Support by calling (800) MICROSOFT (642-7676).
-   Inform the customer service representative that a COSA/APN database update is needed.
-   Provide the spreadsheet to the support engineer.
-   If asked, specify Windows 8 or Windows 10 as the product, as appropriate.

> [!NOTE]
> You will need to provide a credit card to open the incident, but you will not be charged. 

## Test your submission for desktop COSA

Use this process for Windows 10, version 1703 and later.

After you have submitted your completed spreadsheet that contains your APN information to your TAM, Microsoft will create a provisioning package (.ppkg) file for you and return it to you so you can install and test your APN. 

For more information about how to install a provisioning package file, see [Apply a provisioning package](https://technet.microsoft.com/itpro/windows/deploy/provisioning-apply-package).

### Modify the local COSA database (desktop COSA)

Follow these steps to test the updated COSA Provisioning Package (PPKG) you received from Microsoft after completing your APN information spreadsheet and submitting it to your TAM.

These steps require a script from Microsoft to apply and test the PPKG file. Use the following link to download the latest version of the script: <https://go.microsoft.com/fwlink/p/?linkid=866771>.

#### Apply the test PPKG file

> [!IMPORTANT]
> Create a backup of the original provisioning package before performing the following actions. The original provisioning package is located here: `%systemroot%\Provisioning\Cosa\Microsoft\Microsoft.Windows.Cosa.Desktop.Client.ppkg`.

1. Remove any SIM from the device, if any.
2. Copy the script and the new PPKG file to a local directory.
3. Open an elevated Command Prompt window and change to the directory containing the script.
4. Run the script with this syntax to apply the PPKG: `ApplyCosaProvisioning.BAT -a <full path to the PPKG local directory>`.
   1. For example: `ApplyCosaProvisioning.BAT -a "C:\FromMicrosoft\Microsoft.Windows.Cosa.Desktop.Client.ppkg"`
5. Insert the SIM and await provisioning.

#### Restore the original PPKG file

> [!WARNING]
> Once validation of the new PPKG received from Microsoft has completed, always restore it with the following steps. Restoring back to the original PPKG will ensure that you receive the latest COSA updates via Windows Update.

1. Once validated, remove the SIM from the device.
2. Run the script with this syntax to restore the original PPKG: `ApplyCosaProvisioning.BAT -r`.
3. Insert the SIM for provisioning to take effect, reading the original PPKG.

#### Collect logs in case of failure

To collect logs in the event of a failure during the testing process, follow these steps:

1. Remove any SIM from the device.
2. Run the script with this syntax to start *netsh* logging: `ApplyCosaProvisioning.BAT -l`.
3. Insert the SIM and wait for provisioning to fail.
4. Follow the tool's prompts to end logging.
5. Send the logs to Microsoft in zipped format.

## Test your submission for the APN database (apndatabase.xml)

Use this process for Windows 8, Windows 8.1, and versions of Windows 10 before Windows 10, version 1703.

There are two ways that you can ensure that the APN entries work before submitting them to Microsoft:

-   [Editing APN values for the current profile](#editprofile)

-   [Modify the local APN database](#modifydatabase)

### <a href="" id="editprofile"></a> Editing APN values for the current profile

A simple way to test that an APN can connect to your network is to edit the current profile and insert the APN to test into the profile. To perform this test, follow these steps:

> [!NOTE]
> This test does not simulate the full experience, which is described in the [Modify the local APN database](#modifydatabase) section. 

1.  Insert a SIM into the PC that works with the APN value you want to test.

2.  Turn on the PC, log on to Windows, and open Windows Connection Manager. The mobile broadband connection should appear.

3.  Right-click the mobile broadband connection, and then select **View connection properties**.

4.  Enter the APN value to test into this dialog box.

5.  Save your changes, and then try to connect to the mobile broadband network.

### <a href="" id="modifydatabase"></a>Modify the local APN database

Before you submit an APN update, you should editing the local APN database or creating a new one for testing. By doing this, you closely simulate the full experience because the APN selection logic that Windows Connection Manager uses is fully tested.

**Modify the local APN connectivity database**

1. **Copy any existing values from the local APN database file** -- View the existing entries in the local APN database on your PC and copy these entries into a new XML file. If you don’t have any APN entries in the local copy of the APN database, skip this step and start with a blank XML file.

2. **Modify values in the XML file according to the published APN schema** – Ensure that your APN entries follow the [APN database schema reference](apn-database-schema-reference.md).

3. **Generate your hardware IDs** – Hardware IDs specify one or more hardware identification strings that match the SIM characteristics to an APN entry in the database. Each string is specified by a [HardwareId](hardwareid-apnxml.md) element. We recommend that you use mbidgenerator.exe to generate your hardware IDs. For more information, see [Using mbidgenerator.exe to generate hardware IDs](using-mbidgeneratorexe-to-generate-hardware-ids.md).

4. **Validate that the file you generated conforms to the published APN database schema** -- Always perform a schema check to ensure that the file you have generated conforms to the [APN database schema reference](apn-database-schema-reference.md).

5. **Overwrite the APN connectivity database on the PC with your new database**

   1.  From an elevated command prompt, type **cd %systemroot%\\system32** and then press ENTER.

   2.  Type **takeown /f .\\ApnDatabase.xml** and then press ENTER.

   3.  Type **icacls .\ApnDatabase.xml /grant %username%:F** and then press ENTER.

   4.  Copy your customized version of the ApnDatabase.xml file to the directory.

6. Validate that the APN entries exist in the local APN database:

   1. Ensure that there are no existing mobile broadband profiles by running the following command: **netsh mb show profiles**

   2. If a mobile broadband profile exists, type **netsh mb profile interface=&lt;Interface name&gt; name=&lt;Profile name&gt;**

   3. Ensure that the device doesn’t have a provisioned context by running the following command: **netsh mb show provisionedcontext interface=&lt;Interface name&gt;**

      **Note**
      If the device provides a provisioned context, Windows will use the APN from that provisioned context instead of the local APN database and you will not able to test your APNs. If the device has a provisioned context, you need to acquire another device that doesn’t provide a provisioned context.    

   4. Open Windows Connection Manager. It will show the Wi-Fi and mobile broadband networks that are within range.

   5. Select the Mobile Network, and then click **Connect**.

   6. If you have multiple APNs that match the SIM properties, Windows Connection Manager will try each of the matching APNs until a successful connection takes place. If none of the APNs connect, Windows Connection Manager will either show an error or show a custom APN entry screen, allowing the user to enter a custom APN.

      **Note**
      The auto-connect order that you specify in the APN database is used to determine the order in which APNs are tried.         

   7. If you have only one APN in the APN database, Windows will automatically connect to the operator network.

> [!NOTE]
> You can see which APN was applied to the connection profile by opening Windows Connection Manager, right-clicking the Mobile Broadband entry for your network, and then clicking **Properties**. 

