---
title: Usage and Management of Organization Vendor IDs
description: Usage and Management of Organization Vendor IDs
MS-HAID:
- 'p\_dashboard.usage\_and\_management\_of\_organization\_vendor\_ids'
- 'hw\_dashboard.usage\_and\_management\_of\_organization\_vendor\_ids'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: CC419814-36AB-4D53-AA7D-761C9CB57BD4
---

# Usage and Management of Organization Vendor IDs


Using hardware IDs incorrectly in driver packages can have significant impact on customers and partners. To ensure that driver packages are suitable for publishing to Windows Update, take advantage of the new logic available for validating Vendor ID code usage.

These changes will take effect sometime after August 2016.

## <span id="Vendor_ID_check"></span><span id="vendor_id_check"></span><span id="VENDOR_ID_CHECK"></span>Vendor ID check


Microsoft will validate the Vendor ID value of the driver strings contained in the driver INF files for device strings on PCI and USB buses. This validation is performed as part of determining whether a device driver is eligible to be published to Windows Update using the Driver Distribution Center, and includes device strings that use the following bus enumerators:

-   PCI
-   USB
-   HDAUDIO
-   HID
-   DOT4
-   DOT4PRT
-   DOT4USB

For drivers using the above bus enumerators, the partner submitting the driver to the Hardware Dev Center Dashboard must be associated to either the Vendor ID code or the SUBSYS Vendor ID code (where present) from each device string in the driver INF file(s) in order for the driver to be published to Windows Update.

If the partner is not associated to either the Vendor ID or SUBSYS Vendor ID code in any device string used in a driver, the partner will not be able to distribute the driver using the Driver Distribution Center. However, the Hardware Dev Center (Sysdev) will still sign the submission, provided the driver meets the other requirements for signing.

While this check is limited to device strings using the bus enumerators above, device strings that use other bus enumerators are still eligible to be published to Windows Update, provided they meet general requirements for the Driver Distribution Center.

## <span id="Distribution_limitations"></span><span id="distribution_limitations"></span><span id="DISTRIBUTION_LIMITATIONS"></span>Distribution limitations


Once a device string has been published to Windows Update from the Driver Distribution Center, only the organization that published the driver (or any sub-division from that organization) can publish newer drivers to Windows Update using the same device string.

**Note**  This applies for all device strings published to Windows Update, regardless of which bus enumerator is used by the driver, or whether a Vendor ID code or SUBSYS Vendor ID code is present.

 

For device strings that use a bus enumerator outlined in the above Vendor ID Check section, either the organization with the Vendor ID code or the organization with the SUBSYS Vendor ID code can publish the driver, when present. However, once an organization publishes the device string, other organizations will not be able to publish the same device string.

## <span id="Distribution_with_a_HWID"></span><span id="distribution_with_a_hwid"></span><span id="DISTRIBUTION_WITH_A_HWID"></span>Distribution with a HWID


An organization which makes a submission or receives a resold submission that is not eligible to be published due to the Vendor ID check can contact [ddchelp@microsoft.com](mailto://ddchelp@microsoft.com%29 for assistance with publishing a device driver using a hardware ID %28HWID) for additional targeting.

## <span id="Reseller_submission_exception"></span><span id="reseller_submission_exception"></span><span id="RESELLER_SUBMISSION_EXCEPTION"></span>Reseller submission exception


When a partner resells a device driver submission they have submitted, the partner that receives the resold submission can distribute the driver(s) for the device strings valid for their organization (per the Vendor ID code and SUBSYS Vendor ID code check described above). In addition, the partner who receives the resold submission can also distribute the driver for any device string associated to the original submitter for that specific resold submission.

If neither the organization which resold the submission nor the organization which received the resold submission is associated to the Vendor ID code or SUBSYS Vendor ID code used in the submission driver, the driver will not be eligible for distribution.

## <span id="Associating_new_Vendor_ID_codes_to_an_organization"></span><span id="associating_new_vendor_id_codes_to_an_organization"></span><span id="ASSOCIATING_NEW_VENDOR_ID_CODES_TO_AN_ORGANIZATION"></span>Associating new Vendor ID codes to an organization


The [Vendor ID List](http://go.microsoft.com/fwlink/p/?LinkId=618598) page (under the Administration section on the Hardware Dev Center) Dashboard lists the known Vendor ID codes associated to your organization. If this list is incomplete or inaccurate, please contact [sysdev@microsoft.com](mailto://sysdev@microsoft.com) to provide the addition or correction.

## <span id="Viewing_publishing_eligibility_status_for_a_submission"></span><span id="viewing_publishing_eligibility_status_for_a_submission"></span><span id="VIEWING_PUBLISHING_ELIGIBILITY_STATUS_FOR_A_SUBMISSION"></span>Viewing publishing eligibility status for a submission


Microsoft will determine whether the device strings included in a device driver submission satisfy the Vendor ID check requirement as part of the submission signing process. Information regarding non-eligible device strings will be included in the submission status email sent from the Hardware Dev Center upon successful completion of a device driver submission. A driver with device strings not eligible to be published to Windows Update can still be signed, provided the submission satisfies the signing requirements.

Additionally, the submission status details page for Approved device driver submissions (located under Hardware Compatibility) includes a Publishing section on the **Summary and tasks** tab that indicates whether the submission contains driver(s) that can be published to Windows Update.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Usage%20and%20Management%20of%20Organization%20Vendor%20IDs%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




