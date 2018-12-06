---
title: Bluetooth Inquiry Record Verifier
description: The Bluetooth Inquiry Record Verifier displays a Bluetooth device’s inquiry record as Microsoft Windows interprets it.
ms.assetid: 3C48EEBA-3407-4A4A-91C2-EF001EFCDA6E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bluetooth Inquiry Record Verifier


The Bluetooth Inquiry Record Verifier displays a Bluetooth device’s inquiry record as Microsoft Windows interprets it. This record is displayed in a tree format, showing both the Service Discovery Protocol’s Record and any Extended Inquiry Response data obtained.

This tool is not a replacement for any portion of the Bluetooth SIG’s qualification process or for the Microsoft Windows Certification Program. It is provided in the Windows Driver Kit to help you troubleshoot interactions between a device and Microsoft Windows.

The Bluetooth Inquiry Record Verifier has three menus: File, Radio and View.

Use the **File** menu to save and open inquiry records and Bluetooth profiles:

-   To save the current inquiry record, click **File &gt; Export**.

-   To open a saved inquiry record, click **File &gt; Import**.

-   To load a profile description, click **File &gt; Load a Profile Description**. By default, Microsoft supplies and loads profile descriptions for 12 common profiles.

-   To choose which profile descriptions to load, click **Manage Profile Descriptions**.

Use the **Radio** menu to display all discoverable and paired devices.

-   To display all discoverable and paired devices, click **Radio &gt; Inquire and Select**. Select a device to view its inquiry record.

-   To query the Bluetooth radio at a specified address, click **Radio &gt; Enter Address**, and type the Bluetooth MAC address in the Select Bluetooth Device dialog box.
-   To refresh the SDP record currently displayed, click **Radio &gt; Requery Current Radio**.

Use the **View** menu to display results and to view errors.

-   To display the results in hexadecimal, click **View &gt; Raw Results**.

-   To display the Attribute Values in line with their Attribute IDs, click **View &gt; Attribute Values as siblings**.

-   To jump from error to error, click **View &gt; Previous Error** or **View &gt; Next Error**

## <span id="Known_Issues__Windows_7_"></span><span id="known_issues__windows_7_"></span><span id="KNOWN_ISSUES__WINDOWS_7_"></span>Known Issues (Windows 7)


-   On searching for remote devices, everything found is listed during the initial inquiry. Once the inquiry is complete, only devices for which we have a friendly name persist.
-   Extended Inquiry Response record parsing does not work.
-   **LanguageBaseAttributeIDList** may be marked incorrectly as invalid.

 

 





