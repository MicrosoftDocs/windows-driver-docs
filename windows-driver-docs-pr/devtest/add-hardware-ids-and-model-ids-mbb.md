---
title: Add Hardware IDs in the Mobile Broadband Metadata Authoring Wizard
description: Add Hardware IDs in the Mobile Broadband Metadata Authoring Wizard
ms.assetid: 1A540E7F-CA03-4CFA-8711-6CDBD7E152AD
keywords: ["Add Hardware IDs in the Mobile Broadband Metadata Authoring Wizard"]
---

# Add Hardware IDs in the Mobile Broadband Metadata Authoring Wizard


Specify a Hardware ID range that the metadata package applies to, based on the IMSI or ICCID (GSM network operators), provider SID, or provider name (CDMA network operators).

The wizard generates Hardware ID values for you; you don't create them manually.

More than one Hardware ID can be used to specify a service. For example, you can input both GSM and CDMA entries for the Hardware ID to create a single metadata package that matches multiple networks.

### <span id="To_add_the_Hardware_ID"></span><span id="to_add_the_hardware_id"></span><span id="TO_ADD_THE_HARDWARE_ID"></span>To add the Hardware ID

1.  Click the **Associations** tab.
2.  Next to **Hardware ID**, click the **Plus Sign (+)**.
3.  From the list next to **Service type**, select one of the following options:
    -   If you have a MobileBroadbandMetadataSubmission.xml file, under the **HardwareID** group, click **Import**, and then select the MobileBroadbandMetadataSubmission.xml file. The tool generates the hardware ID based on the MobileBroadbandMetadataSubmission.xml file, and the hardware IDs are displayed in the **HardwareID** group.

        If you want to match your package by using the IMSI values on the SIM, select **GSM Provider (IMSI)**.

        GSM network operators should specify the IMSI ranges that they want device metadata package to apply to.

        -   Enter the concatenated MCC and MNC in the **Provider ID** field.
            **Note**  This works for 6-digit and 5-digit MCC + MNC combinations.

             

        -   Enter the full IMSI (MCC + MNC + MSIN) Begin value and End value in the **Ranges** field.
            **Note**  To protect user privacy, the last two digits of the IMSI are ignored for matching purposes. The full IMSI is never sent to the server for matching purposes. Specify your IMSI ranges in even blocks of 100. The Begin value must end in 00, and the End value must end in 99.

             

        -   The next page shows the generated **Hardware ID** values that correspond to your ranges. Several **Hardware ID** values may appear in the list. Make sure that all of them are selected, and then click **Next**.

            You can add more ranges by clicking the **Plus Sign (+)** button under **Hardware ID** on the **Associations** tab. You can add IMSI ranges, as well as ICCID ranges, within the same package submission.

    -   To specify ICCID ranges, select **GSM Provider (ICCID)**.

        GSM network operators can use ICCID ranges to match their service metadata packages.

        -   In the **Provider ID** field, enter the Issuer Identification Number that begins the ICCID number reported by the SIMs. This is a 6- or 7 -digit number that includes the "89” prefix.
        -   Enter the full ICCID (including the "89” prefix) Begin value and End value in the **Ranges** field .

            **Note**  To help protect user privacy, the last two digits of the ICCID are ignored and the full ICCID is never sent to the server for matching purposes. Specify your ICCID ranges in even blocks of 100. The Begin value must end in 00, and the End value must end in 99.

             

        -   The next page shows the generated **Hardware ID** values that correspond to your ranges. Several **Hardware ID** values may appear in the list. Make sure that all of them are selected, and then click **Next**.

            You can add more ranges by clicking the **Plus Sign (+)** button under **Hardware ID** on the **Associations** tab. You can add IMSI ranges, as well as ICCID ranges, to the same package submission.

    -   If you want to match using the provider ID value on the mobile broadband modem, select **CDMA Provider ID**.
        **Note**  We recommend using a **Provider ID** (SID), because **Provider Name** is a text value and susceptible to matching errors due to spelling variations. For more information, see [WWAN\_REGISTRATION\_STATE structure](http://go.microsoft.com/fwlink/p/?linkid=225972).

         

        -   Enter the **Provider ID**, which is the System Identification Number (SID) assigned to an operator by 3GPP2.
            **Note**  You can add multiple **Provider ID** values by clicking the **Plus Sign (+)** button on the **Associations** tab. You can add a combination of **Provider ID** and **Provider Name** values for matching purposes.

             

        -   Each **Provider ID** value that you specify appears on the **Associations** tab as a specially formatted Hardware ID entry. Make sure that each check box is selected, and click **Next** when you finish entering Provider IDs.
    -   If you want to match by using the provider name on the mobile broadband modem, select **CDMA Provider Name** in addition to or instead of a Provider ID.
        **Note**  If all of the mobile broadband hardware you provide to customers uses Provider ID values, you don't need to add **Provider Name** information in your device metadata package. **Provider Name** is only checked for matching purposes if the Provider ID is blank or has a value of zero. For more information, see [WWAN\_REGISTRATION\_STATE structure](http://go.microsoft.com/fwlink/p/?linkid=225972).

         

        -   Enter the **Provider Name**. This case-sensitive value is used to generate Hardware IDs. If you have mobile broadband hardware that represents the **Provider Name** in various ways, enter each variation separately, accounting for all capitalization and spelling combinations of the operator’s name.
        -   Each **Provider Name** value that you specify appears in the **Associations** tab as a specially formatted Hardware ID entry. Make sure that each checkbox is selected, and click **Next** when you finish entering Provider Names.

4.  Click **OK** to return to the **Associations** tab.

For detailed information about the Hardware ID for each service style, see [Service Metadata Package Schema Reference for Windows 8](https://msdn.microsoft.com/library/windows/hardware/dn973175).

For more information about matching, see [Delivering experiences for MVNOs](https://msdn.microsoft.com/library/windows/hardware/dn973075).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\dma]:%20Add%20Hardware%20IDs%20in%20the%20Mobile%20Broadband%20Metadata%20Authoring%20Wizard%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




