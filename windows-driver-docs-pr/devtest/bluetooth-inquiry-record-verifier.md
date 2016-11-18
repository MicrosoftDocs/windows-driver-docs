---
title: Bluetooth Inquiry Record Verifier
description: The Bluetooth Inquiry Record Verifier displays a Bluetooth device’s inquiry record as Microsoft Windows interprets it.
ms.assetid: 3C48EEBA-3407-4A4A-91C2-EF001EFCDA6E
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Bluetooth%20Inquiry%20Record%20Verifier%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




